# SFS Mod Mananger
# Credits: Roshan, Engine
# ========== Configs ========== #

import shutil
import os
import webbrowser
import subprocess
import sys

try:
    import customtkinter
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "customtkinter"])

VER = "0.3.10"  # Version number

os.chdir(os.path.abspath(os.path.dirname(__file__)))  # Fixes permission errors

# ========== Startup =========== #

def WarnBox(title, message):  # Shows a box with a warning
    def button_event():
        WarnBox.destroy
        quit()

    WarnBox = customtkinter.CTkToplevel()
    WarnBox.title(title)
    WarnBox.grid_columnconfigure((0, 1), weight=1)
    WarnBox.label = customtkinter.CTkLabel(WarnBox, text=message, fg_color="transparent")
    WarnBox.label.grid(row=1, column=0, padx=0, pady=0, sticky="ew", columnspan=2)
    WarnBox.button = customtkinter.CTkButton(WarnBox, text="Close", command=button_event)
    WarnBox.button.grid(row=2, column=0, padx=0, pady=0, sticky="ew", columnspan=2)

folder = "SFS Mod Manager"  # The mod manager folder
if not os.path.isdir(folder):  # Creating the folder for mod storage
    os.mkdir(folder)
    os.mkdir(f"{folder}/Modded")
    os.mkdir(f"{folder}/Modded/Mods")
dirprofiles = os.listdir(folder)
dirprofiles.append("Vanilla")
profiles = dirprofiles

if (not os.path.exists(f"{folder}/sfs_dir.txt") or os.path.getsize(f"{folder}/sfs_dir.txt") == 0):
    filename = customtkinter.filedialog.askdirectory(title="Open SFS Directory (...\Spaceflight Simulator\Spaceflight Simulator Game)")
    SFS_DIR = filename
    with open(f"{folder}/sfs_dir.txt", "w") as f:
        f.write(filename)
else:
    with open(f"{folder}/sfs_dir.txt", "r") as f:
        SFS_DIR = f.read()
profiles.remove("sfs_dir.txt")

if not os.path.isdir(f"{SFS_DIR}/Mods"):
    WarnBox("Error", " SFS files are missing. Please launch SFS to fix. ")
    profilefolder = os.path.join(folder, "Modded", "Mods")
    shutil.copytree(profilefolder,f"{SFS_DIR}/Mods",)

ModdedFolder = os.path.join(folder, "Modded/Mods")
if not os.path.isdir(ModdedFolder):
    shutil.copytree(f"{SFS_DIR}/Mods",ModdedFolder,)

# ========== Varibles ========== #

# the profile to launch from
option = "Modded"

# ========== Functions ========== #

def optionmenu_callback(choice):  # Dropdown menu
    global option
    option = choice

def ToVanilla():  # FIXED
    os.removedirs(f"{SFS_DIR}/Mods")

def ToModded():
    profilefold = folder, option, "Mods"
    profilefolder = "/".join(profilefold)
    shutil.rmtree(f"{SFS_DIR}/Mods")
    shutil.copytree(profilefolder,f"{SFS_DIR}/Mods",)

def launch():  # Launches the game
    if option == "Vanilla":
        ToVanilla()
        webbrowser.open("steam://rungameid/1718870")
    else:
        ToModded()
        webbrowser.open("steam://rungameid/1718870")

# ========== GUI code ========== #

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("SFS Mod Manager | " + VER)
        self.geometry("540x270")
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((2, 3), weight=1)
        self.button = customtkinter.CTkButton(self, text="Launch", command=self.button_callback)
        self.button.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
        self.label = customtkinter.CTkLabel(self, text="Placeholder", fg_color="transparent")
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=profiles, command=optionmenu_callback)
        self.optionmenu.grid(row=1, column=0, padx=0, pady=0)

    def button_callback(self):
        launch()

app = App()
app.mainloop()
