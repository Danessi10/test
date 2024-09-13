@echo off

REM Создание виртуальной среды
python -m venv env

call env\Scripts\activate.bat
pip install -r requirements.txt