import os
import time
import shutil


class OrganizeFolder():
    def __init__(self):
        #! Variables
        self.max_filename_len = 40
        self.max_folder_len = 15
        self.file_types = [
            {
                'name': 'PDF',
                'extensions': ['.pdf']
            },
            {
                'name': 'Programs',
                'extensions': ['.exe', '.deb', '.msi', '.bat', '.sh', '.apk']
            },
            {
                'name': 'Videos',
                'extensions': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.m3u8']
            },
            {
                'name': 'Compressed',
                'extensions': ['.zip', '.rar', '.gz', '.xz', '.7z', '.tar', '.bz2']
            },
            {
                'name': 'Pictures',
                'extensions': ['.png', '.jpg', '.jpeg', '.svg', '.gif', '.bmp', '.tiff', '.webp']
            },
            {
                'name': 'Music',
                'extensions': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a']
            },
            {
                'name': 'Documents',
                'extensions': ['.doc', '.docx', '.txt', '.rtf', '.odt', '.md']
            },
            {
                'name': 'Spreadsheets',
                'extensions': ['.xls', '.xlsx', '.ods', '.csv']
            },
            {
                'name': 'Presentations',
                'extensions': ['.ppt', '.pptx', '.odp']
            },
            {
                'name': 'Code',
                'extensions': ['.py', '.js', '.java', '.c', '.cpp', '.cs', '.html', '.css', '.php', '.rb', '.go', '.ts', '.json', '.xml', '.sh', '.bat']
            },
        ]

    #! Methods
    def get_folder_name(self, file_ext: str):
        for i in self.file_types:
            if file_ext in i['extensions']:
                return i['name']

        return 'Others'

    def print_table(self):
        print(
            f"{'No.':<5} {'File':<{self.max_filename_len}} {'→':^5} {'Folder':<{self.max_folder_len}}")
        print("-" * (10 + self.max_filename_len + self.max_folder_len))

    def print_file(self, index: int, filename: str, file_ext: str, folder_name: str):
        name = filename + file_ext
        if len(name) > self.max_filename_len:
            name = name[:self.max_filename_len - 3] + '...'

        print(
            f"{index:<5} {name:<{self.max_filename_len}} {'→':^5} {folder_name:<{self.max_folder_len}}")

    def move_file(self, path: str, folder_to: str, filename: str):
        source = os.path.join(path, filename)
        destination = os.path.join(path, folder_to, filename)

        if not os.path.exists(os.path.join(path, folder_to)):
            os.makedirs(os.path.join(path, folder_to))

        shutil.move(source, destination)

    #! OS
    def windows(self, path: str = 'C:\\Users\\user\\Downloads\\'):
        list_files = os.listdir(path)

        self.print_table()

        for index, file in enumerate(list_files, start=1):
            full_path = os.path.join(path, file)
            filename, file_ext = os.path.splitext(file)

            if os.path.isfile(full_path):
                folder_name = self.get_folder_name(file_ext)

                self.move_file(path, folder_name, filename + file_ext)
                self.print_file(index, filename, file_ext, folder_name)
        
        print("\nAll files have been organized successfully!")
