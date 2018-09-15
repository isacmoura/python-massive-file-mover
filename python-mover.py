import os
import shutil

path = input('Digite o caminho do repositório\n')
os.chdir(path)
files = sorted(os.listdir(path))
total = int(input('Quantas imagens deseja mover?\n'))


while True:
    question = int(input('\nDeseja criar um novo diretório ou mover as imagens para um diretório existente?\n1 - CRIAR\n2 - MOVER PARA EXISTENTE\n'))
    if question == 1:
        mvdir = input('Digite o nome do novo diretório\n')
        os.mkdir(mvdir)
    elif question == 2:
        mvdir = input('Digite o local do diretório\n')
    else:
        break
        
    #Percorrer imagens e movê-las (começa em 0 até total a ser movido)
    for file_names in files[:total]:
        print('Movendo imagem - ' + file_names + ' para ' + mvdir)
        shutil.move(file_names, mvdir)
    
    #Pergunta se o usuário deseja mover mais alguma leva de arquivos
    choice = int(input('\nDeseja continuar?\n1 para SIM\n2 para não\n'))
    if choice == 2:
        break

print('\nSistema finalizado!')
