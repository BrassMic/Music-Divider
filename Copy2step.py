import os, subprocess
from pathlib import Path
from progress.bar import Bar
from progress.spinner import Spinner

def main():
    # Root directory
    dir_name = 'Z:/03. Music Department_Content Do Podziału'

    #Dictionary with formulas for each species
    genre_patterns = {
        'N1.0': ('**/*_N1_*.0.wav', '**/*_N1_*.0(G).wav'),
        'N2.0': ('**/*_N2_*.0.wav', '**/*_N2_*.0(G).wav'),
        'N3.0': ('**/*_N3_*.0.wav', '**/*_N3_*.0(G).wav'),
        'N5.0': ('**/*_N5_*.0.wav', '**/*_N5_*.0(G).wav'),
        'N6.0': ('**/*_N6*_*.0.wav', '**/*_N6*_*.0(G).wav'),
        'N7.0': ('**/*_N7_*.0.wav', '**/*_N7_*.0(G).wav'),
        'N8.0': ('**/*_N8_*.0.wav', '**/*_N8_*.0(G).wav'),
        'N9.0': ('**/*_N9_*.0.wav', '**/*_N9_*.0(G).wav'),
        'J1.0': ('**/*_J1_*.0.wav', '**/*_J1_*.0(G).wav'),
        'J2.0': ('**/*_J2_*.0.wav', '**/*_J2_*.0(G).wav'),
        'J3.0': ('**/*_J3_*.0.wav', '**/*_J3_*.0(G).wav'),
        'J4.0': ('**/*_J4_*.0.wav', '**/*_J4_*.0(G).wav'),
        'J5.0': ('**/*_J5_*.0.wav', '**/*_J5_*.0(G).wav'),
        'J6.0': ('**/*_J6_*.0.wav', '**/*_J6_*.0(G).wav'),
        'J7.0': ('**/*_J7_*.0.wav', '**/*_J7_*.0(G).wav'),
        'J8.0': ('**/*_J8_*.0.wav', '**/*_J8_*.0(G).wav'),
        'C1.0': ('**/*_C1_*.0.wav', '**/*_C1_*.0(G).wav'),
        'C2.0': ('**/*_C2_*.0.wav', '**/*_C2_*.0(G).wav'),
        'C3.0': ('**/*_C3_*.0.wav', '**/*_C3_*.0(G).wav'),
        'C4.0': ('**/*_C4_*.0.wav', '**/*_C4_*.0(G).wav'),
        'N1.*': ('**/*_N1_*.1.wav', '**/*_N1_*.1(G).wav','**/*_N1_*.2.wav', '**/*_N1_*.2(G).wav','**/*_N1_*.3.wav', '**/*_N1_*.3(G).wav','**/*_N1_*.4.wav', '**/*_N1_*.4(G).wav'),
        'N2.*': ('**/*_N2_*.1.wav', '**/*_N2_*.1(G).wav','**/*_N2_*.2.wav', '**/*_N2_*.2(G).wav','**/*_N2_*.3.wav', '**/*_N2_*.3(G).wav','**/*_N2_*.4.wav', '**/*_N2_*.4(G).wav'),
        'N3.*': ('**/*_N3_*.1.wav', '**/*_N3_*.1(G).wav','**/*_N3_*.2.wav', '**/*_N3_*.2(G).wav','**/*_N3_*.3.wav', '**/*_N3_*.3(G).wav','**/*_N3_*.4.wav', '**/*_N3_*.4(G).wav'),
        'N5.*': ('**/*_N5_*.1.wav', '**/*_N5_*.1(G).wav','**/*_N5_*.2.wav', '**/*_N5_*.2(G).wav','**/*_N5_*.3.wav', '**/*_N5_*.3(G).wav','**/*_N5_*.4.wav', '**/*_N5_*.4(G).wav'),
        'N6.*': ('**/*_N6*_*.1.wav', '**/*_N6*_*.1(G).wav','**/*_N6*_*.2.wav', '**/*_N6*_*.2(G).wav','**/*_N6*_*.3.wav', '**/*_N6*_*.3(G).wav','**/*_N6*_*.4.wav', '**/*_N6*_*.4(G).wav'),
        'N7.*': ('**/*_N7_*.1.wav', '**/*_N7_*.1(G).wav','**/*_N7_*.2.wav', '**/*_N7_*.2(G).wav','**/*_N7_*.3.wav', '**/*_N7_*.3(G).wav','**/*_N7_*.4.wav', '**/*_N7_*.4(G).wav'),
        'N8.*': ('**/*_N8_*.1.wav', '**/*_N8_*.1(G).wav','**/*_N8_*.2.wav', '**/*_N8_*.2(G).wav','**/*_N8_*.3.wav', '**/*_N8_*.3(G).wav','**/*_N8_*.4.wav', '**/*_N8_*.4(G).wav'),
        'N9.*': ('**/*_N9_*.1.wav', '**/*_N9_*.1(G).wav','**/*_N9_*.2.wav', '**/*_N9_*.2(G).wav','**/*_N9_*.3.wav', '**/*_N9_*.3(G).wav','**/*_N9_*.4.wav', '**/*_N9_*.4(G).wav'),
        'J1.*': ('**/*_J1_*.1.wav', '**/*_J1_*.1(G).wav','**/*_J1_*.2.wav', '**/*_J1_*.2(G).wav','**/*_J1_*.3.wav', '**/*_J1_*.3(G).wav','**/*_J1_*.4.wav', '**/*_J1_*.4(G).wav'),
        'J2.*': ('**/*_J2_*.1.wav', '**/*_J2_*.1(G).wav','**/*_J2_*.2.wav', '**/*_J2_*.2(G).wav','**/*_J2_*.3.wav', '**/*_J2_*.3(G).wav','**/*_J2_*.4.wav', '**/*_J2_*.4(G).wav'),
        'J3.*': ('**/*_J3_*.1.wav', '**/*_J3_*.1(G).wav','**/*_J3_*.2.wav', '**/*_J3_*.2(G).wav','**/*_J3_*.3.wav', '**/*_J3_*.3(G).wav','**/*_J3_*.4.wav', '**/*_J3_*.4(G).wav'),
        'J4.*': ('**/*_J4_*.1.wav', '**/*_J4_*.1(G).wav','**/*_J4_*.2.wav', '**/*_J4_*.2(G).wav','**/*_J4_*.3.wav', '**/*_J4_*.3(G).wav','**/*_J4_*.4.wav', '**/*_J4_*.4(G).wav'),
        'J5.*': ('**/*_J5_*.1.wav', '**/*_J5_*.1(G).wav','**/*_J5_*.2.wav', '**/*_J5_*.2(G).wav','**/*_J5_*.3.wav', '**/*_J5_*.3(G).wav','**/*_J5_*.4.wav', '**/*_J5_*.4(G).wav'),
        'J6.*': ('**/*_J6_*.1.wav', '**/*_J6_*.1(G).wav','**/*_J6_*.2.wav', '**/*_J6_*.2(G).wav','**/*_J6_*.3.wav', '**/*_J6_*.3(G).wav','**/*_J6_*.4.wav', '**/*_J6_*.4(G).wav'),
        'J7.*': ('**/*_J7_*.1.wav', '**/*_J7_*.1(G).wav','**/*_J7_*.2.wav', '**/*_J7_*.2(G).wav','**/*_J7_*.3.wav', '**/*_J7_*.3(G).wav','**/*_J7_*.4.wav', '**/*_J7_*.4(G).wav'),
        'J8.*': ('**/*_J8_*.1.wav', '**/*_J8_*.1(G).wav','**/*_J8_*.2.wav', '**/*_J8_*.2(G).wav','**/*_J8_*.3.wav', '**/*_J8_*.3(G).wav','**/*_J8_*.4.wav', '**/*_J8_*.4(G).wav'),
        'C1.*': ('**/*_C1_*.1.wav', '**/*_C1_*.1(G).wav','**/*_C1_*.2.wav', '**/*_C1_*.2(G).wav','**/*_C1_*.3.wav', '**/*_C1_*.3(G).wav','**/*_C1_*.4.wav', '**/*_C1_*.4(G).wav'),
        'C2.*': ('**/*_C2_*.1.wav', '**/*_C2_*.1(G).wav','**/*_C2_*.2.wav', '**/*_C2_*.2(G).wav','**/*_C2_*.3.wav', '**/*_C2_*.3(G).wav','**/*_C2_*.4.wav', '**/*_C2 _*.4(G).wav'),
        'C3.*': ('**/*_C3_*.1.wav', '**/*_C3_*.1(G).wav','**/*_C3_*.2.wav', '**/*_C3_*.2(G).wav','**/*_C3_*.3.wav', '**/*_C3_*.3(G).wav','**/*_C3_*.4.wav', '**/*_C3_*.4(G).wav'),
        'C4.*': ('**/*_C4_*.1.wav', '**/*_C4_*.1(G).wav','**/*_C4_*.2.wav', '**/*_C4_*.2(G).wav','**/*_C4_*.3.wav', '**/*_C4_*.3(G).wav','**/*_C4_*.4.wav', '**/*_C4_*.4(G).wav')
    }

    # Dictionary with destination directories for each species
    genre_dirs = {
        'N1.0': 'Z:/06. iTunes_Apple Music_original version/NA - N1/N1 - NATURE',
        'N2.0': 'Z:/06. iTunes_Apple Music_original version/NA - N1/N2 - MEDITATION',
        'N3.0': 'Z:/06. iTunes_Apple Music_original version/NA - N1/N3 - HZ, FREQUENCIES',
        'N5.0': 'Z:/06. iTunes_Apple Music_original version/NA - N1/N5 - INSTRUMENTAL',
        'N6.0': 'Z:/06. iTunes_Apple Music_original version/NA - N1/N6 - WORLD ETHNIC',
        'N7.0': 'Z:/06. iTunes_Apple Music_original version/NA - N1/N7 - CHILDREN',
        'N8.0': 'Z:/06. iTunes_Apple Music_original version/NA - N1/N8 - SOUND EFFECT',
        'N9.0': 'Z:/06. iTunes_Apple Music_original version/NA - N1/N9 - HOLIDAY',
        'J1.0': 'Z:/06. iTunes_Apple Music_original version/JAZZ - J1/J1 - INSTRUMENTAL',
        'J2.0': 'Z:/06. iTunes_Apple Music_original version/JAZZ - J1/J2 - HOLIDAY',
        'J3.0': 'Z:/06. iTunes_Apple Music_original version/JAZZ - J1/J3 - REGGAE',
        'J4.0': 'Z:/06. iTunes_Apple Music_original version/JAZZ - J1/J4 - COUNTRY',
        'J5.0': 'Z:/06. iTunes_Apple Music_original version/JAZZ - J1/J5 - JAZZ',
        'J6.0': 'Z:/06. iTunes_Apple Music_original version/JAZZ - J1/J6 - BLUES',
        'J7.0': 'Z:/06. iTunes_Apple Music_original version/JAZZ - J1/J7 - LATINO',
        'J8.0': 'Z:/06. iTunes_Apple Music_original version/JAZZ - J1/',
        'C1.0': 'Z:/06. iTunes_Apple Music_original version/CHILL - C1/C1 - ELECTRONIC',
        'C2.0': 'Z:/06. iTunes_Apple Music_original version/CHILL - C1/C2 - HIP HOP',
        'C3.0': 'Z:/06. iTunes_Apple Music_original version/CHILL - C1/C3 - HOLIDAY',
        'C4.0': 'Z:/06. iTunes_Apple Music_original version/CHILL - C1/C4 - CHILL',
        'N1.*': 'Z:/01a. Music from 02.22 Modifications/NA - N1/N1 - NATURE',
        'N2.*': 'Z:/01a. Music from 02.22 Modifications/NA - N1/N2 - MEDITATION',
        'N3.*': 'Z:/01a. Music from 02.22 Modifications/NA - N1/N3 - HZ, FREQUENCIES',
        'N5.*': 'Z:/01a. Music from 02.22 Modifications/NA - N1/N5 - INSTRUMENTAL',
        'N6.*': 'Z:/01a. Music from 02.22 Modifications/NA - N1/N6 - WORLD ETHNIC',
        'N7.*': 'Z:/01a. Music from 02.22 Modifications/NA - N1/N7 - CHILDREN',
        'N8.*': 'Z:/01a. Music from 02.22 Modifications/NA - N1/N8 - SOUND EFFECT',
        'N9.*': 'Z:/01a. Music from 02.22 Modifications/NA - N1/N9 - HOLIDAY',
        'J1.*': 'Z:/01a. Music from 02.22 Modifications/JAZZ - J1/J1 - INSTRUMENTAL',
        'J2.*': 'Z:/01a. Music from 02.22 Modifications/JAZZ - J1/J2 - HOLIDAY',
        'J3.*': 'Z:/01a. Music from 02.22 Modifications/JAZZ - J1/J3 - REGGAE',
        'J4.*': 'Z:/01a. Music from 02.22 Modifications/JAZZ - J1/J4 - COUNTRY',
        'J5.*': 'Z:/01a. Music from 02.22 Modifications/JAZZ - J1/J5 - JAZZ',
        'J6.*': 'Z:/01a. Music from 02.22 Modifications/JAZZ - J1/J6 - BLUES',
        'J7.*': 'Z:/01a. Music from 02.22 Modifications/JAZZ - J1/J7 - LATINO',
        'J8.*': 'Z:/01a. Music from 02.22 Modifications/JAZZ - J1/',
        'C1.*': 'Z:/01a. Music from 02.22 Modifications/CHILL - C1/C1 - ELECTRONIC',
        'C2.*': 'Z:/01a. Music from 02.22 Modifications/CHILL - C1/C2 - HIP HOP',
        'C3.*': 'Z:/01a. Music from 02.22 Modifications/CHILL - C1/C3 - HOLIDAY',
        'C4.*': 'Z:/01a. Music from 02.22 Modifications/CHILL - C1/C4 - CHILL',

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
        num_files = sum(len(files) for files in genre_files.values())  
        num_checked_files = 0  
        bar = Bar('', max=num_files, width=70, suffix='%(percent)d%%')
        spinner = Spinner()
        for genre, files in genre_files.items():
            dest = genre_dirs[genre]
            for file in files:
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

if __name__ == '__main__':
    main()