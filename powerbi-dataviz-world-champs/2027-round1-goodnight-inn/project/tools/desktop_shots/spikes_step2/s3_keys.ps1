param([int]$ProcId, [string]$Tile = "Breakfast upgrade", [string]$Do = "list", [string]$Page = "S-3 selector")
# S-3 (doc 23 step 2): the button slicer in the THROWAWAY copy, by keyboard and by click.
#   -Do list    print the slicer's tiles as UI Automation sees them (type, focusable, selected)
#   -Do space   focus the tile, post Space to the report's render widget, print the tile's state before and after
#   -Do tab     focus the tile, post Tab, print which element has the focus afterwards
#   -Do click   post a left click on the tile (the mouse path, for the reload test)
# Keys and clicks are posted to the Chrome_RenderWidgetHostHWND of the report view (the method of spikes_step1/s6_click.ps1);
# nothing is saved.
Add-Type -AssemblyName UIAutomationClient, UIAutomationTypes
Add-Type @"
using System;
using System.Text;
using System.Collections.Generic;
using System.Runtime.InteropServices;
public class S3Win {
  public delegate bool EnumProc(IntPtr hWnd, IntPtr lParam);
  [DllImport("user32.dll")] public static extern bool EnumChildWindows(IntPtr parent, EnumProc cb, IntPtr lParam);
  [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern int GetClassName(IntPtr hWnd, StringBuilder s, int n);
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr hWnd, out RECT r);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr hWnd);
  [DllImport("user32.dll")] public static extern bool ScreenToClient(IntPtr hWnd, ref POINT p);
  [DllImport("user32.dll")] public static extern bool PostMessage(IntPtr hWnd, uint msg, IntPtr w, IntPtr l);
  [DllImport("user32.dll")] public static extern uint MapVirtualKey(uint code, uint mapType);
  [StructLayout(LayoutKind.Sequential)] public struct RECT { public int L, T, R, B; }
  [StructLayout(LayoutKind.Sequential)] public struct POINT { public int X, Y; }
  public static List<IntPtr> Children(IntPtr parent, string cls) {
    var list = new List<IntPtr>();
    EnumChildWindows(parent, (h, l) => {
      var sb = new StringBuilder(256); GetClassName(h, sb, 256);
      if (sb.ToString() == cls && IsWindowVisible(h)) list.Add(h);
      return true; }, IntPtr.Zero);
    return list;
  }
}
"@
$AE = [System.Windows.Automation.AutomationElement]
$TS = [System.Windows.Automation.TreeScope]
$win = $AE::RootElement.FindFirst($TS::Children, (New-Object System.Windows.Automation.PropertyCondition($AE::ProcessIdProperty, [int]$ProcId)))
if (-not $win) { "no window"; return }

$names = "Booking app", "Revenue management", "Kiosks at 20 desks", "Breakfast upgrade", "Gatwick +40 rooms", "Toronto +40 rooms",
         "Kingston +40 rooms", "Energy programme", "Boston new hotel", "Refresh 10 oldest"

