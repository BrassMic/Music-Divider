import os
import re
def main():
  # A function that checks if the folder name contains a date in one of the supported formats
  def is_date(name):
    patterns = [
      re.compile(r'\d{2}\.\d{2}\.\d{4}'),
      re.compile(r'\d{4}-\d{2}-\d{2}'),
      re.compile(r'\d{2}-\d{2}-\d{4}'),
      re.compile(r'\d{4}\.\d{2}\.\d{2}'),
      re.compile(r'\d{2}\.\d{2}\.\d{2}'),
      re.compile(r'\d{2}-\d{2}-\d{2}'),
      re.compile(r'\d{2}\.\d{2}\.\d{2}'),
      re.compile(r'\d{2}_\d{2}_\d{4}'),
      re.compile(r'\d{2}\_\d{2}\_\d{4}'),
      re.compile(r'\d{4}_\d{2}_\d{2}'),
      re.compile(r'\d{4}\_\d{2}\_\d{2}'),
      re.compile(r'\d{2}_\d{2}_\d{2}'),
      re.compile(r'\d{2}\_\d{2}\_\d{2}'),
      re.compile(r'\d{2}_\d{2}_\d{2}'),
      re.compile(r'\d{2}\_\d{2}\_\d{2}'),
      re.compile(r'\d{1}\.\d{2}\.\d{4}'),
      re.compile(r'\d{4}-\d{2}-\d{1}'),
      re.compile(r'\d{1}-\d{2}-\d{4}'),
      re.compile(r'\d{4}\.\d{2}\.\d{1}'),
      re.compile(r'\d{1}\.\d{2}\.\d{2}'),
      re.compile(r'\d{1}-\d{2}-\d{2}'),
      re.compile(r'\d{2}\.\d{2}\.\d{1}'),
      re.compile(r'\d{1}_\d{2}_\d{4}'),
      re.compile(r'\d{1}\_\d{2}\_\d{4}'),
      re.compile(r'\d{4}_\d{2}_\d{1}'),
      re.compile(r'\d{4}\_\d{1}\_\d{2}'),
      re.compile(r'\d{1}_\d{2}_\d{2}'),
      re.compile(r'\d{2}\_\d{2}\_\d{1}'),
      re.compile(r'\d{2}_\d{1}_\d{2}'),
    ]
    for pattern in patterns:
      if pattern.search(name):
        return True
    return False

  # Retrieve the folder names containing the date
  folders = []
  for root, dirs, files in os.walk('Y:/'):
    if is_date(os.path.basename(root)):
      folders.append(root)

  def get_folder_number(name):
    match = re.search(r'\d+', name)
    if match:
      return int(match.group())
    return -1

  # Sort the list of folders by the number in the name in ascending order
  folders = sorted(folders, key=lambda x: get_folder_number(os.path.basename(x)))


  # Display the number of files in each folder
  for folder in folders:
    num_files = len(os.listdir(folder))
    print(f'Folder {folder[:]} contains --> {num_files} files')

if __name__ == '__main__':
    main()