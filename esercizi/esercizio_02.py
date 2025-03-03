anno = 2025

anno_nascita = int(input("Inserisci il tuo anno di nascita: "))

eta = anno - anno_nascita
maggiorenne= bool(eta > 18)

print(f"Hai {eta} anni, sei maggiorenne? {maggiorenne}")