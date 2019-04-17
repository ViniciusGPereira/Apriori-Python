#http://artedosdados.blogspot.com/2015/02/regras-de-associacao-em-python-modulo.html
from collections import Counter
import itertools
import sys
#-Cria as regras de associação
def frequentItems(items, trans, n, s):
   itemsets = set(itertools.combinations(items, n))
   itemTransactions = []
   for i in itemsets:
     for k,v in transacoes.items():
       if set(v).intersection(set(i)) == set(i):
         itemTransactions.append(i)
   ret = []
   for k,v in sorted(Counter(itemTransactions).items()):
     if v >= s * len(trans):
       ret.append([k, v])
   return(dict(ret))
#while True:

#-Dicionario de transações
transacoes = {     1: {"Cerveja", "Bolacha","Amendoim", "Frango", "Laranja"},
                   2: {"Cerveja", "Cafe", "Frango", "Laranja", "Chocolate", "Amendoim"},
                   3: {"Cerveja", "Batata", "Laranja", "Ovos"},
                   4: {"Cerveja", "Amendoim", "Frango","Ovos", "Batata","Leite"},
                   5: {"Cafe", "Bolacha", "Laranja", "Chocolate" ,"Frango", "Ovos", "Batata","Leite"},
                   6: {"Cafe", "Laranja", "Ovos", "Bolacha", "Leite"},
                   7: {"Laranja","Batata", "Cafe", "Bolacha", "Cerveja", "Ovos"},
                   8: {"Amendoim", "Cafe", "Frango", "Cerveja", "Chocolate", "Ovos"},
                   9: {"Amendoim", "Laranja","Batata", "Cerveja", "Ovos"},
                   10:{"Amendoim", "Frango", "Cafe", "Cerveja", "Bolacha", "Ovos"}
}
#-Imprime lista de compras
print("")
print("Para os calculos, será considera os itens de 10 compras realizadas: ")
print("")
item_aux = []
for linha in transacoes.values():
    for itm in linha:
        item_aux.append(itm)
    print(item_aux)
    item_aux.clear()
print("")

# -Parametros de confiança e suporte
s = float(input("Insira de 0.0 à 0.9 o suporte que preferir"))
c = float(input("Insira de 0.0 à 0.9 a confiança que preferir"))

#-Faz a leitura do dicionario
#Armazena cada item no vetor itens
items = []
for itemsets in transacoes.values():
    for item in itemsets:
        items.append(item)
items = set(items)

#Mostra os resultados dos itens mais frequentes
print("1- itens mais frequentes:")
print(frequentItems(items, transacoes, 1, s))
print("")
print("2-Duplas mais frequentes:")
print(frequentItems(items, transacoes, 2, s))
print("")
print("3-Trios mais frequentes:")
print(frequentItems(items, transacoes, 3, s))
print("#############################################")
print("\n")

# Imprime as regras de associação
# De acordo com o suporte e confiança
print("Regras de associacao com suporte")
print("e confianca maiores que 50%")
f2 = frequentItems(items, transacoes, 2, s)
k2 = [k for k in f2.keys()]
v2 = [v for v in f2.values()]
f1 = frequentItems(items, transacoes, 1, s)
k1 = [k[0] for k in f1.keys()]
v1 = [v for v in f1.values()]
for i in range(len(k2)):
    i1 = k2[i][0]
    i2 = k2[i][1]
    for j in range(len(k1)):
        if k1[j] == i1:
            confidence = v2[i] / v1[j]
    if v2[i] >= s * len(transacoes) and confidence >= c:
        print("{0:<6} -> {1:<6}: ({2},{3})".format(i1, i2, str(v2[i]), confidence))
    i1 = k2[i][1]
    i2 = k2[i][0]
    for j in range(len(k1)):
        if k1[j] == i1:
            confidence = v2[i] / v1[j]
    if v2[i] >= s * len(transacoes) and confidence >= c:
        print("{0:<6} -> {1:<6}: ({2},{3})".format(i1, i2, str(v2[i]), confidence))
        print("")
