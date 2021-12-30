#ヒューマンクラス
class Human:
    def __init__(self, name, age):
        print('ヒューマンクラスのコンストラクタ')
        self.name = name
        self.age = age
    def __del__(self):
        print('ヒューマンクラスのデストラクタ')
    def printName(self):
        print('my name is ' + self.name)
    def printAge(self):
        print('im ' + str(self.age) + ' years old')
    def setAge(self, num):
        self.age = num