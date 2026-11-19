<#
Close a Power BI Desktop window and answer its "Wilt u de wijzigingen opslaan?" dialog (16 Nov 2026, docs 36 and 39).
ONLY on Bjorn's explicit request to save or restart his window; a throwaway window is stopped instead.

  powershell -ExecutionPolicy Bypass -File project\tools\desktop_shots\close_with_save.ps1 -DesktopPid <pid> [-Answer "Opslaan" | "Niet opslaan"]

The dialog is an embedded Internet Explorer control that UI Automation cannot read. Its HTML document is fetched with
WM_HTML_GETOBJECT and ObjectFromLresult, and the answer is the DIV of class o-action-button with that text.
Run with Windows PowerShell 5.1.
#>
param([int]$DesktopPid, [string]$Answer = "Opslaan")

Add-Type -AssemblyName UIAutomationClient, UIAutomationTypes
Add-Type @"
using System; using System.Runtime.InteropServices;
public static class HtmlDlg {
  [DllImport("user32.dll", CharSet=CharSet.Unicode)] static extern uint RegisterWindowMessage(string s);
  [DllImport("user32.dll")] static extern IntPtr SendMessageTimeout(IntPtr hWnd, uint Msg, IntPtr wParam, IntPtr lParam, uint flags, uint timeout, out UIntPtr result);
  [DllImport("oleacc.dll", PreserveSig=false)] [return: MarshalAs(UnmanagedType.Interface)] static extern object ObjectFromLresult(UIntPtr lResult, [MarshalAs(UnmanagedType.LPStruct)] Guid refiid, IntPtr wParam);
  public static object Doc(IntPtr h) {
    uint msg = RegisterWindowMessage("WM_HTML_GETOBJECT"); UIntPtr res;
    SendMessageTimeout(h, msg, IntPtr.Zero, IntPtr.Zero, 2, 3000, out res);
    if (res == UIntPtr.Zero) return null;
    return ObjectFromLresult(res, new Guid("626FC520-A41E-11CF-A731-00A0C9082637"), IntPtr.Zero);
  }
}
"@

$p = Get-Process -Id $DesktopPid -ErrorAction Stop
"window: '$($p.MainWindowTitle)' responding=$($p.Responding)"
[void]$p.CloseMainWindow()
$root = [System.Windows.Automation.AutomationElement]::RootElement
$byPid = New-Object System.Windows.Automation.PropertyCondition([System.Windows.Automation.AutomationElement]::ProcessIdProperty, [int]$DesktopPid)
$ieClass = New-Object System.Windows.Automation.PropertyCondition([System.Windows.Automation.AutomationElement]::ClassNameProperty, 'Internet Explorer_Server')
$clicked = $false
for ($i = 0; $i -lt 40 -and -not $clicked; $i++) {
    Start-Sleep -Milliseconds 750
    if (-not (Get-Process -Id $DesktopPid -ErrorAction SilentlyContinue)) { "closed without a dialog (nothing to save)"; exit 0 }
    foreach ($w in $root.FindAll([System.Windows.Automation.TreeScope]::Children, $byPid)) {
        $ie = $w.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $ieClass)
        if (-not $ie) { continue }
        $doc = [HtmlDlg]::Doc([IntPtr]$ie.Current.NativeWindowHandle)
        if (-not $doc) { continue }
        $text = ("" + $doc.body.innerText) -replace "\s+", " "
        if ($text -notmatch "opslaan") { continue }
        "dialog: $text"
        foreach ($e in $doc.all) {
            if (("" + $e.className) -match "o-action-button" -and ("" + $e.innerText).Trim() -eq $Answer) { $e.click(); "answered '$Answer'"; $clicked = $true; break }
        }
        if ($clicked) { break }
    }
}
if (-not $clicked) { "no save dialog found in 30 s; the window is still open"; exit 1 }
for ($i = 0; $i -lt 120; $i++) { if (-not (Get-Process -Id $DesktopPid -ErrorAction SilentlyContinue)) { "Desktop $DesktopPid has closed"; exit 0 }; Start-Sleep -Milliseconds 750 }
"Desktop $DesktopPid is still running after 90 s"; exit 1
