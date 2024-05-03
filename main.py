from FileManager import FileManager
from config import base_dir


def main():
    file_manager = FileManager(base_dir)

    while True:
        command = input("Введите команду: ")

        parts = command.split()
        operation = parts[0]
        if operation == "list_dir":
            file_manager.list_dir()
        elif operation == "change_dir":
            directory = parts[1]
            file_manager.change_dir(directory)
        elif operation == "create_dir":
            directory = parts[1]
            file_manager.create_dir(directory)
        elif operation == "delete_dir":
            directory = parts[1]
            file_manager.delete_dir(directory)
        elif operation == "create_file":
            file_name = parts[1]
            file_manager.create_file(file_name)
        elif operation == "read_file":
            file_name = parts[1]
            file_manager.read_file(file_name)
        elif operation == "write_file":
            file_name = parts[1]
            content = ' '.join(parts[2:])
            file_manager.write_file(file_name, content)
        elif operation == "delete_file":
            file_name = parts[1]
            file_manager.delete_file(file_name)
        elif operation == "copy_file":
            file_name = parts[1]
            destination = parts[2]
            file_manager.copy_file(file_name, destination)
        elif operation == "move_file":
            file_name = parts[1]
            destination = parts[2]
            file_manager.move_file(file_name, destination)
        elif operation == "rename_file":
            file_name = parts[1]
            new_name = parts[2]
            file_manager.rename_file(file_name, new_name)
        elif operation == "exit":
            print("Завершение работы")
            break
        else:
            print("Некорректная команда")


if __name__ == "__main__":
    main()

