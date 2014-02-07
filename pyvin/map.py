import sys

CMAGENTA = '\033[95m'
CBLUE = '\033[94m'
CYELLOW = '\033[93m'
CGREEN = '\033[92m'
CRED = '\033[91m'
CGRAY = '\033[90m'
CEND = '\033[0m'

def cmagenta(s):
    return CMAGENTA + s + CEND

def cblue(s):
    return CBLUE + s + CEND

def cyellow(s):
    return CYELLOW + s + CEND

def cgreen(s):
    return CGREEN + s + CEND

def cred(s):
    return CRED + s + CEND

def cgray(s):
    return CGRAY + s + CEND

class Map:
    def __init__(self, tiles, size, heroes, id):
        self.id = id
        self.items = []
        y = 0
        for line in [tiles[i:i+size*2] for i in range(0, len(tiles), size*2)]:
            x = 0
            self.items.append([])
            for item in [line[i:i+2] for i in range(0, len(line), 2)]:
                self.items[len(self.items)-1].append(item)
                if item[0]=='$':
                    try:
                        hero_id = int(item[1])
                        heroes[hero_id-1].mines.append((x, y))
                    except:
                        pass
                x += 1
            y += 1

    def display(self, indent=0):
        disp_indent = lambda n: '    '*n
        print '[Map]'
        print disp_indent(indent+1) + '      ',
        x = 0
        for col in self.items[0]:
            print str(x).rjust(2, '0'),
            x += 1
        print ''
        print disp_indent(indent+1) + '      ',
        for col in self.items[0]:
            print '--',
        print ''
        for y, row in enumerate(self.items):
            print disp_indent(indent+1),
            print str(y).rjust(2, '0') + ' | ',
            for col in row:
                if col[0]=='#':
                    print cgray(col),
                elif col[0]=='[':
                    print cblue(col),
                elif col[0]=='$':
                    s = cyellow(col[0])
                    if col[1]=='-':
                        s += cyellow(col[1])
                    elif int(col[1])==self.id:
                        s += cgreen(col[1])
                    else:
                        s += cred(col[1])
                    print s,
                elif col[0]=='@':
                    if int(col[1])==self.id:
                        print cgreen(col),
                    else:
                        print cred(col),
                else:
                    print col,
            print ''
