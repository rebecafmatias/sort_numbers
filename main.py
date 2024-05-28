import random

def gerar_dezenas():
    numeros = list(range(1, 26))
    pesos = {
        1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1,  # pesos para números de 1 a 9
        10: 1.7, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1,  # pesos para números de 10 a 19
        20: 2, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1.3  # pesos para números de 20 a 25
    }
    
    dezenas1 = random.choices(numeros, weights=[pesos[num] for num in numeros], k=15)
    dezenas = []
    for dezena in dezenas1:
        if dezena not in dezenas:
            dezenas.append(dezena)
        else:
            dezenas.append(random.choice([num for num in numeros if num not in dezenas]))
    return dezenas

for _ in range(10):
    resultado = gerar_dezenas()
    print(resultado)
    
