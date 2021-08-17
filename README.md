# En_Kor-Converter
This program is for Converting Korean that typed in English charactors to Korean.\
The basic architecture is Mealy Machine.


### Symbol Set
Σ = {ㄱ,ㄴ,ㄷ,ㄹ,ㅁ,ㅂ,ㅅ,ㅇ,ㅈ,ㅊ,ㅋ,ㅌ,ㅍ,ㅎ,ㄲ,ㄸ,ㅃ,ㅆ,ㅉ,ㅏ,ㅑ,ㅓ,ㅕ,ㅗ,ㅛ,ㅜ,ㅠ,ㅡ,ㅣ}


### Example
"dkssud" → "안녕"\
"tjltkd" → "세상"


### How to Run

    $ python3 run.py


### Files
- ```/run.py``` : Run file
- ```/test.py``` : Examples with using DFA and Me
- ```/automata/DFA.py``` : Implements on Deterministric Finite Automata (DFA)
- ```/automata/MealyMachine.py``` : Implements on Mealy Machine (Me)
- ```/model/Hangul.py``` : Implements on EnKor Converter based on Me


### Reference
[1] : [A study on the Hangul formation](https://koasas.kaist.ac.kr/handle/10203/33466, "Paper Link")
