@echo off
echo creating virtual environment
python -m venv venv
call venv\Scripts\activate.bat

echo installing requirements
python -m pip install -r requirements.txt

echo starting app
start pyw -m pfp_maker
