import cv2
import mediapipe as mp
from math import sqrt
import time
import numpy as np
import mcpi.minecraft as minecraft
import pynput


mc=minecraft.Minecraft.create("172.18.208.1",4711) # ip地址
playerId = mc.getPlayerEntityId("yuan") # 玩家名称
print(playerId)
pos=mc.entity.getPos(playerId)
print(pos)

cap = cv2.VideoCapture(0)

ret=cap.set(3,1092)
ret=cap.set(4,1080)
a=cap.get(3)
b=cap.get(4)
print(a,b)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
ctr1 = pynput.mouse.Controller()
ctr2 = pynput.keyboard.Controller()


def getDis(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


x4, y4 = x8, y8 = x10, y10=x5, y5=x12, y12= 0, 0

while True:
    img = cv2.flip(cap.read()[1], 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    pos = mc.entity.getTilePos(playerId)
#界面操作设置
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.rectangle(img,(0,180),(540,360),(0,255,255),3)
                cv2.rectangle(img,(180,0),(360,540),(0,255,255),3)
                if id == 4:
                    x4, y4 = cx, cy
                    #print(x4,y4)
                if id == 8:
                    x8, y8 = cx, cy
                if id == 5:
                    x5, y5 = cx, cy
                if id == 12:
                    x12, y12 = cx, cy
                if id == 10:
                    x10, y10 = cx, cy
                if x10 > 360 and y10 > 180 and y10 < 360 and x10 < 540:
                    #mc.player.setPos(pos.x + 1, pos.y, pos.z)
                    ctr2.press('d')
                    ctr2.release('d')
                    print("右")
                if x10 < 180 and y10 > 180 and y10 < 360:
                    #mc.player.setPos(pos.x - 1, pos.y, pos.z)
                    ctr2.press('a')
                    ctr2.release('a')
                    print("左")
                if x10 > 180 and y10 < 180 and x10 < 360:
                    #mc.player.setPos(pos.x, pos.y, pos.z - 1)
                    ctr2.press('w')
                    ctr2.release('w')
                    print("前")
                if x10 > 180 and y10 > 360 and x10 < 360:
                    #mc.player.setPos(pos.x, pos.y, pos.z + 1)
                    ctr2.press('s')
                    ctr2.release('s')
                    print("后")
                if x5 > 540 and x5 < 680:
                    ctr1.move(-1,0)
                if x5 > 820 and x5 < 960:
                    ctr1.move(1,0)

                if getDis(x5, y5, x12, y12)<=25:
                    ctr1.click(pynput.mouse.Button.right)

                cv2.putText(img, str(int(id)), (cx + 10, cy + 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
            cv2.line(img, (x4, y4), (x8, y8), (100, 100, 200), 2)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    cv2.imshow("image", img)
    if cv2.waitKey(2) & 0xFF == 27:
        break

cap.release()

