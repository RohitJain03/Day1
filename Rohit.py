z = 5
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")
cars = ["bmw", "mercedes", "lamborgini", "tata"]
for cars in cars:
    print(cars)
i = 0
while i < 5:
    print(i)
    i += 1
cars = ["bmw", "mercedes", "lamborgini", "tata"]
for cars in cars:
    if cars == "lamborgini":
        break
    print(cars)
cars = ["bmw", "mercedes", "lamborgini", "tata"]
for cars in cars:
    if cars == "lamborgini":
        continue
    print(cars)

#OUTPUT

#z is positive
#bmw
#mercedes
#lamborgini
#tata
#0
#1
#2
#3
#4
#bmw
#mercedes
#bmw
#mercedes
#tata
#[Program finished]