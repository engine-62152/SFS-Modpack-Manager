ver = "beta 1"

import customtkinter, subprocess, os, shutil, pathlib

option = "Modded"
user = os.path.expanduser("~")
joint = os.path.expanduser("~"), "\Documents\SFS Mod Manager"
folder = "".join(joint)
profiles = os.listdir(folder)


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)
    global option
    if choice == "Vanilla":
        option = "Vanilla"
    elif choice == "Modded":
        option = "Modded"


def ToVanilla():
    shutil.rmtree(
        "C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods"
    )


def ToModded():
    profilefold = folder, option
    profilefolde = "/".join(profilefold), "Mods"
    profilefolder = "/".join(profilefolde)
    shutil.rmtree(
        "C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods"
    )
    shutil.copytree(
        profilefolder,
        "C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods",
    )


def launch():
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


def LoadBox():
    LoadingBox = customtkinter.CTk()
    LoadingBox.title("Loading...")
    LoadingBox.grid_columnconfigure((0, 1), weight=1)
    LoadingBox.label = customtkinter.CTkLabel(
        LoadingBox, text="Launching...", fg_color="transparent"
    )
    LoadingBox.label.grid(row=1, column=0, padx=0, pady=0, sticky="ew", columnspan=2)
    LoadingBox.mainloop()


if not os.path.isdir(folder) == True:  # Creating the folder for mod storage
    os.mkdir(folder)
    if not os.path.isdir(
        "C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods"
    ):
        os.mkdir(
            "C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods"
        )
else:
    if not os.path.isdir(
        "C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods"
    ):
        os.mkdir(
            "C:/Program Files (x86)/Steam/steamapps/common/Spaceflight Simulator/Spaceflight Simulator Game/Mods"
        )


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
