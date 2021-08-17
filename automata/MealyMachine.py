class State:
    def __init__(self, name):
        self.name = name
        self.trans = dict()
    
    def setTrans(self, symbol, next_, output):
        if symbol in self.trans.keys():
            raise ValueError(f"duplicated domain : {symbol}")
        self.trans[symbol] = (next_,output)
    
    def __add__(self, symbol):
        if symbol in self.trans.keys():
            State.log(self.trans[symbol][1])
            return self.trans[symbol][0]
        return None

    def next_(self, symbol):
        if symbol in self.trans.keys():
            return self.trans[symbol]
        return None, ""

    def __str__(self):
        return self.name

    def log(string):
        print(string, end = "")

class MealyM():
    #states         [str]
    #symbols_in     str
    #symbols_out    str
    #transfers      [(str,str,str)]  from,symbols,to,output
    #start          str

    def __init__(self, states, symbols_in, symbols_out, transfers, start):
        self.states = dict()
        self.start = None
        self.symbols_in = symbols_in
        self.symbols_out = symbols_out

        for state in states:
            St = State(state)
            if state == start:
                self.start = St
            self.states[state] = St

        for froms,symbols,to,output in transfers:
            for c in output:
                if c not in self.symbols_out:
                    raise ValueError(f"unexpected output in transfer: {c} is not in {self.symbols_out}")
            if type(froms) != list:
                froms = [froms]
            for from_ in froms:
                for symbol in symbols:
                    if symbol not in self.symbols_in:
                        raise ValueError(f"unexpected symbol in transfer: {symbol} is not in {self.symbols_in}")
                    St = self.states[from_]
                    St.setTrans(symbol,self.states[to],output)

    def sequence(self, query, isPrint = True):
        output = ""
        if isPrint:
            print("output from Mealy Machine : ",end = "")
        curr = self.start
        for s in query:
            name = str(curr)
            if isPrint:
                curr += s
            else:
                curr,out = curr.next_(s)
                output += out
            if curr is None:
                raise ValueError(f"unexpected transfer : {name}({s})")
        return output