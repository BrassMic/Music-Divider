import os
def main():
    # Dir list
    na = 'Z:/2. New Age'
    jazz = 'Z:/1. Jazz'
    chill = 'Z:/3. Chill'

    def add_prefix_and_number_to_filenames(folder_path):
        number = int(input(f"Enter the starting number for {folder_path}: ")) + 1
        for filename in os.listdir(folder_path):
            new_filename = "REHPL" + " - " + str(number) + "_" + filename
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            number += 1
        print(f'The last number for {folder_path} is:')
        print(number - 1)



    add_prefix_and_number_to_filenames(na)
    add_prefix_and_number_to_filenames(jazz)
    add_prefix_and_number_to_filenames(chill)

if __name__ == '__main__':
    main()