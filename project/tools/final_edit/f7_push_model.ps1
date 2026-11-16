<#
Doc 36 (16 Nov 2026 evening): bring the model that an OPEN Power BI Desktop window holds in line with the files after
f7_package_a.py, without reopening the window. Run with Windows PowerShell 5.1 (pwsh 7 cannot load Desktop's DLLs):

  powershell -ExecutionPolicy Bypass -File project\tools\final_edit\f7_push_model.ps1 -DesktopPid <pid> -Port <AS port> -Model <that copy's .SemanticModel dir>

1. the measures (sync_measures_to_desktop.ps1 on that copy's _Measures.tmdl);
2. the lineage tag of the one new measure, so a save writes the tag the files carry;
3. the two titles of the calculated table WaitOption (Tranche -> Step), then that table recalculated.
#>
param([int]$DesktopPid, [int]$Port, [string]$Model)

& powershell -ExecutionPolicy Bypass -File "$PSScriptRoot\..\sync_measures_to_desktop.ps1" -Port $Port -Tmdl "$Model\definition\tables\_Measures.tmdl" | Where-Object { $_ -notmatch '^Parsed' }

$bin = Split-Path (Get-Process -Id $DesktopPid).Path
Add-Type -Path "$bin\Microsoft.AnalysisServices.Server.Core.dll"; Add-Type -Path "$bin\Microsoft.AnalysisServices.Server.Tabular.dll"
$srv = New-Object Microsoft.AnalysisServices.Tabular.Server; $srv.Connect("Data Source=localhost:$Port")
$tom = $srv.Databases[0].Model  # not $model: PowerShell names ignore case, and -Model is the folder

$tagLine = (Select-String -Path "$Model\definition\tables\_Measures.tmdl" -Pattern "measure 'Move Row Tint'" -Context 0, 4 -Encoding UTF8).Context.PostContext | Where-Object { $_ -match 'lineageTag: (\S+)' } | Select-Object -First 1
$tag = if ($tagLine -match 'lineageTag: (\S+)') { $Matches[1] } else { '' }
$m = $tom.Tables["_Measures"].Measures["Move Row Tint"]
if ($m -and $tag -and $m.LineageTag -ne $tag) { $m.LineageTag = $tag; "lineage tag of Move Row Tint set" }

$w = $tom.Tables["WaitOption"]
$p = $w.Partitions[0]
$old = $p.Source.Expression
$new = $old.Replace('"Tranche 2 ', '"Step 2 ').Replace('"Tranche 3 ', '"Step 3 ')
if ($new -ne $old) { $p.Source.Expression = $new; "WaitOption: titles reworded" } else { "WaitOption: titles already say Step" }
try { $tom.SaveChanges() | Out-Null; "saved" } catch { "SAVE FAILED: $($_.Exception.Message) $($_.Exception.InnerException.Message)"; $srv.Disconnect(); exit 1 }
if ($new -ne $old) {
    try { $w.RequestRefresh([Microsoft.AnalysisServices.Tabular.RefreshType]::Calculate); $tom.SaveChanges() | Out-Null; "WaitOption recalculated" }
    catch { "RECALC FAILED: $($_.Exception.Message) $($_.Exception.InnerException.Message)"; $srv.Disconnect(); exit 1 }
}
"measures in the open model: " + $tom.Tables["_Measures"].Measures.Count
$srv.Disconnect()
