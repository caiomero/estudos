
frutas = []
for n in range(5):
    frutas.append(input('digite o nome da fruta:'))
frutas = list(set(frutas))

print(frutas)