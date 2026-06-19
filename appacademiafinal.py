import json

def carregar_treinos(nome_arquivo="banco de dados.json"):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as file:
            dados = json.load(file)
            return dados.get("treinos", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_treinos(treinos, nome_arquivo="banco de dados.json"):
    with open(nome_arquivo, "w", encoding="utf-8") as file:
        json.dump({"treinos": treinos}, file, indent=2, ensure_ascii=False)


treinos = carregar_treinos()

def adicionar_treino(treinos):
     while True:
          opcao2 = input("Adicionar treino? S/N")
          if opcao2.lower() == "n":
               break
          elif opcao2.lower() =="s":
               try: 
                    exercicio = input("Escolha um exercicio: ")
                    reps =  int(input("Quantas reps: "))
                    peso = int(input("Peso: "))
                    treinos.append ([exercicio,reps,peso])
                    print("Treino salvo!")
                    break
               except:
                    print("apenas informacoes validas")     
     


def mostrar_treino(treinos):
        
          
          
        if not treinos:
            print("Nenhum treino salvo!")
        else:
               for i, t in enumerate(treinos):
                    print(f"{i+1} - Exercicio: {t[0]} / Reps: {t[1]} / Peso: {t[2]}")


def remover_treino(treinos):
     if not treinos:
          print("Nenhum treino adicionado!")
          return
     mostrar_treino(treinos)
     numero = int(input("Qual treino remover?"))
     indice = numero - 1
     if indice >= 0 and indice < len(treinos):
          treinos.pop(indice)     
          print("Treino removido! ")
     else:
          print("Treino invalido! ")

while True:
    print("1 - Adicionar treino")
    print("2 - Ver treinos")
    print("3 - Remover treino")
    print("4 - Sair")
    opcao = input("Escolha : ")

    if opcao == "1":
         adicionar_treino(treinos)
         salvar_treinos(treinos)
    elif opcao == "2":
         mostrar_treino(treinos)
    elif opcao == "3":
          remover_treino(treinos)
          salvar_treinos(treinos)
    elif opcao == "4":
         break
    else:
         print("Opção invalida")

salvar_treinos(treinos)
