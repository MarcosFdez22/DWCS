#1
def tripleCheck(array):
    for i in range(len(array)):
        if array[i] == array[i+1] == array [i+2]:
            return True
        else:
            return False

print(tripleCheck([ 1, 1, 2, 2, 1 ]))

print(tripleCheck([ 1, 1, 2, 1, 2, 3 ]))

print(tripleCheck([ 1, 1, 1, 2, 2, 2, 1]))



#2

cp = {
    "Italia":"Roma", "Luxemburgo":"Luxemburgo", "Bélgica":"Bruselas", "Dinamarca":"Copenhague", "Finlandia":"Helsinki", "Francia":"París", "Eslovaquia":"Bratislava", "Eslovenia":"Liubliana", "Alemania":"Berlín", "Grecia":"Atenas", "Irlanda":"Dublín", "Países Bajos":"Ámsterdam", "Portugal":"Lisboa", "España":"Madrid", "Suecia":"Estocolmo", "Reino Unido":"Londres", "Chipre":"Nicosia", "Lituania":"Vilna", "República Checa":"Praga", "Estonia":"Tallin", "Hungría":"Budapest", "Letonia":"Riga", "Malta":"La Valeta", "Austria":"Viena", "Polonia":"Varsovia"
}


def Capital(cp):
    for key in cp:
        print("The capital of " + key +  " is " + cp[key])


Capital(cp)
