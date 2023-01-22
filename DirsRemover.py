import os, shutil, re
from dateutil import parser
from datetime import datetime
def main():
    root_dir = 'Y:/'

    folder_name_pattern = re.compile(r"(\w+)\s+(\d{2}[\.\/-]\d{2}[\.\/-]\d{2,4})|(\d{2}[\.\/-]\d{2}[\.\/-]\d{2,4})\s+(\w+)")

    date_formats = {
      'DD.MM.YYYY': '%d.%m.%Y',
      'DD/MM/YYYY': '%d/%m/%Y',
      'DD-MM-YYYY': '%d-%m-%Y',
      'DD.MM.YY': '%d.%m.%y',
      'DD/MM/YY': '%d/%m/%y',
      'DD-MM-YY': '%d-%m-%y',
      'YYYY.MM.DD': '%Y.%m.%d',
      'YYYY/MM/DD': '%Y/%m/%d',
      'YYYY-MM-DD': '%Y-%m-%d',
      'YY.MM.DD': '%y.%m.%d',
      'YY/MM/DD': '%y/%m/%d',
      'YY-MM-DD': '%y-%m-%d',
      'MM.DD.YYYY': '%m.%d.%Y',
      'MM/DD/YYYY': '%m/%d/%Y',
      'MM-DD-YYYY': '%m-%d-%Y',
      'MM.DD.YY': '%m.%d.%y',
      'MM/DD/YY': '%m/%d/%y',
      'MM-DD-YY': '%m-%d-%y',
      'DD_MM_YYYY': '%d_%m-%Y',
      'DD_MM_YY': '%d_%m_%y',
      'YYYY_MM_DD': '%Y_%m-%d',
      'YY_MM_DD': '%y_%m_%d',
      'MM_DD_YYYY': '%m_%d_%Y',
      'MM_DD_YY': '%m_%d_%y',
    }

    def extract_date(folder_name, date_formats):
        # Try matching the folder name with a regex
        match = folder_name_pattern.match(folder_name)
        if match is None:
            return None

        # Extract the date and ID parts from the folder name
        date_part, id_part = match.groups()[0:2]
        # print(date_part)
        # print(id_part)
        if date_part is None:
            date_part, id_part = match.groups()[2:]
        else:
            if id_part is not None or id_part[0] == 'A':
                # Swap date and id parts
                date_part, id_part = id_part, date_part

        # Try parsing the date part using different date formats

        for fmt, strptime_fmt in date_formats.items():
            try:
                return datetime.strptime(date_part, strptime_fmt)
            except ValueError:
                continue
        # Return False if part of the date cannot be parsed
        return None

    def should_remove_folder(folder_name, user_date):
      # Extract the date from the folder
      folder_date = extract_date(folder_name, date_formats)
      # Return True if the folder date is earlier than a user-specified date
      return folder_date is not None and folder_date.date() < user_date.date()
      # Return False if the folder name does not match the regular expression or if the date was not earlier than a user-specified date



    user_date = input('Enter the date (format DD-MM-YYYY): ')


    try:
        user_date = parser.parse(user_date)
    except ValueError:
        print('Invalid date format')
        exit()



    # We retrieve the list of subfolders in the root directory
    for dir_path, subdir_list, file_list in os.walk(root_dir):
        for subdir in subdir_list:
            full_path = os.path.join(dir_path, subdir)
            if should_remove_folder(subdir, user_date):
                confirm = input(f'Do you want to delete the {full_path} folder? (Y/N)')
                if confirm.lower() == 'y':
                    shutil.rmtree(full_path)
                else:
                    print(f'Folder {full_path} will not be deleted.')
                    continue

if __name__ == '__main__':
    main()