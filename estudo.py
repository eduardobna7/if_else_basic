opcao=int(input("Digite [1] para sacar e [2] para depositar\n"))
saldo=1000

if opcao==1:
    valor=float(input("informe o valor do saque: "))
    if saldo>=valor:
        print("saque efetuado com sucesso, o seu saldo agora é: ", float(saldo-valor))
    else:
        print("saldo insuficiente")
elif opcao==2:
    deposito=float(input("informe o valor do depósito: "))
    if deposito>=0:
        print("depósito efetuado com sucesso, o seu saldo agora é:", float(saldo+deposito))
else:
    exit("opção inválida")
