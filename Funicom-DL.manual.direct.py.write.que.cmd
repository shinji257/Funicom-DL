@echo off
CD /D %~dp0
if not exist "Funicom-DL_Manual.txt" call :CLI
if exist "Funicom-DL_Manual.txt" call :GUI
if exist "Funicom-DL_Manual.txt" del "Funicom-DL_Manual.txt"
if "%prefix%"=="" set prefix=0
if "%def%"=="" set def=480
if "%def%"=="1" set def=1080
if "%def%"=="7" set def=720
if "%def%"=="4" set def=480
if "%def%"=="1080" set bit=4000K
if "%def%"=="720" set bit=3500K
if "%def%"=="480" set bit=2000K
if /I "%prefix%"=="V" set prefix=V
if /I "%prefix%"=="M" set prefix=M
if /I "%lang:~0,1%"=="e" set lang=ENG
if /I "%lang:~0,1%"=="j" set lang=JPN
IF /I "%show:~0,1%"=="A" set show1=A
IF /I "%show:~0,1%"=="B" set show1=B
IF /I "%show:~0,1%"=="C" set show1=C
IF /I "%show:~0,1%"=="D" set show1=D
IF /I "%show:~0,1%"=="E" set show1=E
IF /I "%show:~0,1%"=="F" set show1=F
IF /I "%show:~0,1%"=="G" set show1=G
IF /I "%show:~0,1%"=="H" set show1=H
IF /I "%show:~0,1%"=="I" set show1=I
IF /I "%show:~0,1%"=="J" set show1=J
IF /I "%show:~0,1%"=="K" set show1=K
IF /I "%show:~0,1%"=="L" set show1=L
IF /I "%show:~0,1%"=="M" set show1=M
IF /I "%show:~0,1%"=="N" set show1=N
IF /I "%show:~0,1%"=="O" set show1=O
IF /I "%show:~0,1%"=="P" set show1=P
IF /I "%show:~0,1%"=="Q" set show1=Q
IF /I "%show:~0,1%"=="R" set show1=R
IF /I "%show:~0,1%"=="S" set show1=S
IF /I "%show:~0,1%"=="T" set show1=T
IF /I "%show:~0,1%"=="U" set show1=U
IF /I "%show:~0,1%"=="V" set show1=V
IF /I "%show:~0,1%"=="W" set show1=W
IF /I "%show:~0,1%"=="X" set show1=X
IF /I "%show:~0,1%"=="Y" set show1=Y
IF /I "%show:~0,1%"=="Z" set show1=Z
IF /I "%show:~0,1%"=="0" set show1=0
IF /I "%show:~0,1%"=="1" set show1=1
IF /I "%show:~0,1%"=="2" set show1=2
IF /I "%show:~0,1%"=="3" set show1=3
IF /I "%show:~0,1%"=="4" set show1=4
IF /I "%show:~0,1%"=="5" set show1=5
IF /I "%show:~0,1%"=="6" set show1=6
IF /I "%show:~0,1%"=="7" set show1=7
IF /I "%show:~0,1%"=="8" set show1=8
IF /I "%show:~0,1%"=="9" set show1=9
IF /I "%show:~1,1%"=="A" set show2=A
IF /I "%show:~1,1%"=="B" set show2=B
IF /I "%show:~1,1%"=="C" set show2=C
IF /I "%show:~1,1%"=="D" set show2=D
IF /I "%show:~1,1%"=="E" set show2=E
IF /I "%show:~1,1%"=="F" set show2=F
IF /I "%show:~1,1%"=="G" set show2=G
IF /I "%show:~1,1%"=="H" set show2=H
IF /I "%show:~1,1%"=="I" set show2=I
IF /I "%show:~1,1%"=="J" set show2=J
IF /I "%show:~1,1%"=="K" set show2=K
IF /I "%show:~1,1%"=="L" set show2=L
IF /I "%show:~1,1%"=="M" set show2=M
IF /I "%show:~1,1%"=="N" set show2=N
IF /I "%show:~1,1%"=="O" set show2=O
IF /I "%show:~1,1%"=="P" set show2=P
IF /I "%show:~1,1%"=="Q" set show2=Q
IF /I "%show:~1,1%"=="R" set show2=R
IF /I "%show:~1,1%"=="S" set show2=S
IF /I "%show:~1,1%"=="T" set show2=T
IF /I "%show:~1,1%"=="U" set show2=U
IF /I "%show:~1,1%"=="V" set show2=V
IF /I "%show:~1,1%"=="W" set show2=W
IF /I "%show:~1,1%"=="X" set show2=X
IF /I "%show:~1,1%"=="Y" set show2=Y
IF /I "%show:~1,1%"=="Z" set show2=Z
IF /I "%show:~1,1%"=="0" set show2=0
IF /I "%show:~1,1%"=="1" set show2=1
IF /I "%show:~1,1%"=="2" set show2=2
IF /I "%show:~1,1%"=="3" set show2=3
IF /I "%show:~1,1%"=="4" set show2=4
IF /I "%show:~1,1%"=="5" set show2=5
IF /I "%show:~1,1%"=="6" set show2=6
IF /I "%show:~1,1%"=="7" set show2=7
IF /I "%show:~1,1%"=="8" set show2=8
IF /I "%show:~1,1%"=="9" set show2=9
IF /I "%show:~2,1%"=="A" set show3=A
IF /I "%show:~2,1%"=="B" set show3=B
IF /I "%show:~2,1%"=="C" set show3=C
IF /I "%show:~2,1%"=="D" set show3=D
IF /I "%show:~2,1%"=="E" set show3=E
IF /I "%show:~2,1%"=="F" set show3=F
IF /I "%show:~2,1%"=="G" set show3=G
IF /I "%show:~2,1%"=="H" set show3=H
IF /I "%show:~2,1%"=="I" set show3=I
IF /I "%show:~2,1%"=="J" set show3=J
IF /I "%show:~2,1%"=="K" set show3=K
IF /I "%show:~2,1%"=="L" set show3=L
IF /I "%show:~2,1%"=="M" set show3=M
IF /I "%show:~2,1%"=="N" set show3=N
IF /I "%show:~2,1%"=="O" set show3=O
IF /I "%show:~2,1%"=="P" set show3=P
IF /I "%show:~2,1%"=="Q" set show3=Q
IF /I "%show:~2,1%"=="R" set show3=R
IF /I "%show:~2,1%"=="S" set show3=S
IF /I "%show:~2,1%"=="T" set show3=T
IF /I "%show:~2,1%"=="U" set show3=U
IF /I "%show:~2,1%"=="V" set show3=V
IF /I "%show:~2,1%"=="W" set show3=W
IF /I "%show:~2,1%"=="X" set show3=X
IF /I "%show:~2,1%"=="Y" set show3=Y
IF /I "%show:~2,1%"=="Z" set show3=Z
IF /I "%show:~2,1%"=="0" set show3=0
IF /I "%show:~2,1%"=="1" set show3=1
IF /I "%show:~2,1%"=="2" set show3=2
IF /I "%show:~2,1%"=="3" set show3=3
IF /I "%show:~2,1%"=="4" set show3=4
IF /I "%show:~2,1%"=="5" set show3=5
IF /I "%show:~2,1%"=="6" set show3=6
IF /I "%show:~2,1%"=="7" set show3=7
IF /I "%show:~2,1%"=="8" set show3=8
IF /I "%show:~2,1%"=="9" set show3=9
IF /I "%show:~3,1%"=="A" set show4=A
IF /I "%show:~3,1%"=="B" set show4=B
IF /I "%show:~3,1%"=="C" set show4=C
IF /I "%show:~3,1%"=="D" set show4=D
IF /I "%show:~3,1%"=="E" set show4=E
IF /I "%show:~3,1%"=="F" set show4=F
IF /I "%show:~3,1%"=="G" set show4=G
IF /I "%show:~3,1%"=="H" set show4=H
IF /I "%show:~3,1%"=="I" set show4=I
IF /I "%show:~3,1%"=="J" set show4=J
IF /I "%show:~3,1%"=="K" set show4=K
IF /I "%show:~3,1%"=="L" set show4=L
IF /I "%show:~3,1%"=="M" set show4=M
IF /I "%show:~3,1%"=="N" set show4=N
IF /I "%show:~3,1%"=="O" set show4=O
IF /I "%show:~3,1%"=="P" set show4=P
IF /I "%show:~3,1%"=="Q" set show4=Q
IF /I "%show:~3,1%"=="R" set show4=R
IF /I "%show:~3,1%"=="S" set show4=S
IF /I "%show:~3,1%"=="T" set show4=T
IF /I "%show:~3,1%"=="U" set show4=U
IF /I "%show:~3,1%"=="V" set show4=V
IF /I "%show:~3,1%"=="W" set show4=W
IF /I "%show:~3,1%"=="X" set show4=X
IF /I "%show:~3,1%"=="Y" set show4=Y
IF /I "%show:~3,1%"=="Z" set show4=Z
IF /I "%show:~3,1%"=="0" set show4=0
IF /I "%show:~3,1%"=="1" set show4=1
IF /I "%show:~3,1%"=="2" set show4=2
IF /I "%show:~3,1%"=="3" set show4=3
IF /I "%show:~3,1%"=="4" set show4=4
IF /I "%show:~3,1%"=="5" set show4=5
IF /I "%show:~3,1%"=="6" set show4=6
IF /I "%show:~3,1%"=="7" set show4=7
IF /I "%show:~3,1%"=="8" set show4=8
IF /I "%show:~3,1%"=="9" set show4=9
SET show=%show1%%show2%%show3%
if "%end%"=="" set end=%begin%
For /L %%A in (%begin%,1,%end%) do call :pro %%A

:pro
set epi=%~1
if %epi% LSS 10 set epi=0%epi%
if %epi% LSS 100 set epi=0%epi%
echo %show%%lang%%prefix%%epi%-%def%-%bit%>>"Funicom-DL.manual.direct.py.que"
goto :EOF

:CLI
echo show 3 letter code?
set /P show={[A-Z0-9][A-Z0-9][A-Z0-9]}:
echo show 3 letter lang code?
set /P lang={ENG,JPN}:
echo Start Episode?
set /P begin={1-999}:
echo End Episode?
set /P end={1-999}:
echo Prefix?
set /P prefix={M=movie,V=ova,0=episode}:
set /P def={1080,720,480}:

goto :EOF

:GUI
set firstline=True
Set InputFile=Funicom-DL_Manual.txt
for /F "tokens=*" %%A in (%InputFile%) do call :subproA %%A
goto :EOF

:subproA
set out=%*
if "%firstline%"=="True" set %out:~3%
if "%firstline%"=="False" set %out%
set firstline=False
goto :EOF