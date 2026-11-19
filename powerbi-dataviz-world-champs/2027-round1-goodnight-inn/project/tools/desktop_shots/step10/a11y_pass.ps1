param([int]$ProcId, [string]$Do = "names", [string]$Page = "The Investment Strategy", [string]$Out = "", [int]$Count = 40, [string]$Start = "", [string]$Keys = "")
# Build step 10 of doc 23 (R-X-1): the keyboard pass and the screen-reader pass on the THROWAWAY copy, through UI Automation.
# What a screen reader speaks for an element is its UI Automation name (and its control type); this script reads those
# names, so the pass can be logged without a person at the keyboard. Nothing is saved.
#   -Do names   select the page tab, then print every named element of the window as a tree line:
#               depth, control type, name, focusable, has focus (-Out <file> writes it as UTF-8)
#   -Do walk    bring Desktop to the foreground, set the focus on the element whose name starts with -Start (or keep
#               the current focus), then send -Keys (SendKeys syntax, e.g. "{TAB}") -Count times and print the focused
#               element after each key: where the focus went and what is heard
#   -Do keys    send -Keys once (e.g. "{ENTER}", "{ESC}", "^{F6}") and print the focused element
Add-Type -AssemblyName UIAutomationClient, UIAutomationTypes, System.Windows.Forms
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class A11yWin {
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr hWnd);
  [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
  [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr hWnd, int n);
  [DllImport("user32.dll")] public static extern void keybd_event(byte vk, byte scan, uint flags, UIntPtr extra);
}
"@
$AE = [System.Windows.Automation.AutomationElement]
$TS = [System.Windows.Automation.TreeScope]
$win = $AE::RootElement.FindFirst($TS::Children, (New-Object System.Windows.Automation.PropertyCondition($AE::ProcessIdProperty, [int]$ProcId)))
if (-not $win) { "no window"; return }

