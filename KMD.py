import urllib.request
import json
import sys
from sys import exit
from ui_kuwo import Ui_kuwo
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import random
import os
import traceback
import request

with open("Save.json","r") as f:
    SaveXX = json.loads(f.read())

def main(url,self):
    global SaveXX
    try:
        rid = str(url.split("/")[-1])
        self.progressBar.setValue(14)
        if True:
            json_text = urllib.request.urlopen("http://www.kuwo.cn/url?format=mp3&rid=%s&response=url&type=convert_url3&br=128kmp3&from=web&t=1611321054772&httpsStatus=1&reqId=4265a0b0-5cb3-11eb-8d35-9939327ef0bf"   %   rid)   .read()  .decode()
            self.progressBar.setValue(28)
            j = json.loads(json_text)
            self.progressBar.setValue(42)
            req = request.get(f"http://m.kuwo.cn/newh5/singles/songinfoandlrc?musicId={rid}&httpsStatus=1&reqId=4dfb9620-9aaf-11eb-988c-d7dfa60cda35")
            J = json.loads(req.text)
            if SaveXX["FileName_Mode"] == 0:
                if SaveXX["Path"] == 0:
                    try:
                        with open(str(J['data']['lrclist'][0]["lineLyric"]+".mp3"),"wb") as f:
                            self.progressBar.setValue(56)
                            music_file_r = urllib.request.urlopen(j["url"])
                            self.progressBar.setValue(70)
                            music = music_file_r.read()
                            self.progressBar.setValue(84)
                            f.write(music)
                    except:
                        with open(str(str(rid)+".mp3"),"wb") as f:
                            self.progressBar.setValue(56)
                            music_file_r = urllib.request.urlopen(j["url"])
                            self.progressBar.setValue(70)
                            music = music_file_r.read()
                            self.progressBar.setValue(84)
                            f.write(music)
                        self.progressBar.setValue(100)
                else:
                    try:
                        with open(str(SaveXX["Path"])+str(J['data']['lrclist'][0]["lineLyric"]+".mp3"),"wb") as f:
                            self.progressBar.setValue(56)
                            music_file_r = urllib.request.urlopen(j["url"])
                            self.progressBar.setValue(70)
                            music = music_file_r.read()
                            self.progressBar.setValue(84)
                            f.write(music)
                    except:
                        with open(str(SaveXX["Path"])+str(str(rid)+".mp3"),"wb") as f:
                            self.progressBar.setValue(56)
                            music_file_r = urllib.request.urlopen(j["url"])
                            self.progressBar.setValue(70)
                            music = music_file_r.read()
                            self.progressBar.setValue(84)
                            f.write(music)
                        self.progressBar.setValue(100)
            elif SaveXX["FileName_Mode"] == 1:
                if SaveXX["Path"] == 0:
                   if True:
                        with open(str(str(rid)+".mp3"),"wb") as f:
                            self.progressBar.setValue(56)
                            music_file_r = urllib.request.urlopen(j["url"])
                            self.progressBar.setValue(70)
                            music = music_file_r.read()
                            self.progressBar.setValue(84)
                            f.write(music)
                        self.progressBar.setValue(100)
                else:
                    if True:
                        with open(str(SaveXX["Path"])+str(str(rid)+".mp3"),"wb") as f:
                            self.progressBar.setValue(56)
                            music_file_r = urllib.request.urlopen(j["url"])
                            self.progressBar.setValue(70)
                            music = music_file_r.read()
                            self.progressBar.setValue(84)
                            f.write(music)
                        self.progressBar.setValue(100)
            elif SaveXX["FileName_Mode"] == 2:
                if SaveXX["Path"] == 0:
                    try:
                        with open(str(J['data']['lrclist'][0]["lineLyric"]+".mp3"),"wb") as f:
                            self.progressBar.setValue(56)
                            music_file_r = urllib.request.urlopen(j["url"])
                            self.progressBar.setValue(70)
                            music = music_file_r.read()
                            self.progressBar.setValue(84)
                            f.write(music)
                    except:
                        self.progressBar.setValue(100)
                else:
                    try:
                        with open(str(SaveXX["Path"])+str(J['data']['lrclist'][0]["lineLyric"]+".mp3"),"wb") as f:
                            self.progressBar.setValue(56)
                            music_file_r = urllib.request.urlopen(j["url"])
                            self.progressBar.setValue(70)
                            music = music_file_r.read()
                            self.progressBar.setValue(84)
                            f.write(music)
                    except:
                        self.progressBar.setValue(100)
            else:
                pass
        return True
    except:
         e=traceback.format_exc()
         QMessageBox.critical(self, "内部错误", e)

class Demo(QMainWindow, Ui_kuwo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)                                          # 1
        ###开始绑定事件###
        self.OkButton.clicked.connect(self.fOkButton) #提交音乐URL | 按钮
        self.actionAbout_Us.triggered.connect(self.factionAbout_Us) #About Us | 菜单栏
        self.actionHome.triggered.connect(self.factionHome) #Home | 菜单栏
        ###结束绑定事件###
        self.show()
    def fOkButton(self):
        text=self.UrlEnit.text()  #点击“提交音乐URL“按钮触发
        print("提交音乐URL")
        self.progressBar.setValue(0)
        if main(text,self):
            QMessageBox.information(self, "提示", "音乐下载完成") 
    def factionAbout_Us(self):
        self.title="About"  #点击“About Us“菜单栏触发
        self.index="关于Kuwo Music Downloader\n版本：V 2.2\n制作：小邓学编程、熊熊糖果\n出品：Miner工作室\nHome: www.minerstudio.xyz\n*本软件仅供学习和测试用途"
        QMessageBox.about(self, self.title, self.index)
    def factionHome(self):
        os.system("start www.minerstudio.xyz") #点击“Home“菜单栏触发

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Demo()
    sys.exit(app.exec_())
