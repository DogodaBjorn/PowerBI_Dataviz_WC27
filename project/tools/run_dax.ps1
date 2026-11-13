<#
Run a DAX query file against the model a running Power BI Desktop has open and write the result as JSON.
A file may hold several EVALUATE statements: the output is a list of tables, each a list of row objects.
Uses the ADOMD client that ships inside Desktop. Read-only. Used by number_checks.py (and build_checks.py).

  powershell -ExecutionPolicy Bypass -File project\tools\run_dax.ps1 -Port <AS port> -Query q.dax -Out result.json

The AS port: refresh_desktop_model.ps1 prints it, or leave -Port 0 to take the single running instance.
#>
param([int]$Port = 0, [string]$Query, [string]$Out)

$proc = Get-Process PBIDesktop -ErrorAction Stop | Select-Object -First 1
$bin = Split-Path $proc.Path
Add-Type -Path "$bin\Microsoft.PowerBI.AdomdClient.dll"
if ($Port -eq 0) {
    $pids = (Get-Process msmdsrv -ErrorAction Stop).Id
    $counts = @{}
    foreach ($line in (netstat -ano)) {
        if ($line -match '^\s*TCP\s+\[?::1\]?:(\d+)\s+\S+\s+ESTABLISHED\s+(\d+)\s*$' -and $pids -contains [int]$Matches[2]) { $counts[$Matches[1]] = 1 + $counts[$Matches[1]] }
    }
    $Port = [int](($counts.GetEnumerator() | Sort-Object Value -Descending | Select-Object -First 1).Key)
}
$con = New-Object Microsoft.AnalysisServices.AdomdClient.AdomdConnection("Data Source=localhost:$Port")
$con.Open()
$text = [System.IO.File]::ReadAllText($Query, [System.Text.Encoding]::UTF8)
# one command per EVALUATE (ADOMD returns one rowset per command); a leading DEFINE block is repeated for each
$define = ""
$body = $text
$i = $text.IndexOf("EVALUATE")
if ($i -gt 0) { $define = $text.Substring(0, $i); $body = $text.Substring($i) }
$parts = [regex]::Split($body, "(?m)^(?=EVALUATE\b)") | Where-Object { $_.Trim() }
$tables = New-Object System.Collections.ArrayList
foreach ($q in $parts) {
    $cmd = $con.CreateCommand(); $cmd.CommandText = $define + $q
    try { $rd = $cmd.ExecuteReader() }
    catch { "QUERY FAILED: " + $_.Exception.InnerException.Message; "  in: " + $q.Substring(0, [Math]::Min(300, $q.Length)); $con.Close(); exit 1 }
    $rows = New-Object System.Collections.ArrayList
    # an error in a measure surfaces on Read, not on ExecuteReader: without this the table came back empty (step 4)
    while ($(try { $rd.Read() } catch { "QUERY FAILED: " + $_.Exception.InnerException.Message; "  in: " + $q.Substring(0, [Math]::Min(300, $q.Length)); $con.Close(); exit 1 })) {
        $row = [ordered]@{}
        for ($c = 0; $c -lt $rd.FieldCount; $c++) {
            $v = $rd.GetValue($c)
            if ($v -is [System.DBNull]) { $v = $null }
            elseif ($v -is [datetime]) { $v = $v.ToString("yyyy-MM-dd") }
            $row[$rd.GetName($c)] = $v
        }
        [void]$rows.Add($row)
    }
    $rd.Close()
    [void]$tables.Add($rows)
}
$con.Close()
$json = ConvertTo-Json -InputObject $tables -Depth 6 -Compress
[System.IO.File]::WriteAllText($Out, $json, (New-Object System.Text.UTF8Encoding($false)))
"run_dax: $($tables.Count) table(s) from localhost:$Port -> $Out"
