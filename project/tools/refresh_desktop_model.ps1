<#
Refresh the semantic model that a running Power BI Desktop instance has open, without
touching the Desktop UI. Uses the Tabular object model shipped inside the Store build of
Desktop and connects to Desktop's local Analysis Services port.

Usage (Windows PowerShell 5.1):
  powershell -ExecutionPolicy Bypass -File project\tools\refresh_desktop_model.ps1            # single instance
  powershell -ExecutionPolicy Bypass -File project\tools\refresh_desktop_model.ps1 -Port 61829

Finds the port from netstat when not given (the local port with the most ESTABLISHED
connections owned by msmdsrv). A first refresh of the PillowKey model asks Desktop for the
anonymous-access choice on the blob URL once: click "Verbinden" in the dialog Desktop shows.
Takes about 12 minutes on this connection (16 Excel sheet reads from the public blob).
#>
param([int]$Port = 0, [string]$DesktopBin = "")

if (-not $DesktopBin) {
    $proc = Get-Process PBIDesktop -ErrorAction Stop | Select-Object -First 1
    $DesktopBin = Split-Path $proc.Path   # WindowsApps is not listable; the running process tells us where bin is
}
Add-Type -Path "$DesktopBin\Microsoft.AnalysisServices.Server.Core.dll"
Add-Type -Path "$DesktopBin\Microsoft.AnalysisServices.Server.Tabular.dll"

if ($Port -eq 0) {
    $pids = (Get-Process msmdsrv -ErrorAction Stop).Id
    $counts = @{}
    foreach ($line in (netstat -ano)) {
        if ($line -match '^\s*TCP\s+\[?::1\]?:(\d+)\s+\S+\s+ESTABLISHED\s+(\d+)\s*$' -and $pids -contains [int]$Matches[2]) {
            $counts[$Matches[1]] = 1 + $counts[$Matches[1]]
        }
    }
    if ($counts.Count -eq 0) { throw "No Desktop Analysis Services instance found; open a .pbip first." }
    $Port = [int](($counts.GetEnumerator() | Sort-Object Value -Descending | Select-Object -First 1).Key)
}
"Connecting to localhost:$Port"
$srv = New-Object Microsoft.AnalysisServices.Tabular.Server
$srv.Connect("Data Source=localhost:$Port")
$db = $srv.Databases[0]
"Model: $($db.Model.Tables.Count) tables"
$db.Model.RequestRefresh([Microsoft.AnalysisServices.Tabular.RefreshType]::Full)
$sw = [Diagnostics.Stopwatch]::StartNew()
try { $db.Model.SaveChanges() | Out-Null; "Refresh done in $([int]$sw.Elapsed.TotalSeconds)s" }
catch { "Refresh failed: $($_.Exception.Message) $($_.Exception.InnerException.Message)" }
foreach ($t in $db.Model.Tables) {
    foreach ($p in $t.Partitions) { if ($p.State -ne "Ready") { "$($t.Name): $($p.State) $(($p.ErrorMessage -split "`n")[0])" } }
}
$srv.Disconnect()
"Then: powerbi-desktop reload --pid <desktop pid> and screenshot."
