@echo off
cd /d F:\hoctap\Python-Sysadmin\FindDeleteFile
powershell -Command "Start-Process 'F:\hoctap\Python-Sysadmin\.venv\Scripts\python.exe' -ArgumentList 'FindDeleteFile.py' -Verb RunAs"
pause