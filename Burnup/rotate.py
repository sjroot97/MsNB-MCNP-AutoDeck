import math

positionxy = {
    12: [ 00.0, 47.0 ],
     2: [ 41.1, 23.7 ],
     4: [ 41.1,-23.7 ],
     6: [ 00.0,-47.0 ],
     8: [-41.1,-23.7 ],
    10: [-41.1, 23.7 ],
}

rad_in='19.0'
rad_out='20.0'
dist=positionxy[12][1]
shield=120

def drum(deg,oclock):
    p=positionxy[oclock]
    n=[float(rad_out)/dist*(p[0]*math.cos(math.radians(deg))-p[1]*math.sin(math.radians(deg)))\
    ,float(rad_out)/dist*(p[0]*math.sin(math.radians(deg))+p[1]*math.cos(math.radians(deg)))]
    #for i, p_i in enumerate(p):
        #p[i]=p[i]-math.cos(math.radians(shield/2))*n[i]

    A=round(n[0],1)
    B=round(n[1],1)
    C=0.0
    D=round(n[0]*(p[0]-math.cos(math.radians(shield/2))*n[0])+n[1]*(p[1]-math.cos(math.radians(shield/2))*n[1]),1)

    plane = str(A) + "  " + str(B) + "  " + str(C) + "  " + str(D) + "  "
    return plane
