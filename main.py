"""
Sistema: Clínica Vida+
Descrição: Sistema simples para cadastro de pacientes e geração de estatísticas.
Disciplina: PROJETO INTEGRADO INOVAÇÃO
Aluno: RODRIGO SANTOS SILVA
"""
pacientes = []

def cadastrar_paciente(pacientes):
    nome = input("Digite o nome do paciente: ")
    idade = int(input("Digite a idade do paciente: "))
    telefone = input ("Digite o telefone do paciente: ")
    
    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }

    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

def listar_pacientes(pacientes):
    if len(pacientes) == 0:
        print("Nenum paciente cadastrado.")
        return
    
    print("\n--- Lista de Pacientes ---")
    for i, paciente  in enumerate(pacientes, start=1):
        print(f"{i}. {paciente['nome']} - {paciente['idade']} anos - {paciente['telefone']}")

def buscar_paciente(pacientes):
    nome_busca = input("Digit o nome do paciente: ").lower()
    encontrado = False

    for paciente in pacientes:
        if paciente["nome"].lower() == nome_busca:
            print("\nPaciente encontrado:")
            print(paciente)
            break


    print("Paciente não encontrado")

def estatisticas(pacientes):
    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")

    soma_idades = 0
    for paciente in pacientes:
        soma_idades += paciente["idade"]

    media = soma_idades / len(pacientes)

    print (f"Total de pacientes: {len(pacientes)}")
    print(f"Idade média: {media: .1f} anos")   


def menu():
    while True:
        print("\n=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente") 
        print("2. Listar pacientes")
        print("3. Buscar paciente")
        print("4. Estatísticas")
        print("5. Sair")
    
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

menu()