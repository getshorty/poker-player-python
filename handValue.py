__author__ = 'nberenyi'
import random

class HandValue(object):
    def __init__(self, cards):
        self.cards = cards
        self.card1 = cards[0]
        self.card2 = cards[1]

    def getValue(self):
        if self.card1['rank'] == 'A' and self.card2['rank'] == 'A':
            return 100
        if self.card1['rank'] == 'A' and self.card2['rank'] == 'K':
            return 98
        if self.card1['rank'] == 'A' and self.card2['rank'] == 'Q':
            return 97
        if self.card1['rank'] == 'A' and self.card2['rank'] == 'J':
            return 95
        if self.card1['rank'] == 'K' and self.card2['rank'] == 'K':
            return 99
        if self.card1['rank'] == 'K' and self.card2['rank'] == 'A':
            return 98
        if self.card1['rank'] == 'K' and self.card2['rank'] == 'Q':
            return 93
        if self.card1['rank'] == 'K' and self.card2['rank'] == 'J':
            return 92
        if self.card1['rank'] == 'Q' and self.card2['rank'] == 'Q':
            return 96
        if self.card1['rank'] == 'Q' and self.card2['rank'] == 'A':
            return 97
        if self.card1['rank'] == 'Q' and self.card2['rank'] == 'K':
            return 93
        if self.card1['rank'] == 'Q' and self.card2['rank'] == 'J':
            return 91
        if self.card1['rank'] == 'J' and self.card2['rank'] == 'J':
            return 90
        if self.card1['rank'] == 'J' and self.card2['rank'] == 'A':
            return 95
        if self.card1['rank'] == 'J' and self.card2['rank'] == 'K':
            return 92
        if self.card1['rank'] == 'J' and self.card2['rank'] == 'Q':
            return 94
        if self.card1['rank'] == self.card2['rank'] and (self.card1['rank'] == 'T' or self.card1['rank'] == '9'):
            return 90
        if self.card1['rank'] == self.card2['rank']:
            return 80
        return 0



if __name__ == "__main__":
    for x in range(0, 200):
        rand1 = random.choice("AKQJT98765432")
        rand2 = random.choice("AKQJT98765432")
        #print rand1, rand2
        hv3 =HandValue([{u'rank': u''+rand1+'', u'suit': u'spades'}, {u'rank': u''+rand2+'', u'suit': u'diamonds'}])
        if hv3.getValue() > 90:
            print rand1, rand2, hv3.getValue()
