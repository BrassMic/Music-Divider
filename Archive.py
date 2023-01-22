import os
import subprocess

def main():
    # path to the folder with wav files
    source_folder = 'Z:/Content'
    # path to the destination folder
    destination_folder = 'X:/2023'

    # Get the folder name from the user
    folder_name = input('Enter a folder name: ')

    # Check if a folder with the given name already exists
    new_folder = os.path.join(destination_folder, folder_name)
    if os.path.exists(new_folder):
        response = input(f"A folder named {folder_name} already exists in {destination_folder}. Do you want to continue and overwrite the files in this folder? (y/n)")
        if response.lower() != 'y':
            return

    # Create a new folder in the destination folder (if it doesn't exist)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    # Get list of wav files from source folder and subfolders
    wav_files = []
    for root, dirs, files in os.walk(source_folder):
        wav_files.extend([os.path.join(root, f) for f in files if f.endswith('.wav')])

    # Launch the progress bar and copy files
    for i, wav_file in enumerate(wav_files):
        destination_path = os.path.join(new_folder)
        subprocess.run(['xcopy', wav_file, destination_path], check=True)

        
        progress = (i + 1) / len(wav_files)
        num_hash = int(progress * 50)
        print(f'Copy files: {"#" * num_hash}{" " * (50 - num_hash)} {int(progress * 100)}%', end='\n')

if __name__ == '__main__':
    main()
