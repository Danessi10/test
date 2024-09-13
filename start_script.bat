@echo off
REM Активация виртуальной среды
call env\Scripts\activate.bat

REM Запуск скрипта
python test.py

exit