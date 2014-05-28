# -*- coding: utf-8 -*-
from cardValue import CardValue
import getRandomDeckforHands
import math



# state = {u'community_cards': [], u'minimum_raise': 10, u'small_blind': 10, u'pot': 30, u'orbits': 0, u'players': [{u'status': u'active', u'hole_cards': [{u'rank': u'2', u'suit': u'spades'}, {u'rank': u'A', u'suit': u'diamonds'}], u'name': u'Peter Python', u'id': 0, u'version': u'Default Python folding player', u'stack': 980, u'bet': 20}, {u'status': u'folded', u'name': u'Peter P2', u'stack': 1000, u'version': u'Default Python folding player', u'id': 1, u'bet': 0}, {u'status': u'folded', u'name': u'Peter P3', u'stack': 1000, u'version': u'Default Python folding player', u'id': 2, u'bet': 0}, {u'status': u'folded', u'name': u'Peter P4', u'stack': 990, u'version': u'Default Python folding player', u'id': 3, u'bet': 10}], u'in_action': 0, u'dealer': 2, u'current_buy_in': 20}
state = {u'community_cards': [{u'rank': u'A', u'suit': u'spades'}, {u'rank': u'A', u'suit': u'diamonds'}], u'minimum_raise': 10, u'small_blind': 10, u'pot': 30, u'orbits': 0, u'players': [{u'status': u'active', u'hole_cards': [{u'rank': u'2', u'suit': u'spades'}, {u'rank': u'A', u'suit': u'diamonds'}], u'name': u'Peter Python', u'id': 0, u'version': u'Default Python folding player', u'stack': 980, u'bet': 20}, {u'status': u'folded', u'name': u'Peter P2', u'stack': 1000, u'version': u'Default Python folding player', u'id': 1, u'bet': 0}, {u'status': u'folded', u'name': u'Peter P3', u'stack': 1000, u'version': u'Default Python folding player', u'id': 2, u'bet': 0}, {u'status': u'folded', u'name': u'Peter P4', u'stack': 990, u'version': u'Default Python folding player', u'id': 3, u'bet': 10}], u'in_action': 0, u'dealer': 2, u'current_buy_in': 20}


class Strategy(object):

    # returns with the raise amount for pre-flop and flop state, based on the given game state
    def do(self, state):
        if (self.isPreFlop(state)):
            return self.doPreFlop(state)
        else:
            return self.doFlop(state)

    def getCommonCards(self, state):
        return state['community_cards']

    # returns true if state is in pre flop
    def isPreFlop(self, state):
        print ("isPreFlop: " + str(len(self.getCommonCards(state)) == 0))
        return len(self.getCommonCards(state)) == 0

    # returns with the raise amount for pre-flop state
    def doPreFlop(self, state):
        print "pre-flop game"

        cards = self.getOurCards(state)
        ranks = self.getRanks(cards)
        #ranks = "AK"   # for test only
        print "card ranks: " + ranks

        # rule 1 - 4
        if (ranks == "AA" or ranks == "KK" or ranks == "QQ" or ranks == "JJ"):
            print "all in AA: " + str(self.getAllin(state))
            return self.getAllin(state)

        # rule 3 AK
        if (ranks == "AK"):
            print "all in AK: " + str(self.getAllin(state))
            return self.getAllin(state)

        if (ranks == "TT" or ranks == "99" or ranks == "AQ" or ranks == "AJ"):
            smallx6 = 6 * self.getSmallBlind(state)
            print "6 x small blind: " + str(smallx6)
            minRaise = self.getMinRaise(state)
            print "6 x small blind: " + str(minRaise)
            if (smallx6 > minRaise):
                return smallx6
            else:
                return self.getAllin(state)

        if (ranks == "88" or ranks == "77"
            or ranks == "66" or ranks == "55" or ranks == "44" or ranks == "33" or ranks == "22"
            or ranks == "KQ"):
            smallx6 = 6 * self.getSmallBlind(state)
            print "6 x small blind: " + str(smallx6)
            minRaise = self.getMinRaise(state)
            print "6 x small blind: " + str(minRaise)
            if (smallx6 > minRaise):
                return smallx6
            else:
                return 0

        return 0

    # returns with the raise amount for flop state
    def doFlop(self, state):
        print "warning: flop game"
        cards = self.getOurCards(state)
        cards2 = self.getCommonCards(state)
        cards3 = list(cards)
        cards3.extend(cards2)
        print "all cards: " + str(cards3)

        cardValue = CardValue(cards3)
        value = cardValue.getValue()
        print "card value " + str(value)
        if (value > 9):
            raisee = math.floor(self.getPot(state) * 3 / 2)
            print "we have one pair, raise: " + str(raisee)
            return raisee

        return 0

    def getOurPlayer(self, state):
        pos = self.getPosition(state)
        print "our position: " + str(pos)
        players = state['players']
        player = players[pos]
        print "player: " + str(player)
        return player

    def getSmallBlind(self, state):
        print "small blind: " + str(state['small_blind'])
        return state['small_blind']

    def getMinRaise(self, state):
        print "min raise: " + str(state['minimum_raise'])
        return state['minimum_raise']

    def getPot(self, state):
        print "pot: " + str(state['pot'])
        return state['pot']

    # returns the stack of our player
    def getAllin(self, state):
        player = self.getOurPlayer(state)
        print "all in: " + str(player['stack'])
        return player['stack']

    def getRanks(self, cards):
        ranks = ""
        for card in cards:
            ranks = ranks + card['rank']
        return ''.join(sorted(ranks))

    def getOurCards(self, state):
        player = self.getOurPlayer(state)
        cards = player['hole_cards']
        print "cards at me: " + str(cards)
        return cards

    def getPosition(self, state):
        return state['in_action']

if __name__ == "__main__":
    s = Strategy()
    v = s.do(state)
    print " raisee" + str(v)
