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
        self.error8_path = ".\\{}\\error8.png".format(self.resolution)

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
                time.sleep(1)
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
                time.sleep(5)
                pyautogui.press("space")
                self.ingame()

            if lvlup is not None:
                print("lvl Up Detected")
                pyautogui.press("space")
                time.sleep(3)
                pyautogui.press("space")
                self.money += 30
                self.exp += 15
                print("You have won", self.money, "money")
                print("You have won", self.exp, "exp")
                time.sleep(5)
                pyautogui.press("space")
                pyautogui.press("space")
                self.ingame()

    def error(self):
        error = pyautogui.locateOnScreen(self.error_path, confidence=0.8)
        error1 = pyautogui.locateOnScreen(self.error1_path, confidence=0.8)
        error2 = pyautogui.locateOnScreen(self.error2_path, confidence=0.8)
        error3 = pyautogui.locateOnScreen(self.error3_path, confidence=0.8)
        error4 = pyautogui.locateOnScreen(self.error4_path, confidence=0.8)
        error5 = pyautogui.locateOnScreen(self.error5_path, confidence=0.8)
        error6 = pyautogui.locateOnScreen(self.error6_path, confidence=0.8)
        error7 = pyautogui.locateOnScreen(self.error7_path, confidence=0.8)
        error8 = pyautogui.locateOnScreen(self.error8_path, confidence=0.8)
        if error is not None or error1 is not None or error2 is not None or error3 is not None or \
                error4 is not None or error5 is not None or error6 is not None or \
                error7 is not None or error8 is not None:
            print("error")
            pyautogui.press("space")
            time.sleep(1)
            pyautogui.click()
            self.lobby()


class bot1:
    def __init__(self):
        self.money = 0
        self.exp = 0

    def lobby(self):
        while True:
            print("-----> Waiting lobby")
            lobby = pyautogui.locateOnScreen("1080/lobby.png")
            lobby1 = pyautogui.locateOnScreen("720/lobby.png")
            lobby2 = pyautogui.locateOnScreen("1080/lobby.png", confidence=0.6)
            lobby3 = pyautogui.locateOnScreen("720/lobby.png", confidence=0.6)
            if lobby is not None or lobby1 is not None or lobby2 is not None or lobby3 is not None:
                print("Lobby")
                print("Lobby1")
                print("Lobby2")
                print("Lobby3")
                if lobby is not None:
                    pyautogui.click(lobby)
                if lobby1 is not None:
                    pyautogui.click(lobby1)
                if lobby2 is not None:
                    pyautogui.click(lobby2)
                if lobby3 is not None:
                    pyautogui.click(lobby3)

                pyautogui.press("space")
                self.ingame()

    def ingame(self):
        while True:
            ingame = pyautogui.locateOnScreen("1080/ingame.png")
            ingame1 = pyautogui.locateOnScreen("720/ingame.png")
            ingame2 = pyautogui.locateOnScreen("1080/ingame.png", confidence=0.6)
            ingame3 = pyautogui.locateOnScreen("720/ingame.png", confidence=0.6)
            if ingame is not None or ingame1 is not None or ingame2 is not None or ingame3 is not None:
                print("Lobby")
                print("Lobby1")
                print("Lobby2")
                print("Lobby3")
                print("Ingame detected")
                self.exit()

    def exit(self):
        while True:
            exits = pyautogui.locateOnScreen("1080/exit.png")
            exits1 = pyautogui.locateOnScreen("720/exit.png")
            exits2 = pyautogui.locateOnScreen("1080/exit.png", confidence=0.6)
            exits3 = pyautogui.locateOnScreen("720/exit.png", confidence=0.6)
            if exits is not None or exits1 is not None or exits2 is not None or exits3 is not None:
                print("Lobby")
                print("Lobby1")
                print("Lobby2")
                print("Lobby3")
                print("exit detected")
                pyautogui.press("esc")
                time.sleep(1)
                pyautogui.press("space")
                pyautogui.press("space")
                self.result()

    def result(self):
        while True:
            results = pyautogui.locateOnScreen("1080/confirm.png")
            results1 = pyautogui.locateOnScreen("720/confirm.png")
            results2 = pyautogui.locateOnScreen("1080/confirm.png", confidence=0.6)
            results3 = pyautogui.locateOnScreen("720/confirm.png", confidence=0.6)
            if results is not None or results1 is not None or results2 is not None or results3 is not None:
                print("Lobby")
                print("Lobby1")
                print("Lobby2")
                print("Lobby3")
                print("Results Detected")
                time.sleep(2)
                self.money += 30
                self.exp += 15
                print("You have won", self.money, "money")
                print("You have won", self.exp, "exp")
                time.sleep(5)
                pyautogui.press("space")
                pyautogui.press("space")
                self.ingame()

            lvlup = pyautogui.locateOnScreen("1080/lvlup.png")
            lvlup1 = pyautogui.locateOnScreen("720/lvlup.png")
            lvlup2 = pyautogui.locateOnScreen("1080/lvlup.png", confidence=0.6)
            lvlup3 = pyautogui.locateOnScreen("720/lvlup.png", confidence=0.6)
            if lvlup is not None or lvlup1 is not None or lvlup2 is not None or lvlup3 is not None:
                pyautogui.press("space")
                time.sleep(5)
                pyautogui.press("space")
                self.money += 30
                self.exp += 15
                print("You have won", self.money, "money")
                print("You have won", self.exp, "exp")
                time.sleep(5)
                pyautogui.press("space")
                pyautogui.press("space")
                self.ingame()


def checkresolution():
    for i in range(0, 9):
        fullhd = pyautogui.locateOnScreen("1080/lobby.png", confidence=0.8)
        if fullhd is not None:
            print("Full HD detected")
            return bot()

        hd = pyautogui.locateOnScreen("720/lobby.png", confidence=0.8)
        if hd is not None:
            print("HD detected")
            return bot(resolution="720")


def checkresolutionEvent():
    fullhdEvent = pyautogui.locateOnScreen("1080/Event/lobby.png", confidence=0.8)
    if fullhdEvent is not None:
        print("Full HD detected")
        return bot(resolution="1080/Event")

    hdEvent = pyautogui.locateOnScreen("720/Event/lobby.png", confidence=0.8)
    if hdEvent is not None:
        print("HD detected")
        return bot(resolution="720/Event")


a = bot1()

print("Welcome to Fall guys Bot")
print("         by jordan123pal")
print()
print("1 = Stable Mode, 1080 and 720 work fine ")
print("2 = Beta Mode, other resolutions maybe with errors")
print("3 = Event Mode 1080 and 720")

menu = int(input("enter you option : "))

if menu == 1:
    print("starting...")
    check = checkresolution()
    if check is not None:
        check.lobby()

if menu == 2:
    print("starting minimeze console pls...")
    time.sleep(3)
    a.lobby()

if menu == 3:
    print("starting minimeze console pls...")
    check1 = checkresolutionEvent()
    time.sleep(3)
    if check1 is not None:
        check1.lobby()
else:
    print("Good Bye")
