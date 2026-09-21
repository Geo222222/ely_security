param([switch]$ApplySafe)
$ErrorActionPreference = "Stop"
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$out = Join-Path $PSScriptRoot "windows-baseline-$stamp.txt"
function Section($name) { "" | Tee-Object -FilePath $out -Append; "==== $name ====" | Tee-Object -FilePath $out -Append }
"ELY WINDOWS HOST GUARD - $(Get-Date -Format o)" | Tee-Object -FilePath $out
Section "Firewall Profiles"
Get-NetFirewallProfile | Select-Object Name,Enabled,DefaultInboundAction,DefaultOutboundAction | Format-Table -AutoSize | Out-String | Tee-Object -FilePath $out -Append
Section "Microsoft Defender"
try { Get-MpComputerStatus | Select-Object AntivirusEnabled,AntispywareEnabled,RealTimeProtectionEnabled,BehaviorMonitorEnabled,IoavProtectionEnabled,NISEnabled,AntivirusSignatureLastUpdated | Format-List | Out-String | Tee-Object -FilePath $out -Append } catch { "Defender status unavailable: $($_.Exception.Message)" | Tee-Object -FilePath $out -Append }
Section "Listening TCP Ports"
Get-NetTCPConnection -State Listen | Sort-Object LocalPort | Select-Object LocalAddress,LocalPort,OwningProcess,@{N='Process';E={(Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).ProcessName}} | Format-Table -AutoSize | Out-String | Tee-Object -FilePath $out -Append
Section "Established TCP Connections"
Get-NetTCPConnection -State Established | Sort-Object RemoteAddress | Select-Object LocalAddress,LocalPort,RemoteAddress,RemotePort,OwningProcess,@{N='Process';E={(Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).ProcessName}} | Format-Table -AutoSize | Out-String | Tee-Object -FilePath $out -Append
Section "SMB Server"
try { Get-SmbServerConfiguration | Select-Object EnableSMB1Protocol,EnableSMB2Protocol,EncryptData,RejectUnencryptedAccess | Format-List | Out-String | Tee-Object -FilePath $out -Append } catch { "SMB status unavailable." | Tee-Object -FilePath $out -Append }
if ($ApplySafe) {
  Section "Applying safe baseline"
  Set-NetFirewallProfile -Profile Domain,Private,Public -Enabled True -DefaultInboundAction Block -DefaultOutboundAction Allow
  try { Set-MpPreference -DisableRealtimeMonitoring $false; "Microsoft Defender real-time monitoring requested ON." | Tee-Object -FilePath $out -Append } catch { "Could not modify Defender: $($_.Exception.Message)" | Tee-Object -FilePath $out -Append }
  "Windows Firewall enabled; inbound default BLOCK; outbound default ALLOW." | Tee-Object -FilePath $out -Append
}
"Report: $out"
Write-Host "No ports were opened and no remote access settings were changed."
