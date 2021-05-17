import random

from Data import *


class Game:
    def __init__(self):
        self.list_verbe = []
        self.list_adjectif = []
        self.list_sujets = []
        self.lists_complements = []
        self.list_mots= []

    def starGame(self):
        self.list_verbe = random.sample(VERBES, 3)
        self.list_adjectif = random.sample(ADJ, 4)
        self.list_sujets = random.sample(SUJETS, 3)
        self.lists_complements = random.sample(COMPL, 3)
        self.list_mots = self.list_sujets + self.list_verbe + self.list_adjectif + self.lists_complements

    def removeWord(self, type, word):
        if type == "adj":
            self.list_adjectif.remove(word)
            self.list_mots.remove(word)
        if type == "verbe":
            self.list_verbe.remove(word)
            self.list_mots.remove(word)
        if type == "sujet":
            self.list_sujets.remove(word)
            self.list_mots.remove(word)
        if type == "compl":
            self.lists_complements.remove(word)
            self.list_mots.remove(word)

    def wordType(self, word):
        if word in self.list_verbe:
            return "verbe"
        if word in self.list_sujets:
            return "sujet"
        if word in self.list_adjectif:
            return "adj"
        if word in self.lists_complements:
            return "compl"