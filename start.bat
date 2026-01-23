@echo off
REM Portfolio Server Start Script

echo.
echo ============================================
echo   Starting Portfolio Server
echo ============================================
echo.

cd backend

REM Check if node_modules exists
if not exist "node_modules" (
    echo ⚠️  Dependencies not found. Installing...
    call npm install
    echo.
)

REM Check if .env exists
if not exist ".env" (
    echo ⚠️  .env file not found!
    echo Please run setup.bat first
    pause
    exit /b 1
)

echo.
echo 🚀 Starting server...
echo.
echo Server will run at: http://localhost:3000
echo.
echo Press Ctrl+C to stop the server
echo.

npm start

pause
