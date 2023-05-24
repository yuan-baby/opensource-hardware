import keyboard
import speech
import action
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create("172.18.208.1",4711)
while True:
    keyboard.wait('r') # 按下R键开始录制
    speech.record_sound()
    command = speech.recogize_speech() # 识别语音指令
    mc.postToChat(command)

    # 将指令中的关键词提取出来 
    attack = action.check_word('skills.txt',command)

    if attack == "普通炮弹":
        action.switch_skills('1')
        action.act()
        print(attack)
    elif attack == "追踪炮弹":
        action.switch_skills('2')
        action.act()
        print(attack)
    elif attack == "爆裂炮弹":
        action.switch_skills('3')
        action.act()
        print(attack)
    elif attack == "超级炮弹":
        action.switch_skills('4')
        action.act()
        print(attack)
    elif attack == "三重炮弹":
        action.switch_skills('5')
        action.act()
        print(attack)
    elif attack == "地雷":
        action.switch_skills('6')
        action.act()
        print(attack)
    elif attack == "遥控地雷":
        action.switch_skills('7')
        action.act()
        print(attack)
    elif attack == "超声冲击":
        action.switch_skills('8')
        action.act()
        print(attack)
    elif attack == "坦克突击":
        action.switch_skills('9')
        action.act()
        print(attack)
