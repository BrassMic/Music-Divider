# Music-Divider
As part of the course and learning python programming I wrote and am improving a program that automates part of my work (which I have to do every day).

Part of my musical job includes checking and sharing the music I receive every day. The program automates all my steps that I had to do manually.

The program does the following:

1.Removes music from the previous day from dedicated folders in which I give all songs an internal ID

2.Removes folders with content with a date lower than the user specified in folders where music producers upload music every day

3.Displays a list of folders with the date in the name and the number of songs in a specific folder for the entry of the internal KPI table

4.Checks whether songs meet the technical requirements (48000hz / 24bit) in producer folders and copies them based on genres to dedicated folders

5.We add a prefix and internal ID numbers to the beginning of the names for each file in each genre (numbering and describing files)

6.Then files are divided by genres into folders from which music is taken to albums (based on genre ID and file type: original and modifications of the original)

7.the last step is to create a folder with the date and archive all wav files in this folder

The program was created as separate scripts that are now combined into one with a basic menu in which you can run all the steps in turn or select each of them separately

In plans:

in point 5 process automation. By default, the program is supposed to connect to the google sheet, download the latest data, then number the files based on them and save the last numbers back to the sheet to the next free cell

improvement of progress bars. Each script used a different library to display the progress bar. By default, the program will use one library and a unified progress bar in all scripts

creating a simple GUI for the program
