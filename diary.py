import datetime
#for timing
def gettime():
    return datetime.datetime.now()

class diary:
    def __init__(self):
        pass


#for writting in diary
    def write(self):
         value= input("Type now\n")
         with open("Your_Diary.txt","a") as op:
            op.write(str([str(gettime())])+": "+value+"\n")
         print("Successfully Written")


#for reading the diary
    def read(self):
        with open("Your_Diary.txt") as op:
            for i in op:
                print(i, end="")
        print('\n\n     Thank you')


print('Welcome to your personal diary dear ')
typing=diary()


count=int(input('Press 0 to exit the diary, else press 1\n'))
if count==1:
    while count == 1:
        decision = str(input(
            'Would you want to write or read\n\nIf you want to write the diary, please enter \"w\"\nand if you want to read the diary, please enter \"r\" \n'))

        if decision == 'w':
            Type = typing.write()
        else:
            Type = typing.read()

        count = int(input('\nif you want to exit the diary, then press 0 else press 1\n'))
        if count==1:
            pass
        else:
            print('\nHave a good day dear\nThank You for sharing things')

else:
    print('\nHave a good day dear\nThank You for sharing things')