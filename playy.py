import play as pg

while True:
    a = pg.confirm("Are you man ?? ", buttons=["yes","Nope"])
    if a=="Yes":
        break
    
