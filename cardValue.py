__author__ = 'qzoltan'

class CardValue(object):
    VALUES = { '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14 }
    
    def __init__(self, cards):
        self.cards = cards
        
        self.equ = {}
        self.col = {}

    # -----------------------------
    def getValue(self):
        rVal = 0

        self.equFunc()
        sames =  max( [ e for e in self.equ.values() ] )

        # --- 1p, dr, po
        try:
          if sames >= 1:
            rVal = { 1:0, 2:10, 3:30, 4:70 }[ sames ]
        except:
          pass
        
        # --- 2p
        doubles = self.countThem( 2 )
        if doubles >= 2:
          rVal = max( rVal, 20 )
          
        # --- fullhouse
        threes =  self.countThem( 3 )
        if doubles >= 1 and threes >= 1 or threes == 2:
          rVal = max( rVal, 60 )
          
        # --- flush
        if 5 <= max( [ c for c in self.col.values() ] ):
          rVal = max( rVal, 50 )

        # --- line
        vals = [ self.VALUES[ v['rank'] ] for v in self.cards ]
        vals.sort()
        
        line = True
        lineC = 0

        for x in range( len (vals[1:]) ):
          if 1 == vals[x+1] - vals[x]:
            lineC += 1
          else:
            lineC = 0
          
        if 5 == lineC:
          rVal = max( rVal, 40 )
        
          
        return rVal
    # -----------------------------
        
        
    # --- FUNC    
    def equFunc( self ):
      for c in self.cards:
        try:
          self.equ[ c['rank'] ] += 1
        except:
           self.equ[ c['rank'] ]  = 1
           
        try:
          self.col[ c['suit'] ] += 1
        except:
          self.col[ c['suit'] ]  = 1

          
           
    def countThem( self, pThem ):
      vRet = 0
      for e in self.equ.values():
        if e == pThem:
          vRet += 1
      return vRet
        
      
        
      
# --- MAIN -----------------------------      
if __name__ == '__main__':
  # --- pok
  dicc = [{u'rank': u'J', u'suit': u'spades'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'K', u'suit': u'diamonds'}]
  hv =CardValue( dicc )
  print dicc
  print 'pok', hv.getValue()
  print

  # --- 2p
  dicc = [{u'rank': u'J', u'suit': u'spades'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'2', u'suit': u'diamonds'}, {u'rank': u'2', u'suit': u'diamonds'}, {u'rank': u'K', u'suit': u'diamonds'}]
  hv =CardValue( dicc )
  print dicc
  print '2p', hv.getValue()
  print

  # --- 2p
  dicc = [{u'rank': u'2', u'suit': u'spades'}, {u'rank': u'A', u'suit': u'diamonds'}, {u'rank': u'2', u'suit': u'spades'}, {u'rank': u'A', u'suit': u'diamonds'}]
  hv =CardValue( dicc )
  print dicc
  print '2p', hv.getValue()
  print

  # --- fullh
  dicc = [{u'rank': u'J', u'suit': u'spades'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'K', u'suit': u'diamonds'}, {u'rank': u'K', u'suit': u'diamonds'}]
  hv =CardValue( dicc )
  print dicc
  print 'fullh', hv.getValue()
  print
  
  # --- double three
  dicc = [{u'rank': u'J', u'suit': u'spades'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'2', u'suit': u'diamonds'}, {u'rank': u'2', u'suit': u'diamonds'}, {u'rank': u'2', u'suit': u'diamonds'},{u'rank': u'J', u'suit': u'diamonds'}]
  hv =CardValue( dicc )
  print dicc
  print 'double three', hv.getValue()
  print
  
  # --- flush
  dicc = [{u'rank': u'2', u'suit': u'spades'}, {u'rank': u'J', u'suit': u'spades'}, {u'rank': u'J', u'suit': u'spades'}, {u'rank': u'K', u'suit': u'spades'}, {u'rank': u'K', u'suit': u'spades'}]
  hv =CardValue( dicc )
  print dicc
  print 'flush', hv.getValue()
  print


# --- line
  dicc = [{u'rank': u'J', u'suit': u'spades'}, {u'rank': u'10', u'suit': u'diamonds'}, {u'rank': u'Q', u'suit': u'diamonds'}, {u'rank': u'9', u'suit': u'spades'}, {u'rank': u'5', u'suit': u'diamonds'},{u'rank': u'8', u'suit': u'diamonds'},{u'rank': u'7', u'suit': u'heart'}]
  hv =CardValue( dicc )
  print dicc
  print 'line', hv.getValue()
  print
        