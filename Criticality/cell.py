def card(deg):
    inputdeck=str(deg)+'\MsNB.inp'
    cellcard = 'cards\cell.txt'

    with open(inputdeck,'a') as deck, open(cellcard,'r') as cell:
        for line in cell:
            deck.write(line)
        deck.write('\n')
