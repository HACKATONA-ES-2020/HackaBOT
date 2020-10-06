# Import Discord Information
import os
import discord
from discord.ext import commands

# put color on the exit
from termcolor import colored
import os

#
# Reading Autorization
#
channel = ""
token = ""
imageName = ""
with open("info/auth.txt","r") as file:
    # Pulando Linhas Desnecessárias
    info = file.readline().strip().split(":")
    info = file.readline().strip().split(":")
    info = file.readline().strip().split(":")
    info = file.readline().strip().split(":")
    # Nome da Imagem
    info = file.readline().strip().split(":")
    if info[0] == "nome":
        imageName = info[1]
    info = file.readline().strip().split(":")
    info = file.readline().strip().split(":")
    if info[0] == "canal":
        channel = info[1]
    info = file.readline().strip().split(":")
    if info[0] == "token":
        token = info[1]

print("Canal: " + channel)
print("Token: " + token)
print("Nome da Imagem: " + imageName)


client = discord.Client()

@client.event
async def on_ready():
    print(colored('[BOT INICIALIZADO COM SUCESSO]','blue'))

# Path and fileName
path = os.path.abspath(os.getcwd()) + "/"
imageName = imageName + ".png"

# Channel Integer
channel = int(channel)

@client.event
async def on_message(message):
    if message.content == '!commits':
        os.system('python3 create_graphic.py')
        # DEVE SER COLOCADO O ID DO CANAL NO LUGAR DO 123456789
        await client.get_channel(channel).send(file=discord.File(path+imageName))
    if message.content == '!code':
        os.system('./teste_valores_lines.sh')
        os.system('python3 reading_lines.py')
        # DEVE SER COLOCADO O ID DO CANAL NO LUGAR DO 123456789
        await client.get_channel(channel).send(file=discord.File(path+imageName))

# Rodar o BOT (DEVE SER COLOCADO O TOKEN PARA FUNCIONAR)
client.run(token)