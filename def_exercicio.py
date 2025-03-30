def sacar(valor):
    saldo=100
    
    if saldo >= valor:
        print("valor sacado")
        print("retire seu dinheiro no caixa!")
    if saldo < valor:
        print ("saldo insuficiente.")
    print("obrigado pela preferência, tenha um bom dia.")   

def depositar(valor):
    saldo=10000
    saldo+=valor

    if valor>=0:
        print("o seu saldo agora é:", (float(saldo+valor)))

depositar(1000)
sacar(70)