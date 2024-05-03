import os
import shutil

class FileManager:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.current_dir = base_dir

    def list_dir(self):
        files = os.listdir(self.current_dir)
        for file in files:
            print(file)

    def change_dir(self, directory):
        if directory == "go_to_base_dir":
            if self.current_dir != self.base_dir:
                self.current_dir = os.path.dirname(self.current_dir)
                print("Текущая директория:", self.current_dir)
            else:
                print("Вы уже находитесь в базовой директории")
        else:
            new_dir = os.path.join(self.current_dir, directory)
            if os.path.isdir(new_dir) and new_dir.startswith(self.base_dir):
                self.current_dir = new_dir
                print("Текущая директория:", self.current_dir)
            else:
                print("Директория не существует или находится за пределами базовой директории")


    def create_dir(self, directory):
        new_dir = os.path.join(self.current_dir, directory)
        try:
            os.mkdir(new_dir)
            print(f"Директория '{directory}' успешно создана")
        except FileExistsError:
            print("Директория уже существует")

    def delete_dir(self, directory):
        dir_to_delete = os.path.join(self.current_dir, directory)
        try:
            os.rmdir(dir_to_delete)
            print(f"Директория '{directory}' успешно удалена")
        except FileNotFoundError:
            print("Директория не найдена")

    def create_file(self, file_name):
        file_path = os.path.join(self.current_dir, file_name)
        with open(file_path, 'w') as f:
            pass
        print(f"Файл '{file_name}' успешно создан")

    def read_file(self, file_name):
        file_path = os.path.join(self.current_dir, file_name)
        try:
            with open(file_path, 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print("Файл не найден")

    def write_file(self, file_name, content):
        file_path = os.path.join(self.current_dir, file_name)
        with open(file_path, 'a') as f: # если нужно только новое записывать, то надо поменять на 'w'
            f.write(content.replace("\\n", "\n"))
        print(f"Содержимое успешно записано в файл '{file_name}'")

    def delete_file(self, file_name):
        file_path = os.path.join(self.current_dir, file_name)
        try:
            os.remove(file_path)
            print(f"Файл '{file_name}' успешно удален")
        except FileNotFoundError:
            print("Файл не найден")

    def copy_file(self, file_name, destination):
        source_path = os.path.join(self.current_dir, file_name)
        destination_path = os.path.join(self.current_dir, destination, file_name)
        shutil.copyfile(source_path, destination_path)
        print(f"Файл '{file_name}' успешно скопирован")

    def move_file(self, file_name, destination):
        source_path = os.path.join(self.current_dir, file_name)
        destination_path = os.path.join(self.current_dir, destination, file_name)
        shutil.move(source_path, destination_path)
        print(f"Файл '{file_name}' успешно перемещен")

    def rename_file(self, file_name, new_name):
        old_path = os.path.join(self.current_dir, file_name)
        new_path = os.path.join(self.current_dir, new_name)
        os.rename(old_path, new_path)
        print(f"Файл '{file_name}' успешно переименован")