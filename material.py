import salt

def card(deg,frac,enrich):
    file=str(deg)+'\MsNB.inp'
    f = open(file, 'a')
    f.write('c      \n')
    f.write('c      -----------\n')
    f.write('c      material cards\n')
    f.write('c      -----------\n')

    f.close()
    salt.card(deg,frac,enrich)
    f.close()

    f = open(file, 'a')
    f.write('c      ---\n')
    f.write('c      316 stainless steel\n')
    f.write('M2     14000.60c -0.010\n')
    f.write('       24000.42c -0.170 25055.66c -0.020 26000.50c -0.655\n')
    f.write('       28000.42c -0.120 42000.42c -0.025\n')
    f.write('c      ---\n')

    f.write('c      Graphite\n')
    f.write('M3     6000.73c 1\n')
    f.write('c      ---\n')

    f.write('c      Beryllium Oxide\n')
    f.write('M4     4009.73c 0.5\n')
    f.write('       8016.73c 0.5\n')
    f.write('c      ---\n')

    f.write('c      Boron Carbide\n')
    f.write('M5     5010.73c 0.16\n')
    f.write('       5011.73c 0.64\n')
    f.write('       6000.73c 0.2\n')
    f.write('c      ---\n')

    f.write('c      Argon\n')
    f.write('M6     18040.73c     0.996\n')
    f.write('       18036.73c     0.004\n')
    f.write('c      ---\n')

    f.write('c      -----------\n')
    f.write('c      end material cards\n')
    f.write('c      -----------\n')
    f.write('c      \n')
    f.write('c      ----------- END CARDS -----------\n')
    f.write('c      \n')
    f.write('c      -----------------------------------------------------------------\n')
    f.close()
