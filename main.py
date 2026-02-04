"""
Sistema: Clínica Vida+
Descrição: Sistema simples para cadastro de pacientes e geração de estatísticas.
Disciplina: PROJETO INTEGRADO INOVAÇÃO
Aluno: RODRIGO SANTOS SILVA
"""
pacientes = []

def mostrar_menu():
    print("\n=== SISTEMA CLÍNICA VIDA+ ===")
    print("1. Cadastrar paciente") 
    print("2. Listar pacientes")
    print("3. Buscar paciente")
    print("4. Estatísticas")
    print("5. Sair\n")

def cadastrar_paciente(pacientes):
    print("\n=== CADASTRO DE PACIENTE ===")

    nome = input("Nome do paciente: ").strip()
    idade = int(input("idade: "))
    telefone = input ("Telefone: ").strip()
    
    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }

    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

def listar_pacientes(pacientes):
    print("\n=== LISTA DE PACIENTES CADASTRADOS ===")
    if not pacientes:
        print("Nenum paciente cadastrado.")
        return
    
    print("\n--- Lista de Pacientes ---")
    for paciente in pacientes:
        print(f"Nome: {paciente['nome']} | Idade: {paciente['idade']} | Telefone: {paciente['telefone']}")

def buscar_paciente(pacientes):
    nome_busca = input("Digit o nome do paciente: ").lower()
    encontrado = False

    for paciente in pacientes:
        if paciente["nome"].lower() == nome_busca:
            print("\nPaciente encontrado:")
            print(f"Nome: {paciente['nome']}")
            print(f"Idade: {paciente['idade']}")
            print(f"Telefone: {paciente['telefone']}")
            encontrado = True
            break

    if not encontrado:
        print("Paciente não encontrado")

def estatisticas(pacientes):
    if not pacientes:
        print ("Nenhum paciente cadastrado")
        return
    total = len(pacientes)
    soma_idades = 0

    for paciente in pacientes:
        soma_idades += paciente["idade"]

    media_idade = soma_idades / total

    print("\n--- Estatísticas ---")
    print (f"Total de pacientes: {total}")
    print(f"Idade média: {media_idade: .1f}")   



while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_paciente(pacientes)

    elif opcao == "2":
        listar_pacientes(pacientes)

    elif opcao == "3":
        buscar_paciente(pacientes)

    elif opcao == "4":
       estatisticas(pacientes)

    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")