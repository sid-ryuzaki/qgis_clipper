::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFDpQQQ2MAE+1EbsQ5+n//NbS9xgcB+dtesKI2bLZbbRH7EapLcB9gTdfnZMJVUpdJ0qoOAwL+iBLtWvl
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSjk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdDyDJGij3XEPCxddXBSHLleLIZwv18v35vqXp18hZcUWS8/41r2eMOUBpED8cPY=
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off

setlocal enabledelayedexpansion

REM "C:\Program Files\QGIS 3.22.16\bin\python-qgis-ltr.bat" main.py

REM Path to the configuration file
set "config_file=config.txt"

for /f "tokens=1,2 delims==" %%A in (%config_file%) do (
    set "%%A=%%B"
)

REM Check if setting is empty

if "%qgis_path%" == "" (
    GOTO ASK_INPUT
) else (
    GOTO RUN
)



:ASK_INPUT
set /P qgis_path=Enter QGIS installation path (eg. C:\Program Files\QGIS 3.22.16):

REM write to file
echo qgis_path=%qgis_path% > config.txt
GOTO RUN

:RUN

SetLocal EnableDelayedExpansion

REM Remove trailing spaces

for /f "tokens=* delims= " %%a in ("%qgis_path%") do set qgis_path=%%a
for /l %%a in (1,1,100) do if "!qgis_path:~-1!"==" " set qgis_path=!qgis_path:~0,-1!

"%qgis_path%\bin\python-qgis-ltr.bat" main.py

endlocal
