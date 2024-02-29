import os
import logging

from collections import namedtuple

logging.basicConfig(filename='file_info.log', level=logging.INFO)

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def get_file_info(path):
    file_info_list = []
    parent_dir = os.path.basename(os.path.normpath(path))

    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        is_dir = os.path.isdir(full_path)

        if is_dir:
            file_info_list.append(FileInfo(item, None, is_dir, parent_dir))
        else:
            name, extension = os.path.splitext(item)
            file_info_list.append(FileInfo(name, extension, is_dir, parent_dir))

    return file_info_list


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    try:
        file_info = get_file_info(directory_path)

        with open('file_info.txt', 'w') as f:
            for info in file_info:
                f.write(
                    f"Name: {info.name}, Extension: {info.extension}, Is Directory: {info.is_directory}, Parent Directory: {info.parent_directory}\n")
                logging.info(
                    f"Name: {info.name}, Extension: {info.extension}, Is Directory: {info.is_directory}, Parent Directory: {info.parent_directory}")

        print("File information saved to file_info.txt")
    except Exception as e:
        print(f"An error occurred: {e}")