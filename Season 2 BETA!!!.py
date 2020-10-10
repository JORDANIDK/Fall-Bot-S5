import pyautogui
import time


class bot:
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
                if lobby != None:
                    pyautogui.click(lobby)
                if lobby1 != None:
                    pyautogui.click(lobby1)   
                if lobby2 != None:
                    pyautogui.click(lobby2)    
                if lobby3 != None:
                    pyautogui.click(lobby3)   
                    
                pyautogui.press("space")
                self.ingame()

    def ingame(self):
        while True:
            print("-----> Waiting ingame")
            ingame = pyautogui.locateOnScreen("1080/ingame.png")
            ingame1 = pyautogui.locateOnScreen("720/ingame.png")
            ingame2 = pyautogui.locateOnScreen("1080/ingame.png", confidence=0.6)
            ingame3 = pyautogui.locateOnScreen("720/ingame.png", confidence=0.6)
            if ingame is not None or ingame1 is not None or ingame2 is not None or ingame3 is not None:
                print("Ingame detected")
                self.exit()

    def exit(self):
        while True:
            print("-----> Waiting exit")
            exits = pyautogui.locateOnScreen("1080/exit.png")
            exits1 = pyautogui.locateOnScreen("720/exit.png")
            exits2 = pyautogui.locateOnScreen("1080/exit.png", confidence=0.6)
            exits3 = pyautogui.locateOnScreen("720/exit.png", confidence=0.6)
            if exits is not None or exits1 is not None or exits2 is not None or exits3 is not None:
                print("exit detected")
                pyautogui.press("esc")
                time.sleep(1)
                pyautogui.press("space")
                pyautogui.press("space")
                self.result()

    def result(self):
        while True:
            print("-----> Waiting results")
            results = pyautogui.locateOnScreen("1080/confirm.png")
            results1 = pyautogui.locateOnScreen("720/confirm.png")
            results2 = pyautogui.locateOnScreen("1080/confirm.png", confidence=0.6)
            results3 = pyautogui.locateOnScreen("720/confirm.png", confidence=0.6)
            if results is not None or results1 is not None or results2 is not None or results3 is not None:
                print("Results Detected")
                time.sleep(2)
                self.money += 30
                self.exp += 15
                print("You have won", self.money, "money")
                print("You have won", self.exp, "exp")
                self.lobby()               
                
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
                self.lobby()


a = bot()


def main():
    print("Welcome to Fall guys Bot")
    print("         by jordan123pal")
    print("")
    menu = int(input("enter 1 to start: "))
    if menu == 1:
        print("starting minimeze console pls...")
        time.sleep(3)
        a.lobby()
    else:
        print("good bye")


main()
