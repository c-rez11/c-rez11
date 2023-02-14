#chapter 9

#reading a text file and returning its contents

HelloFile = open('C:\\Users\cresnick\\OneDrive - Epic\\Desktop\\python projects\\Udemy courses\\new_era\\c-rez11\\ECO_685\\Hello World!.txt')
#print('done')

HelloContent = HelloFile.read()
print(HelloContent)

#append to the file
AppendFile = open('C:\\Users\cresnick\\OneDrive - Epic\\Desktop\\python projects\\Udemy courses\\new_era\\c-rez11\\ECO_685\\Hello World!.txt', 'a')
AppendFile.write('\nBy Gary SquarePants')
AppendFile.close()
