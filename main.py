from Human import Human
from Programer import Programer

def main():
    print('hello world')
    kame = Programer('かめ', 27, ['python', 'C++', 'java', 'VBA'])
    kame.printName()
    kame.printAge()
    kame.printLangs()
    kame.setAge(28)
    kame.printAge()
    kame.addLang('JS')
    kame.printLangs()

    # human2 = Human('ゆうや', 27)
    # human2.printName()
    # human2.printAge()

if __name__ == '__main__':
    main()