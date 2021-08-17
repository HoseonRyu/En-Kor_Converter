from automata.DFA import DFA
from automata.MealyMachine import MealyM

STATES = ["q1","q2","q3"]
SYMBOLS_IN = "01"
SYMBOLS_OUT = "abcd"

TRANSFERS_DFA = [("q1","0","q2"),
            ("q2","0","q2"),
            ("q2","1","q3"),
            ("q3","0","q1")]

TRANSFERS_ME = [("q1","01","q2","a"),
                ("q2","0","q2","b"),
                ("q2","1","q3","c"),
                ("q3","01","q1","d")]
START = "q1"
FINAL = ["q2","q3"]

Q = "00100010"


def main():
    dfa = DFA(STATES, SYMBOLS_IN, TRANSFERS_DFA, START, FINAL)
    print(f"query in language by DFA :{dfa.sequence(Q)}")

    Me = MealyM(STATES, SYMBOLS_IN, SYMBOLS_OUT, TRANSFERS_ME, START)
    Me.sequence(Q)

if __name__ == "__main__":
    main()