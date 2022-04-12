import os
#Arc-theme
os.system("sudo apt install arc-theme -y")
print("Arc-theme installed")
#Breez-cursor-theme
os.system("sudo apt install breeze-cursor-theme")
print("Breeze-cursor-theme installed")
#Tela-icon-theme
os.system("git clone https://github.com/vinceliuice/Tela-icon-theme")
print("Tela-icon-theme installed")
#Pi-apps
os.system("wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash")
print("Pi-apps installed")
#Python3
os.system("sudo apt install python3 idle3 -y")
os.system("sudo apt upgrade python3 idle3 -y")
print("Python3 idle3 installed")