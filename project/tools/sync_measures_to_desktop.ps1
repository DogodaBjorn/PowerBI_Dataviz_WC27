<#
Push the _Measures table from the TMDL on disk into a running Power BI Desktop instance
(expressions, format strings, display folders, descriptions) without reopening the file.
Use after regenerating the model with sketch_model.py while Desktop has the PBIP open.

  powershell -ExecutionPolicy Bypass -File project\tools\sync_measures_to_desktop.ps1 -Port 61829

Only measures are synced; columns, tables and relationships still need a reopen.
#>
param([int]$Port, [string]$Tmdl = "$PSScriptRoot\..\pbip\PillowKey.SemanticModel\definition\tables\_Measures.tmdl", [string]$DesktopBin = "")

if (-not $DesktopBin) {
    $proc = Get-Process PBIDesktop -ErrorAction Stop | Select-Object -First 1
    $DesktopBin = Split-Path $proc.Path   # WindowsApps is not listable; the running process tells us where bin is
}
Add-Type -Path "$DesktopBin\Microsoft.AnalysisServices.Server.Core.dll"
Add-Type -Path "$DesktopBin\Microsoft.AnalysisServices.Server.Tabular.dll"

$lines = Get-Content $Tmdl -Encoding UTF8
$measures = @{}
$doc = ""
for ($i = 0; $i -lt $lines.Count; $i++) {
    $l = $lines[$i]
    if ($l -match '^\t/// (.*)$') { $doc = $Matches[1]; continue }
    if ($l -match "^\tmeasure (?:'([^']+)'|(\S+)) = (.*)$") {
        $name = if ($Matches[1]) { $Matches[1] } else { $Matches[2] }
        $m = @{ expr = $Matches[3]; fmt = ""; folder = ""; doc = $doc }
        for ($j = $i + 1; $j -lt $lines.Count -and $lines[$j] -match '^\t\t'; $j++) {
            if ($lines[$j] -match '^\t\tformatString: (.*)$') { $m.fmt = $Matches[1] }
            if ($lines[$j] -match '^\t\tdisplayFolder: (.*)$') { $m.folder = $Matches[1] }
        }
        $measures[$name] = $m; $doc = ""
    }
}
"Parsed $($measures.Count) measures from TMDL"

$srv = New-Object Microsoft.AnalysisServices.Tabular.Server
$srv.Connect("Data Source=localhost:$Port")
$db = $srv.Databases[0]
$t = $db.Model.Tables["_Measures"]
$changed = 0
foreach ($name in $measures.Keys) {
    $m = $t.Measures[$name]; $d = $measures[$name]
    if (-not $m) {
        $m = New-Object Microsoft.AnalysisServices.Tabular.Measure
        $m.Name = $name; $m.Expression = $d.expr; $m.FormatString = $d.fmt; $m.DisplayFolder = $d.folder; $m.Description = $d.doc
        $t.Measures.Add($m); $changed++; "added $name"; continue
    }
    if ($m.Expression -ne $d.expr -or $m.FormatString -ne $d.fmt -or $m.DisplayFolder -ne $d.folder -or $m.Description -ne $d.doc) {
        $m.Expression = $d.expr; $m.FormatString = $d.fmt; $m.DisplayFolder = $d.folder; $m.Description = $d.doc; $changed++; "updated $name"
    }
}
try { $db.Model.SaveChanges() | Out-Null; "Saved: $changed measure(s) changed on port $Port" }
catch { "Save failed: $($_.Exception.Message) $($_.Exception.InnerException.Message)" }
$srv.Disconnect()
