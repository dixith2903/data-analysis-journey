import os # Import the os module to interact with the operating system
import shutil # Import the shutil module to perform high-level file operations like moving files

# folder path you want to organize
FOLDER_PATH = os.getcwd() # Current working directory

# file types and their corresponding folders

FILE_TYPES = {
    'Image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Document': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Video': ['.mp4', '.avi', '.mkv', '.mov'],
    'Archive': ['.zip', '.rar', '.tar', '.gz'],
    'Code': ['.js', '.html', '.css', '.java', '.cpp']
}

# Create folders if they don't exist

for folder in FILE_TYPES.keys(): # Create folders based on file types
    folder_path = os.path.join(FOLDER_PATH, folder) # Get the full path of the folder
    if not os.path.exists(folder_path): # Check if the folder already exists
        os.makedirs(folder_path) # Create the folder if it doesn't exist


# organize files based on their extensions

for filename in os.listdir(FOLDER_PATH): # Iterate through each file in the folder
    file_path = os.path.join(FOLDER_PATH, filename) # Get the full path of the file
    
    # Skip folders
    if os.path.isdir(file_path):# Check if the path is a directory
        continue


    # Get file extension
    file_extension = os.path.splitext(filename)[1].lower() # Get the file extension and convert it to lowercase

    for folder, extensions in FILE_TYPES.items(): # Iterate through each folder and its corresponding extensions
        if file_extension in extensions:# Check if the file extension matches any of the extensions in the current folder
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder, filename))# Move the file to the corresponding folder

print("Files have been organized successfully! ✅")  