__author__ = 'szszrenko'
import random

#USAGE
#import getRandomDeckforHands
#getRandomDeckforHands.hv.getChoice()
class RandomDeck(object):
    def __init__(self, cards):
        self.cards = cards
        self.card1 = cards[0]
        self.card2 = cards[1]

    def getChoice(self):
        return self.cards

hv= RandomDeck([{u'rank': u''+random.choice("AKQJT98765432")+'', u'suit': u''+random.choice(['spades', 'diamonds', 'aces', 'clubs'])+''}, {u'rank': u''+random.choice("AKQJT98765432")+'', u'suit': u''+random.choice(['spades', 'diamonds', 'aces', 'clubs'])+''}])
