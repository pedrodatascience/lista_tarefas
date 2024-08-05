#lista vazia

tarefas = []

#inicio do loop

while True:
    #lista de opções
    print('Programinha de tarefas\n')
    print('1 - Inserir tarefa')
    print('2 - Visualizar tarefas')
    print('3 - Sair\n')
   
    
    #opção de escolha
    opcao = input('Digite o número da opção: ')

    #verifica a opção escolhida

    match opcao:
        case '1':
            nova_tarefa = input('Escreva o nome da tarefa: ')
            tarefas.append(nova_tarefa)
            print('tarefa adicionada')
            continue

        case '2':
            print('*** LISTA DE TAREFAS ***')
            for i in tarefas:
                print(i)
            print('\n')

        case '3':
            print('Você está saindo...')
            break
        case _:
            print('\nOpção inválida, digite o número correto.\n')


