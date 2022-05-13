import salt

def card(deg):
    inputdeck=str(deg)+'\MsNB.inp'

    with open(inputdeck, 'a') as deck, open('cards\\burned_material.txt') as material:
        for line in material:
            deck.write(line)
