@echo off
set "keyword=v0c0n,"

REM Get the directory of the batch file
set "masterdir=%~dp0"

REM Recursively go through all .txt files in the directory and subdirectories
for /r "%masterdir%" %%f in (*.txt) do (
    REM Read the original content and prepend the keyword to it
    (echo|set /p=%keyword% <nul & type "%%f") > "%%f.tmp"
    
    REM Replace the original file with the modified file
    move /y "%%f.tmp" "%%f" >nul
)

echo Keyword prepended to all .txt files in %masterdir% and subdirectories.
pause
