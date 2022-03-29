def printInstructions(instruction):
    print(instruction)


def getUserScore(userName):
    try:
        input = open("userScores.txt", "r")
        for line in input:
            content = line.split(', ')
            if content == userName:
                input.close()
                return content[1]
        input.close()
        return '-1'
    except IOError:
        print('Файл не найден. Файл доджен быть создан.')
        input = open('userScores.txt', 'w')
        input.close()
        return '-1'


def updateUserScore(newUser, userName, score):
    from os import remove, rename
    if newUser == True:
        file = open('userScores.txt', 'a')
        file.write(userName + ', ' + score + '\n')
        file.close()
    else:
        temp = open('userScores.tmp', 'w')
        file = open('userScores.txt', 'r')
        for line in file:
            content = line.split(', ')
            if content[0] == userName:
                temp.write(userName + ', ' + score + '\n')
            else:
                temp.write(line)

        file.close()
        temp.close()

        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')

updateUserScore(False, 'Anna', '5')