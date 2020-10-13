import time
import pyautogui


class bot:
    def __init__(self, resolution="1080"):
        self.resolution = resolution

        # path

        self.lobby_path = ".\\{}\\lobby.png".format(self.resolution)
        self.ingame_path = ".\\{}\\ingame.png".format(self.resolution)
        self.exit_path = ".\\{}\\exit.png".format(self.resolution)
        self.ok_path = ".\\{}\\ok.png".format(self.resolution)
        self.confirm_path = ".\\{}\\confirm.png".format(self.resolution)
        self.lvlup_path = ".\\{}\\lvlup.png".format(self.resolution)

        # Path error

        self.error_path = ".\\{}\\error.png".format(self.resolution)
        self.error1_path = ".\\{}\\error1.png".format(self.resolution)
        self.error2_path = ".\\{}\\error2.png".format(self.resolution)
        self.error3_path = ".\\{}\\error3.png".format(self.resolution)
        self.error4_path = ".\\{}\\error4.png".format(self.resolution)
        self.error5_path = ".\\{}\\error5.png".format(self.resolution)
        self.error6_path = ".\\{}\\error6.png".format(self.resolution)
        self.error7_path = ".\\{}\\error7.png".format(self.resolution)

        # Save exp

        self.exp = 0
        self.money = 0

    def lobby(self):
        while True:
            self.error()
            print("Waiting lobby...")
            time.sleep(2)
            lobby = pyautogui.locateOnScreen(self.lobby_path, confidence=0.8)
            if lobby is not None:
                print("Lobby detected ")
                pyautogui.click(lobby)
                pyautogui.press("space")
                self.ingame()
                break

    def ingame(self):
        while True:
            self.error()
            ingame = pyautogui.locateOnScreen(self.ingame_path, confidence=0.8)
            if ingame is not None:
                print("Ingame detected")
                self.exit()
                break

    def exit(self):
        while True:
            self.error()
            salir = pyautogui.locateOnScreen(self.exit_path, confidence=0.8)
            if salir is not None:
                print("exit detected")
                pyautogui.press("esc")
                self.ok()
                break

    def ok(self):
        while True:
            self.error()
            ok2 = pyautogui.locateOnScreen(self.ok_path, confidence=0.8)
            if ok2 is not None:
                pyautogui.press("space")
                self.results()
                break

    def results(self):
        while True:
            self.error()
            result = pyautogui.locateOnScreen(self.confirm_path, confidence=0.8)
            lvlup = pyautogui.locateOnScreen(self.lvlup_path, confidence=0.8)
            if result is not None:
                pyautogui.click(result)
                pyautogui.press("space")
                self.money += 30
                self.exp += 15
                print("You have won", self.money, "money")
                print("You have won", self.exp, "exp")
                self.lobby()

            if lvlup is not None:
                pyautogui.press("space")
                time.sleep(3)
                pyautogui.press("space")
                self.money += 30
                self.exp += 15
                print("You have won", self.money, "money")
                print("You have won", self.exp, "exp")
                self.lobby()

    def error(self):
        error = pyautogui.locateOnScreen(self.error_path, confidence=0.8)
        error1 = pyautogui.locateOnScreen(self.error1_path, confidence=0.8)
        error2 = pyautogui.locateOnScreen(self.error2_path, confidence=0.8)
        error3 = pyautogui.locateOnScreen(self.error3_path, confidence=0.8)
        error4 = pyautogui.locateOnScreen(self.error4_path, confidence=0.8)
        error5 = pyautogui.locateOnScreen(self.error5_path, confidence=0.8)
        error6 = pyautogui.locateOnScreen(self.error6_path, confidence=0.8)
        error7 = pyautogui.locateOnScreen(self.error7_path, confidence=0.8)
        if error is not None or error1 is not None or error2 is not None or error3 is not None or error4 is not None or error5 is not None or error6 is not None or error7 is not None:
            print("error")
            pyautogui.press("space")
            time.sleep(1)
            pyautogui.click()
            pyautogui.press("enter")
            self.lobby()


def checkresolution():
    for i in range(0, 4):
        fullhd = pyautogui.locateOnScreen("1080/lobby.png", confidence=0.8)
        if fullhd is not None:
            print("Full HD detected")
            return bot()

        hd = pyautogui.locateOnScreen("720/lobby.png", confidence=0.8)
        if hd is not None:
            print("HD detected")
            return bot(resolution="720")



print("Welcome to Fall guys Bot")
print("         by jordan123pal")
print()
print("1920x1080 and 1280x720 work")
print("Other resolution IDK!!!")
print()

menu = int(input("enter 1 to start: "))

if menu == 1:
    print("starting...")
    check = checkresolution()
    if check is not None:
        check.lobby()
    else:
        print("no resolution detected")
