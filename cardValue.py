__author__ = 'nberenyi'

class CardValue(object):
    PAIR=2
    def __init__(self, cards):
        self.cards = cards
        self.card1 = cards[0]
        self.card2 = cards[1]
        
        self.equ = {}

    def getValue(self):
##        if self.card1['rank'] == 'A' and self.card2['rank'] == 'A':
##            return 100
##        return 0

        val = 0

        self.equFunc()
        sames =  max( [ e  for e in self.equ.values() ] )

        # --- 1p, dr, po        
        if sames >= 1:
          val = { 1:0, 2:10, 3:30, 4:70 }[ sames ]
        
        # --- 2p
        doubles = self.countThem( 2 )
        
        if doubles == 2:
          val = max( val, 20 )
          
        # --- fullhouse
        threes =  self.countThem( 3 )
        if doubles == 1 and threes == 3:
          val = max( val, 30 )

          
        return val
        
        
    # --- FUNC    
    def equFunc( self ):
      for c in self.cards:
        try:
          self.equ[ c['rank'] ] += 1
        except:
           self.equ[ c['rank'] ]  = 1
           
      ##print 1111, self.equ
      ##return max( [ e  for e in self.equ.values() ] )
      
      
    def countThem( self, pThem ):
      vRet = 0
      for e in self.equ.values():
        if e >= pThem:
          vRet += 1
      return vRet
        
      
        
      
      
if __name__ == '__main__':
  dicc = [{u'rank': u'J', u'suit': u'spades'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'K', u'suit': u'diamonds'}]
  hv =CardValue( dicc )
  print dicc
  print hv.getValue()
  print

  dicc = [{u'rank': u'J', u'suit': u'spades'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'K', u'suit': u'diamonds'}, {u'rank': u'K', u'suit': u'diamonds'}]
  hv =CardValue( dicc )
  print dicc
  print hv.getValue()
  print
