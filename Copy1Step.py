import subprocess, os
from pathlib import Path
from progress.bar import Bar
from progress.spinner import Spinner

def main():
    #Catalogues
    dir_name = 'Y:/'
    chill_dir = 'Z:/3. Chill'
    jazz_dir = 'Z:/1. Jazz'
    na_dir = 'Z:/2. New Age'

    #Dictionary with formulas for each species
    genre_patterns = {
        'NA': ('**/*_N1_*.wav', '**/*_N2_*.wav','**/*_N3_*.wav', '**/*_N5_*.wav', '**/*_N6*_*.wav', '**/*_N7_*.wav', '**/*_N8_*.wav','**/*_N9_*.wav'),
        'Jazz': ('**/*_J1_*.wav', '**/*_J2_*.wav', '**/*_J3_*.wav', '**/*_J4_*.wav', '**/*_J5_*.wav', '**/*_J6_*.wav', '**/*_J7_*.wav', '**/*_J8_*.wav'),
        'Chill': ('**/*_C1_*.wav', '**/*_C2_*.wav', '**/*_C3_*.wav', '**/*_C4_*.wav')
    }

    #Dictionary with destination directories for each species
    genre_dirs = {
        'NA': na_dir,
        'Jazz': jazz_dir,
        'Chill': chill_dir
    }

    def get_files(patterns):
        all_files = {}
        for genre, pat in patterns.items():
            all_files[genre] = []
            for p in pat:
                all_files[genre].extend([Path(dir_name).joinpath(path) for path in Path(dir_name).glob(p)])
        for genre, files in all_files.items():
            print(f'Number of files per genre "{genre}": {len(files)}')
        return all_files


    genre_files = get_files(genre_patterns)


    def copy_files(genre_files, genre_dirs):
        num_files = sum(len(files) for files in genre_files.values())  # We calculate the total number of files
        num_checked_files = 0  # Counter of checked files
        bar = Bar('', max=num_files, width=70, suffix='%(percent)d%%')
        spinner = Spinner()
        for genre, files in genre_files.items():
            dest = genre_dirs[genre]
            for file in files:
                # Check if the file already exists in the destination directory
                if not os.path.exists(os.path.join(dest, file.name)):
                    subprocess.run(['xcopy', file, dest, '/Y'], check=True)
                num_checked_files += 1
                bar.next()
                spinner.next()
            print('\n' + '-' * 140)
            print(len(files), 'Files Copied')
            print('-' * 140)
        bar.finish()

    copy_files(genre_files, genre_dirs)
    # print(genre_files)

if __name__ == '__main__':
    main()