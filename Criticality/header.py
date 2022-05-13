import datetime
now=datetime.date.today()

def card(deg):
    inputdeck=str(deg)+'\MsNB.inp'
    headercard= 'cards\header.txt'

    with open(inputdeck,'w') as deck, open(headercard,'r') as header:
        deck.write((f'Molten Salt Nuclear Battery with Control Drums at {deg} degrees\n'))
        deck.write(f'c      revised {now}\n')
        for line in header:
            deck.write(line)
