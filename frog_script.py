import webbrowser
import tkinter as tk

print("Frog script")
print("Use 'help()' para te ajudar")
variaveis = []
listas = []
while True:
    try:
        linha = str(input(">>> "))
        match linha:
            case "add()":
                nome = str(input("Nome da variavel: "))
                variavel = input("Valor da variavel: ")
                tipo = str(input("Tipo de variavel: ")).strip().lower()
                valor_variavel = variavel
                try:
                    match tipo:
                        case "int":
                            variaveis.append(f"{nome} = {int(variavel)}")
                            print("Variaveis:")
                            for num,variavel in enumerate(variaveis, start=1):
                                print(f"{num} - {variavel}")
                        case "float":
                            variaveis.append(f"{nome} = {float(variavel)}")
                            print("Variaveis:")
                            for num,variavel in enumerate(variaveis, start=1):
                                print(f"{num} - {variavel}")
                        case "str":
                            variaveis.append(f"{nome} = {str(variavel)}")
                            print("Variaveis:")
                            for num,variavel in enumerate(variaveis, start=1):
                                print(f"{num} - {variavel}")
                        case "bool":
                            variaveis.append(f"{nome} = {bool(variavel)}")
                            print("Variaveis:")
                            for num,variavel in enumerate(variaveis, start=1):
                                print(f"{num} - {variavel}")
                        case _:
                            print("ERRO DE SYNTAX")
                except ValueError:
                    print("ERRO NO VALOR")
            case "remove()":
                print("Variaveis:")
                for num,variavel in enumerate(variaveis, start=1):
                    print(f"{num} - parte para digitar({variavel})")
                remover = str(input("remover: "))
                variaveis.remove(remover)
                print("Variaveis:")
                for num,variavel in enumerate(variaveis, start=1):
                    print(f"{num} - {variavel}")
            case "show()":
                if len(variaveis) == 0:
                    print("Não tem nenhuma variavel")
                else:
                    print("Variaveis:")
                    for num,variavel in enumerate(variaveis, start=1):
                        print(f"{num} - {variavel}")
            case "exit()":
                break
            case "about()":
                webbrowser.open_new_tab("https://github.com/tralaleritogamer/Frog-script")
            case "math()":
                try:
                    num1 = int(input("Num1: "))
                    num2 = int(input("Num2: "))
                    operation = str(input("oper(+-/*%): ")).strip()
                    match operation:
                        case "+":
                            resultado = num1 + num2
                            print(f"Resultado e {resultado}")
                        case "-":
                            resultado = num1 - num2
                            print(f"Resultado e {resultado}")
                        case "/":
                            resultado = num1 / num2
                            print(f"Resultado e {resultado}")
                        case "*":
                            resultado = num1 * num2
                            print(f"Resultado e {resultado}")
                        case "%":
                            resultado = num1 % 2
                            if resultado == 0:
                                print("O numero e primo")
                                print(f"Resultado e {resultado}")
                            else:
                                print("O numero e primo")
                                print(f"Resultado e {resultado}")
                    definir = str(input("Quer defini como uma variavel(s,n)? ")).strip().lower()
                    if definir == "s":
                        tipo_p = str(input("Qual tipo de variavel(int,float)? "))
                        if tipo_p == "int":
                            variaveis.append(f"{int(resultado)} = int")
                        if tipo_p == "float":
                            variaveis.append(f"{float(resultado)} = float")
                    elif definir == "n":
                        print()
                    else:
                        print("ERRO DE DIGITAÇÃO")
                except ValueError:
                    print("ERRO NO VALOR")
            case "list()":
                try:
                    nome_l = str(input("Digite o nome da lista: "))
                    lista = []
                    listas.append(nome_l)
                    quantos = int(input(f"Quantos itens você quer na lista {nome_l}? "))
                    for item in range(quantos):
                        item = str(input("Escreva um item para a lista: "))
                        lista.append(item)
                    for numero,item in enumerate(lista, start=1):
                        print(f"{numero} - {nome_l} - {item}")
                except ValueError:
                    print("ERRO NO VALOR")
            case "behind_code(frog_script)":
                if len(variaveis) == 0:
                    print("Não tem variavel")
                else:
                    print("Variaveis")
                print(variaveis)
                if len(listas) == 0:
                    print("Não temos listas")
                else:
                    print("Listas:")
                print(listas)
            case "type()":
                try:
                    if len(variaveis) == 0:
                        print("Você não tem nenhuma variavel")
                    else:
                        print("Variaveis:")
                    for num,variavel in enumerate(variaveis, start=1):
                        print(f"{num} - {valor_variavel}")
                    qual = str(input("Digite a variavel para verificar o tipo: "))
                    if qual in variaveis:
                        indice = variaveis.index(qual)
                        tipo_item = type(variaveis[indice])
                        if tipo_item == str:
                            print(f"O tipo da variavel '{qual}' e string")
                        elif tipo_item == int:
                            print(f"O tipo da variavel '{qual}' e int(numeros inteiros)")
                        elif tipo_item == float:
                            print(f"O tipo da variavel '{qual}' e float(numeros decimais)")
                        else:
                            print("ERRO")
                        print(f"Tipo: {tipo_item}")
                    else:
                        print("Variavel não encontrada")
                except ValueError:
                    print("ERRO NO VALOR")
            case "color()":
                erro = 0
                r = int(input("Digite um valor entre 0-255 no R: "))
                if r > 255 or r < 0:
                    print("ERRO")
                    erro = 1
                else:
                    print("Cor definida")
                    erro = 0
                g = int(input("Digite um valor entre 0-255 no G: "))
                if g > 255 or r < 0:
                    print("ERRO")
                    erro = 1
                else:
                    print("Cor definida")
                    erro = 0
                b = int(input("Digite um valor entre 0-255 no B: "))
                if b > 255 or r < 0:
                    print("ERRO")
                    erro = 1
                else:
                    print("Cor definida")
                    erro = 0

                app = tk.Tk()
                app.title("Teste de cor")
                app.geometry("1280x720")
                if erro == 1:
                    app.destroy()
                else:
                    app.mainloop()
                    hex_color = f"#{r:02x}{g:02x}{b:02x}"

                texto = tk.Label(
                    app,
                    text="Texto de teste",
                    font=("Consolas", 40),
                    fg=hex_color,    
                )
                texto.place(x=180,y=200)

                app.mainloop()
            case "invert()":
                try:
                    for num,variavel in enumerate(variaveis, start=1):
                        print(f"{num} - {valor_variavel}")
                    qual_2 = str(input("Digite a parte para inverter: "))
                    if qual_2 in variaveis:
                        indice_2 = variaveis.index(qual_2)
                    else:
                        print("Não encontrado")
                    print(f"A string invertido fica '{qual_2[::-1]}'")
                except ValueError:
                    print("ERRO NO VALOR")
            case "bin()":
                binario = str(input("Digite um texto: "))
                conversão = bin(binario)
            case "help()":
                print("add() para adicionar uma variavel")
                print("remove() para remover uma variavel")
                print("show() para ver as variaveis e as listas")
                print("exit() para sair")
                print("about() vai para github da linguagem de programação")
                print("math() faz calculos matematicos e pode definir ele como variaveis")
                print("list() para criar uma lista")
                print("type() para ver o tipo da variavel")
                print("color() para ver a cor de acordo com um texto em rgb hex")
                print("invert() para inverter uma string")
                print("bin() crie um texto binario e defina como uma variavel")
                print("Tipos de variaveis:")
                print("int = numero inteiro, float = numero decimais, str = texto, bool = booleana(Apenas dois valores que pode ser True e verdadeiro ou False para falso), bin = binario(0,1)")
            case _:
                print("ERRO DE SYNTAX")
    except ValueError:
        print("ERRO NO PROGRAMA")