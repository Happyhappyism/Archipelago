@echo off
setlocal

::Define apworld name
set "apworld=pokemon_pinball"
:: Define the path to the folder
set "sourceFolder=C:\Gaming\Arch\HappyhappyGit\Archipelago\worlds\%apworld%"
set "outputFolder=C:\Gaming\Arch\HappyhappyGit\Archipelago\worlds"

:: Define the name of the file to delete within the folder
set "fileToDelete=%apworld%.apworld"

:: Define the name for the output zip file
set "zipFileName=%apworld%.apworld"

:: Define the path to 7-Zip executable (adjust if different)
set "sevenZipPath=C:\Program Files\WinRAR\WinRar.exe"

:: 1. Delete the specified file
if exist "%sourceFolder%\%fileToDelete%" (
    del /f /q "%sourceFolder%\%fileToDelete%"
    echo Deleted: "%sourceFolder%\%fileToDelete%"
) else (
    echo File not found: "%sourceFolder%\%fileToDelete%"
)

:: 2. Zip the directory
if exist "%sevenZipPath%" (
	cd "%sourceFolder
    ::pushd "%sourceFolder%"
	::echo "%sevenZipPath%" a "%outputFolder%\%zipFileName%" * .\%*
    "%sevenZipPath%" a -afzip "%apworld%.apworld" "%apworld%"
    ::popd
    echo Zipped "%sourceFolder%" to "%outputFolder%\%zipFileName%"
) else (
    echo 7-Zip executable not found at: "%sevenZipPath%"
    echo Please install 7-Zip or adjust the "sevenZipPath" variable.
)
echo Installing Apworld
"%apworld%.apworld"
endlocal
exit