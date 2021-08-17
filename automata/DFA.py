class State:
    def __init__(self, name):
        self.name = name
        self.trans = dict()
        self.isFinal = False
    
    def setFinal(self):
        self.isFinal = True
    
    def setTrans(self, symbol, next_):
        if symbol in self.trans.keys():
            raise ValueError(f"duplicated domain : {symbol}")
        self.trans[symbol] = next_
    
    def __add__(self, symbol):
        if symbol in self.trans.keys():
            return self.trans[symbol]
        return None

    def __str__(self):
        return self.name

class DFA():
    #states     [str]
    #symbols    str
    #transfers  [(str,str,str)]  from,symbol,to
    #start      str
    #final      [str]

    def __init__(self, states, symbols, transfers, start, final):
        self.states = dict()
        self.start = None
        self.symbols = symbols

        for state in states:
            St = State(state)
            if state == start:
                self.start = St
            if state in final:
                St.setFinal()
            self.states[state] = St

        for from_,symbol,to in transfers:
            if symbol not in self.symbols:
                raise ValueError(f"unexpected symbol in transfer: {symbol}")
            St = self.states[from_]
            St.setTrans(symbol,self.states[to])

    def sequence(self, query):
        curr = self.start
        for s in query:
            name = str(curr)
            curr += s
            if curr is None:
                raise ValueError(f"unexpected transfer : {name}({s})")
        return curr.isFinal