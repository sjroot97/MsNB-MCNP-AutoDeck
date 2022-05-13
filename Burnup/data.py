def card(deg):
    inputdeck=str(deg)+'\MsNB.inp'
    with open(inputdeck, 'a') as deck, open('cards\\data.txt','r') as data:
        deck.write('\n')
        for line in data:
            deck.write(line)
