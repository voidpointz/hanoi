import pygame
import os
from PyQt5.QtCore import QThread


class Bgm(QThread):

    def __init__(self):
        super().__init__()

    def run(self):
        # 线程相关代码
        def bgm():
            pygame.mixer.init()
            bgm_assert = "A Little Story.mp3"
            # bgm_assert = "resource" + os.sep + "Serenity.mp3"
            pygame.mixer.music.load(bgm_assert)
            while True:
                #检查音乐流播放，有返回True，没有返回False
                #如果没有音乐流则选择播放
                if pygame.mixer.music.get_busy()==False:
                    pygame.mixer.music.play()
        bgm()
# 创建一个新的线程

