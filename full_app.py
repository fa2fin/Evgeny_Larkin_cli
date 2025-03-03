import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Файловый Менеджер")

        # Создание текстового поля для вывода информации
        self.text_area = scrolledtext.ScrolledText(root, width=50, height=20)
        self.text_area.pack(pady=10)

        # Создание кнопок
        self.create_buttons()

        self.current_directory = os.getcwd()
        self.update_text_area(f"Текущий каталог: {self.current_directory}\n")

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        btn_ls = tk.Button(button_frame, text="Содержимое директории", command=self.list_directory)
        btn_cd = tk.Button(button_frame, text="Переход в директорию", command=self.change_directory)
        btn_cp = tk.Button(button_frame, text="Копирование", command=self.copy_file)
        btn_mv = tk.Button(button_frame, text="Перемещение", command=self.move_file)
        btn_rm = tk.Button(button_frame, text="Удаление", command=self.remove_file)
        btn_help = tk.Button(button_frame, text="Помощь", command=self.print_help)
        btn_exit = tk.Button(button_frame, text="Выход", command=self.exit_app)

        btn_ls.pack(side=tk.LEFT, padx=5)
        btn_cd.pack(side=tk.LEFT, padx=5)
        btn_cp.pack(side=tk.LEFT, padx=5)
        btn_mv.pack(side=tk.LEFT, padx=5)
        btn_rm.pack(side=tk.LEFT, padx=5)
        btn_help.pack(side=tk.LEFT, padx=5)
        btn_exit.pack(side=tk.LEFT, padx=5)

    def update_text_area(self, message):
        self.text_area.insert(tk.END, message)
        self.text_area.see(tk.END)

    def list_directory(self):
        items = os.listdir(self.current_directory)
        self.update_text_area("Содержимое текущего каталога:\n" + "\n".join(items) + "\n")

    def change_directory(self):
        path = filedialog.askdirectory(initialdir=self.current_directory)
        if path:
            try:
                os.chdir(path)
                self.current_directory = os.getcwd()
                self.update_text_area(f"Перешли в каталог: {self.current_directory}\n")
            except Exception as e:
                self.update_text_area(f"Ошибка: {e}\n")

    def copy_file(self):
        src = filedialog.askopenfilename()
        dst = filedialog.asksaveasfilename(initialdir=self.current_directory)
        if src and dst:
            try:
                shutil.copy(src, dst)
                self.update_text_area(f"Скопирован: {src} -> {dst}\n")
            except Exception as e:
                self.update_text_area(f"Ошибка: {e}\n")

    def move_file(self):
        src = filedialog.askopenfilename()
        dst = filedialog.asksaveasfilename(initialdir=self.current_directory)
        if src and dst:
            try:
                shutil.move(src, dst)
                self.update_text_area(f"Перемещен: {src} -> {dst}\n")
            except Exception as e:
                self.update_text_area(f"Ошибка: {e}\n")

    def remove_file(self):
        path = filedialog.askopenfilename()
        if path:
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    self.update_text_area(f"Удален каталог: {path}\n")
                else:
                    os.remove(path)
                    self.update_text_area(f"Удален файл: {path}\n")
            except Exception as e:
                self.update_text_area(f"Ошибка: {e}\n")

    def print_help(self):
        help_text = """
        Доступные команды:
        - ls                : Показать содержимое текущего каталога.
        - cd                : Перейти в указанный каталог.
        - cp                : Скопировать файл или каталог.
        - mv                : Переместить файл или каталог.
        - rm                : Удалить файл или каталог.
        - help              : Показать это сообщение.
        - exit              : Выйти из программы.
        """
        self.update_text_area(help_text)

    def exit_app(self):
        confirmed = messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?")
        if confirmed:
            self.root.quit()


def main():
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()