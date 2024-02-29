import logging
import os

from collections import namedtuple

# Настройка логирования
logging.basicConfig(filename='directory_info.log', level=logging.INFO,
                    format='%(asctime)s :: %(levelname)s :: %(message)s')

# Создание объекта namedtuple для хранения информации о файле/каталоге
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def get_directory_info(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    name, extension = os.path.splitext(entry.name)
                    file_info = FileInfo(name, extension, False, entry.path)
                    logging.info(f'File found: {file_info}')
                elif entry.is_dir():
                    directory_info = FileInfo(entry.name, '', True, entry.path)
                    logging.info(f'Directory found: {directory_info}')

    except Exception as e:
        logging.error(f'Error while scanning directory: {e}')


if __name__ == "__main__":
    directory_path = input("Введите путь до директории на ПК: ")
    get_directory_info(directory_path)
