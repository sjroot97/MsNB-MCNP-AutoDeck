#Atom Fractions
#FLiNaK
Li = 0.2325
Na = 0.0575
K  = 0.21
Fc = 0.5
#UF4
U  = 0.2
Ff = 0.8

#Isotopic Abunances
Li6=0.0485
Li7=0.9515
Na23=1
K39=0.93
K41=0.07
F19=1

def card(deg,frac,enrich):
    #Calculate the atom fractions of each species
    xLi6=round(Li6*Li*(1-frac),5)
    xLi7=round(Li7*Li*(1-frac),5)
    xNa23=round(Na23*Na*(1-frac),5)
    xK39=round(K39*K*(1-frac),5)
    xK41=round(K41*K*(1-frac),5)
    xF19=round(F19*(Fc*(1-frac)+Ff*frac),5)
    xU235=round(U*enrich*frac,5)
    xU238=round(U*(1-enrich)*frac,5)

    #Write Card
    file=str(deg)+'\MsNB.inp'
    f = open(file, 'a')
    string='c      Salt (FLiNaK w/ ' + str(frac*100) + 'mol% UF @ ' + str(enrich*100)+ '% enrichment\n'
    f.write(string)
    string='M1     3006.73c  ' + str(xLi6) + ' 3007.73c ' + str(xLi7) + '\n'
    f.write(string)
    string='       11023.73c ' + str(xNa23) + '\n'
    f.write(string)
    string='       19039.73c ' + str(xK39) + ' 19041.73c ' + str(xK41) + '\n'
    f.write(string)
    string='       9019.73c  ' + str(xF19) + '\n'
    f.write(string)
    string='       92235.73c ' + str(xU235) + ' 92238.73c ' + str(xU238) + '\n'
    f.write(string)
