rm = {6: 17, 7: 14, 8: 11,
      27: 6, 30: 7, 33: 8,
      47: 27, 46: 30, 45: 33,
      17: 47, 14: 46, 11: 45,
      18: 24, 19: 21, 20: 18, 23: 19, 26: 20, 25: 23, 24: 26, 21: 25}
rml = list(rm.keys())
    
rt = {v: k for k, v in rm.items()}
rtl = list(rt.keys())

r2 = {6: 47, 7: 46, 8: 45,
      27: 17, 30: 14, 33: 11,
      47: 6, 46: 7, 45: 8,
      17: 27, 14: 30, 11: 33,
      18: 26, 19: 25, 20: 24, 23: 21, 26: 18, 25: 19, 24: 20, 21: 23}
r2l = list(r2.keys())




um = {38: 11, 37: 10, 36: 9,
      29: 38, 28: 37, 27: 36,
      20: 29, 19: 28, 18: 27,
      11: 20, 10: 19, 9: 18,
      0: 6, 1: 3, 2: 0, 5: 1, 8: 2, 7: 5, 6: 8, 3: 7}
uml = list(um.keys())
    
ut = {v: k for k, v in um.items()}
utl = list(ut.keys())

u2 = {38: 20, 37: 19, 36: 18,
      29: 11, 28: 10, 27: 9,
      20: 38, 19: 37, 18: 36,
      11: 29, 10: 28, 9: 27,
      0: 8, 1: 7, 2: 6, 5: 3, 8: 0, 7: 1, 6: 2, 3: 5}
u2l = list(u2.keys())




fm = {0: 44, 3: 41, 6: 38,
      18: 0, 21: 3, 24: 6,
      45: 18, 48: 21, 51: 24,
      38: 51, 41: 48, 44: 45,
      9: 15, 10: 12, 11: 9, 14: 10, 17: 11, 16: 14, 15: 17, 12: 16}
fml = list(fm.keys())

ft = {v: k for k, v in fm.items()}
ftl = list(ft.keys())

f2 = {0: 45, 3: 48, 6: 51,
      18: 44, 21: 41, 24: 38,
      45: 0, 48: 3, 51: 6,
      38: 24, 41: 21, 44: 18,
      9: 17, 10: 16, 11: 15, 14: 12, 17: 9, 16: 10, 15: 11, 12: 14}
f2l = list(f2.keys())




bm = {2: 20, 5: 23, 8: 26,
      20: 47, 23: 50, 26: 53,
      47: 42, 50: 39, 53: 36,
      42: 2, 39: 5, 36: 8,
      27: 33, 28: 30, 29: 27, 32: 28, 35: 29, 34: 32, 33: 35, 30: 34}
bml = list(bm.keys())

bt = {v: k for k, v in bm.items()}
btl = list(bt.keys())

b2 = {2: 47, 5: 50, 8: 53,
      20: 42, 23: 39, 26: 36,
      47: 2, 50: 5, 53: 8,
      42: 20, 39: 23, 36: 26,
      27: 35, 28: 34, 29: 33, 32: 30, 35: 27, 34: 28, 33: 29, 30: 32}
b2l = list(b2.keys())




lt = {0: 15, 1: 12, 2: 9,
      29: 0, 32: 1, 35: 2,
      53: 29, 52: 32, 51: 35,
      15: 53, 12: 52, 9: 51,
      36: 38, 37: 41, 38: 44, 41: 43, 44: 42, 43: 39, 42: 36, 39: 37}
ltl = list(lt.keys())
                                      #    _ ___    __   __
lm = {v: k for k, v in lt.items()}    #|  |_  |    |  | |__|
lml = list(lm.keys())                 #|_ |_  |    |__| |
                                      #
l2 = {0: 53, 1: 52, 2: 51,
      29: 15, 32: 12, 35: 9,
      53: 0, 52: 1, 51: 2,
      15: 29, 12: 32, 9: 35,
      36: 44, 37: 43, 38: 42, 41: 39, 44: 36, 43: 37, 42: 38, 39: 41}
l2l = list(l2.keys())




dm = {15: 42, 16: 43, 17: 44,
      24: 15, 25: 16, 26: 17,
      33: 24, 34: 25, 35: 26,
      42: 33, 43: 34, 44: 35,
      45: 51, 46: 48, 47: 45, 50: 46, 53: 47, 52: 50, 51: 53, 48: 52}
dml = list(dm.keys())

dt = {v: k for k, v in dm.items()}
dtl = list(dt.keys())

d2 = {15: 33, 16: 34, 17: 35,
      24: 42, 25: 43, 26: 44,
      33: 15, 34: 16, 35: 17,
      42: 24, 43: 25, 44: 26,
      45: 53, 46: 52, 47: 51, 50: 48, 53: 45, 52: 46, 51: 47, 48: 50}
d2l = list(d2.keys())




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
