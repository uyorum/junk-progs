Param($vmname)
if ($vmname -eq $null) {
  Write-Host "Usage: get-vm-address-hyperv.ps1 <VMName>"
  exit
}
$vm = Get-VMNetworkAdapter -VMName $vmname
$address = ($vm.IPAddresses -match "^\d+\.\d+\.\d+\.\d+$") -Join "`n"
[byte[]][char[]]$address | Set-Content -Path "address" -Encoding Byte
