from time import sleep
import webbrowser

print("Frog script")
sleep(1)
print("Versão 0.1")
sleep(1)
print("Use 'help();' para te ajudar")
v = []
sleep(1)
while True:
    linha = str(input(">>> "))
    match linha:
        case "add();":
            variavel = input("Variavel: ")
            tipo = str(input("Tipo de variavel: ")).strip().lower()
            try:
                match tipo:
                    case "int":
                        v.append(f"{int(variavel)} = int")
                        for num,variavel in enumerate(v, start=1):
                            print(f"{num} - {variavel}")
                    case "float":
                        v.append(f"{float(variavel)} = float")
                        for num,variavel in enumerate(v, start=1):
                            print(f"{num} - {variavel}")
                    case "str":
                        v.append(f"{str(variavel)} = str")
                        for num,variavel in enumerate(v, start=1):
                            print(f"{num} - {variavel}")
                    case _:
                        print("ERRO DE SYNTAX")
            except ValueError:
                print("ERRO NO VALOR")
        case "remove();":
            for num,variavel in enumerate(v, start=1):
                print(f"{num} - {variavel}")
            remover = str(input("remover: "))
            v.remove(remover)
            for num,variavel in enumerate(v, start=1):
                print(f"{num} - {variavel}")
        case "show();":
            for num,variavel in enumerate(v, start=1):
                print(f"{num} - {variavel}")
        case "exit();":
            exit
        case "break();":
            break
        case "about();":
            webbrowser.open_new_tab("https://github.com/tralaleritogamer/Frog-script")
        case "help()":
            print("add(); para adicionar uma variavel")
            print("remove(); para remover uma variavel")
            print("show(); para ver as variaveis")
            print("exit(); para sair")
            print("break(); para parar o programa")
            print("edit(); para editar uma variavel")
            print("about(); vai para github da linguagem de programação")
            print("Variaveis:")
            print("int = numero inteiro, float = numero decimais, str = texto")
        case _:
            print("ERRO DE SYNTAX")