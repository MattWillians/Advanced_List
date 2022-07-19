listapecas = [] #<---- aqui entram todas as informações do dicionario
dicionariopecas = {}#<----- Aqui, ficam armazenadas as informações digitadas

def cadastrarPeca(codigo):
  #MENU AMIGAVEI PARA O USUARIO
  print('______________________________')
  print('Iniciando cadastro de peças...')
  print('Codigo do produto: {}'.format(codigo))
  print('')
  #ENTRAR COM OS DADOS PARA A LISTA
  nome = input('Digite o nome da peça em questão: ')
  fabricante = input('Digite o nome do fabricante: ')
  valor = float(input('Digite o valor da peça: '))
  print('')
  
  #SALVAR OS DADOS DA LISTA EM M DICIONARIO
  dicionariopecas = {'CODIGO:': codigo,
                     'NOME:': nome,
                     'VALOR:': valor,
                     'FABRICANTE:': fabricante} 
  
  #CRIA UMA COPIA DOS DADOS PARA A LISTA
  listapecas.append(dicionariopecas.copy())

def consultarPeca():
  #INICIA UM LAÇO PARA CONSULTAR AS PEÇAS
  while True:
    try:
      #MENU AMIGAVEL COM TRATAMENTO DE ERROS
      print('')
      print('Iniciando consulta de peças...')
      print('Consulta de peças selecionada, digite uma das opções para começar a consulta:')
      print('')
      print('1 - Consultar todas as peças')
      print('2 - Consultar peças por código')
      print('3 - Consultar peças por fabricante')
      print('4 - Retornar')
      
      consultar = int(input('Escolha uma das 4 opções para iniciar a consulta: '))
      #INICIO DA CONSULTA
      if(consultar == 1):
        print('')
        print('Consultando todas as opções...')
        for tudo in listapecas:#VARRE A LISTA, BUSCANDO TODOS OS ITENS
          for i,j in tudo.items():#PEGA OS ITENS 
            print('{} : {}'.format(i,j))#IMPRIMI TODOS DE FORMA ORDENADA
    
        
      elif(consultar == 2):
        print('')
        print('Iniciando consulta por CODIGO: ')
        code = int(input('Digite o codigo desejado para consulta: '))
        for pecas in listapecas:#VARRE A LISTA NOVAMENTE
          if(pecas['CODIGO:'] == code):#VERIFICA SE O CODIGO EXISTE
            for key, value in pecas.items():#PEGA AS INFIRMAÇÕES DESEJADAS
              print('---------------------------')
              print('{} : {}'.format(key, value))#IMPRIMI NA TELA AS INFORMAÇÕES
              print('---------------------------')

      elif(consultar == 3):
        #MESMA DEFINIÇÃO ACIMA, COM A DIFERENÇA QUE A BUSCA É POR MEIO DO FABRICANTE
        print('')
        print('Iniciando consulta por FABRICANTE')
        fabricant = input('Digite o FABRICANTE desejado para consulta: ')
        for pecas in listapecas:
          if(pecas['FABRICANTE:'] == fabricant):
            for key, value in pecas.items():
              print('---------------------------')
              print('{} : {}'.format(key, value))
              print('---------------------------')

      elif(consultar == 4):
        #RETORNA AO MENU PRINCIPAL
        print('---------------------------')
        print('Retornando ao começo...')
        print('---------------------------')
        return
      
      elif(consultar > 4):
        print('')
        print('Valor invalido!')
        continue

    except SyntaxError:
      print('')
      print('Oops, opção digitada inexistente!')
      continue

def removerPeca():
  #REMOVER ALGUMA PEÇA
  print('')
  print('Iniciando remoção de peças...')
  remove = int(input('Digite o codigo da peça desejada para remoção: '))
  for peca in listapecas:
    if(peca['CODIGO:'] == remove):#PROCURA PELA PEÇA DIGITADA E A REMOVE
      listapecas.remove(peca)
      print('Peça de codigo {} removida!'.format(remove))#CONFIRMA QUE A PEÇA FOI REMOVIDA
        
cadastro = 0 #CONTADOR DE CADASTROS FEITOS

#----------------- PROGRAMA PRINCIPAL--------------------#
print('BEM VINDO AO CADASTRO DE PEÇAS DO MATHEUS PEREIRA')
while True:

  print('Ações possiveis:')
  print('1 - Cadastrar Peças!')
  print('2 - Consultar Peças!')
  print('3 - Remover Peças!')
  print('4 - Encerrar programa')
  
  try:
    escolha = int(input('Digite uma das opções: '))
  
    if(escolha == 1):
      cadastro += 1
      cadastrarPeca(cadastro)#INICIA O CADASTRO DA PEÇA E CONTA O CODIGO DELA

    elif(escolha == 2):#INICIA A CONSULTA DE PEÇAS
      consultarPeca()

    elif(escolha == 3):#INICIA A REMOÇÃO DE PEÇAS
      removerPeca()

    elif(escolha == 4):#ENCERRA O PROGRAMA
      break

    else:
      print('Valor invalido!')#ESCOLHA NÃO EXISTE

  except ValueError:
    print('Oops, opção digitada inexistente!')#ERRO DE DIGITAÇÃO
    continue