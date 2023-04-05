import requests
import wget
import subprocess
from tkinter import *

def oui():
    url = 'http://natsrv/Setup/'
    filename = wget.download(url)
    filename
    subprocess.call([r'dele.bat'])
def non():
    subprocess.call([r'run.bat'])


def telechargement():
    win = Tk()
    btnoui = Button(win, text='Faire la mise a jour', command=oui)
    btnoui.pack(side=LEFT)
    btnon = Button(win, text='Continuer sans la maj', command=non)
    btnon.pack(side=RIGHT)


    win.mainloop()
url= "http://natsrv/v1.yml"
response = requests.get(url, stream = True)
for chunk in response.iter_content(chunk_size=1024):
    print(chunk)
    break

fichier = 'version = 1'
print(fichier)
fichierconf = len(fichier)
print(fichierconf)
chunkconf = chunk

reponse_1= len(chunk)
print(reponse_1)

if reponse_1 == fichierconf:
    print('ok:c est bon')
    subprocess.call([r'run.bat'])

else:
    telechargement()


