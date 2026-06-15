import keyboard
import subprocess

REPO_PATH = r"C:\Users\thinzano\Desktop\git project\project 3"

def open_git_commit():
    cmd = (
        f'cd /d "{REPO_PATH}" && '
        f'git add . && '
        f'set /p MSG=">> Название коммита: " && '
        f'git commit -m "%MSG%" && '
        f'git push && '
        f'echo. && echo Готово! && pause > nul'
    )
    subprocess.Popen(
        ["cmd.exe", "/K", cmd],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

print("Запущено! Нажми Ctrl+S для создания коммита\n(ПРОВЕРЬ! Правильно ли указан путь, а так же запущена ли консоль от имени администратора)")
keyboard.add_hotkey('ctrl+s', open_git_commit)
keyboard.wait() 