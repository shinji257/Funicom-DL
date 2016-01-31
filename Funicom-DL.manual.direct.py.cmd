@echo off
CD /D %~dp0
for /F "tokens=*" %%A in (Funicom-DL.manual.direct.py.que) do call :pro %%A

goto :eof
:pro
mkdir tmp
cd tmp
"..\Funicom-DL.manual.direct.py" "%~1"
cd ..
rd /S /Q tmp
goto :EOF
