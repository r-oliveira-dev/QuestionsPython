def questao1():
  # Q.44:

  print("="*20)
  print(" MERCADO")
  print("="*20)
  print()
  produtoPreco = float(input("Informe o preço do produto: R$"))
  print("O preço do produto é:{}".format(produtoPreco))
  print("""
  [1] - À vista dinheiro/cheque: 10% de desconto
  [2] - À vista no cartão: 5% de desconto
  [3] - Em até 2X no cartão: preço normal
  [4] - 3x ou mais no cartão: 20% de juros""")
  opcaoPagamento = int(input("Informe a opção de pagamento:"))
  if opcaoPagamento == 1: 
      precoAtualizado = produtoPreco - (produtoPreco*0.10) 
      print("O preço atual é: R${}".format(precoAtualizado))
  elif opcaoPagamento == 2: 
      precoAtualizado = produtoPreco - (produtoPreco*0.5) 
      print("O preço atual é: R${}".format(precoAtualizado))
  elif opcaoPagamento == 3: 
      precoAtualizado = produtoPreco 
      print("O preço atual é: R${}".format(precoAtualizado))
  elif opcaoPagamento == 4: 
      precoAtualizado = produtoPreco + (produtoPreco*0.2)
      print("O preço atual é: R${}".format(precoAtualizado))

  print()
  print('''Você deseja voltar ao menu ou continuar?
  
      [1] Continuar
      [2] Voltar
      ''')
  opcao = int(input())

  if opcao == 1:
    questao2()
  elif opcao == 2:
    menu()

def questao2():
  # Q.45
  from random import randint
  from time import sleep 

  lista = ("Pedra", "Papel", "Tesoura") 
  computador = randint(0,2)
  perguntar = int(input('''Escolha uma opção para jogar:

  [0] Pedra 
  [1] Papel 
  [2] Tesoura 
  
  Digite sua escolha: ''')) 
  
  print("JO\n") 
  sleep(1) 
  print("KEN\n") 
  sleep(1) 
  print("POOH!!!\n") 
  
  print("-="*20) 
  print("O computador escolheu: {}".format(lista[computador])) 
  print("O jogador escolheu: {}".format(lista[perguntar])) 
  print("-="*20) 
  
  if computador == 0:    
      if perguntar == 0:         
          print("Empate!")     
      elif perguntar == 1:        
          print("Jogador perdeu")    
      elif perguntar == 2:        
          print("Computador venceu")     
      else:         
          print("Operacao invalida") 
  
  elif computador == 1:    
      if perguntar == 0:         
          print("Computador perdeu")    
      elif perguntar == 1:         
          print("Empate!")     
      elif perguntar == 2:         
          print("Jogador venceu")     
      else:        
          print("Operacao invalida") 
  
  elif computador == 2: 
      if perguntar == 0:         
          print("Jogador venceu")     
      elif perguntar == 1:        
          print("Computador venceu")     
      elif perguntar == 2:        
          print("Empate!")     
      else:         
          print("Operacao invalida") 
  else:     
      print("Operacao invalida")

  print()
  print('''Você deseja voltar ao menu ou continuar?
  
      [1] Continuar
      [2] Voltar
      ''')
  opcao = int(input())

  if opcao == 1:
    questao3()
  elif opcao == 2:
    menu()

def questao3():
  # Q.46
  from time import sleep
  for contagem in range(10,0,-1):    
      print(contagem)    
      sleep(1)
  print("BOOOOOMMMMMM!")

  print()
  print('''Você deseja voltar ao menu ou continuar?
  
      [1] Continuar
      [2] Voltar
      ''')
  opcao = int(input())

  if opcao == 1:
    questao4()
  elif opcao == 2:
    menu()

def questao4():
  # Q.47
  for i in range(1, 50):
      if i % 2 == 0: 
       print(i)

  print()
  print('''Você deseja voltar ao menu ou continuar?
  
      [1] Continuar
      [2] Voltar
      ''')
  opcao = int(input())

  if opcao == 1:
    questao5()
  elif opcao == 2:
    menu()

