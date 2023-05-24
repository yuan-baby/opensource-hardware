from pymouse import *
from pykeyboard import *

# 判断指令中是否存在特定词语
def check_word(wordbank,string):
    with open(wordbank, 'r', encoding='utf-8') as f:
        words = f.read().splitlines()
    for word in words:
        if word in string:
            return word
    return 'nothing'

# 行动        
def act():
    # 模拟鼠标输入
    m = PyMouse()
    location = m.position()
    m.click(location[0],location[1],button=2,n=1) # 必须要传入鼠标坐标，后两个参数是操作类型和次数

def switch_skills(num): # num是一个数字的字符变量
    # 模拟键盘输入
    keyboard = PyKeyboard()
    keyboard.tap_key(num)