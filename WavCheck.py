import os
import wave
import time
import subprocess

def main():
    music_folder = 'Y:/'

    # A function that checks whether a wav file meets certain parameters
    def check_wav_file(wav_file_path):
        with wave.open(wav_file_path, 'r') as wav_file:
            # We take the sample rate and the number of bits per sample
            sample_rate = wav_file.getframerate()
            sample_width = wav_file.getsampwidth()
            frames = wav_file.getnframes()
            # We check that the sample rate is 48000hz and the number of bits per sample is 24
            if sample_rate == 48000 and sample_width == 3 and frames > 0:
                return True
            else:
                return False

    # We search directories for wav files
    num_files = 0  # Number of wav files in directories
    num_checked_files = 0  # Number of checked wav files
    for root, dirs, files in os.walk(music_folder):
        for file in files:
            if file.endswith('.wav'):
                num_files += 1

    for root, dirs, files in os.walk(music_folder):
        for file in files:
            if file.endswith('.wav'):
                wav_file_path = os.path.join(root, file)

                # Check the wav file
                if not check_wav_file(wav_file_path):
                    print(wav_file_path)

                    # We convert the wav file to the correct format
                    output_file_path = wav_file_path[:-3] + 'converted.wav'
                    command = f'ffmpeg -i "{wav_file_path}" -ar 48000 -ac 1 -acodec pcm_s24le "{output_file_path}"'
                    subprocess.run(command, shell=True)

                num_checked_files += 1
                progress = num_checked_files / num_files * 100  # Calculate progress as a percentage
                print(f'\rProgress: {progress:.2f}%', end='')  # Update the progress bar in one line
                time.sleep(0.1)
    print(' \n')
    print("All files checked")

if __name__ == '__main__':
    main()