function Describe($e) {
  $c = $e.Current
  $s = "[" + $c.ControlType.ProgrammaticName.Replace("ControlType.", "") + "/" + $c.LocalizedControlType + "] '" + $c.Name + "'"
  try { $s += " toggle=" + $e.GetCurrentPattern([System.Windows.Automation.TogglePattern]::Pattern).Current.ToggleState } catch {}
  try { $s += " selected=" + $e.GetCurrentPattern([System.Windows.Automation.SelectionItemPattern]::Pattern).Current.IsSelected } catch {}
  if ($c.HelpText) { $s += " help='" + $c.HelpText + "'" }
  if ($c.ItemStatus) { $s += " status='" + $c.ItemStatus + "'" }
  $s
}
function SelectPage {
  $tabCond = New-Object System.Windows.Automation.PropertyCondition($AE::ControlTypeProperty, [System.Windows.Automation.ControlType]::TabItem)
  # the report view first (Dutch Desktop: 'Rapportweergave'): the page tabs and the canvas only exist in that view
  foreach ($t in $win.FindAll($TS::Descendants, $tabCond)) {
    if ($t.Current.Name -in "Rapportweergave", "Report view") {
      $sel = $t.GetCurrentPattern([System.Windows.Automation.SelectionItemPattern]::Pattern)
      if (-not $sel.Current.IsSelected) { $sel.Select(); Start-Sleep -Milliseconds 4000; "report view selected" }
      break
    }
  }
  $null = $win.FindAll($TS::Descendants, [System.Windows.Automation.Condition]::TrueCondition)   # a full walk: the WebView's elements appear after it
  foreach ($t in $win.FindAll($TS::Descendants, $tabCond)) {
    if ($t.Current.Name -eq $Page) {
      $sel = $t.GetCurrentPattern([System.Windows.Automation.SelectionItemPattern]::Pattern)
      if (-not $sel.Current.IsSelected) { $sel.Select(); Start-Sleep -Milliseconds 3000; "page tab '$Page' selected" } else { "page tab '$Page' is open" }
      return
    }
  }
  "page tab '$Page' not found"
}
function Foreground {
  $h = [IntPtr]$win.Current.NativeWindowHandle
  [A11yWin]::keybd_event(0x12, 0, 0, [UIntPtr]::Zero); [A11yWin]::keybd_event(0x12, 0, 2, [UIntPtr]::Zero)   # a tap on Alt lets this process take the foreground
  [A11yWin]::ShowWindow($h, 5) | Out-Null
  [A11yWin]::SetForegroundWindow($h) | Out-Null
  Start-Sleep -Milliseconds 500
  "foreground: " + ([A11yWin]::GetForegroundWindow() -eq $h)
}
$script:visuals = @()
function Visuals {
  # the visuals of the open page: the siblings of the logo ('Goodnight Inn'), one element each, with their rectangles
  $all = $win.FindAll($TS::Descendants, [System.Windows.Automation.Condition]::TrueCondition)
  $logo = $null
  foreach ($e in $all) { if ($e.Current.Name.Trim() -eq "Goodnight Inn" -and $e.Current.ControlType -eq [System.Windows.Automation.ControlType]::Image) { $logo = $e; break } }
  if (-not $logo) { return }
  $w = [System.Windows.Automation.TreeWalker]::ControlViewWalker
  # up to the report ('Power BI-rapport'), counting the levels; then every element of the report at the logo's level
  $root = $logo; $depth = 0
  while ($root -and $root.Current.Name -notin "Power BI-rapport", "Power BI Report") { $root = $w.GetParent($root); $depth++ }
  if (-not $root) { return }
  $list = New-Object System.Collections.ArrayList
  function Level($e, $d) {
    if ($d -eq $depth) { [void]$list.Add($e); return }
    $k = $w.GetFirstChild($e)
    while ($k) { Level $k ($d + 1); $k = $w.GetNextSibling($k) }
  }
  Level $root 0
  $script:visuals = $list
}
function Under($f) {
  # Desktop puts the focus of a selected visual on its header button ('Meer opties'), which hangs at the visual's top
  # right corner: the visual is the one whose top right corner is nearest
  $fr = $f.Current.BoundingRectangle; $best = $null; $bd = 1e9
  foreach ($v in $script:visuals) {
    $r = $v.Current.BoundingRectangle
    if ($r.IsEmpty) { continue }
    $d = [Math]::Abs($r.Right - $fr.Right) + [Math]::Abs($r.Top - $fr.Bottom)
    if ($d -lt $bd) { $bd = $d; $best = $v }
  }
  if ($best) { "  => " + [int]$bd + " px from [" + $best.Current.LocalizedControlType + "] '" + $best.Current.Name.Trim() + "'" } else { "" }
}
function Focused {
  try { $f = $AE::FocusedElement } catch { return "no focused element: " + $_.Exception.Message }
  if ($f.Current.Name -eq "" -and $script:visuals.Count) {
    # an element without a name: say which visual it lies in (the WebView runs in a process of its own)
    $fr = $f.Current.BoundingRectangle
    foreach ($v in $script:visuals) {
      $r = $v.Current.BoundingRectangle
      if (-not $r.IsEmpty -and [Math]::Abs($r.Left - $fr.Left) -lt 3 -and [Math]::Abs($r.Top - $fr.Top) -lt 3 -and [Math]::Abs($r.Width - $fr.Width) -lt 3) {
        return "[" + $f.Current.LocalizedControlType + "] unnamed, the rectangle of [" + $v.Current.LocalizedControlType + "] '" + $v.Current.Name.Trim() + "'"
      }
    }
    return "[" + $f.Current.LocalizedControlType + "] unnamed, class '" + $f.Current.ClassName + "', rect " + $fr.ToString()
  }
  if ($f.Current.Name -in "Meer opties", "More options") { return "visual header" + (Under $f) }
  $anc = @(); $w = [System.Windows.Automation.TreeWalker]::ControlViewWalker; $p = $f
  for ($i = 0; $i -lt 6; $i++) { $p = $w.GetParent($p); if (-not $p) { break }; if ($p.Current.Name) { $anc += "'" + $p.Current.Name.Substring(0, [Math]::Min(60, $p.Current.Name.Length)) + "'" } }
  (Describe $f) + "   < " + ($anc -join " < ")
}

