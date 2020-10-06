# Imports
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import os
from github import Github


#
# Creating the Files with line numbers
#
userName = ""
passwordGit = ""
organizationName = ""
title = ""
imageName = ""
colorName = ""
with open("info/auth.txt","r") as file:
    info = file.readline().strip().split(":")
    if info[0] == "usuario":
        userName = info[1]
    info = file.readline().strip().split(":")
    if info[0] == "senha":
        passwordGit = info[1]
    info = file.readline().strip().split(":")
    if info[0] == "organizacao":
        organizationName = info[1]
    info = file.readline().strip().split(":")
    if info[0] == "titulo":
        title = info[1]
    info = file.readline().strip().split(":")
    if info[0] == "nome":
        imageName = info[1]
    info = file.readline().strip().split(":")
    if info[0] == "cor":
        colorName = info[1]
g = Github(userName,passwordGit)
org = g.get_organization(organizationName)
org.login
repos = []
for repo in org.get_repos():
    name = repo.full_name.split('/')
    repos.append(name[1])
    location = os.getcwd()
    os.system("git clone https://github.com/{}/{}.git".format(organizationName,name[1]))
    os.chdir("{}/".format(name[1]))
    os.system("git ls-files | xargs wc -l > {}.txt".format(name[1]))
    os.system("mv {}.txt {}".format(name[1],location)) 
    os.chdir(location)
    os.system("rm -rf {}".format(name[1]))


#
# Get only the Numbers of Lines
#
print(repos)
totalRepos = len(repos)
index = 0
linhasFeitas = []
while index < totalRepos:
    arquivo = "{}.txt".format(repos[index])
    with open(arquivo,"r") as file:
        first = file.readline()
        for lastLine in file:
            pass
        lastLine = lastLine.strip().split(' ')
        lastLine = int(lastLine[0])
        linhasFeitas.append(lastLine)
    index += 1


#
# GRAPHIC
#

x = np.arange(len(repos))
width = 0.20
fig = plt.figure(figsize=(20,6))
ax = plt.subplot()

ax.set_title(title)
ax.bar(repos,linhasFeitas,width,color=colorName,align='center')

# Se quiser ver antes de Publicar
# plt.show()

plt.savefig(imageName)
os.system("./clear.sh")