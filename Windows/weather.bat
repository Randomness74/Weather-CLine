@echo off
set arg1=%1
set arg2=%2
set arg3=%3
shift
shift
shift
REM The below is a hot mess, due to batch limitations. Basically, it is a layered if statement.
REM Remember to place file path with your path to the py file. And also add this file to path if you want to have this as a system command.
if "%arg2%"=="" (if "%arg3%"=="" (python "\path\to\file\weather.py" "%arg1%") else (python "\path\to\file\weather.py" "%arg1%" "%arg3%" )) else (if "%arg3%"=="" (python "\path\to\file\weather.py" "%arg1%" "%arg2%") else (python "\path\to\file\weather.py" "%arg1%" "%arg2%" "%arg3%"))
