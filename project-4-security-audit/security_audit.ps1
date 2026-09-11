# ===================================================
# DecodeLabs Internship - Project 4
# Personal System Security Audit Script
# ===================================================

Write-Host "=====================================================" -ForegroundColor Cyan
Write-Host "  DecodeLabs Security Audit - $(Get-Date)" -ForegroundColor Cyan
Write-Host "=====================================================" -ForegroundColor Cyan

$findings = @()

function Report-Finding {
    param($Category, $Check, $Status, $Detail, $Severity)
    $color = switch ($Status) {
        "PASS" { "Green" }
        "FAIL" { "Red" }
        default { "Yellow" }
    }
    Write-Host "`n[$Category] $Check" -ForegroundColor White
    Write-Host "  Status: $Status" -ForegroundColor $color
    Write-Host "  Detail: $Detail"
    if ($Status -eq "FAIL") {
        Write-Host "  Severity: $Severity" -ForegroundColor Yellow
        $script:findings += [PSCustomObject]@{
            Category = $Category
            Check    = $Check
            Detail   = $Detail
            Severity = $Severity
        }
    }
}

# --- STEP 1: IDENTITY / FIREWALL (network layer, but checked here for flow) ---
Write-Host "`n--- STEP 1: Identity & Access ---" -ForegroundColor Magenta
$guest = Get-LocalUser -Name "Guest" -ErrorAction SilentlyContinue
if ($guest) {
    if ($guest.Enabled) {
        Report-Finding "Identity" "Guest Account Status" "FAIL" "Guest account is ENABLED" "Medium"
    } else {
        Report-Finding "Identity" "Guest Account Status" "PASS" "Guest account is disabled" ""
    }
}

# --- STEP 2: PATCH MANAGEMENT ---
Write-Host "`n--- STEP 2: Patch Management ---" -ForegroundColor Magenta
$lastUpdate = Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 1
if ($lastUpdate) {
    $daysSince = (Get-Date) - $lastUpdate.InstalledOn
    if ($daysSince.Days -gt 30) {
        Report-Finding "Patch Management" "Last Windows Update" "FAIL" "Last update was $($lastUpdate.InstalledOn), $($daysSince.Days) days ago" "High"
    } else {
        Report-Finding "Patch Management" "Last Windows Update" "PASS" "Last update was $($lastUpdate.InstalledOn), $($daysSince.Days) days ago" ""
    }
}

# --- STEP 3: HUMAN PERIMETER / ADMIN AUDIT ---
Write-Host "`n--- STEP 3: Human Perimeter ---" -ForegroundColor Magenta
$admins = Get-LocalGroupMember -Group "Administrators"
Report-Finding "Human Perimeter" "Administrator Accounts" "INFO" "$($admins.Count) account(s) with admin rights: $($admins.Name -join ', ')" ""
if ($admins.Count -gt 2) {
    Report-Finding "Human Perimeter" "Admin Account Count" "FAIL" "$($admins.Count) accounts have admin rights - review for privilege creep" "Medium"
}

# --- STEP 4: NETWORK & DISK ---
Write-Host "`n--- STEP 4: Network & Endpoint Hygiene ---" -ForegroundColor Magenta
$fw = Get-NetFirewallProfile
foreach ($profile in $fw) {
    if ($profile.Enabled -eq $true) {
        Report-Finding "Network" "Firewall - $($profile.Name)" "PASS" "Firewall is active" ""
    } else {
        Report-Finding "Network" "Firewall - $($profile.Name)" "FAIL" "Firewall is DISABLED" "Critical"
    }
}

try {
    $bl = Get-BitLockerVolume -MountPoint "C:" -ErrorAction Stop
    if ($bl.ProtectionStatus -eq "On") {
        Report-Finding "Endpoint" "Disk Encryption (BitLocker)" "PASS" "C: drive is encrypted, protection is ON" ""
    } else {
        Report-Finding "Endpoint" "Disk Encryption (BitLocker)" "FAIL" "C: drive protection is OFF" "Critical"
    }
} catch {
    Report-Finding "Endpoint" "Disk Encryption (BitLocker)" "FAIL" "Could not check BitLocker status - may need admin rights" "Critical"
}

# --- SUMMARY ---
Write-Host "`n=====================================================" -ForegroundColor Cyan
Write-Host "  AUDIT SUMMARY" -ForegroundColor Cyan
Write-Host "=====================================================" -ForegroundColor Cyan
if ($findings.Count -eq 0) {
    Write-Host "No critical flaws found. System appears hardened." -ForegroundColor Green
} else {
    Write-Host "$($findings.Count) issue(s) requiring attention:`n" -ForegroundColor Yellow
    $findings | Format-Table -AutoSize
}