class Hero:

    def __init__(self, name, word):
        self.name = name
        self.word = word

    def __str__(self):
        return self.name

    def sravni(self, word_1, word_2):
        self.word_1 = word_1
        self.word_2 = word_2
        print(word_1 != word_2)

def words(i):
    for word in range(i):
        print(word)


if __name__ == "__main__":

    words(23)

    word = Hero("Kulich", "geroi")
    print(word)

    word.sravni("T22oo", "T2oo")
