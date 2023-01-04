import requests
import os


def start_server():
    os.system("java -Xmx" + requested_ram + "M -Xms" + requested_ram + "M -jar spigot.jar nogui")


def change_eula():
    start_server()
    with open("eula.txt" , 'r') as file:
        eula_file = file.read()
        eula_file = eula_file.replace("false", "true")
    with open("eula.txt", "w") as file:
        file.write(eula_file)

    checking_eula()


def checking_eula():
    with open("eula.txt", "r") as eula:
        content = eula.read()
        while "eula=false" in content:
            print("Waiting for Eula to change")
        else:
            print("Eula has been changed!")
            start_server()


requested_ram = input("How much ram would you like your server to have in MB (Ex. 1024, 2048, 4096, etc)? ")

if os.path.exists("spigot.jar") is False:

    # fetches the spigot.jar file
    URL = "https://download.getbukkit.org/spigot/spigot-1.19.3.jar"

    # downloads the data
    response = requests.get(URL)

    # copies the data and creates the file
    open("spigot.jar", "wb").write(response.content)

    if requested_ram.isnumeric():
        change_eula()

    else:
        requested_ram = input("How much ram would you like your server to have in MB (Ex. 1024, 2048, 4096, etc)? ")
else:
    start_server()
