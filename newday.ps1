# Description: A PowerShell script to create a new folder and copy over the template file for a new day of Advent of Code 2024. The day needs to be passed as the first argument. If the folder already exists, the script will stop. Generated with AI.
#
# Usage: .\newday.ps1 <day_number>

param (
    [Parameter(Position = 0, Mandatory = $true)]
    [int]$number
)

# Define the folder name and the new file name
$folderName = $number.ToString()
$newFileName = "day$($number).py"
$templateFile = "template.py"

# Check if the folder already exists
if (Test-Path -Path $folderName) {
    Write-Host "The folder '$folderName' already exists. Exiting script." -ForegroundColor Red
    exit
}

# Create the new folder
New-Item -Path $folderName -ItemType Directory | Out-Null
Write-Host "Created folder: $folderName" -ForegroundColor Green

# Check if the template file exists
if (-Not (Test-Path -Path $templateFile)) {
    Write-Host "The file '$templateFile' does not exist in the root directory. Exiting script." -ForegroundColor Red
    exit
}

# Copy the template file to the new folder with the new name
Copy-Item -Path $templateFile -Destination "$folderName\$newFileName"
Write-Host "Copied '$templateFile' to '$folderName' as '$newFileName'" -ForegroundColor Green
