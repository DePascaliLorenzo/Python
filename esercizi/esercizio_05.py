parola = input("Inserisci una parola: ")
pal = bool(parola == parola[::-1])

print(f"La parola è: {parola}, è palindroma? {pal}")