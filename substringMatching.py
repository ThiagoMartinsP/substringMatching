import time

from time import perf_counter

tempos = {"compara": [],"comparatotal": [], "contido" : [], "contidototal": []}

def compara(p, s, pos):
    
    inicio = perf_counter()
    
    for i in range(len(p)):
        if pos + i >= len(s) or s[pos + i] != p[i]:
            tempos["compara"].append(perf_counter() - inicio)
            return False
        
    tempos["compara"].append(perf_counter() - inicio)
    
    return True

def contido(p, s, inicio, fim):

    inicio1 = perf_counter()
    if fim - inicio + 1 < len(p):
        tempos["contido"].append(perf_counter() - inicio1)
        return -1  
    
    inicio2 = perf_counter()
    if inicio == fim: 
        if compara(p, s, inicio):
            tempos["contido"].append(perf_counter() - inicio2)
            return inicio
        tempos["contido"].append(perf_counter() - inicio2)
        return -1
    

    meio = (inicio + fim) // 2


    inicio3 = perf_counter()
    pos_esq = contido(p, s, inicio, meio)
    if pos_esq != -1:
        tempos["contido"].append(perf_counter() - inicio3)
        return pos_esq
    

    inicio4 = perf_counter()

    pos_dir = contido(p, s, meio + 1, fim)
    if pos_dir != -1:
        tempos["contido"].append(perf_counter() - inicio4)
        return pos_dir  

    inicio5 = perf_counter()

    inicio_cruzado = max(meio - len(p) + 1, inicio)
    fim_cruzado = meio
    
    for i in range(inicio_cruzado, fim_cruzado + 1):
        if compara(p, s, i): 
            tempos["contido"].append(perf_counter() - inicio5)
            return i

    tempos["contidototal"].append(perf_counter() - inicio1)
    return -1  


string = 'a'
substring = 'abc'

res = contido(substring, string, 0, len(string) -1)

if res != -1:
    print(f"\nA substring encontra-se no índice {res}.")
else:
    print("Substring não encontrada.")

tempos["contidototal"] = sum(tempos["contido"])
tempos["comparatotal"] = sum(tempos["compara"])

print(f"\nCOMPARA\n Tempo total: {tempos['comparatotal'] * 1e6:.1f} µs")
print(f" Tempo de cada vez em que a funcao foi executada (µs): {[f'{t * 1e6:.1f}' for t in tempos['compara']]}")


print(f"\nCONTIDO\n Partes executadas: {len(tempos['contido'])}")
print(f" Tempo de cada parte (ns): {[f'{t * 1e9:.0f}' for t in tempos['contido']]}")
print(f" Tempo total: {tempos['contidototal'] * 1e9:.0f} ns\n")

