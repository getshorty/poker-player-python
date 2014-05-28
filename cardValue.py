__author__ = 'qzoltan'

class CardValue(object):
    PAIR=2
    
    def __init__(self, cards):
        self.cards = cards
        
        self.equ = {}
        self.col = {}

    def getValue(self):
        rVal = 0

        self.equFunc()
        sames =  max( [ e for e in self.equ.values() ] )

        # --- 1p, dr, po        
        if sames >= 1:
          rVal = { 1:0, 2:10, 3:30, 4:70 }[ sames ]
        
        # --- 2p
        doubles = self.countThem( 2 )
        if doubles == 2:
          rVal = max( rVal, 20 )
          
        # --- fullhouse
        threes =  self.countThem( 3 )
        if doubles == 1 and threes == 1:
          rVal = max( rVal, 60 )
          
        # --- flush
        if 5 <= max( [ c for c in self.col.values() ] ):
          rVal = max(  rVal, 50 )

        # --- line ERROR
        vals = [ v for v in self.equ.values() ]
        vals.sort()
        ##difis = reduce( lambda x,y: 1 == abs(y - x), vals )
        ##print 'DIFIS', difis
        line = True
        for x in range( len (vals[1:]) ):
          line = line and 1 == vals[x+1] - vals[x]
         
        if line:
          rVal = max( rVal, 40 )
        
          
        return rVal
        
        
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
  print hv.getValue()
  print

  # --- 2p
  dicc = [{u'rank': u'J', u'suit': u'spades'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'2', u'suit': u'diamonds'}, {u'rank': u'2', u'suit': u'diamonds'}, {u'rank': u'K', u'suit': u'diamonds'}]
  hv =CardValue( dicc )
  print dicc
  print hv.getValue()
  print

  # --- fullh
  dicc = [{u'rank': u'J', u'suit': u'spades'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'J', u'suit': u'diamonds'}, {u'rank': u'K', u'suit': u'diamonds'}, {u'rank': u'K', u'suit': u'diamonds'}]
  hv =CardValue( dicc )
  print dicc
  print hv.getValue()
  print
  
  # --- flush
  dicc = [{u'rank': u'2', u'suit': u'spades'}, {u'rank': u'J', u'suit': u'spades'}, {u'rank': u'J', u'suit': u'spades'}, {u'rank': u'K', u'suit': u'spades'}, {u'rank': u'K', u'suit': u'spades'}]
  hv =CardValue( dicc )
  print dicc
  print hv.getValue()
  print
