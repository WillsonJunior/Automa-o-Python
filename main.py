from pathlib import Path
import shutil
#printar o diretorio raiz atual
#print(Path.cwd())

#caminho = Path('C:/Users/wilson.junior/PycharmProjects/pythonProject')

#listar os arquidos do caminho

#arquivos = caminho.iterdir()

#for arquivo in arquivos:
    #print(arquivo)

#criar uma pasta

#Path('C:/Users/wilson.junior/PycharmProjects/backup/teste3').mkdir()

print('insira o camiho da pasta onde estão os arquivos a serem copiados')
arquivo_copiar= input(Path(''))

print(('insira o camiho  e o nome da nova pasta onde  os arquivos serao colados'))
arquivo_colar= input(Path(''))

shutil.copytree(arquivo_copiar, arquivo_colar)


#criar um arquivo executavel
#comando no terminla #pyinstaller --onefile "nomedoarquivo.py"

