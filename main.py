# Dicionários para armazenar funcionários, clientes e agendamentos
funcionarios = {}
clientes = {}
horario = {}

# Lista para armazenar os horários agendados
horarios = []

# Função para cadastrar um novo funcionário
def cadastrar_funcionario(id_funcionario, nome, cargo, remuneracao):
    #Verifica se o ID cadastrado já existe
    if id_funcionario in funcionarios:
        print("\nEsse ID já foi cadastrado, tente novamente criando outro ID!")
        input("Digite ENTER para continuar")
    else:    
        funcionarios[id_funcionario] = {"nome": nome, "cargo": cargo, "remuneracao": remuneracao }
        print("\nFuncionário cadastrado com sucesso!")
        input("Digite ENTER para continuar")

# Função para remover um funcionário pelo ID do funcionário
def remover_funcionario(id_funcionario):
    #Verifica se o funcionário procurado foi encontrado
    if id_funcionario in funcionarios:
        del funcionarios[id_funcionario]
        print("\nFuncionário removido com sucesso.")
        input("Digite ENTER para continuar!")
    else:
        print("\nFuncionário não encontrado.")
        input("Digite ENTER para continuar!")

# Função para listar todos os funcionários cadastrados
def listar_funcionarios(funcionarios):
    os.system("cls || clear")
  
    #Verifica se existe algum funcionário cadastrado
    if bool(funcionarios) == False:
        print("\nNenhum funcionário cadastrado!")  
        input("Digite ENTER para continuar!")
    else:  
        print("=== Lista de funcionários: ===")
        for id_funcionario, dados in funcionarios.items():
            print("ID:", id_funcionario)
            print("Nome:", dados["nome"])
            print("Cargo:", dados["cargo"])
            print("Remuneração:", dados["remuneracao"])
            print("---------------------------")
        input("\nDigite ENTER para continuar!")

# Função para editar as informações de um funcionário a partir do ID do funcionário
def editar_funcionario(id_funcionario, nome, cargo, remuneracao):
    funcionarios[id_funcionario] = {"nome": nome, "cargo": cargo, "remuneracao": remuneracao }
    print("\nFuncionário editado com sucesso.")
    input("Digite ENTER para continuar!")

# Função para cadastrar um novo cliente
def cadastrar_cliente(id_cliente, nome, cpf, telefone):
    #Verifica se o ID inserido já foi cadastrado
    if id_cliente in clientes:
        print("\nEsse ID já foi cadastrado, tente novamente criando outro ID!")
        input("Digite ENTER para continuar")
    else:
        clientes[id_cliente] = {"nome": nome, "cpf": cpf, "telefone": telefone}
        print("\nCliente cadastrado com sucesso!")
        input("Digite ENTER para continuar!")

# Função para remover um cliente pelo ID do cliente
def remover_cliente(clientes, id_cliente):
    #Verifica se o cliente procurado está cadastrado
    if id_cliente in clientes:
        del clientes[id_cliente]
        print("\nCliente removido com sucesso.")
        input("Digite ENTER para continuar!")
    else:
        print("\nCliente não encontrado.")
        input("Digite ENTER para continuar!")

# Função para listar todos os clientes cadastrados
def listar_clientes(clientes):
    os.system("cls || clear")

    #Verifica se existe algum cliente cadastrado
    if bool(clientes) == False:
        print("\nNenhum cliente cadastrado!\n")
        input("Digite ENTER para continuar!")
    else:
        print("=== Lista de clientes: ===\n")
        for id_cliente, dados in clientes.items():
            print("ID:", id_cliente)
            print("Nome:", dados["nome"])
            print("CPF:", dados["cpf"])
            print("Telefone:", dados["telefone"])
            print("---------------------------")
        input("\nDigite ENTER para continuar!")

# Função para editar as informações de um cliente pelo ID do cliente
def editar_cliente(id_cliente, nome, cpf, telefone):
    clientes[id_cliente] = {"nome": nome, "cpf": cpf, "telefone": telefone}
    print("\nCliente editado com sucesso!")
    input("Digite ENTER para continuar!")

