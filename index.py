import os
import signal
import sys
import subprocess


def sigint_handler(signal, frame):
    print()
    print()
    print("  The script has been stopped")
    print()
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)


def launchServer():
    print()
    print("         Minecraft Installer by kangapi")
    print()
    print("1. Launch a minecraft server")
    print()
    print("2. Exit")
    print()
    print()
    first = input("  Please enter the number[1-2]: ")
    print()

    return first


launchServerChoice = launchServer()

while launchServerChoice != "1" and launchServerChoice != "2":
    print("  Please enter the number[1-2]")
    print()
    launchServerChoice = launchServer()

if launchServerChoice == "2":
    sys.exit()


def serverPort():
    print()
    third = input("  Please enter the port of the server[25565]: ")
    print()

    return third


serverPortChoice = serverPort()

if serverPortChoice == "":
    serverPortChoice = "25565"


def serverType():
    print("Select the type of the server")
    print()
    print("1. Paper")
    print()
    print("2. Forge")
    print()
    print("3. Vanilla")
    print()
    print()
    fourth = input("  Please enter the number[1-2-3]: ")
    print()

    return fourth


serverTypeChoice = serverType()

while serverTypeChoice != "1" and serverTypeChoice != "2" and serverTypeChoice != "3":
    print("  Please enter the number[1-2-3]")
    print()
    serverTypeChoice = serverType()

# By default, the server type is Vanilla
serverTypeArg = "VANILLA"

if serverTypeChoice == "1":
    serverTypeArg = "PAPER"
if serverTypeChoice == "2":
    serverTypeArg = "FORGE"


def serverVersion():
    print()
    fifth = input("  Please enter the version of the server[latest]: ")
    print()

    return fifth


serverVersionChoice = serverVersion()

if serverVersionChoice == "":
    serverVersionChoice = "latest"

serverName = "minecraft-" + serverTypeArg + "-" + serverVersionChoice


def serverPath():
    print()
    sixth = input("  Please enter the path where the server will be installed[/home/minecraft/" + serverName + "]: ")
    print()

    return sixth


serverPathChoice = serverPath()

if serverPathChoice == "":
    serverPathChoice = "/home/minecraft/" + serverName


def serverWithSameName():
    print()
    print("Another server with the same name already exists")
    print()
    print("1. Stop the existing server")
    print()
    print("2. Remove the existing server")
    print()
    print("3. Create a new server with another name and another port")
    print()
    print()
    seventh = input("  Please enter the number[1-2-3]: ")
    print()

    return seventh


serverWithSameNameChoice = serverWithSameName()

while serverWithSameNameChoice != "1" and serverWithSameNameChoice != "2" and serverWithSameNameChoice != "3":
    print("  Please enter the number[1-2-3]")
    print()
    serverWithSameNameChoice = serverWithSameName()

if serverWithSameNameChoice == "1":
    os.system("docker container stop " + serverName)
if serverWithSameNameChoice == "2":
    os.system("docker container stop " + serverName)
    os.system("docker container rm " + serverName)
if serverWithSameNameChoice == "3":
    serverName = serverName + "-2"
    serverPathChoice = serverPathChoice + "-2"
    serverPortChoice = str(int(serverPortChoice) + 1)


out = subprocess.Popen(['docker ps'], stdout=subprocess.PIPE, shell=True)
stdout = out.communicate()
if stdout[0].decode("utf-8").find("minecraft-" + serverTypeArg + "-" + serverVersionChoice) != -1:
    print("  The server is already running")

serverCommand = f"docker run -d -it -v {serverPathChoice}:/data -e TYPE={serverTypeArg} -e VERSION={serverVersionChoice} -p {serverPortChoice}:{serverPortChoice} -e EULA=TRUE --name {serverName} itzg/minecraft-server"

os.system(serverCommand)

print()
print("  The server has been created")


def serverActions():
    print()
    print("1. Show the logs of the server")
    print()
    print("2. Attach to the server")
    print()
    print("3. Exit")
    print()
    print()
    second = input("  Please enter the number[1-2-3]: ")
    print()

    return second


serverActionsChoice = serverActions()
while serverActionsChoice != "1" and serverActionsChoice != "2" and serverActionsChoice != "3":
    print("  Please enter the number[1-2-3]")
    print()
    serverActionsChoice = serverActions()

if serverActionsChoice == "1":
    os.system("docker logs -f " + serverName)
if serverActionsChoice == "2":
    os.system("docker attach " + serverName)
if serverActionsChoice == "3":
    sys.exit()

# docker run -d -it -v /path/on/host:/data -e TYPE=PAPER -e VERSION=1.18.2 -p 25565:25565 -e EULA=TRUE --name mc itzg/minecraft-server
