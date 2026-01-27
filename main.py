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
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair\n")

def cadastrar_paciente(pacientes):
    print("\n=== CADASTRO DE PACIENTE ===")

    nome = input("Nome do paciente: ").strip()

    if nome == "":
        print("Nome não pode ser vazio.")
        return
    try:
        idade = int(input("idade: "))
        if idade <= 0:
            print ("Idade inválida.")
            return
    except ValueError:
        print("Digite um número válido para idade.")
        return
    
    telefone = input ("Telefone: ").strip()

    if telefone == "":
        print("Telefone não pode ser vazio")
        return
    
    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }

    pacientes.append(paciente)

    print("Paciente cadastrado com sucesso!")

def listar_pacientes(pacientes):
    print("\n=== LISTA DE PACIENTES CADASTRADOS ===")

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return

    for i, paciente in enumerate(pacientes, start=1):
        print(f"\nPaciente {i}")
        print(f"Nome     : {paciente['nome']}")
        print(f"Idade    : {paciente['idade']}")
        print(f"Telefone : {paciente["telefone"]}")

def buscar_paciente(pacientes):
    print("\n=== BUSCAR PACIENTE ===\n")

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return
    nome_busca = input("Digite o nome do paciente: ").strip().lower()

    encontrado = False
    
    for paciente in pacientes:
        if paciente["nome"].lower() == nome_busca:
            print("\nPaciente encontrado!")
            print(f"Nome     : {paciente['nome']}")
            print(f"Idade    : {paciente['idade']}")
            print(f"Telefone : {paciente["telefone"]}")
            encontrado = True
            break

    if not encontrado:
        print("\nPaciente não encontrado.")

def ver_estatisticas(pacientes):
    print("\n=== ESTATÍSTICAS DA CLÍNICA ===")

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado")
        return
    total_pacientes = len(pacientes)
    soma_idades = 0

    paciente_mais_novo = pacientes[0]
    paciente_mais_velho = pacientes[0]

    for paciente in pacientes:
        soma_idade += paciente["idade"]

        if paciente["idade"] < paciente_mais_novo["idade"]:
            paciente_mais_novo = paciente

        if paciente["idade"] > paciente_mais_velho["idade"]:
            paciente_mais_velho = paciente

    idade_media = soma_idades/total_pacientes

    print(f"\nTotal de pacientes: {total_pacientes}")
    print(f"\nIdade média:{idade_media:.1f} anos")
    print(f"Paciente mais novo: {paciente_mais_novo['nome']} ({paciente_mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {paciente_mais_velho['nome']} ({paciente_mais_velho['idade']} anos)")




while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_paciente(pacientes)

    elif opcao == "2":
        ver_estatisticas(pacientes)

    elif opcao == "3":
        buscar_paciente(pacientes)

    elif opcao == "4":
       listar_pacientes(pacientes)

    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")