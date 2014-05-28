__author__ = 'nberenyi'
import random

class HandValue(object):
    def __init__(self, cards):
        self.cards = cards
        self.card1 = cards[0]
        self.card2 = cards[1]

    def getCards(self):
        return self.card1['rank'] + self.card2['rank']

    def getValue(self):
        if self.card1['rank'] == 'A' and self.card2['rank'] == 'A':
            return 100
        if self.card1['rank'] == 'A' and self.card2['rank'] == 'K':
            return 90
        if self.card1['rank'] == 'A' and self.card2['rank'] == 'Q':
            return 90
        if self.card1['rank'] == 'A' and self.card2['rank'] == 'J':
            return 90
        if self.card1['rank'] == 'K' and self.card2['rank'] == 'K':
            return 100
        if self.card1['rank'] == 'K' and self.card2['rank'] == 'A':
            return 90
        if self.card1['rank'] == 'K' and self.card2['rank'] == 'Q':
            return 90
        if self.card1['rank'] == 'K' and self.card2['rank'] == 'J':
            return 90
        if self.card1['rank'] == 'Q' and self.card2['rank'] == 'Q':
            return 100
        if self.card1['rank'] == 'Q' and self.card2['rank'] == 'A':
            return 90
        if self.card1['rank'] == 'Q' and self.card2['rank'] == 'K':
            return 90
        if self.card1['rank'] == 'Q' and self.card2['rank'] == 'J':
            return 90
        if self.card1['rank'] == 'J' and self.card2['rank'] == 'J':
            return 100
        if self.card1['rank'] == 'J' and self.card2['rank'] == 'A':
            return 90
        if self.card1['rank'] == 'J' and self.card2['rank'] == 'K':
            return 90
        if self.card1['rank'] == 'J' and self.card2['rank'] == 'Q':
            return 90
        #if self.card1['rank'] == self.card2['rank']:
        #    return 100
        return 0

#for x in range(0, 10):
#    hv3 =HandValue([{u'rank': u''+random.choice("AKQJT98765432")+'', u'suit': u'spades'}, {u'rank': u''+random.choice("AKQJT98765432")+'', u'suit': u'diamonds'}])
#    if hv3.getValue() > 90:
#        print hv3.getCards()
#        print hv3.getValue()

