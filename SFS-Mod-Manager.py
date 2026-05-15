# SFS Mod Mananger
# NEED TO CHANGE TOVANILLA(), it seems to be broken.
# ========== Configs ========== #

import shutil
import os
import subprocess
import customtkinter
ver = "0.3.5"  # Version number

# ========== Startup =========== #

def WarnBox(title,message): # Shows a box with a warning
    def button_event():
        WarnBox.destroy
        quit()
    WarnBox = customtkinter.CTk()
    WarnBox.title(title)
    WarnBox.grid_columnconfigure((0, 1), weight=1)
    WarnBox.label = customtkinter.CTkLabel(WarnBox, text=message, fg_color="transparent")
    WarnBox.label.grid(row=1, column=0, padx=0, pady=0, sticky="ew", columnspan=2)
    WarnBox.button = customtkinter.CTkButton(WarnBox, text="Close", command=button_event)
    WarnBox.button.grid(row=2, column=0, padx=0, pady=0, sticky="ew", columnspan=2)
    WarnBox.mainloop()

if not os.name == 'n':
    print(os.name)
    WarnBox('Unsupported OS',' Your OS (detected as "'+ os.name +'") is unsupported. ')

joint = os.path.expanduser("~"), "\Documents\SFS Mod Manager"
folder = "".join(joint)  # The mod manager folder
if not os.path.isdir(folder):  # Creating the folder for mod storage
    os.mkdir(folder)
dirprofiles = os.listdir(folder)
dirprofiles.append("Vanilla")
profiles = dirprofiles

if not os.path.isdir(
        "C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods"
    ):
        WarnBox('Error',' SFS files are missing. Please launch SFS to fix. ')
        profilefold = folder, 'Modded', "Mods"
        profilefolder = "/".join(profilefold)
        shutil.copytree(
        profilefolder,
          "C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods")


ModdedJoint = folder, "Modded/Mods"
ModdedFolder = "/".join(ModdedJoint)
if not os.path.isdir(ModdedFolder):
    shutil.copytree(
        "C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods",
        ModdedFolder,
    )

# ========== Varibles ========== #

option = (
    # Which profile to launch from (profiles don't really exist at the moment)
    "Modded"
)

# ========== Functions ========== #


def optionmenu_callback(choice):  # Dropdown menu
    global option
    option = choice


def ToVanilla():  # FIX: Copy a clean copy instead just removing
    shutil.rmtree(
        "C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods"
    )


def ToModded():
    profilefold = folder, option, "Mods"
    profilefolder = "/".join(profilefold)
    shutil.rmtree(
        "C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods"
    )
    shutil.copytree(
        profilefolder,
        "C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods",
    )


def launch():  # Launches the game
    if option == "Vanilla":
        ToVanilla()
        subprocess.Popen(
            ["C:/Program Files (x86)/Steam/steam.exe", "-applaunch", "1718870"]
        )
    else:
        ToModded()
        subprocess.Popen(
            ["C:/Program Files (x86)/Steam/steam.exe", "-applaunch", "1718870"]
        )


#    LoadBox()
#    ToVanilla()


def LoadBox():  # Shows a box with a loading message
    LoadingBox = customtkinter.CTk()
    LoadingBox.title("Loading...")
    LoadingBox.grid_columnconfigure((0, 1), weight=1)
    LoadingBox.label = customtkinter.CTkLabel(
        LoadingBox, text="Launching...", fg_color="transparent"
    )
    LoadingBox.label.grid(
        row=1,
        column=0,
        padx=0,
        pady=0,
        sticky="ew",
        columnspan=2)
    LoadingBox.mainloop()


# ========== GUI code ========== #

app = customtkinter.CTk()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("SFS Mod Manager | " + ver)
        self.geometry("540x270")
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((2, 3), weight=1)

        self.button = customtkinter.CTkButton(
            self, text="Launch", command=self.button_callback
        )
        self.button.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
        self.label = customtkinter.CTkLabel(
            self, text="Placeholder", fg_color="transparent"
        )
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.optionmenu = customtkinter.CTkOptionMenu(
            self, values=profiles, command=optionmenu_callback
        )
        self.optionmenu.grid(row=1, column=0, padx=0, pady=0)

    def button_callback(self):
        launch()


app = App()
app.mainloop()
