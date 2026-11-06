import os
import shutil

# Select folder
folder_path = input("Enter folder path: ")

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Documents": [".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Others": []
}

if not os.path.isdir(folder_path):
    print("Invalid folder path!")

else:
    for filename in os.listdir(folder_path):

        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):

            extension = os.path.splitext(filename)[1].lower()

            category = "Others"

            for folder, extensions in file_types.items():
                if extension in extensions:
                    category = folder
                    break

            destination_folder = os.path.join(
                folder_path, category
            )

            os.makedirs(destination_folder, exist_ok=True)

            destination_path = os.path.join(
                destination_folder, filename
            )

            if os.path.exists(destination_path):
                print("Skipped:", filename)
                continue

            shutil.move(file_path, destination_path)

            print(filename, "moved to", category)

    print("File organization completed!")