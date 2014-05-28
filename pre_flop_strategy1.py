# -*- coding: utf-8 -*-
from cardValue import CardValue
import getRandomDeckforHands
import math



state = {u'community_cards': [], u'minimum_raise': 10, u'small_blind': 300, u'pot': 30, u'orbits': 0, u'players': [{u'status': u'active', u'hole_cards': [{u'rank': u'7', u'suit': u'spades'}, {u'rank': u'K', u'suit': u'diamonds'}], u'name': u'Peter Python', u'id': 0, u'version': u'Default Python folding player', u'stack': 980, u'bet': 20}, {u'status': u'folded', u'name': u'Peter P2', u'stack': 1000, u'version': u'Default Python folding player', u'id': 1, u'bet': 0}, {u'status': u'folded', u'name': u'Peter P3', u'stack': 1000, u'version': u'Default Python folding player', u'id': 2, u'bet': 0}, {u'status': u'folded', u'name': u'Peter P4', u'stack': 990, u'version': u'Default Python folding player', u'id': 3, u'bet': 10}], u'in_action': 0, u'dealer': 2, u'current_buy_in': 20}
#state = {u'community_cards': [{u'rank': u'K', u'suit': u'diamonds'}, {u'rank': u'A', u'suit': u'diamonds'}, {u'rank': u'A', u'suit': u'diamonds'}], u'minimum_raise': 10, u'small_blind': 10, u'pot': 30, u'orbits': 0, u'players': [{u'status': u'active', u'hole_cards': [{u'rank': u'2', u'suit': u'spades'}, {u'rank': u'A', u'suit': u'diamonds'}], u'name': u'Peter Python', u'id': 0, u'version': u'Default Python folding player', u'stack': 980, u'bet': 20}, {u'status': u'folded', u'name': u'Peter P2', u'stack': 1000, u'version': u'Default Python folding player', u'id': 1, u'bet': 0}, {u'status': u'folded', u'name': u'Peter P3', u'stack': 1000, u'version': u'Default Python folding player', u'id': 2, u'bet': 0}, {u'status': u'folded', u'name': u'Peter P4', u'stack': 990, u'version': u'Default Python folding player', u'id': 3, u'bet': 10}], u'in_action': 0, u'dealer': 2, u'current_buy_in': 20}
#state = {u'community_cards': [{u'rank': u'A', u'suit': u'spades'}, {u'rank': u'K', u'suit': u'diamonds'}, {u'rank': u'A', u'suit': u'diamonds'}, {u'rank': u'A', u'suit': u'diamonds'}], u'minimum_raise': 10, u'small_blind': 10, u'pot': 30, u'orbits': 0, u'players': [{u'status': u'active', u'hole_cards': [{u'rank': u'2', u'suit': u'spades'}, {u'rank': u'A', u'suit': u'diamonds'}], u'name': u'Peter Python', u'id': 0, u'version': u'Default Python folding player', u'stack': 980, u'bet': 20}, {u'status': u'folded', u'name': u'Peter P2', u'stack': 1000, u'version': u'Default Python folding player', u'id': 1, u'bet': 0}, {u'status': u'folded', u'name': u'Peter P3', u'stack': 1000, u'version': u'Default Python folding player', u'id': 2, u'bet': 0}, {u'status': u'folded', u'name': u'Peter P4', u'stack': 990, u'version': u'Default Python folding player', u'id': 3, u'bet': 10}], u'in_action': 0, u'dealer': 2, u'current_buy_in': 20}


class Strategy(object):

    # returns with the raise amount for pre-flop and flop state, based on the given game state
    def do(self, state):
        if (self.isPreFlop(state)):
            return self.doPreFlop(state)
        else:
#            if (not self.isRiver(state)):
            return self.doFlop(state)
#            else:
#                return self.doRiver(state)

    def getCommonCards(self, state):
        return state['community_cards']

    # returns true if state is in pre flop
    def isPreFlop(self, state):
        print ("isPreFlop: " + str(len(self.getCommonCards(state)) == 0))
        return len(self.getCommonCards(state)) == 0

    # returns true if state is in river
    def isRiver(self, state):
        print ("isRiver: " + str(len(self.getCommonCards(state)) == 4))
        return len(self.getCommonCards(state)) == 4

    # returns true if state is in turn
    def isTurn(self, state):
        print ("isTurn: " + str(len(self.getCommonCards(state)) == 5))
        return len(self.getCommonCards(state)) == 5

    # returns with the raise amount for pre-flop state
    def doPreFlop(self, state):
        print "pre-flop game"

        cards = self.getOurCards(state)
        ranks = self.getRanks(cards)
        #ranks = "AK"   # for test only
        print "card ranks: " + ranks

        isRateLow = self.isRateLow(state)
        print "isRateLow: " + str(isRateLow)

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
            if (isRateLow):
                return self.getAllin(state)
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
            if (isRateLow):
                return self.getAllin(state)
            if (smallx6 > minRaise):
                return smallx6
            else:
                return 0

        if (isRateLow):
            if (ranks == "7A" or ranks =="8A" or ranks == "9A" or ranks == "AT"
                or ranks == "7K" or ranks =="8K" or ranks == "9K" or ranks == "KT"):
                return self.getAllin(state)

        return 0

    # returns with the raise amount for flop state
    def doFlop(self, state):
        
        print " flop game"
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

    # returns with the raise amount for river state
    def doRiver(self, state):
        
        print "warning: river game"
        rate = self.getRate(state)
        
        cards = self.getOurCards(state)
        cards2 = self.getCommonCards(state)
        cards3 = list(cards)
        cards3.extend(cards2)
        print "all cards: " + str(cards3)

        cardValueCommon = CardValue(cards2)
        valueCommon = cardValue.getValue()
        print "card value common" + str(valueCommon)

        cardValueAll = CardValue(cards3)
        valueAll = cardValue.getValue()
        print "card value all" + str(valueAll)
        if (valueAll > 9):
            raisee = math.floor(self.getPot(state) * 3 / 2)
            print "we have one pair, raise: " + str(raisee)
            return raisee

        return 0

    def isRateLow(self, state):
        rate = self.getRate(state)
        return rate < 10

    def getRate(self, state):
        ourStack = self.getAllin(state)
        bigBlind = 2 * self.getSmallBlind(state)
        rate = ourStack / bigBlind
        print "rate: " + str(rate)
        return rate

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

    def getHighestRank(self, cards):
        pass

if __name__ == "__main__":
    s = Strategy()
    v = s.do(state)
    print " raisee" + str(v)
