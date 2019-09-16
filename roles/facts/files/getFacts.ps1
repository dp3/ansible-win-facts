#sourced from https://hindenes.com/trondsworking/2016/11/05/using-ansible-as-a-software-inventory-db-for-your-windows-nodes/
$packages = Get-WmiObject -Class Win32_Product
$returnpackages = @{}
foreach ($package in $packages)
{
    $subpackagedictionary = @{"Name" = $Package.Name; "Version" = $Package.Version; "Caption" = $Package.Caption;}
    $returnpackages.Add($Package.Name, $subpackagedictionary)
}
#Write-Host $returnpackages."Google Chrome".Name
#Write-Host $returnpackages."Google Chrome".Version
$returnpackages