if ($Do -eq "names") {
  SelectPage
  $w = [System.Windows.Automation.TreeWalker]::ControlViewWalker
  $lines = New-Object System.Collections.Generic.List[string]
  function Walk($e, $d) {
    $c = $e.Current
    if ($c.Name -or $c.IsKeyboardFocusable) {
      $lines.Add(("{0,2} {1}{2}{3}" -f $d, (Describe $e), $(if ($c.IsKeyboardFocusable) { " focusable" } else { "" }), $(if ($c.HasKeyboardFocus) { " FOCUS" } else { "" })))
    }
    $k = $w.GetFirstChild($e)
    while ($k) { Walk $k ($d + 1); $k = $w.GetNextSibling($k) }
  }
  Walk $win 0
  if ($Out) { [System.IO.File]::WriteAllLines($Out, $lines, (New-Object System.Text.UTF8Encoding($false))); "written: $Out (" + $lines.Count + " lines)" } else { $lines }
  return
}

SelectPage
Foreground
Visuals
"visuals on the page: " + $script:visuals.Count
if ($Start) {
  $all = $win.FindAll($TS::Descendants, [System.Windows.Automation.Condition]::TrueCondition)
  $t = $null
  foreach ($e in $all) { if ($e.Current.Name -and $e.Current.Name.Trim().StartsWith($Start) -and $e.Current.IsKeyboardFocusable) { $t = $e; break } }
  if ($t) { try { $t.SetFocus() } catch { "SetFocus failed: " + $_.Exception.Message }; Start-Sleep -Milliseconds 500; "start: " + (Focused) } else { "start element '$Start' not found" }
}
if ($Do -eq "canvaswalk") {
  # Ctrl+F6 moves between the sections of Desktop (title bar, ribbon, view switcher, canvas, panes); stop on the canvas
  # (the focus is on one of the page's visuals), then walk with -Keys
  $names = @{}; foreach ($v in $script:visuals) { if ($v.Current.Name.Trim()) { $names[$v.Current.Name.Trim()] = 1 } }
  $on = $false
  for ($i = 1; $i -le 14 -and -not $on; $i++) {
    [System.Windows.Forms.SendKeys]::SendWait("^{F6}"); Start-Sleep -Milliseconds 700
    try { $f = $AE::FocusedElement; if ($f.Current.Name -and $names.ContainsKey($f.Current.Name.Trim())) { $on = $true; "canvas reached after $i x Ctrl+F6: " + (Focused) } } catch {}
  }
  if (-not $on) { "the canvas did not take the focus"; return }
  for ($i = 1; $i -le $Count; $i++) {
    [System.Windows.Forms.SendKeys]::SendWait($Keys)
    Start-Sleep -Milliseconds 650
    $where = Focused
    ("{0,2} {1}" -f $i, $where)
    # the focus fell into a visual's header (its 'More options' button): Escape hands it back to the visual
    if ($where.StartsWith("visual header")) { [System.Windows.Forms.SendKeys]::SendWait("{ESC}"); Start-Sleep -Milliseconds 500; "   Esc: " + (Focused) }
  }
  return
}
if ($Do -eq "keys") { [System.Windows.Forms.SendKeys]::SendWait($Keys); Start-Sleep -Milliseconds 900; "after $Keys : " + (Focused); return }
if ($Do -eq "walk") {
  for ($i = 1; $i -le $Count; $i++) {
    [System.Windows.Forms.SendKeys]::SendWait($Keys)
    Start-Sleep -Milliseconds 700
    ("{0,2} {1}" -f $i, (Focused))
  }
}
