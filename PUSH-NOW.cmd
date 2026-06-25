@echo off
cd /d "%~dp0"
echo ============================================
echo  Day plugin content-engine-by-ruby len GitHub
echo ============================================
echo.
echo [1/4] Go bo file lock ket lai...
del /q ".git\index.lock" ".git\HEAD.lock" 2>nul
echo [2/4] Them .gitignore da va...
git add .gitignore
echo [3/4] Commit not vet va...
git commit -m "harden .gitignore: ignore all hidden config secret files"
echo [4/4] Day len GitHub (commit v0.16.0 + va .gitignore)...
git push
echo.
echo ============================================
echo  XONG. Doc dong tren xem co bao loi khong.
echo  Neu thay 'Everything up-to-date' hoac ten branch -^> da day thanh cong.
echo ============================================
pause
