@echo off
cd backend
echo Installing/Verifying dependencies...
pip install -r requirements.txt
cls
echo Starting EDITH...
python edith_terminal.py
pause
