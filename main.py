import os
import time

#configurations
sh="psh"
ver="1.0.0"
ob="archlinux"


#main program
while True:
    cmd = input("psh $ ")

    if cmd.lower() == "exit":
        print("Quitting the shell.")
        break

    if cmd == "install":
        pkg = input("Package that is going to be installed: ")
        os.system(f"sudo pacman -S {pkg}")

    elif cmd == "update":
        print("Updating... This may take a while.")
        os.system("sudo pacman -Syu")

    elif cmd == "run":
        exe = input("Package that will be executed: ")
        os.system(exe)

    elif cmd.lower().startswith("say "):
        print(cmd[4:])

    elif cmd == "root":
        os.system("sudo su")

    elif cmd == "dirs":
        os.system(ls)

    elif cmd == "info":
        print("Shell:",sh)
        print("PShell version:",ver)
        print("OS build;",ob)

    elif cmd.lower().startswith("wait "):
        sn = int(cmd[5:])
        time.sleep(sn)

    else:
        print("Invalid command.")
