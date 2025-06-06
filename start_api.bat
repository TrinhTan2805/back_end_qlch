@echo off
REM Kích hoạt môi trường ảo Python
call "%~dp0venv\Scripts\activate.bat"

REM Di chuyển vào thư mục chứa mã nguồn (nếu cần)
cd /d "%~dp0"

REM Chạy FastAPI (hoặc Flask tùy bạn)
uvicorn main:app --host 0.0.0.0 --port 8000
