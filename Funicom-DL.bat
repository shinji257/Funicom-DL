@echo off
cd /D %~dp0
:lp
if exist "Funicom-DL.que.que" del Funicom-DL.que.tmp
copy Funicom-DL.que Funicom-DL.que.tmp
if exist "Funicom-DL.que.bak" del Funicom-DL.que.bak
copy Funicom-DL.que Funicom-DL.que.bak
set g=-l e -fb
set u=False
for /F "tokens=*" %%A in (Funicom-DL.que.tmp) do call :pro %%A
del Funicom-DL.que.tmp

goto :EOF
:pro
set toRun=rem none
if "%~1"=="" goto :EOF
if "%~1"=="#" goto :EOF
set i=%~1
if "%i:~0,1%"=="#" goto :EOF
if "%~1"=="--skip" if /I "%~2"=="" set t_s=
if "%~1"=="--skip" if /I "%~2"=="" if "%s%"=="True" set t_s=False
if "%~1"=="--skip" if /I "%~2"=="" if "%s%"=="False" set t_s=True
if "%~1"=="--skip" if /I "%~2"=="" set s=%t_s%
if "%~1"=="--skip" if /I "%~2"=="True" set s=True
if "%~1"=="--skip" if /I "%~2"=="T" set s=True
if "%~1"=="--skip" if /I "%~2"=="1" set s=True
if "%~1"=="--skip" if /I "%~2"=="On" set s=True
if "%~1"=="--skip" if /I "%~2"=="False" set s=False
if "%~1"=="--skip" if /I "%~2"=="F" set s=False
if "%~1"=="--skip" if /I "%~2"=="2" set s=False
if "%~1"=="--skip" if /I "%~2"=="Off" set s=False
if "%~1"=="-S" if /I "%~2"=="" set t_s=
if "%~1"=="-S" if /I "%~2"=="" if "%s%"=="True" set t_s=False
if "%~1"=="-S" if /I "%~2"=="" if "%s%"=="False" set t_s=True
if "%~1"=="-S" if /I "%~2"=="" set s=%t_s%
if "%~1"=="-S" if /I "%~2"=="True" set s=True
if "%~1"=="-S" if /I "%~2"=="T" set s=True
if "%~1"=="-S" if /I "%~2"=="1" set s=True
if "%~1"=="-S" if /I "%~2"=="On" set s=True
if "%~1"=="-S" if /I "%~2"=="False" set s=False
if "%~1"=="-S" if /I "%~2"=="F" set s=False
if "%~1"=="-S" if /I "%~2"=="2" set s=False
if "%~1"=="-S" if /I "%~2"=="Off" set s=False
if "%s%"=="True" goto :EOF
if "%~1"=="--global" set g=%*
if "%~1"=="--global" set g=%g:~8%
if "%~1"=="--global" goto :EOF
if "%~1"=="-G" set g=%*
if "%~1"=="-G" set g=%g:~2%
if "%~1"=="-G" goto :EOF
if "%~1"=="--uploader" if /I "%~2"=="" set t_u=
if "%~1"=="--uploader" if /I "%~2"=="" if "%u%"=="True" set t_u=False
if "%~1"=="--uploader" if /I "%~2"=="" if "%u%"=="False" set t_u=True
if "%~1"=="--uploader" if /I "%~2"=="" set u=%t_u%
if "%~1"=="--uploader" if /I "%~2"=="True" set u=True
if "%~1"=="--uploader" if /I "%~2"=="T" set u=True
if "%~1"=="--uploader" if /I "%~2"=="1" set u=True
if "%~1"=="--uploader" if /I "%~2"=="On" set u=True
if "%~1"=="--uploader" if /I "%~2"=="False" set u=False
if "%~1"=="--uploader" if /I "%~2"=="F" set u=False
if "%~1"=="--uploader" if /I "%~2"=="2" set u=False
if "%~1"=="--uploader" if /I "%~2"=="Off" set u=False
if "%~1"=="--uploader" goto :EOF
if "%~1"=="-U" if /I "%~2"=="" set t_u=
if "%~1"=="-U" if /I "%~2"=="" if "%u%"=="True" set t_u=False
if "%~1"=="-U" if /I "%~2"=="" if "%u%"=="False" set t_u=True
if "%~1"=="-U" if /I "%~2"=="" set u=%t_u%
if "%~1"=="-U" if /I "%~2"=="True" set u=True
if "%~1"=="-U" if /I "%~2"=="T" set u=True
if "%~1"=="-U" if /I "%~2"=="1" set u=True
if "%~1"=="-U" if /I "%~2"=="On" set u=True
if "%~1"=="-U" if /I "%~2"=="False" set u=False
if "%~1"=="-U" if /I "%~2"=="F" set u=False
if "%~1"=="-U" if /I "%~2"=="2" set u=False
if "%~1"=="-U" if /I "%~2"=="Off" set u=False
if "%~1"=="-U" goto :EOF
if "%~1"=="--quit" del Funicom-DL.que.tmp
if "%~1"=="--quit" exit
if "%~1"=="-Q" del Funicom-DL.que.tmp
if "%~1"=="-Q" exit
if "%~1"=="-R" if _%2_==__ goto :EOF
if "%~1"=="-R" set toRun=%*
if "%~1"=="-R" set toRun=%toRun:~2%
if "%~1"=="-R" echo running && %toRun% && echo ran
if "%~1"=="-R" goto :EOF
if "%~1"=="--run" if _%2_==__ goto :EOF
if "%~1"=="--run" set toRun=%*
if "%~1"=="--run" set toRun=%toRun:~5%
if "%~1"=="--run" echo running && %toRun% && echo ran
if "%~1"=="--run" goto :EOF
if not exist "tmp" MD "tmp"
CD tmp
if exist "..\Funicom-DL.py" copy "..\Funicom-DL.py" "Funicom-DL.py"
echo %*>cur.que
if exist "..\UserExcept.pyni" copy "..\UserExcept.pyni" UserExcept.py
if not exist "..\UserExcept.pyni" if exist "..\UserExcept.py.ini" copy "..\UserExcept.py.ini" UserExcept.py
if exist "..\PikaExcept.pycni" copy "..\PikaExcept.pycni" PikaExcept.pyc
if not exist "..\PikaExcept.pycni" if exist "..\PikaExcept.pyni" copy "..\PikaExcept.pyni" PikaExcept.py
if "%u%"=="False" Funicom-DL.py %* %g%
if "%u%"=="True" Funicom-DL.py %* %g% -q 720p
if "%u%"=="True" Funicom-DL.py %* %g% -q 1080p
del cur.que
cd ..
RD /S /Q tmp

goto :EOF