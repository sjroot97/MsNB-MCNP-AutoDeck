def card(deg):
    file=str(deg)+'\MsNB.inp'
    f = open(file, 'a')
    f.write('\nc      -----------\n')
    f.write('c      data card\n')
    f.write('c      -----------\n')
    f.write('MODE   n\n')
    f.write('KCODE  10000 1.0 100 1100\n')
    f.write('KSRC   0 0 0\n')
    f.write('c      -----------\n')
    f.write('c      end data card\n')
    f.write('c      -----------\n')
    f.close()
