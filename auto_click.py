import pyautogui as pg
import sys, time

def print_pos():
    """マウスのポジョン出力する
    """
    pg.PAUSE = 1
    pg.FAILSAFE = True
    while True:
        x, y = pg.position()
        print(str(x) + "," + str(y))

def test():
    i = 0
    while True:
        print(str(i))
        i += 1
        time.sleep(1)

def main():
    pg.PAUSE = 60
    pg.FAILSAFE = True
    while True: pg.click(1032, 543)

if __name__ == "__main__":
    try: main()
    except Exception as e: print(e)
    print("END")