import os
import shutil
import func


def main():
    print("Добро пожаловать в файловый менеджер! Введите 'help' для получения списка команд.")
    while True:
        command = input(f"{os.getcwd()}> ").strip().split()

        if not command:
            continue

        cmd = command[0]

        if cmd == 'help':
            func.print_help()

        elif cmd == 'ls':
            func.list_directory()

        elif cmd == 'cd':
            if len(command) > 1:
                func.change_directory(command[1])
            else:
                print("Ошибка: Не указан путь для перехода.")


if __name__ == "__main__":
    main()