# Função para agendar um horário
def agendar_horario(horarios, id_cliente, id_funcionario, data, hora, servico):
    # Verifica se o funcionário e o cliente estão cadastrados
    if id_funcionario in funcionarios and id_cliente in clientes:
        # Gera um número de agendamento único e aleatório (entre 1 e 1000) para evitar conflitos
        numero = random.randint(1, 1000)
        while numero in horarios:
            numero = random.randint(1, 1000)

        # Cria um dicionário com as informações do agendamento e o adiciona à lista de horários
        horario = {"cliente": id_cliente, "funcionario": id_funcionario, "data": data, "hora": hora, "servico": servico, "numero": numero}
        horarios.append(horario)

        print("\nHorário agendado com sucesso.")
        input("Digite ENTER para continuar!")
    else:
        print("\nErro! Funcionário ou cliente não encontrado.")
        input("Digite ENTER para continuar!")

# Função para listar todos os horários agendados
def listar_agendamentos(horarios, clientes, funcionarios):
    os.system("cls || clear")
    if len(horarios) == 0:
        print("\nNenhum agendamento!")
        input("Digite ENTER para continuar!")
    else:
        print("Lista de horários agendados:\n")
        for horario in horarios:
            print("Cliente Agendado:", clientes[horario["cliente"]]["nome"])
            print("CPF do cliente:", clientes[horario["cliente"]]["cpf"])
            print("Funcionário Agendado:", funcionarios[horario["funcionario"]]["nome"])
            print("Data:", horario["data"])
            print("Hora:", horario["hora"])
            print("Serviço:", horario["servico"])
            print("Numero do agendamento:", horario["numero"])
            print("---------------------------")
        input("Digite ENTER para continuar!")

# Função para apagar um agendamento a partir do número do agendamento
def apagar_agendamento(horarios, numero_agendamento):
    for horario in horarios:
        if horario["numero"] == numero_agendamento:
            horarios.remove(horario)
            print("\nAgendamento removido com sucesso.")
            input("Digite ENTER para continuar!")
            return
    print("\nAgendamento não encontrado.")
    input("Digite ENTER para continuar!")

# Função para editar um agendamento a partir do número do agendamento
def editar_agendamento(horarios, numero_agendamento, id_cliente, id_funcionario, data, hora, servico):
    for horario in horarios:
        if horario["numero"] == numero_agendamento:
            horario["cliente"] = id_cliente
            horario["funcionario"] = id_funcionario
            horario["data"] = data
            horario["hora"] = hora
            horario["servico"] = servico
            print("\nAgendamento editado com sucesso.")
            input("Digite ENTER para continuar!")
            return
    print("\nAgendamento não encontrado.")
    input("Digite ENTER para continuar!")

# Importa o módulo "os" para limpar a tela do console e o módulo "random" para gerar números aleatórios
import os
import random

# Exibe o menu principal e realiza a interação com o usuário
print("=====================================")
print("==== M E N U   P R I N C I P A L ====")
print("=====================================")
print()
print("\t1 - Clientes")
print("\t2 - Funcionários")
print("\t3 - Agenda")
print("\t0 - Finalizar Programa")
print()
print("=====================================")
print()

op1 = input("Escolha sua opção: ")

os.system("cls || clear")

