# 📁 Smart File Organizer

A Python-based file management tool that automatically organizes files into different folders based on their file extensions.

## 🚀 About the Project

Managing multiple files can become messy and time-consuming. The **Smart File Organizer** solves this problem by automatically sorting files into categorized folders such as Images, PDFs, Documents, Videos, Music, and Spreadsheets.

This project uses Python's built-in libraries to simplify file organization.

## ✨ Features

- Automatically organizes files by extension.
- Creates category folders automatically.
- Supports multiple file formats.
- Moves files into their respective folders.
- Skips files if a file with the same name already exists in the destination.
- Organizes uncategorized file types into an Others folder.

## 🛠️ Technologies Used

- **Python 3**
- **OS Module** – File and directory handling.
- **Shutil Module** – Moving files between folders.

## 📂 Supported File Categories

| Category | File Extensions |
|---|---|
| Images | .jpg, .jpeg, .png, .gif |
| PDFs | .pdf |
| Documents | .doc, .docx, .txt |
| Videos | .mp4, .mkv, .avi |
| Music | .mp3, .wav |
| Spreadsheets | .xls, .xlsx, .csv |
| Others | All remaining file types |

## 💻 How to Run the Project

**Step 1:** Clone the repository.

```bash
git clone https://github.com/SwarnaliMoitra/smart-file-organizer.git
```

**Step 2:** Open the project folder.

```bash
cd smart-file-organizer
```

**Step 3:** Run the Python file.

```bash
python smart_file_organizer.py
```

**Step 4:** Enter the folder path when prompted.

Example:

```text
C:\Users\YourName\Desktop\testfiles
```

The program will automatically organize the files inside that folder.

## 📸 Expected Output

```text
Enter folder path: C:\Users\YourName\Desktop\testfiles

photo.jpg moved to Images
notes.pdf moved to PDFs
assignment.docx moved to Documents

File organization completed!
```

*Example output; actual results depend on the files in the selected folder.*

## 📁 Project Structure

```text
smart-file-organizer/
│
├── smart_file_organizer.py
├── README.md
└── .gitignore
```

## ⚠️ Important Note

The program moves files from their original location into category folders. Always test it using a sample folder or backup your files before running it on important data.

## 🎯 Future Improvements

- Graphical User Interface (GUI).
- Support for more file formats.
- File organization by date and size.
- Duplicate file detection.
- Detailed activity logs.

## 👩‍💻 Author

**Swarnali Moitra**

ECE Undergraduate | Python & Programming Enthusiast

[GitHub Profile](https://github.com/SwarnaliMoitra)

---

⭐ If you find this project useful, consider giving it a star!
