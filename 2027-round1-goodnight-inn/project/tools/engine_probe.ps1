<#
Ask Power BI Desktop's own engine what it thinks of the model, without opening the project.

Deploys the model's metadata (no data) as a temporary database into the local Analysis Services instance of a
running Desktop, prints the engine's refusal if it has one (the text Desktop hides behind "Er zijn problemen
gevonden"), then lists every measure, column and partition the engine marks with an error, and drops the database.
Use it on a THROWAWAY Desktop window (any file open, also an empty one), never on the project's window.

Input is a .bim: Desktop ships no TMDL reader that PowerShell can load, so export one first with the modelling MCP
(connection_operations ConnectFolder on project/pbip/PillowKey.SemanticModel, then database_operations ExportToBimFile).

  powershell -ExecutionPolicy Bypass -File project\tools\engine_probe.ps1 -Port <AS port> -Bim <model.bim>

The AS port: `netstat -ano` for the msmdsrv process, or refresh_desktop_model.ps1 prints it.
Found with it on 13 Nov 2026: a measure may not carry both formatString and formatStringDefinition.
#>
param([int]$Port, [string]$Bim, [string]$Name = "engine_probe")

$proc = Get-Process PBIDesktop -ErrorAction Stop | Select-Object -First 1
$bin = Split-Path $proc.Path
Add-Type -Path "$bin\Microsoft.AnalysisServices.Server.Core.dll"
Add-Type -Path "$bin\Microsoft.AnalysisServices.Server.Tabular.dll"
Add-Type -Path "$bin\Microsoft.AnalysisServices.Server.Tabular.Json.dll"

$json = [System.IO.File]::ReadAllText($Bim)
$rx = New-Object System.Text.RegularExpressions.Regex('"name":\s*null')
$json = $rx.Replace($json, '"name": "' + $Name + '"', 1)   # a TMDL folder without a database name exports null
try { $db = [Microsoft.AnalysisServices.Tabular.JsonSerializer]::DeserializeDatabase($json) }
catch { "BIM DOES NOT LOAD: " + $_.Exception.InnerException.Message; exit 1 }
$db.Name = $Name; $db.ID = $Name

$srv = New-Object Microsoft.AnalysisServices.Tabular.Server
$srv.Connect("Data Source=localhost:$Port")
$old = $srv.Databases.FindByName($Name)
if ($old) { $old.Drop() }
try {
    $srv.Databases.Add($db) | Out-Null
    $db.Update([Microsoft.AnalysisServices.UpdateOptions]::ExpandFull)
} catch {
    $e = $_.Exception; while ($e.InnerException) { $e = $e.InnerException }
    "ENGINE REFUSES THE MODEL: " + $e.Message
    $srv.Disconnect(); exit 1
}
$srv.Disconnect(); $srv.Connect("Data Source=localhost:$Port")
$live = $srv.Databases.FindByName($Name)
$bad = 0
foreach ($t in $live.Model.Tables) {
    foreach ($m in $t.Measures) { if ($m.ErrorMessage) { $bad++; "MEASURE  [" + $m.Name + "]: " + $m.ErrorMessage } }
    foreach ($c in $t.Columns) { if ($c.ErrorMessage) { $bad++; "COLUMN   " + $t.Name + "[" + $c.Name + "]: " + $c.ErrorMessage } }
    foreach ($p in $t.Partitions) { if ($p.ErrorMessage) { $bad++; "PARTITION " + $t.Name + ": " + $p.ErrorMessage } }
}
$n = ($live.Model.Tables | ForEach-Object { $_.Measures.Count } | Measure-Object -Sum).Sum
"engine accepts the model: $($live.Model.Tables.Count) tables, $n measures, $bad object(s) with an error"
$live.Drop()
$srv.Disconnect()
if ($bad -gt 0) { exit 1 }
