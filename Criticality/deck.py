import header, cell, surface, data, salt, material, os, burned_material
DEG=[0,15,30,45,60,75,90,105,120,135,150,165,180]
#DEG=[89.0,89.2,89.4,89.6,89.8,90.0,90.2,90.4,90.6,90.8,91.0]
frac=0.35
enrich=0.55

with open('delete.bat','w') as delete, open('run.bat', 'w') as run:
    delete.write('')
    run.write('')

for deg in DEG:
    os.mkdir(str(deg))
    plotbatch=str(deg)+'\plot.bat'

    with open(plotbatch, 'a') as plot,\
    open('cards\\plot.txt','r') as pt,\
    open('delete.bat','a') as delete,\
    open('run.bat', 'a') as run,\
    open('cards\\run.txt','r') as rt:
        for line in pt:
            plot.write(line)

        delete.write(f'del {str(deg)}/f /q\n')
        delete.write(f'rmdir {str(deg)}\n\n')

        run.write(f'cd {str(deg)}\n')
        for line in rt:
            run.write(line)

    header.card(deg)
    cell.card(deg)
    surface.card(deg)
    data.card(deg)
    #salt.card(deg,frac,enrich)
    #material.card(deg)
    burned_material.card(deg)
