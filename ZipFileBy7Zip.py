// Description: This script compresses all folders in the current directory using 7-zip.
// It uses the subprocess module to run the 7-zip command-line tool to compress each folder.\
// The 7-zip executable path is specified at the beginning of the script, and the compress_folder function takes a folder path as input and compresses it using 7-zip.



import os
import subprocess

# Path to 7-zip executable - modify this according to your 7-zip installation
SEVEN_ZIP_PATH = r"C:\Program Files\7-Zip\7z.exe"

def compress_folder(folder_path):
    """Compress a folder using 7-zip"""
    folder_name = os.path.basename(folder_path)
    output_zip = f"{folder_path}.zip"
    
    # Create 7-zip command
    cmd = [SEVEN_ZIP_PATH, 'a', '-tzip', output_zip, f"{folder_path}\\*"]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"Successfully compressed {folder_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error compressing {folder_name}: {e}")

def main():
    # Get current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Get all folders in current directory
    folders = [f for f in os.listdir(current_dir) 
              if os.path.isdir(os.path.join(current_dir, f))]
    
    # Compress each folder
    for folder in folders:
        folder_path = os.path.join(current_dir, folder)
        compress_folder(folder_path)

if __name__ == "__main__":
    main()
