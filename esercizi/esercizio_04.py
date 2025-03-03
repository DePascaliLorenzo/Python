anno = 2025
anno_nascita = int(input('Inserisci il tuo anno di anno_nascita: '))

eta = anno - anno_nascita

pari = bool(eta % 2 == 0)

print(f"Hai {eta} anni. La tua età è pari? {pari}")