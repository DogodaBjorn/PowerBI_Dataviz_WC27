param([int]$ProcId, [string]$Match = "Page 2: the plan", [switch]$NoClick)
# S-6: Ctrl+click the candidate page-navigation button in the THROWAWAY copy and report the selected page tab.
Add-Type -AssemblyName UIAutomationClient, UIAutomationTypes
Add-Type @"
using System;
using System.Text;
using System.Collections.Generic;
using System.Runtime.InteropServices;
public class S6Win {
  public delegate bool EnumProc(IntPtr hWnd, IntPtr lParam);
  [DllImport("user32.dll")] public static extern bool EnumChildWindows(IntPtr parent, EnumProc cb, IntPtr lParam);
  [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern int GetClassName(IntPtr hWnd, StringBuilder s, int n);
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr hWnd, out RECT r);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr hWnd);
  [DllImport("user32.dll")] public static extern bool ScreenToClient(IntPtr hWnd, ref POINT p);
  [DllImport("user32.dll")] public static extern bool PostMessage(IntPtr hWnd, uint msg, IntPtr w, IntPtr l);
  [DllImport("user32.dll")] public static extern void keybd_event(byte vk, byte scan, uint flags, UIntPtr extra);
  [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr hWnd, out uint pid);
  [DllImport("kernel32.dll")] public static extern uint GetCurrentThreadId();
  [DllImport("user32.dll")] public static extern bool AttachThreadInput(uint a, uint b, bool attach);
  [DllImport("user32.dll")] public static extern bool GetKeyboardState(byte[] s);
  [DllImport("user32.dll")] public static extern bool SetKeyboardState(byte[] s);
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
$root = $AE::RootElement
$win = $root.FindFirst($TS::Children, (New-Object System.Windows.Automation.PropertyCondition($AE::ProcessIdProperty, [int]$ProcId)))
if (-not $win) { "no window"; return }

function Tabs {
  $c = New-Object System.Windows.Automation.PropertyCondition($AE::ControlTypeProperty, [System.Windows.Automation.ControlType]::TabItem)
  foreach ($t in $win.FindAll($TS::Descendants, $c)) {
    $sel = ""
    try { $sel = $t.GetCurrentPattern([System.Windows.Automation.SelectionItemPattern]::Pattern).Current.IsSelected } catch {}
    if ($t.Current.Name -match "SPIKE|Brand Review|Investment Strategy") { "  tab '" + $t.Current.Name + "' selected=" + $sel }
  }
}
"before:"; Tabs
$all = $win.FindAll($TS::Descendants, [System.Windows.Automation.Condition]::TrueCondition)
$target = $null
foreach ($e in $all) {
  if ($e.Current.Name -and $e.Current.Name.Contains($Match)) {
    $r = $e.Current.BoundingRectangle
    "  candidate [" + $e.Current.ControlType.ProgrammaticName + "] '" + $e.Current.Name + "' rect=" + [int]$r.X + "," + [int]$r.Y + "," + [int]$r.Width + "," + [int]$r.Height
    if (-not $target -and $r.Width -gt 0) { $target = $e }
  }
}
if (-not $target) { "button not found in the UI tree"; return }
if ($NoClick) { return }
$r = $target.Current.BoundingRectangle
$sx = [int]($r.X + $r.Width / 2); $sy = [int]($r.Y + $r.Height / 2)
$tabSel = { (Tabs) -join "; " }
foreach ($h in [S6Win]::Children([IntPtr]$win.Current.NativeWindowHandle, "Chrome_RenderWidgetHostHWND")) {
  $rc = New-Object S6Win+RECT; [S6Win]::GetWindowRect($h, [ref]$rc) | Out-Null
  if (-not ($sx -ge $rc.L -and $sx -le $rc.R -and $sy -ge $rc.T -and $sy -le $rc.B)) { continue }
  $pt = New-Object S6Win+POINT; $pt.X = $sx; $pt.Y = $sy
  [S6Win]::ScreenToClient($h, [ref]$pt) | Out-Null
  $lp = [IntPtr](($pt.Y -shl 16) -bor ($pt.X -band 0xFFFF))
  $tpid = 0; $tid = [S6Win]::GetWindowThreadProcessId($h, [ref]$tpid); $me = [S6Win]::GetCurrentThreadId()
  [S6Win]::AttachThreadInput($me, $tid, $true) | Out-Null
  $ks = New-Object byte[] 256; [S6Win]::GetKeyboardState($ks) | Out-Null
  $old = $ks[0x11]; $ks[0x11] = 0x80; [S6Win]::SetKeyboardState($ks) | Out-Null     # Ctrl held, in the target's key state
  [S6Win]::PostMessage($h, 0x0200, [IntPtr]0x0008, $lp) | Out-Null                    # WM_MOUSEMOVE
  Start-Sleep -Milliseconds 150
  [S6Win]::PostMessage($h, 0x0201, [IntPtr]0x0009, $lp) | Out-Null                    # WM_LBUTTONDOWN
  Start-Sleep -Milliseconds 80
  [S6Win]::PostMessage($h, 0x0202, [IntPtr]0x0008, $lp) | Out-Null                    # WM_LBUTTONUP
  Start-Sleep -Milliseconds 400
  $ks[0x11] = $old; [S6Win]::SetKeyboardState($ks) | Out-Null
  [S6Win]::AttachThreadInput($me, $tid, $false) | Out-Null
  Start-Sleep -Milliseconds 2000
  "widget " + $h + " (" + $rc.L + "," + $rc.T + "," + $rc.R + "," + $rc.B + ") client " + $pt.X + "," + $pt.Y + " ->"
  $t = Tabs; $t
  if (($t -join " ") -match "Investment Strategy' selected=True") { "NAVIGATED"; break }
}
