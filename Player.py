class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.insult = ""
        self.endInsult = False

    def play(self, game, type, word):
        game.removeWord(type, word)
        self.insult += word + " "
        self.score = len(self.insult)

    def checkInsult(self, game):
        listInsult = self.insult.split(" ")
        if len(listInsult) > 3:
            if game.wordType(listInsult[0])=="sujet" and game.wordType(listInsult[1])=="verbe" and game.wordType(listInsult[1])=="comp":
                self.score +=5
            else:
                self.score -=5