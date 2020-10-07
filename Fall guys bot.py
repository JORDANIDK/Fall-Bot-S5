import time
import pyautogui
import threading


class bot:
    def __init__(self, resolution="1080", confidence=1):
        self.resolution = resolution
        self.confidence = confidence

        # path

        self.lobby_path = ".\\{}\\lobby.png".format(self.resolution)
        self.ingame_path = ".\\{}\\ingame.png".format(self.resolution)
        self.exit_path = ".\\{}\\exit.png".format(self.resolution)
        self.ok_path = ".\\{}\\ok.png".format(self.resolution)
        self.confirm_path = ".\\{}\\confirm.png".format(self.resolution)

        # Path error

        self.error_path = ".\\{}\\error.png".format(self.resolution)
        self.error1_path = ".\\{}\\error1.png".format(self.resolution)
        self.error2_path = ".\\{}\\error2.png".format(self.resolution)
        self.error3_path = ".\\{}\\error3.png".format(self.resolution)
        self.error4_path = ".\\{}\\error4.png".format(self.resolution)

        # Save exp

        self.exp = 0
        self.money = 0

    def lobby(self):
        while True:
            self.error()
            print("Waiting lobby...")
            time.sleep(2)
            lobby = pyautogui.locateOnScreen(self.lobby_path, self.confidence)
            if lobby is not None:
                print("Lobby detected ")
                pyautogui.click(lobby)
                pyautogui.press("space")
                self.ingame()
                break

    def ingame(self):
        while True:
            self.error()
            ingame = pyautogui.locateOnScreen(self.ingame_path, self.confidence)
            if ingame is not None:
                print("Ingame detected")
                self.exit()
                break

    def exit(self):
        while True:
            self.error()
            salir = pyautogui.locateOnScreen(self.exit_path, self.confidence)
            if salir is not None:
                print("exit detected")
                time.sleep(2)
                pyautogui.press("esc")
                self.ok()
                break

    def ok(self):
        while True:
            self.error()
            ok2 = pyautogui.locateOnScreen(self.ok_path, self.confidence)
            if ok2 is not None:
                time.sleep(1)
                pyautogui.press("space")
                self.results()
                break

    def results(self):
        while True:
            self.error()
            result = pyautogui.locateOnScreen(self.confirm_path, self.confidence)
            if result is not None:
                pyautogui.click(result)
                pyautogui.press("space")
                self.money += 30
                self.exp += 15
                print("You have won", self.money, "money")
                print("You have won", self.exp, "exp")
                self.lobby()

    def error(self):
        time.sleep(3)
        error = pyautogui.locateOnScreen(self.error_path, self.confidence)
        error1 = pyautogui.locateOnScreen(self.error1_path, self.confidence)
        error2 = pyautogui.locateOnScreen(self.error2_path, self.confidence)
        error3 = pyautogui.locateOnScreen(self.error3_path, self.confidence)
        error4 = pyautogui.locateOnScreen(self.error4_path, self.confidence)
        print("No errors")
        if error is not None or error1 is not None or error2 is not None or error3 is not None or error4 is not None:
            print("error")
            pyautogui.press("space")
            time.sleep(1)
            pyautogui.click()
            pyautogui.press("enter")
            self.lobby()


def checkresolution():
    fullhd = pyautogui.locateOnScreen("1080/lobby.png")
    if fullhd is not None:
        print("Full HD detected")
        return bot()

    hd = pyautogui.locateOnScreen("720/lobby.png")
    if hd is not None:
        print("HD detected")
        return bot(resolution="720")

    fullhdlow = pyautogui.locateOnScreen("1080/lobby.png", confidence=0.6)
    if fullhdlow is not None:
        print("Full HD Low detected")
        return bot(confidence=0.6)

    hdlow = pyautogui.locateOnScreen("720/lobby.png")
    if hdlow is not None:
        print("HD Low detected")
        return bot(resolution="720", confidence=0.6)


print("Welcome to Fall guys Bot")
print("         by jordan123pal")
print("")
menu = int(input("enter 1 to start: "))

if menu == 1:
    print("starting...")
    time.sleep(5)
    check = checkresolution()
    if check is not None:
        check.lobby()
    else:
        print("no resolution detected, try resizing the game and focus the game")
