from Game import Game
from Player import Player

run = True
player1 = Player("Joueur 1")
player2 = Player("Joueur 2")
game = Game()
game.starGame()
print(game.list_mots)
while run:
    if not player1.endInsult:
        print("--------------------Player 1 Score: ", player1.score)
        print("\t\t\t\t\tPhrase: ", player1.insult)
        word = input("\t\t\t\t\tChoix: ")
        if word == "end":
            player1.endInsult = True

        else:
            if word in game.list_mots:
                type = game.wordType(word)
                player1.play(game, type, word)
                player1.checkInsult(game)
                print(game.list_mots)
    if not player2.endInsult:
        print("------------------Player 2 Score: ", player2.score)
        print("\t\t\t\t\tPhrase: ", player2.insult)
        word = input("\t\t\t\t\tChoix: ")
        if word == "end":
            player2.endInsult = True

        else:
            if word in game.list_mots:
                type = game.wordType(word)
                player2.play(game, type, word)
                player2.checkInsult(game)
                print(game.list_mots)
    if player1.endInsult == True and player2.endInsult == True:
        run = False


print("------------------Player 1 Scrore:", player1.score)
print("------------------Player 2 Score: ", player2.score)
if player1.score > player2.score:
    print("------------------Player 1 Win------------------")
else:
    print("------------------Player 2 Win------------------")
