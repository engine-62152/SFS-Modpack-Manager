# SFS Mod Mananger

# ========== Configs ========== #

ver = '0.2.0' # Version number

# ========== Modules ========== #

import customtkinter, subprocess, os, shutil, pathlib

# ========== Varibles ========== #

option = 'Vanilla' # Which profile to launch from (profiles don't really exist at the moment)
user = os.path.expanduser('~')
joint = os.path.expanduser('~'),'\Documents\SFS Mod Manager'
folder = "".join(joint) # The mod manager folder
profiles = os.listdir(folder)

# ========== Functions ========== #

def optionmenu_callback(choice): # Sort of a placeholder, but useful for logging
    print("optionmenu dropdown clicked:", choice)
    global option
    if choice == 'Vanilla':
        option = 'Vanilla'
        print (option) # More logging
    elif choice == 'Modded':
        option = 'Modded'
        print (option)


def ToVanilla(): # Works, but not finished 
    shutil.rmtree('C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods')

def ToModded():
    profilefold = folder, option
    profilefolde = "/".join(profilefold), 'Mods'
    profilefolder = "/".join(profilefolde)
    shutil.rmtree('C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods')
    shutil.copytree(profilefolder,'C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods')

def launch(): # Launches the game
    if option == 'Vanilla':
        print('Van')
        ToVanilla()
        subprocess.Popen(['C:/Program Files (x86)/Steam/steam.exe', '-applaunch', '1718870'])
    else:
        ToModded()
        subprocess.Popen(['C:/Program Files (x86)/Steam/steam.exe', '-applaunch', '1718870'])
        print(option)
        print('Mod')
#    LoadBox()
#    ToVanilla()

def LoadBox(): # Shows a box with a loading message
    LoadingBox = customtkinter.CTk()
    LoadingBox.title("Loading...")
    LoadingBox.grid_columnconfigure((0, 1), weight=1)
    LoadingBox.label = customtkinter.CTkLabel(LoadingBox, text="Launching...", fg_color="transparent")
    LoadingBox.label.grid(row=1, column=0, padx=0, pady=0, sticky="ew", columnspan=2)
    LoadingBox.mainloop()

# ========== Startup =========== #

#print(os.path.expanduser('~')+'/Documents/SFSMM')
print (user) # For denugging
print (folder)
if not os.path.isdir(folder) == True: # Creating the folder for mod storage
    os.mkdir(folder)
    if not os.path.isdir('C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods'):
        os.mkdir('C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods')
else:
    if not os.path.isdir('C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods'):
        os.mkdir('C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods')
    

# ========== GUI code ========== #

app = customtkinter.CTk()
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("SFS Mod Manager | "+ver)
        self.geometry("540x270")
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((2,3), weight=1)

        self.button = customtkinter.CTkButton(self, text="Launch", command=self.button_callback)
        self.button.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
        self.label = customtkinter.CTkLabel(self, text="Placeholder", fg_color="transparent")
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.optionmenu = customtkinter.CTkOptionMenu(self, values=profiles,command=optionmenu_callback)
        self.optionmenu.grid(row=1, column=0, padx=0, pady=0)
        
    def button_callback(self):
        launch()

app = App()
app.mainloop()