import WavRemove, DirsRemover, Counter, Copy1Step, Copy2step, Archive, WavCheck, RenameFiles


print(' ')
print('-'*60)
print('Welcome to MUSIC DIVIDER by BrassMic')
print('alpha version 0.1.0')
print('-'*60)
print(' ')

def menu():
      print(' ')
      print('|'*100)
      print('Choose what you want to do(1-default):\n'
            '1. Program start\n'
            '2. Delete old files in Music -> 03. Music Department_Content Do Podziału\n'
            '3. Delete old folders in Music Department\n'
            '4. Download Data for KPI\n'
            '5. Copying ALL Wav files from Music Department\n'
            '6. Wav file numbering \n'
            '7. Split ALL files from Music -> 03. Music Department_Content Do Podziału \n'
            '8. Copying files to Music Archive\n'
            '9. Close the program')
      print('|' * 100)
      print(' ')
while True:
      menu()
      choice = input('Your choice: ')

      if choice == '1':
            WavRemove.main()
            DirsRemover.main()
            print('-' * 60)
            Counter.main()
            print('-' * 60)
            input("Press enter to continue...")
            WavCheck.main()
            Copy1Step.main()
            print('-' * 60)
            RenameFiles.main()
            input("Press enter to continue...")
            Copy2step.main()
            Archive.main()
            print('Everything has been done, SEE YOU!')
            exit()
      elif choice == '2':
            WavRemove.main()
      elif choice == '3':
            DirsRemover.main()
      elif choice == '4':
            Counter.main()
      elif choice == '5':
            WavCheck.main()
            Copy1Step.main()
      elif choice == '6':
            RenameFiles.main()
      elif choice == '7':
            Copy2step.main()
      elif choice == '8':
            Archive.main()
      elif choice == '9':
            print('SEE YOU!')
            break
            exit()


