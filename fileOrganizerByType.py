import os
import shutil

file_types = {
    "Documents": [".doc", ".docx", ".pdf", ".txt", ".xls", ".xlsx"],
    "Compressed": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executables": [".exe", ".msi", ".bat"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Presentations": [".ppt", ".pptx", ".key"],
    "Spreadsheets": [".ods", ".csv"],
    "Scripts": [".py", ".js", ".sh", ".rb", ".php"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "CAD": [".dwg", ".dxf"],
    "3D Models": [".obj", ".stl", ".fbx"],
    "Web Files": [".html", ".css", ".js"],
    "Database": [".sql", ".db", ".sqlite"],
    "System Files": [".sys", ".dll", ".ini"],
    "Logs": [".log"],
    "Backups": [".bak", ".old"],
    "Others": []
}

def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    folder_path = os.path.join(directory, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    moved = True
                    break
            if not moved:
                other_folder_path = os.path.join(directory, "Others")
                if not os.path.exists(other_folder_path):
                    os.makedirs(other_folder_path)
                shutil.move(file_path, os.path.join(other_folder_path, filename))

if __name__ == "__main__":
    # Specify the folder
    my_folder = os.path.expanduser("~/Downloads")
    organize_files(my_folder)
    
    # Example of how to apply the script to another path
    # my_folder = "/path/to/another/folder"
    # organize_files(my_folder)