def questao5():
  #Q. Entrada e Saida
  
  print('-'*20)
  print('calculadora de soma')
  print('-'*20)
  print( )
  
  num1 = int(input('Insira o primeiro numero para a soma: '))
  num2 = int(input('Insira o segundo numero para a soma: '))
  soma = num1 + num2
  print( )
  
  print('O resultado da soma entre {} e {} é o numero: {} '.format(num1, num2, soma))

  print()
  print('''Você deseja voltar ao menu ou continuar?
  
      [1] Continuar
      [2] Voltar
      ''')
  opcao = int(input())

  if opcao == 1:
    questao6()
  elif opcao == 2:
    menu()

def questao6():
  #Q. Condicionais

  print('-'*27)
  print('leitor de origem de produto')
  print('-'*27)
  print( )
  
  code = int(input('''digite o codigo do produto: 
       [1 até 11] Nacional
       [12 ou +] Internacional
       '''))
  print( )
  
  if code == 1:
    print('este produto é do Sul')

  elif code == 2:
    print('este produto é do Norte')

  elif code == 3:
    print('este produto é do Leste')

  elif code == 4:
    print('este produto é do Oeste')

  elif code == 5:
    print('este produto é do Nordeste')

  elif code == 6:
    print('este produto é do Nordeste')

  elif code == 7:
    print('este produto é do Sudeste')

  elif code == 8:
    print('este produto é do Sudeste')

  elif code == 9:
    print('este produto é do Sudeste')

  elif code == 10:
    print('este produto é do Centro-Oeste')

  elif code == 11:
    print('este produto é do Noroeste')

  else:
    print('este produto é importado')

  print()
  print('''Você deseja voltar ao menu ou continuar?
  
      [1] Continuar
      [2] Voltar
      ''')
  opcao = int(input())

  if opcao == 1:
    questao7()
  elif opcao == 2:
    menu()

def questao7():
  #Q. Repetições e Condicionais

  print('Gerador de Tabuadas')
  tabuada = int(input("Tabuada do numero: "))

  for count in range(10):
      print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )

  print()
  print('''Você deseja voltar ao menu ou continuar?
  
      [1] Continuar
      [2] Voltar
      ''')
  opcao = int(input())

  if opcao == 1:
    questao8()
  elif opcao == 2:
    menu()

def questao8():
  #Q. Listas ou Tuplas

  print('-'*20)
  print('corretor de provas')
  print('-'*20)
  print( )

  soma = 0
  n = 0


  while n < 30:
      print(f"Questão {n+1}:")
      gabarito = str(input("Digite o gabarito: "))
      nota = str(input("Digite a resposta do aluno: "))
      print("\n")
      n = n + 1
      if nota == gabarito:
          soma = soma + 1
  print(f"A pontuação do aluno foi: {soma}", 'de 30')

  print()
  print('''Você deseja voltar ao menu ou continuar?
  
      [1] Continuar
      [2] Voltar
      ''')
  opcao = int(input())

  if opcao == 1:
    questao9()
  elif opcao == 2:
    menu()


def questao9():
  #Q. Dicionarios

  print('-'*25)
  print('CADASTRO DE PESSOAS')
  print('-'*25)
  print( )
  
  listas = [[]]

  while True:
      print("1-Cadastrar pessoa")
      print("2-Lista Cadastros")
      print("3-Procurar Pessoa Especifica")
      print('4-Sair')
      print( )

      op = int(input())
      if op == 1:
          nova = []
          print('se cadastre: ')
          id = input("Id da pessoa: ")
          nome = input("Digite o nome da pessoa: ")
          idade = input("Idade da pessoa: ")
          print('escreva seu endereço: ')
          rua = input('Escreva o nome da rua: ')
          CEP = input('Digite o CEP: ')
          bairro = input('Escreva o nome do bairro: ')
          cidade = input('Escreva o nome da cidade: ')
          print( )

          nova.append(id)
          nova.append(nome)
          nova.append(idade)
          nova.append(rua)
          nova.append(CEP)
          nova.append(bairro)
          nova.append(cidade)

          listas.append(nova)
      elif op == 2:
          for mostrar in listas:
              for mostrar2 in mostrar:
                  print(mostrar2)
              print( )

      elif op == 3:
        print("Pensando...")
        pessoa = str(input('Digite o nome da pessoa que procura: '))
        pessoa == nome 
        for pessoa in listas:
            print('Achamos! Seu nome é ', nome, ', seu ID é ', id, 'sua idade é ', 
               idade, ', ele(a) mora na rua', rua, ', no bairro ', bairro,
               ', na cidade', cidade, ' e seu CEP é ', CEP)
            print( )

      elif op == 4:
        print('o programa foi fechado')
        break

  print()
  print('''Você deseja voltar ao menu ou continuar?
  
      [1] Continuar
      [2] Voltar
      ''')
  opcao = int(input())

  if opcao == 1:
    questao10()
  elif opcao == 2:
    menu()

