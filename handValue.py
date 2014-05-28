__author__ = 'nberenyi'

class HandValue(object):
    def __init__(self, cards):
        self.cards = cards
        self.card1 = cards[0]
        self.card2 = cards[1]

    def getValue(self):
        if self.card1['rank'] == 'A' and self.card2['rank'] == 'A':
            return 100

        return 0

hv =HandValue([{u'rank': u'J', u'suit': u'spades'}, {u'rank': u'A', u'suit': u'diamonds'}])
print hv.getValue()


