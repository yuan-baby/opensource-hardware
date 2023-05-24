这一部分是坦克大战插件的语音识别部分

请先保证电脑中有anaconda用来创建虚拟环境

```shell
conda create -n play python = 3.7 # 或者将环境命名为你喜欢的名字，pyHook只有python3.7的版本所以要环境需配置为3.7
pip install -r requirements.txt # 安装需要的库
pip install pyHook-1.5.1-cp37-cp37m-win_amd64.whl
```

由于百度语音识别api需要联网运行，游玩时请保持联网

运行main.py开启语音识别模块，按r开始录音2秒（这个录音时间可以在speech.py的第12行改），此后开始攻击