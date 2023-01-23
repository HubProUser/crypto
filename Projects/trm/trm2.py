import pyautogui
import datetime
import screen_brightness_control as sbc
from clicker.base import Clicker


class Moves(Clicker):

    def click(self, x, y):
        self.human_click([x, y])

    @classmethod
    def sleep(cls, a):
        pyautogui.sleep(a)


run = Moves()


class Race(object):

    @classmethod
    def race_f(cls):
        run.click(1191, 352)
        run.sleep(7)
        trm.firstf()
        run.click(518, 721)
        trm.firstf()
        run.click(688, 718)
        trm.firstf()
        run.click(854, 728)
        trm.firstf()
        run.click(971, 721)
        trm.firstf()
        run.click(1164, 716)
        run.sleep(90)
        run.click(536, 726)
        run.click(536, 686)
        run.click(536, 646)
        run.click(536, 596)
        run.click(536, 546)

    @classmethod
    def race_s(cls):
        trm.secondf()
        run.click(518, 721)
        trm.secondf()
        run.click(688, 718)
        trm.secondf()
        run.click(854, 728)
        trm.secondf()
        run.click(971, 721)
        trm.secondf()
        run.click(1164, 716)
        run.sleep(90)
        run.click(536, 726)
        run.click(536, 686)
        run.click(536, 646)
        run.click(536, 596)
        run.click(536, 546)

    @classmethod
    def firstf(cls):
        run.click(193, 301)
        run.click(1073, 472)
        run.click(1027, 491)
        run.click(1061, 511)
        run.click(235, 427)
        run.click(299, 444)
        run.click(299, 512)
        run.click(297, 585)   # 2.1

    @classmethod
    def secondf(cls):
        run.click(193, 301)
        run.click(425, 632)
        run.click(1073, 472)
        run.click(1027, 491)
        run.click(1061, 511)
        run.click(235, 427)
        run.click(299, 444)
        run.click(299, 512)
        run.click(297, 585)


trm = Race()

minutes = datetime.datetime.now().time().minute   # minutes now
seconds = datetime.datetime.now().time().second   # seconds now

startmin = 27
startsec = 1
z = 3

backup_brightness = sbc.get_brightness()
sbc.set_brightness(0)
# playing the game :)
try:
    while True:
        if minutes == startmin and seconds >= startsec:
            print(f'started at {minutes} minutes, {seconds} seconds')
            trm.race_f()
            startmin += z
            if startmin == 62:
                startmin = 2
            break

        else:
            minutes = datetime.datetime.now().time().minute
            seconds = datetime.datetime.now().time().second
            run.sleep(0.1)

    while True:
        if minutes == startmin and seconds >= startsec:
            print(f'Second race started at {minutes} minutes, {seconds} seconds')
            trm.race_s()
            startmin += z
            if startmin == 62:
                startmin = 2
        else:
            minutes = datetime.datetime.now().time().minute
            seconds = datetime.datetime.now().time().second
            run.sleep(0.1)
except KeyboardInterrupt:
    sbc.set_brightness(backup_brightness)
