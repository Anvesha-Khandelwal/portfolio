@echo off
REM Portfolio Setup Script for Windows

echo.
echo ============================================
echo   Portfolio Backend Setup
echo ============================================
echo.

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is not installed!
    echo Please download from: https://nodejs.org/
    pause
    exit /b 1
)

echo ✅ Node.js found: 
node --version

echo.
echo Installing dependencies...
cd backend
call npm install

if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ============================================
echo ✅ Setup Complete!
echo ============================================
echo.
echo Next steps:
echo.
echo 1. Configure Email (Optional):
echo    - Edit backend\.env
echo    - Add your Gmail credentials
echo    - Instructions in backend\README.md
echo.
echo 2. Start the server:
echo    - npm start        (production)
echo    - npm run dev      (development with auto-reload)
echo.
echo 3. Open in browser:
echo    - http://localhost:3000
echo.
echo 4. Send a test message!
echo.
echo ============================================
echo.
pause
