#プログラマクラス
from Human import Human

class Programer(Human):
    def __init__(self, name, age, langs):
        super().__init__(name, age)
        self.langs = langs
    def printLangs(self):
        for lang in self.langs:
            print(lang)
    def addLang(self, lang):
        self.langs.append(lang)