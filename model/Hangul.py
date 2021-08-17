from automata.MealyMachine import MealyM

def strDiff(str1, str2):
    ret = ""
    for c in str1:
        if c not in str2:
            ret += c
    return ret


STATES = ["S", "V", "O", "U", "A", "I", "K", "N", "R", "L"]

C = "rsefaqtdwczxvgREQTW"
V = "kijuhynbml"
SYMBOLS_IN = C+V

# 0 : First-Syllable
# 1 : MIDDEL-Syllable
# 2 : FINAL-Syllable
# . : delimiter
# d : remove the Syllable before it
SYMBOLS_OUT = "012.d"

TRANSFERS_ME = [("S", C, "V", "0"),
                ("V", "h", "O", "1"),
                ("V", "n", "U", "1"),
                ("V", "kijum", "A", "1"),
                ("V", "ybl", "I", "1"),
                ("O", "k", "A", "1"),
                ("U", "j", "A", "1"),
                (["O", "U", "A"], "l", "I", "1"),
                (["O", "U", "A", "I"], "rq", "K", "2"),
                (["O", "U", "A", "I"], "s", "N", "2"),
                (["O", "U", "A", "I"], "f", "R", "2"),
                (["O", "U", "A", "I"], "eatdwczxvgRT", "L", "2"),
                (["O", "U", "A", "I"], "EQW", "V", ".0"),
                (["K", "N", "R", "L"], "h", "O", "d.01"),
                (["K", "N", "R", "L"], "n", "U", "d.01"),
                (["K", "N", "R", "L"], "kijum", "A", "d.01"),
                (["K", "N", "R", "L"], "ybl", "I", "d.01"),
                ("K", "t", "L", "2"),
                ("K", strDiff(C,"t"), "V", ".0"),
                ("N", "wg", "L", "2"),
                ("N", strDiff(C,"wg"), "V", ".0"),
                ("R", "raqtxvg", "L", "2"),
                ("R", strDiff(C,"raqtxvg"), "V", ".0"),
                ("L", C, "V", ".0")]

START = "S"

FIRST = ['r', 'R', 's', 'e', 'E', 'f', 'a', 'q', 'Q', 't',
        'T', 'd', 'w', 'W', 'c', 'z', 'x', 'v', 'g']

MIDDLE = ['k', 'kl', 'i', 'il', 'j', 'jl', 'u', 'ul', 'h',
        'hk', 'hkl', 'hl', 'y', 'n', 'nj', 'njl', 'nl', 'b',
        'm', 'ml', 'l']

LAST = ['', 'r', 'R', 'rt', 's', 'sw', 'sg', 'e', 'f', 'fr',
        'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'a', 'q', 'qt',
        't', 'T', 'd', 'w', 'c', 'z', 'x', 'v', 'g']

class HangulMe(MealyM):
    def __init__(self):
        super().__init__(STATES, SYMBOLS_IN, SYMBOLS_OUT,
            TRANSFERS_ME, START)
    
    #override
    def sequence(self, query):
        syllable_code = super().sequence(query,False)
        return HangulMe.convertToHangul(query, syllable_code)
        

    def convertToHangul(query, code):
        code_new = ""
        for c in code:
            if c == 'd':
                code_new = code_new[:-1]
            else:
                code_new += c
        code_no_dot = code_new.replace(".","")
        len_list = [len(c) for c in code_new.split(".")]

        idx = 0
        segments_query = []
        segments_code = []
        for leng in len_list:
            segments_query.append(query[idx:idx+leng])
            segments_code.append(code_no_dot[idx:idx+leng])
            idx += leng

        output = ""
        for q,c in zip(segments_query, segments_code):
            output += HangulMe.HangulChar(q,c)

        return output

    def HangulChar(query, code):
        f_chr = ""
        m_chr = ""
        l_chr = ""
        for i, c in enumerate(code):
            if c == "0":
                f_chr += query[i]
            elif c == "1":
                m_chr += query[i]
            else:
                l_chr += query[i]
        f=FIRST.index(f_chr)
        m=MIDDLE.index(m_chr)
        l=LAST.index(l_chr)

        return chr(f *588 + m *28 + l + 44032)