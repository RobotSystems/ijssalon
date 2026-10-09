
# dictionairy wordt "prijzen" 
prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}
aanbieding = prijzen["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"

reclame_tekst2 = reclame_tekst[:63]  
print(reclame_tekst2)

# de tekst op het vliegtuigje moet in hoofdletters
reclame_tekst3 = reclame_tekst2.upper()

# voor de drukker moet de tekst in een list
reclame_tekst4 = reclame_tekst2
reclame_lijst = reclame_tekst3.split()

# Ellie wil voor haar flyer alle characters onder elkaar 
for el in reclame_tekst4:
    print(el.upper())

# Nu wil Ellie weer kleine letters
for el in reclame_tekst4:
    print(el.lower())

# Nu moeten alleen de woorden met meer dan 5 characters hoofdletters krijgen
for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())

