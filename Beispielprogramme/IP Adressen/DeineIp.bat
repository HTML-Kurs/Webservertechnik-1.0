@echo off
color 2
echo Deine (Remote) IP ist: 
for /f "skip=4 usebackq tokens=2" %%a in (`nslookup myip.opendns.com resolver1.opendns.com`) do echo %%a
pause > Nul
