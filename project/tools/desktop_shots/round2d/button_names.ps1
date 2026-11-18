param([int]$ProcId, [string]$Match = 'Recommended|What waits|Build your own|Brand Review|Next')
# Review round 2, step E: what Desktop hands a screen reader for the report's buttons (name and help text), read from the
# window's UI Automation tree. A button whose action still carries Power BI's own tooltip shows it here as its help text
# or at the end of its name ("... Ctrl+klik hier om te volgen"); with visualLink.showDefaultTooltip false it must not.
# The WebView's elements appear only after one full walk of the tree, so the tree is walked twice.
Add-Type -AssemblyName UIAutomationClient, UIAutomationTypes
$root = [System.Windows.Automation.AutomationElement]::RootElement
$cond = New-Object System.Windows.Automation.PropertyCondition([System.Windows.Automation.AutomationElement]::ProcessIdProperty, [int]$ProcId)
$win = $root.FindFirst([System.Windows.Automation.TreeScope]::Children, $cond)
if (-not $win) { "no window for $ProcId"; exit 1 }
$null = $win.FindAll([System.Windows.Automation.TreeScope]::Descendants, [System.Windows.Automation.Condition]::TrueCondition)
Start-Sleep -Seconds 2
$all = $win.FindAll([System.Windows.Automation.TreeScope]::Descendants, [System.Windows.Automation.Condition]::TrueCondition)
"elements: $($all.Count)"
$seen = @{}
foreach ($e in $all) {
  $n = $e.Current.Name
  if ($n -match $Match -and $n.Length -lt 260) {
    $line = "$($e.Current.ControlType.ProgrammaticName -replace 'ControlType\.','') | name: $n | help: $($e.Current.HelpText) | status: $($e.Current.ItemStatus)"
    if (-not $seen.ContainsKey($line)) { $seen[$line] = 1; $line }
  }
}
