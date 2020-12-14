import pyautogui as pg

def chk_pos():
    pg.PAUSE = 1
    pg.FAILSAFE = True
    while True:
        x, y = pg.position()
        print(str(x) + "," + str(y))


def main():
    pg.PAUSE = 1
    pg.FAILSAFE = True
    while True: pg.click(1032, 543)

if __name__ == "__main__":
    try: main()
    except: print("終了")