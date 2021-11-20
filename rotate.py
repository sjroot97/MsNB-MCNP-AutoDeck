import math

positionxy = {
    12: [ 00.0, 49.0 ],
     2: [ 42.9, 24.7 ],
     4: [ 42.9,-24.7 ],
     6: [ 00.0,-49.0 ],
     8: [-42.9,-24.7 ],
    10: [-42.9, 24.7 ],
}

def drum(deg,oclock):
    p=positionxy[oclock]
    n=[p[0]*math.cos(math.radians(deg))-p[1]*math.sin(math.radians(deg)),p[0]*math.sin(math.radians(deg))+p[1]*math.cos(math.radians(deg))]

    A=round(n[0],1)
    B=round(n[1],1)
    C=0.0
    D=round(n[0]*p[0]+n[1]*p[1],1)

    plane = str(A) + "  " + str(B) + "  " + str(C) + "  " + str(D) + "  "
    return plane
