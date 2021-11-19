"""
Um programa que peça ao usuario para digitar um numero inteiro e informe se este numero é par ou impar.
Caso o usuario não digite um numero inteiro, informe que não é inteiro
"""

try:
    num = input("Introduza um numero inteiro: ")

    numtype = num.isnumeric()  #Verifica se a string é numérica
    #print(numtype)

    if numtype == True:     #verifica se o numero tem casas decimais
        num = float(num)
        restonum = num % 1
    elif numtype == False:
        quit()
    if restonum > 0:
        print("O numero não é inteiro")

    impar = num % 2     #Verifica se o numero a dividir por 2 tem resto > 0 para verificar se é impar ou par
    # print(impar)
    if impar > 0:
        print("O número introduzido é impar")
    elif impar == 0:
        print("O número introduzido é par.")

except:
    print("Não introduziu um numero inteiro")