import keyboard
import subprocess
import os
import tempfile

REPO_PATH = r"C:\Users\thinzano\Desktop\git project\project 3"

def git_commit():
    bat_content = f"""@echo off
cd /d "{REPO_PATH}"
git add .
set /p MSG=">> Название коммита: "
git commit -m "%MSG%"
git push
echo.
echo Готово!
pause
"""
    bat_path = os.path.join(tempfile.gettempdir(), "git_commit.bat")
    with open(bat_path, "w", encoding="cp866") as f:
        f.write(bat_content)

    subprocess.Popen(
        ["cmd.exe", "/K", bat_path],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
print("Запущено! Нажми Ctrl+S для создания коммита\n(ПРОВЕРЬ! Правильно ли указан путь, а так же запущена ли консоль от имени администратора)")
keyboard.add_hotkey('ctrl+s', git_commit)
keyboard.wait() 