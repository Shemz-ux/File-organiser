
# File organiser
# Here is what this program will do:
# - Scan the downloads folder for files
# - Identifying files based on its type zip files, music projects, adobe projects, and more).
# - Move the files into categorized folders (e.g., "Images", "Documents") based on file extensions.

#Hello world 

import os
import shutil

folder_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".HEIC", ".avif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv", ".dotx"],
    "Creative": [".ai", ".psd", ".prt", ".aep", ".fig"],
    "Music creation": [".logicx", ".flp", ".band", ".concert"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".ipynb"],
    "Disk images": [".dmg"],
    "Fonts": [".ttf", ".otf", ".otc", ".ttc"],
    "Other": []
}
        
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads") #Defines the file path for us

# Creating folders to contain files
def create_folders():
    for folder in folder_categories:
        folder_path = os.path.join(downloads_folder, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# Organising the files by their extension
def organise_files(filename):
    # _, what is this underscore for?
    name, extension = os.path.splitext(filename) 
    for category, extensions in folder_categories.items():
        if extension in extensions:
            return category
    return "Other"

# Move files to respective folders 
def move_files(downloads_folder):
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)

        if os.path.isdir(file_path): 
            continue

        category = organise_files(filename)
        destination_folder = os.path.join(downloads_folder, category)

        shutil.move(file_path, os.path.join(destination_folder, filename))
        print(f"Moved: {filename} -> {category}")

def main():
    create_folders()

    move_files(downloads_folder)

    print("Download folder organised successfully!")

if __name__ == "__main__":
    main()

# Run this in terminal python file_organizer.py

# rm -rf .git // to remove git !

# Additional features to add:
# - Date-based Folders: Organize by date as well as type (e.g., Images/2024).
# - File Size Checks: Move only files above a certain size.
# - Undo Functionality: Log file movements in case you want to restore them.
# - Scheduled Automation: Use a task scheduler (like cron on Linux or Task Scheduler on Windows) to run it daily.
    








