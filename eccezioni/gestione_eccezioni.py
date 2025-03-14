def divisione(a, b):
    try:
        print(int(a) / int(b), type(a), type(b))
    except ValueError as v:
        print(v)
    except ZeroDivisionError as z:
        print(z)

def divisione_due(a, b):
    try:
        print(int(a) / int(b))
    except (ValueError, ZeroDivisionError) as e:
        print("Valori non corretti") if isinstance(e, ValueError) else print('Divisione per 0: IMPOSSIBILE')

def divisione_tre(a, b):
    try:
        print(int(a) / int(b))
    except (ValueError, ZeroDivisionError) as e:
        print("Valori non corretti") if isinstance(e, ValueError) else print('Divisione per 0: IMPOSSIBILE')
    else:
        print('Tutto è andato per il meglio')
    finally:
        print('Questa istruzione viene comunque eseguita')

print('AVVIO PROGRAMMA')

print('')

divisione('5','0')

print('')

divisione_due("3",'3')

print('')

divisione_tre('5','2')

print('FINE PROGRAMMA')