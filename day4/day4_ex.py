# 7.11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"
start1 = '! '.join(start1)
start1 = start1.title()
print(start1+'! '+ rhymes[0][0].capitalize()+'!')
print(start2 +' ' +rhymes[0][1]+'.')