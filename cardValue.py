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

        self.equFunc()
        
        sames =  max( [ e  for e in self.equ.values() ] )
        
        if sames >= 1:
          val = { 1:0, 2:10, 3:30, 4:70 }[ sames ]
        
        doubles = 0
        for e in self.equ.values():
          if e >= 2:
            doubles +=1
            
        if doubles == 2:
          val = max( val, 20 )

          
        return val
        
        
    def equFunc( self ):
      for c in self.cards:
        try:
          self.equ[ c['rank'] ] += 1
        except:
           self.equ[ c['rank'] ]  = 1
           
      ##print 1111, self.equ
      ##return max( [ e  for e in self.equ.values() ] )
      
        
      
      
if __name__ == '__main__':
  dicc = [{u'rank': u'J', u'suit': u'spades'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'K', u'suit': u'diamonds'}]
  hv =CardValue( dicc )
  print hv.getValue()

  dicc = [{u'rank': u'J', u'suit': u'spades'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'K', u'suit': u'diamonds'}, {u'rank': u'K', u'suit': u'diamonds'}]
    
  hv =CardValue( dicc )
  print 
  print hv.getValue()
  
  
  
  
