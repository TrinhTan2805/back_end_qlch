@echo off
cd /d D:\duongdan\fastapi_project

REM Kích hoạt môi trường ảo
call venv\Scripts\activate.bat

REM Chạy FastAPI bằng Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000

pause
