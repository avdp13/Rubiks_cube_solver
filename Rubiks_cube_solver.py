from Rubiks_cube_data import *

def rotate(pos, rn):
    l = list(pos)    
    lb = list(pos)
    
    if rn == "R'":
        for f in rtl:
            l[f] = lb[rt[f]]
    elif rn == "R":
        for f in rml:
            l[f] = lb[rm[f]]
    elif rn == "R2":
        for f in r2l:
            l[f] = lb[r2[f]]

    elif rn == "U":
        for f in uml:
            l[f] = lb[um[f]]
    elif rn == "U'":
        for f in utl:
            l[f] = lb[ut[f]]
    elif rn == "U2":
        for f in u2l:
            l[f] = lb[u2[f]]

    elif rn == "F":
        for f in fml:
            l[f] = lb[fm[f]]
    elif rn == "F'":
        for f in ftl:
            l[f] = lb[ft[f]]
    elif rn == "F2":
        for f in f2l:
            l[f] = lb[f2[f]]

    elif rn == "L":
        for f in lml:
            l[f] = lb[lm[f]]
    elif rn == "L'":
        for f in ltl:
            l[f] = lb[lt[f]]
    elif rn == "L2":
        for f in l2l:
            l[f] = lb[l2[f]]

    elif rn == "B":
        for f in bml:
            l[f] = lb[bm[f]]
    elif rn == "B'":
        for f in btl:
            l[f] = lb[bt[f]]
    elif rn == "B2":
        for f in b2l:
            l[f] = lb[b2[f]]

    elif rn == "D":
        for f in dml:
            l[f] = lb[dm[f]]
    elif rn == "D'":
        for f in dtl:
            l[f] = lb[dt[f]]
    elif rn == "D2":
        for f in d2l:
            l[f] = lb[d2[f]]
    
    npos = ''.join(l)
    return npos

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

pos = ''#input('Wat is de positie van de rubiks cube? ')#'WWWWWWWWWRRRRRRRRRBBBBBBBBBOOOOOOOOOGGGGGGGGGYYYYYYYYY'#'YGYWWBRBGBRBYRRBWYWRRYBGROGWYROOOYBWGROYGGGGOBWOBYOWWO'
origpos = 'WWWWWWRRGRRYRRWRRRBBWOBBWBBOBBOOOOOOOGGGGGGGGBYYYYYYYY'


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
#                zetten.append(wla[f'lag{d}'][-1])
        
        d = len(wla[f'lag{a}'])

        nd = pm[d]

        if rz[nd] == lz:
            wla[f'lag{a}'].append(nd)
            continue

        lz = pm[d]
    
        pos = rotate(pos, nd)
        wla[f'lag{a}'].append(nd)
#        zetten.append(nd)

        if len(zetten) == 20:
            wla[f'lag{a}'].pop()
#            zetten.pop()
            a -= 2
    
        a += 1

        for h in wla:
            if len(wla[h]) == 18:
                wla[h] = []


    except IndexError:
#        print('IndexError')
        a -= 1
#        print('IndexError')
#    except KeyError:
#        print('keyerr')
#        a += 3
#        pass
#        a += 2
#        print(a)
#        wla[f'lag{a}'] = []
#        print('KeyError')

zetten = []
for d in range(a):
    zetten.append(wla[f'lag{d}'][-1])

print()
print(zetten)
