
class MyString(str):

    def __init__(self, word):
        self.word = word

    def append(self, word_to_append):
        self.word += word_to_append
        return self.word
        
    def pop(self, letter):
        if letter != "":
            letters = self.word.split(letter) 
            self.word = "".join(letters)

        return self.word


s = MyString("Hello")

print(s.append(", world!"))
print(s.append(" I JUST LOST THE GAME"))

print(s.pop("o"))
print(s.pop("T"))