import os
from progress.bar import Bar

def main():
    root_dir = 'Z:/Content'

    response = input('Do you want to delete all .wav files in the specified directory and its subdirectories? (y/n) ')

    if response.lower() == 'y':
        files_count = 0
        for subdir, dirs, files in os.walk(root_dir):
            for file in files:
                if file.endswith('.wav'):
                    files_count += 1

        bar = Bar(max=files_count, suffix='%(percent)d%%', empty=' ')
        for subdir, dirs, files in os.walk(root_dir):
            for file in files:
                if file.endswith('.wav'):
                    file_path = os.path.join(subdir, file)
                    os.remove(file_path)
                    print(f'Plik {file_path} has been removed', end='\n')
                    bar.next()
        bar.finish()
    else:
        print('I''m not deleting any files')

if __name__ == '__main__':
    main()