def questao10():
  #Q. Modularização

  def ePrimo(numero):
  
    if (numero == 1):
      return True
    if (numero < 1):
      return False
  
    if (primerPrimoDeUmNumero(numero) == numero) :
      return True
    return False

  def primerPrimoDeUmNumero(n): 
    primo = 2
    while ((n%primo) != 0):
      primo += 1
    return primo

  print(ePrimo(int(input('digite o numero: '))))

  print()
  print('Para voltar ao menu. Digite [1].')
  opcao = int(input())

  if opcao == 1:
    menu()
  else:
    menu()

def creditos():
  membro_da_equipe = int(input('''Escolha um membro da equipe 03:
  
      [1] Rhanna Luiza
      [2] Eloisa Braga
      [3] Maria Geovana
      [4] Iann Carlos
      [5] Sair
      '''))
  
  def rhanna():
     print('''Você escolheu Rhanna Luiza.
    Este membro da equipe foi responsável pela revisão dos
    códigos, correção de erros e por desenvolver o switch case.''')
     print()
     creditos()
  def eloisa():
     print('''Você escolheu Eloisa Braga. 
     Este membro da equipe foi responsável pela organização, testagem 
     e desenvolvimento das questões 44 até a 47.''')
     print()
     creditos()
  def geovana():
     print('''Você escolheu Maria Geovana.
     Este membro foi responsável pela revisão dos códigos.''')
     print()
     creditos()
  def iann():
     print('''Você escolheu Iann Carlos.
     Este membro foi responsável pela organização, testagem e desenvolvimento
     das questões 3s.''')
     print()
     creditos()

  if membro_da_equipe == 1:
   rhanna()
  elif membro_da_equipe == 2:
   eloisa()
  elif membro_da_equipe == 3:
   geovana()
  elif membro_da_equipe == 4:
    iann()
  elif membro_da_equipe == 5:
    menu()
  else:
    print('Não temos outro membro na equipe!')
    creditos()

def sair():
  print('O programa foi encerrado!')
  
def menu():

  print('-'*35)
  print('        Questões de Python')
  print('-'*35)

  questao = int(input('''Escolha uma opção:

    [1] Questão 44
    [2] Questão 45
    [3] Questão 46
    [4] Questão 47

    * Questões 3s *

    [5] Entrada e Saída
    [6] Condicionais
    [7] Repetições e Condicionais
    [8] Listas ou Tuplas
    [9] Dicionários
    [10] Modularização

    * Adicionais *
    [11] Créditos
    [12] Sair

    ------------------------------------

  '''))

  if questao == 1:
    questao1()
  elif questao == 2:
    questao2()
  elif questao == 3:
    questao3()
  elif questao == 4:
    questao4()
  elif questao == 5:
    questao5()
  elif questao == 6:
    questao6()
  elif questao == 7:
    questao7()
  elif questao == 8:
    questao8()
  elif questao == 9:
    questao9()
  elif questao == 10:
    questao10()
  elif questao == 11:
    creditos()
  elif questao == 12:
    sair()
  else:
    print('Opção inválida. Tente novamente.')
    menu()

menu()