function State($e) {
  $s = ""
  try { $s += " selected=" + $e.GetCurrentPattern([System.Windows.Automation.SelectionItemPattern]::Pattern).Current.IsSelected } catch {}
  try { $s += " toggle=" + $e.GetCurrentPattern([System.Windows.Automation.TogglePattern]::Pattern).Current.ToggleState } catch {}
  $s
}
function Describe($e) {
  $r = $e.Current.BoundingRectangle
  "[" + $e.Current.ControlType.ProgrammaticName.Replace("ControlType.", "") + "] '" + $e.Current.Name + "' focusable=" + $e.Current.IsKeyboardFocusable +
    " focused=" + $e.Current.HasKeyboardFocus + (State $e) + " rect=" + $r.ToString()
}
function Tiles {
  # one full walk of the tree (the WebView's elements only appear after it), then the tiles by name
  $all = $win.FindAll($TS::Descendants, [System.Windows.Automation.Condition]::TrueCondition)
  $out = @()
  foreach ($e in $all) {
    $n = $e.Current.Name
    if (-not $n) { continue }
    foreach ($m in $names) { if ($n -eq $m -or $n.StartsWith($m + ",") -or $n.StartsWith($m + " ")) { $out += $e; break } }
  }
  $out
}
function Widget($sx, $sy) {
  foreach ($h in [S3Win]::Children([IntPtr]$win.Current.NativeWindowHandle, "Chrome_RenderWidgetHostHWND")) {
    $rc = New-Object S3Win+RECT; [S3Win]::GetWindowRect($h, [ref]$rc) | Out-Null
    if ($sx -ge $rc.L -and $sx -le $rc.R -and $sy -ge $rc.T -and $sy -le $rc.B) { return $h }
  }
  return [IntPtr]::Zero
}
function Key($h, [uint32]$vk) {
  $scan = [S3Win]::MapVirtualKey($vk, 0)
  $down = [IntPtr](1 -bor ($scan -shl 16))
  $up = [IntPtr]::new([int64](1 -bor ($scan -shl 16) -bor 0xC0000000))
  [S3Win]::PostMessage($h, 0x0100, [IntPtr]$vk, $down) | Out-Null   # WM_KEYDOWN
  if ($vk -eq 0x20) { [S3Win]::PostMessage($h, 0x0102, [IntPtr]0x20, $down) | Out-Null }  # WM_CHAR ' '
  Start-Sleep -Milliseconds 60
  [S3Win]::PostMessage($h, 0x0101, [IntPtr]$vk, $up) | Out-Null     # WM_KEYUP
}

# the page tab first: `powerbi-desktop reload` keeps the page that was open
$tabCond = New-Object System.Windows.Automation.PropertyCondition($AE::ControlTypeProperty, [System.Windows.Automation.ControlType]::TabItem)
foreach ($t in $win.FindAll($TS::Descendants, $tabCond)) {
  if ($t.Current.Name -eq $Page) {
    $sel = $t.GetCurrentPattern([System.Windows.Automation.SelectionItemPattern]::Pattern)
    if (-not $sel.Current.IsSelected) { $sel.Select(); Start-Sleep -Milliseconds 2500; "page tab '$Page' selected" }
  }
}
$tiles = Tiles
"tiles found: " + $tiles.Count
if ($Do -eq "list") { foreach ($t in $tiles) { "  " + (Describe $t) }; return }

# each tile is three elements; the Button is the one that takes the focus and carries the toggle state
$isBtn = { $_.Current.ControlType -eq [System.Windows.Automation.ControlType]::Button -and $_.Current.Name.StartsWith($Tile) }
$target = $tiles | Where-Object $isBtn | Select-Object -First 1
if (-not $target) { "tile '$Tile' not found"; return }
"before: " + (Describe $target)
$r = $target.Current.BoundingRectangle
$sx = [int]($r.X + $r.Width / 2); $sy = [int]($r.Y + $r.Height / 2)
$h = Widget $sx $sy
if ($h -eq [IntPtr]::Zero) { "no render widget under the tile"; return }

if ($Do -eq "click") {
  $pt = New-Object S3Win+POINT; $pt.X = $sx; $pt.Y = $sy
  [S3Win]::ScreenToClient($h, [ref]$pt) | Out-Null
  $lp = [IntPtr](($pt.Y -shl 16) -bor ($pt.X -band 0xFFFF))
  [S3Win]::PostMessage($h, 0x0200, [IntPtr]0, $lp) | Out-Null; Start-Sleep -Milliseconds 150
  [S3Win]::PostMessage($h, 0x0201, [IntPtr]1, $lp) | Out-Null; Start-Sleep -Milliseconds 80
  [S3Win]::PostMessage($h, 0x0202, [IntPtr]0, $lp) | Out-Null
} else {
  try { $target.SetFocus() } catch { "SetFocus failed: " + $_.Exception.Message }
  Start-Sleep -Milliseconds 400
  "focused: " + (Describe $target)
  if ($Do -eq "space") { Key $h 0x20 }
  if ($Do -eq "tab") { Key $h 0x09 }
}
Start-Sleep -Milliseconds 1500
$after = (Tiles) | Where-Object $isBtn | Select-Object -First 1
if ($after) { "after:  " + (Describe $after) }
# Desktop is not the foreground window, so the focus is read inside its own tree
$all = $win.FindAll($TS::Descendants, [System.Windows.Automation.Condition]::TrueCondition)
foreach ($e in $all) { if ($e.Current.HasKeyboardFocus) { "focus now on: " + (Describe $e) } }