# Início do loop principal do programa
while op1 != "0":
    if op1 == "1":
        # Menu de opções para clientes
        print("===  Página de Clientes  ===")
        print("\t1 - Cadastrar clientes")
        print("\t2 - Visualizar clientes cadastrados")
        print("\t3 - Apagar cliente cadastrado")
        print("\t4 - Editar cliente cadastrado")
        print("\t0 - Sair\n")

        op2 = int(input("Escolha sua opção: "))

        if op2 == 1:
            os.system("cls || clear")

            id_cliente = input("Digite o ID do cliente: ")
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            telefone = input("Digite o telefone do cliente:")
            cadastrar_cliente(id_cliente, nome, cpf, telefone)
        
        elif op2 == 2:
            listar_clientes(clientes)
        
        elif op2 == 3:
            os.system("cls || clear")
            id_cliente = input("Digite o ID do cliente a ser removido: ")
            remover_cliente(clientes, id_cliente)
        
        elif op2 == 4:
            os.system("cls || clear")
            id_cliente = input("Digite o ID do cliente que deseja editar:")
          
            #Verifica se o cliente pesquisado está cadastrado
            if id_cliente in clientes:
                nome = input("Digite o nome do cliente: ")
                cpf = input("Digite o CPF do cliente: ")
                telefone = input("Digite o telefone do cliente:")
                editar_cliente(id_cliente, nome, cpf, telefone)
            else:
                print("Cliente não encontrado!")
                input("Digitte ENTER para continuar")      
            
    elif op1 == "2":
        # Menu de opções para funcionários
        print("===   Página de Funcionários   ===")
        print("\t1 - Cadastrar funcionário")
        print("\t2 - Visualizar funcionários cadastrados")
        print("\t3 - Apagar funcionário cadastrado")
        print("\t4 - Editar funcionário cadastrado")
        print("\t0 - Sair\n")

        op2 = int(input("Escolha sua opção: "))

        if op2 == 1:
            os.system("cls || clear")

            id_funcionario = input("Digite o ID do funcionário: ")
            nome = input("Digite o nome do funcionário: ")
            cargo = input("Digite o cargo do funcionário: ")
            remuneracao = float(input("Digite a remuneração do funcionário: ")) 
            cadastrar_funcionario(id_funcionario, nome, cargo, remuneracao)
        
        elif op2 == 2:
            listar_funcionarios(funcionarios)
        
        elif op2 == 3:
            id_funcionario = input("Digite o ID do funcionário a ser removido: ")
            remover_funcionario(id_funcionario)
          
        elif op2 == 4:
            os.system("cls || clear")

            id_funcionario = input("Digite o ID do funcionário que deseja editar: ")          
            #Verifica se o funcionario procurado foi encontrado
            if id_funcionario in funcionarios:
                nome = input("Digite o nome do funcionário: ")
                cargo = input("Digite o cargo do funcionário: ")
                remuneracao = float(input("Digite a remuneração do funcionário: ")) 
                editar_funcionario(id_funcionario, nome, cargo, remuneracao)
            else:
                print("Usuário não encontrado!")
                input("Digite ENTER para continuar!")
    
    elif op1 == "3":
        # Menu de opções para a agenda
        print("===           Agenda           ===")
        print("\t1 - Agendar horário")
        print("\t2 - Visualizar agendamentos")
        print("\t3 - Apagar horário agendado")
        print("\t4 - Editar horário agendado")
        print("\t0 - Sair\n")

        op2 = int(input("Escolha sua opção: "))

        os.system("cls || clear")

        if op2 == 1:
            id_cliente = input("Digite o ID do cliente: ")
            id_funcionario = input("Digite o ID do funcionário: ")
            data = input("Digite a data do agendamento (dd/mm): ")
            hora = input("Digite a hora do agendamento (min:hora): ")
            servico = input("Qual o serviço do agendamento? ")
          
            agendar_horario(horarios, id_cliente, id_funcionario, data, hora, servico)
        
        elif op2 == 2:
            listar_agendamentos(horarios, clientes, funcionarios)

        elif op2 == 3:
            numero_agendamento = int(input("Digite o número do agendamento a ser removido: "))
            apagar_agendamento(horarios, numero_agendamento)

            os.system("cls || clear")

        elif op2 == 4:
            numero_agendamento = int(input("Digite o número do agendamento a ser editado: "))
            id_cliente = input("Digite o ID do cliente: ")
            id_funcionario = input("Digite o ID do funcionário: ")
            data = input("Digite a nova data do agendamento (dd/mm): ")
            hora = input("Digite a nova hora do agendamento (min:hora): ")
            servico = input("Qual o novo serviço do agendamento? ")
            editar_agendamento(horarios, numero_agendamento, id_cliente, id_funcionario, data, hora, servico)

            os.system("cls || clear")

    elif op1 == 0:
        # Encerra o programa
        break

    else:
        print("===   Opção Inválida   ===")
        input("Digite ENTER para continuar!")

    os.system("cls || clear")

    # Exibe novamente o menu principal e aguarda a próxima escolha do usuário
    print("=====================================")
    print("==== M E N U   P R I N C I P A L ====")
    print("=====================================")
    print()
    print("\t1 - Clientes")
    print("\t2 - Funcionários")
    print("\t3 - Agenda")
    print("\t0 - Finalizar Programa")
    print()
    print("=====================================")
    print()

    op1 = input("Escolha sua opção: ")

    os.system(" cls|| clear ")
