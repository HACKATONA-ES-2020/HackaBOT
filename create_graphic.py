# Import Github API
from github import Github

# Import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

#
# Getting Auth.txt for identification
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


#
# Authentication
#
# user = input("Enter your Github Username: ")
# password = input("Enter your Github Password: ")
g = Github(userName,passwordGit)

#
# Organization
#
# organization = input("Enter the Organization Name: ")
org = g.get_organization(organizationName)
org.login

#
# Getting the Number of Commits from all Org Repos
#
repoCommits = 0
commitsFeitos = []
repos = []
for repo in org.get_repos():
    name = repo.full_name.split('/') # Divide o nome entrado
    print("Repo Reading [ "+name[1]+" ]")
    for commits in org.get_repo(name[1]).get_commits():
        repoCommits += 1
    commitsFeitos.append(repoCommits)
    repoCommits = 0
    repos.append(name[1])
print(repos)
print(commitsFeitos) 

#
# Graphic
#
x = np.arange(len(repos))
width = 0.35
fig = plt.figure(figsize=(12,6)) # modify if the names are too big
ax = plt.subplot()
# title = input("Define the title for the Graphic: ")
ax.set_title(title)
# colorChoose = input("Define the Color for the Graphic: ")
ax.bar(repos,commitsFeitos,width,color=colorName,align='center')

#plt.show()
# imageName = input("Defining image name: ")
plt.savefig(imageName)