
class HeadsUp(object):
    def __init__(self):
        pass

    def do(self, hand, stack):

        [large, small] = self.getCardsInOrder(hand)
 #       print "ls" + str(large) + str(small)

        if large == 14:
            return stack
        elif large == small:
            return stack
        elif large == 13 and small >=6:
            return stack
        else:
            return 0

    def getValue(self, card):
        if card == 'A':
            return 14
        elif card == 'K':
            return 13
        elif card == 'Q':
            return 12
        elif card == 'J':
            return 11
        elif card == 'T':
            return 10
        else:
            try:
                return int(card)
            except ValueError:
                return 1

    def getCardsInOrder(self, cards):
#        print cards
        card1 = self.getValue(cards[0]['rank'])
        card2 = self.getValue(cards[1]['rank'])

        if card1 > card2:
            return [card1, card2]
        else:
            return [card2, card1]

if __name__ == "__main__":
    for c1 in "23456789TJQKA":
        for c2 in "23456789TJQKA":
            hand = [{'rank':c1}, {'rank':c2}]
            stack = 1000
            hu = HeadsUp()
            r = hu.do(hand, stack)
            if r > 10:
                print str(c1) + ", " + str(c2) + " : " + str(r)

    hand = [{'rank': '6'}, {'rank': '7'}]
    stack = 1000
    hu = HeadsUp()
    r = hu.do(hand, stack)
    print "ee: " + str(r)