import os

def folderSize(folder, folderList):
    sizeSum = 0
    for item in folder:
        if type(folder[item]) is not dict:
            sizeSum += int(folder[item])
        else: 
            subfolderSize = folderSize(folder[item], folderList)
            folderList.append((item, subfolderSize))
            sizeSum += subfolderSize
    return sizeSum


with open('input.txt', 'r') as inputFile:
    dirs = {}
    crumbs = []
    currentDir = dirs

    command = inputFile.readline()
    commandBits = command.strip().split(' ')

    while command != '':
        if commandBits[0] == '$':
            # cd command
            if commandBits[1] == 'cd':
                if commandBits[2] == '..':
                    crumbs.pop()
                    currentDir = dirs
                    for level in crumbs:
                        currentDir = currentDir[level]
                    command = inputFile.readline()
                    commandBits = command.strip().split(' ')
                else: 
                    crumbs.append(commandBits[2])
                    currentDir[commandBits[2]] = {}
                    currentDir = currentDir[commandBits[2]]
                    command = inputFile.readline()
                    commandBits = command.strip().split(' ')
            # ls command
            elif commandBits[1] == 'ls':
                command = inputFile.readline()
                while len(command) > 0 and command[0] != '$':
                    fileDetails = command.strip().split(' ')
                    if fileDetails[0] == 'dir':
                        currentDir[fileDetails[1]] = {}
                    else:
                        currentDir[fileDetails[1]] = fileDetails[0]
                    command = inputFile.readline()
                commandBits = command.strip().split(' ')
    print('done')
    folderList = []
    folderList.append(('/', folderSize(dirs['/'], folderList)))
    finalList = []
    for folder in folderList:
        if folder[1] <= 100000:
            finalList.append(folder)
    finalSum = 0
    for folder in finalList:
        finalSum += folder[1]

    print('The final sum is: ' + str(finalSum))

    totalDiskSpace = 70000000
    remainingSpace = totalDiskSpace - folderList[len(folderList) - 1][1]
    requiredSpace = 30000000
    spaceToDelete = requiredSpace - remainingSpace

    folderList.sort(key = lambda x: x[1])
    # eligibleFolders = filter(lambda x: x[1] <= remainingSpace, folderList)

    print('Remaining space: ' + str(remainingSpace))
    print('Space to delete: ' + str(spaceToDelete))

    for folder in folderList:
        if folder[1] >= spaceToDelete:
            print(folder)
            break