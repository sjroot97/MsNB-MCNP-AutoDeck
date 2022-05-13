import rotate



def card(deg):
    inputdeck=str(deg)+'\MsNB.inp'
    reactor='cards\\reactor.txt'
    graphitearray='cards\\array.txt'
    with open(inputdeck, 'a') as deck, open(reactor,'r') as reac, open(graphitearray,'r') as array:
        for line in reac:
            deck.write(line)
        deck.write("c      12 o'clock control drum\n")
        deck.write(f"31     C/Z  {str(rotate.positionxy[12][0])} {str(rotate.positionxy[12][1])} {rotate.rad_in}    $inner\n")
        deck.write(f"41     C/Z  {str(rotate.positionxy[12][0])} {str(rotate.positionxy[12][1])} {rotate.rad_out}    $outer\n")
        deck.write(f"51     P    {rotate.drum(deg,12)}   $bisector\n")
        deck.write('c      ---\n')
        deck.write("c      2 o'clock control drum\n")
        deck.write(f"32     C/Z  {str(rotate.positionxy[2][0])} {str(rotate.positionxy[2][1])} {rotate.rad_in}    $inner\n")
        deck.write(f"42     C/Z  {str(rotate.positionxy[2][0])} {str(rotate.positionxy[2][1])} {rotate.rad_out}    $outer\n")
        deck.write(f"52     P    {rotate.drum(deg,2)}   $bisector\n")
        deck.write('c      ---\n')
        deck.write("c      4 o'clock control drum\n")
        deck.write(f"33     C/Z  {str(rotate.positionxy[4][0])} {str(rotate.positionxy[4][1])} {rotate.rad_in}    $inner\n")
        deck.write(f"43     C/Z  {str(rotate.positionxy[4][0])} {str(rotate.positionxy[4][1])} {rotate.rad_out}    $outer\n")
        deck.write(f"53     P    {rotate.drum(deg,4)}   $bisector\n")
        deck.write('c      ---\n')
        deck.write("c      6 o'clock control drum\n")
        deck.write(f"34     C/Z  {str(rotate.positionxy[6][0])} {str(rotate.positionxy[6][1])} {rotate.rad_in}    $inner\n")
        deck.write(f"44     C/Z  {str(rotate.positionxy[6][0])} {str(rotate.positionxy[6][1])} {rotate.rad_out}    $outer\n")
        deck.write(f"54     P    {rotate.drum(deg,6)}   $bisector\n")
        deck.write('c      ---\n')
        deck.write("c      8 o'clock control drum\n")
        deck.write(f"35     C/Z  {str(rotate.positionxy[8][0])} {str(rotate.positionxy[8][1])} {rotate.rad_in}    $inner\n")
        deck.write(f"45     C/Z  {str(rotate.positionxy[8][0])} {str(rotate.positionxy[8][1])} {rotate.rad_out}    $outer\n")
        deck.write(f"55     P    {rotate.drum(deg,8)}   $bisector\n")
        deck.write('c      ---\n')
        deck.write("c      10 o'clock control drum\n")
        deck.write(f"36     C/Z  {str(rotate.positionxy[10][0])} {str(rotate.positionxy[10][1])} {rotate.rad_in}    $inner\n")
        deck.write(f"46     C/Z  {str(rotate.positionxy[10][0])} {str(rotate.positionxy[10][1])} {rotate.rad_out}    $outer\n")
        deck.write(f"56     P    {rotate.drum(deg,10)}   $bisector\n")
        deck.write('c      ---\n')

        for line in array:
            deck.write(line)
