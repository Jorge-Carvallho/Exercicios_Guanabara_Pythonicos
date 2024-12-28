# Exercício listas

# Crie uma variável chamada minha_lista e atribua a ela a lista: ['x', 'y', 'z'].
# Adicione o elemento 'w' à lista.
# Ordene a lista em ordem alfabética reversa.
# Reordene a lista em ordem alfabética normal.
# Imprima a lista completa.
# Faça um slice que capture e imprima os elementos do índice 1 ao 2 (inclusive).
# Crie uma cópia rasa da lista chamada copia_lista e adicione o elemento 'k' a essa nova lista.
# Verifique se minha_lista e copia_lista têm IDs diferentes.
# Crie uma nova lista chamada referencia_lista que aponte para minha_lista e adicione o elemento 'j'.
# Verifique se minha_lista e referencia_lista têm o mesmo ID.

minha_lista = ['x','y','z']
minha_lista.append('w')
print(minha_lista)
minha_lista.sort(reverse=True)
print(minha_lista)
minha_lista.sort()
print(minha_lista)
print(minha_lista[1:2])
copia_lista = minha_lista[:]
print(copia_lista)
copia_lista.append('k')
print(copia_lista)
print(id(copia_lista), id(minha_lista))
referencia_lista = minha_lista
referencia_lista.append('j')
print(id(referencia_lista), id(minha_lista))
# Crie uma função adiciona_elemento que recebe uma lista e um elemento como parâmetros, adiciona o elemento à lista e retorna a lista. Use essa função para adicionar o número 99 a minha_lista.

lista = []
def adiciona_elemento(x):
    lista.append(x)
    return lista
    
    
adiciona_elemento('99')
print(lista)
#  oouu
                         

def adicionar_elemento(lista, elemento):
    lista.append(elemento)
    return lista
    
minha_lista = adicionar_elemento(minha_lista,'99')
print(minha_lista)
# Crie uma função adiciona_sem_referencia que recebe uma lista e um elemento como parâmetros, faz uma cópia rasa da lista, adiciona o elemento à cópia e retorna a cópia. Use essa função para adicionar o número 100 a minha_lista.

def adiciona_sem_referencia(lista, elemento):
    lista_copia = lista[:]
    lista_copia.append(elemento)
    return lista_copia

nova_lista = adiciona_sem_referencia(minha_lista,'100')
print(minha_lista)
print(nova_lista)
print(id(minha_lista), id(nova_lista))

minha_lista = adiciona_sem_referencia(minha_lista, '101')
print(minha_lista)




listinha = []

def adiciona(x,elemento):
    x.append(elemento)
    return x

listinha = adiciona(listinha,'22')
print(listinha)


l = [1,2,3,[5,6,7]]
m = l[3:]
m.append(9)
print(m)
print(l)
