import random

def main():
    numCharacters = input("How many characters: ")
    intNumChars = 0
    try:
        intNumChars = int(numCharacters)
        print(createPassword(int(numCharacters)))
    except Exception as e:
        print('error: Did you input an integer?')


def createPassword(numChars):
    pwd = ""
    alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()=-+_][}{></\|}]"
    for i in range(0, numChars):
        randIndex = random.randint(0, len(alphabet))
        pwd += alphabet[randIndex]

    return pwd
main()
