try:
    fileInput=input('Enter the file to be read:')
    fileRead = open(fileInput, 'r')
    readContent=fileRead.read()
    fileOutput = input('Enter the file to write: ')
    fileWrite = open(fileOutput, 'w')
    fileWrite.write(readContent.upper())
except:
    print('File does not exist')
    quit()


