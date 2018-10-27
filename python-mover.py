import os
import shutil

lang = 'en-US'
lang_strings = {
    "pt-BR" : {
        "path" : "Digite o caminho do repositório\n",
        "image_cnt" : "Quantas imagens deseja mover?\n",
        "create_dir" : "\nDeseja criar um novo diretório ou mover as imagens para um diretório existente?\n",
        "new_dir_name" : 'Digite o nome do novo diretório\n',
        "new_dir_path" :  'Digite o local do diretório\n',
        "moving-image" : 'Movendo imagem - ',
        "moving-image-to" : ' para ',
        "continue" : '\nDeseja continuar?\n1 para SIM\n2 para não\n',
        "finalized": '\nSistema finalizado!'
    },
    "en-US" : {
        "path" : "Type the name of the repository\n",
        "image_cnt" : "How many images do you want to move?\n",
        "create_dir" : "\nDo you want to create a new directory or move the images to a existing directory?\n",
        "new_dir_name" : 'Type the name of the new directory\n',
        "new_dir_path" :  'Type the path of the new directory\n',
        "moving-image" : 'Moving image - ',
        "moving-image-to" : ' to ',
        "continue" : '\nDo you wish to continue?\n1 for YES\n2 for NO\n',
        "finalized": '\nSystem finalized!'
    }
}
strings = lang_strings[lang]

path = input(strings["path"])
os.chdir(path)
files = sorted(os.listdir(path))
total = int(input(strings["image_cnt"]))


while True:
    question = int(input(strings["create_dir"]))
    if question == 1:
        mvdir = input(strings["new_dir_name"])
        os.mkdir(mvdir)
    elif question == 2:
        mvdir = input(strings["new_dir_path"])
    else:
        break
        
    #Percorrer imagens e movê-las (começa em 0 até total a ser movido)
    for file_names in files[:total]:
        print(strings["moving-image"] + file_names + strings["moving-image-to"] + mvdir)
        shutil.move(file_names, mvdir)
    
    #Pergunta se o usuário deseja mover mais alguma leva de arquivos
    choice = int(input(strings["continue"]))
    if choice == 2:
        break

print(strings["finalized"])
