from Rubiks_cube_data import *#   This is my other code named Rubiks_cube_data.py

wh = {"R'": [rtl, rt], "R": [rml, rm], "R2": [r2l, r2],
      "U'": [utl, ut], "U": [uml, um], "U2": [u2l, u2],
      "F'": [ftl, ft], "F": [fml, fm], "F2": [f2l, f2],
      "L'": [ltl, lt], "L": [lml, lm], "L2": [l2l, l2],
      "B'": [btl, bt], "B": [bml, bm], "B2": [b2l, b2],
      "D'": [dtl, dt], "D": [dml, dm], "D2": [d2l, d2]}

ch = {5: 'W', 13: 'R', 22: 'B', 31: 'O', 40: 'G', 49: 'Y'}

def rotate(pos, rn):#    Rotates a move on rubiks cube
    l = list(pos)    
    lb = list(pos)

    for f in wh[rn][0]:
        l[f] = lb[wh[rn][1][f]]

    npos = ''.join(l)
    return npos

ch = {5: 'W', 13: 'R', 22: 'B', 31: 'O', 40: 'G', 49: 'Y'}

def check(pos):#    Checks if the rubiks cube is filled out correctly.
    tof = True

    tellen = []
    tellen.append(pos.count('W'))
    tellen.append(pos.count('R'))
    tellen.append(pos.count('B'))
    tellen.append(pos.count('O'))
    tellen.append(pos.count('G'))
    tellen.append(pos.count('Y'))

    for w in ch:
        if pos[w] != ch[w]:
            print('Niet juist ingevuld: Center(s) niet juist.')
            tof = False
            break
    if len(pos) != 54:
        print('Niet juist ingevuld: Foute hoeveelheid vakjes.')
        tof = False
    if not len(set(tellen)) == 1:
        print('Niet juist ingevuld: Foute hoeveelheid van een bepaalde kleur.')
        tof = False
    
    if not tof:
        origpos = 'WWWWWWRRGRRYRRWRRRBBWOBBWBBOBBOOOOOOOGGGGGGGGBYYYYYYYY'.upper()
        check(origpos)

print("""
               ----------------
               | 0  | 1  | 2  |
               ----------------
               | 3  | W  | 5  |
               ----------------
               | 6  | 7  | 8  |
               ----------------
-------------------------------------------------------------
| 9  | 10 | 11 | 18 | 19 | 20 | 27 | 28 | 29 | 36 | 37 | 38 |
-------------------------------------------------------------
| 12 | R  | 14 | 21 | B  | 23 | 30 | O  | 32 | 39 | G  | 41 |
-------------------------------------------------------------
| 15 | 16 | 17 | 24 | 25 | 26 | 33 | 34 | 35 | 42 | 43 | 44 |
-------------------------------------------------------------
               ----------------
               | 45 | 46 | 47 |
               ----------------
               | 48 | Y  | 50 |
               ----------------
               | 51 | 52 | 53 |
               ----------------""")

pos = ''#input('Wat is de positie van de rubiks cube? ')#'WWWWWWWWWRRRRRRRRRBBBBBBBBBOOOOOOOOOGGGGGGGGGYYYYYYYYY'
origpos = 'WWWWWWRRGRRYRRWRRRBBWOBBWBBOBBOOOOOOOGGGGGGGGBYYYYYYYY'.upper()# Has to be an input later.

check(origpos)


rz = {"F": "F'", "F'": "F", "F2": "F2",
      "R": "R'", "R'": "R", "R2": "R2",
      "U": "U'", "U'": "U", "U2": "U2",
      "D": "D'", "D'": "D", "D2": "D2",
      "B": "B'", "B'": "B", "B2": "B2",
      "L": "L'", "L'": "L", "L2": "L2",}

pm = ["F", "F'", "F2", "R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'", "D2", "B", "B'", "B2"]
zetten = []

wla = {}

for s in range(20):
    wla[f'lag{s}'] = []

a = 0
lz = ''


while pos != 'WWWWWWWWWRRRRRRRRRBBBBBBBBBOOOOOOOOOGGGGGGGGGYYYYYYYYY':
    try:
        pos = origpos

        for d in range(a):
            if lz != wla[f'lag{d}'][-1] and d == a - 1:
                a -= 1
                break
            else:
                pos = rotate(pos, wla[f'lag{d}'][-1])

#        print(wla)
#        print(a)
        
        d = len(wla[f'lag{a}'])

        nd = pm[d]
        lz = pm[d]
    
        pos = rotate(pos, nd)
        wla[f'lag{a}'].append(nd)

        if a == 19:
            wla[f'lag{a}'].pop()
            a -= 2
    
        a += 1

        for h in wla:
            if len(wla[h]) == 18:
                wla[h] = []
                a -= 1


#    except IndexError:
#        print('in')
#        if a != 0:
#            a -= 1
    finally:
        pass

zetten = []
for d in range(a):
    zetten.append(wla[f'lag{d}'][-1])

print()
print(zetten)



