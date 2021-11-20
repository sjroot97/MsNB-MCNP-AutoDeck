import header, cell, surface, data, material, os

DEG=[0,15,30,45,60,75,90,105,120,135,150,165,180]
frac=0.35
enrich=0.55

d=open('del.bat','w')
d.write('')
d.close()

r=open('run.bat', 'w')
r.write('')
r.close()

for deg in DEG:
    os.mkdir(str(deg))
    string=str(deg)+'\plot.bat'
    p=open(string, 'a')
    p.write('MCNP6 IP i=MsNB.inp\n')
    p.write('del comout\n')
    p.write('del outp\n')
    p.write('del srctp\n')
    p.close()

    string1 = 'del '+str(deg)+'/f /q''\n'
    string2 = 'rmdir ' +str(deg)+'\n\n'
    d=open('del.bat','a')
    d.write(string1)
    d.write(string2)
    d.close()

    string = 'cd '+str(deg)+'\n'
    r=open('run.bat', 'a')
    r.write(string)
    r.write('del MsNB.inpo\n')
    r.write('MCNP6 n=MsNB.inp\n')
    r.write('del MsNB.inps\n')
    r.write('del MsNB.inpr\n')
    r.write('cd ..\n')
    r.write('\n')

    header.card(deg)
    cell.card(deg)
    surface.card(deg)
    data.card(deg)
    material.card(deg,frac,enrich)
