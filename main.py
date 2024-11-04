print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10%3)
print(10+3)
alphabet= "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, r, s, t, u, v, y, z"
alphabet= "z, y, v, u, t, s, r, p, o, n, m, l, k, j, i, h, g, f, e, d, c, b, a"
ma_string="Je suis une String"
num1=40
num2=2
num1=3
num2=14
machines= ["lave-linge" , "lave-vaisselle" , "seche-linge" , "frigo"]
machines("lave-linge=500")
machines("lave-vaisselle=500")
machines("seche-linge=499")
machines("frigo=600")
machines=("lave-linge=500")
##

machines.count("lave-linge=50")
machines.count("lave-vaisselle=50")
machines.count("seche-linge=20")
##
mot="pierre"
i=0
while i<len(mot):
    print(mot[i])
    i=i+1

##
num = 0
while num <=5:
    print(num)
    num = num + 1

##
x="3"
print(x)

## 

nom = "Moby Dick"
page = 195
poid = 13.45
neuf = True

print(nom)
print(type(poid))
print(type(neuf))
print(type(poid))

##
i = 21
for i in range(21):
    print(i)

##

N = 1
while N < 13:
    print(N)
    N = N + 1  

##
for N in range(1, 13):
      print (N)


##


N = 1
while N < 13:
    print(N)


##

for N in range(1, 13):
    print (N)

##


N = int(input("Entrez un entier : "))
i = 1
while i <= 10:
    resultat = N * 7 * i
    print(f"{N} * 7 * {i} = {resultat}")
    i += 1


##

# Initialiser le compteur
tour = 1

# Boucle while pour effectuer 12 tours
while tour <= 12:
    resultat = 3 * tour - 2
    print(f"Tour {tour}: {resultat}")
    tour += 1  # Incrémenter le compteur


    # Initialiser le compteur
tour = 1

# Boucle while pour effectuer 12 tours
while tour <= 12:
    resultat = (tour - 1) * 2 + 2
    print(f"Tour {tour}: {resultat}")
    tour += 1  # Incrémenter le compteur

# Initialiser le compteur
nombre = 1

# Boucle while pour parcourir les nombres de 1 à 30
while nombre <= 30:
    if nombre % 2 == 0:
        print(f"Pair: {nombre}")
    else:
        print(f"Impair: {nombre}")
    nombre += 1  # Incrémenter le compteur
