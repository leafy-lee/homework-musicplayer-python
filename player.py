import requests
import os
import json
from tkinter.ttk import *
from tkinter import *
import tkinter.messagebox as mb
import urllib.request
import pygame
from tkinter import scrolledtext
from PIL import Image,ImageTk
import tkinter.font as tkFont
from numpy import *
import wx
import wx.html2
import random
#2806848825
sid=[]
mp3_name=[]
songers=[]
class MyBrowser(wx.Dialog):
    def __init__(self,*args,**kwds):
        wx.Dialog.__init__(self,*args,**kwds)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.browser = wx.html2.WebView.New(self)
        sizer.Add(self.browser,1,wx.EXPAND,10)
        self.SetSizer(sizer)
        self.SetSize((350,500))

def main():
    ass = 1
    def playit(lb,data):
        which=lb.curselection()[0]
        playitt(which = which,data = data)
    def playitt(which,data):
        k=0
        #上层界面
        top1 = Toplevel()
        top1.geometry('600x500')
        picurl = data[which]['album']['picUrl']
        r = requests.get(picurl)
        #path1 = 'D:\hanpididi\\' + str(which)+'.jpg'
        path1 =  str(which)+'.jpg'
        with open(path1,'wb') as f:
            f.write(r.content)
            f.close()
        global imgg 
        im=Image.open(str(which)+".jpg")
        img=im.resize((100,100),Image.ANTIALIAS)
        imgg=ImageTk.PhotoImage(img)
        imLabel=Label(top1,image=imgg)
        imLabel.place(x=20,y=10)
        pr = 0
        key = sid[which]
        mp3_namei,songeri=mp3_name[which],songers[which]
        urll = 'http://music.163.com/song/media/outer/url?id=%d.mp3'%key
        ho=mp3_namei+"-"+songeri
        top1.title(str(ho))
        def paly(event):
            nonlocal k
            nonlocal pr
            if not k%2:
                pimLabel1.place_forget()
                pimLabel.place(x =76, y =446)
                pygame.mixer.music.pause()
                '''stop = time.time()
                p=0
                p += stop - play
                pr = p/tim'''
                k+=1
                #print('b')
            else:
                #print(pr)
                pimLabel.place_forget()
                pimLabel1.place(x = 76, y =446)
                pygame.mixer.music.unpause()
                #play = time.time()
                #print('a')
                k+=1

        global pimgg1
        global pimgg2      
        global pimgg3
        global pimgg4
        global pimgg

        

        def next(event):
            nonlocal ass
            global gedan
            nonlocal path11
            top1.destroy()
            playitt((which+1)%len(sid),data = gedan)
            pygame.mixer.music.queue(path11)
        
        def last(event):
            nonlocal ass
            global gedan
            nonlocal path11
            top1.destroy()
            playitt((which-1)%len(sid),data = gedan)
            pygame.mixer.music.queue(path11)

        def voicecontrol(text):
            pygame.mixer.music.set_volume(int(scale1.get())/100)
            

        typ = 0
        
        def choosetype(event):
            global gedan
            nonlocal pimLabel4
            pimLabel4.place_forget()
            nonlocal typ
            nonlocal ass
            a = ['sing','randome','round']
            print(typ)
            if typ == 1:
                    pim5=Image.open("randome.png")
                    pimg5=pim5.resize((24,24),Image.ANTIALIAS)
                    pimgg5=ImageTk.PhotoImage(pimg5)
                    pimLabel5=Label(top1,image=pimgg5)
                    pimLabel5.bind("<Button-1>",choosetype)
                    pimLabel5.place(x = 0, y =452)
                    ass = random.randint(0,10)
            elif typ == 2:
                    pim5=Image.open("randome.png")
                    pimg5=pim5.resize((24,24),Image.ANTIALIAS)
                    pimgg5=ImageTk.PhotoImage(pimg5)
                    pimLabel5=Label(top1,image=pimgg5)
                    pimLabel5.bind("<Button-1>",choosetype)
                    pimLabel5.place(x = 0, y =452)
                    ass = 0
            else:
                    pim5=Image.open("randome.png")
                    pimg5=pim5.resize((24,24),Image.ANTIALIAS)
                    pimgg5=ImageTk.PhotoImage(pimg5)
                    pimLabel5=Label(top1,image=pimgg5)
                    pimLabel5.bind("<Button-1>",choosetype)
                    pimLabel5.place(x = 0, y =452)
                    ass = 1
            typ= (typ+1)%3
                
        pim=Image.open("play.png")
        pimg=pim.resize((36,36),Image.ANTIALIAS)
        pimgg=ImageTk.PhotoImage(pimg)
        pimLabel=Label(top1,image=pimgg)
        pimLabel.bind("<Button-1>",paly)

        pim1=Image.open("pause.png")
        pimg1=pim1.resize((36,36),Image.ANTIALIAS)
        pimgg1=ImageTk.PhotoImage(pimg1)
        pimLabel1=Label(top1,image=pimgg1)
        pimLabel1.place(x = 76, y =446)
        pimLabel1.bind("<Button-1>",paly)

        pim2=Image.open("next.png")
        pimg2=pim2.resize((24,24),Image.ANTIALIAS)
        pimgg2=ImageTk.PhotoImage(pimg2)
        pimLabel2=Label(top1,image=pimgg2)
        pimLabel2.place(x = 114, y =452 )
        pimLabel2.bind("<Button-1>",next)

        pim3=Image.open("last.png")
        pimg3=pim3.resize((24,24),Image.ANTIALIAS)
        pimgg3=ImageTk.PhotoImage(pimg3)
        pimLabel3=Label(top1,image=pimgg3)
        pimLabel3.place(x = 50, y =452 )
        pimLabel3.bind("<Button-1>",last)

        pim4=Image.open("round.png")
        pimg4=pim4.resize((24,24),Image.ANTIALIAS)
        pimgg4=ImageTk.PhotoImage(pimg4)
        pimLabel4=Label(top1,image=pimgg4)
        pimLabel4.place(x = 0, y =452)
        pimLabel4.bind("<Button-1>",choosetype)

        pim5=Image.open("volume.png")
        pimg5=pim5.resize((20,20),Image.ANTIALIAS)
        pimgg5=ImageTk.PhotoImage(pimg5)
        pimLabel5=Label(top1,image=pimgg5)
        pimLabel5.place(x = 450, y = 460)

        # variable = v #绑定变量
        v=IntVar()
        scale1 = Scale(top1,from_=0,to=100,resolution=1,orient=HORIZONTAL,variable=v,command = voicecontrol)
        scale1.place(x = 480, y=440)
        v.set(50)


        kk =Listbox(top1,width=40,height=14)
        bar1 = Scrollbar(kk)
        bar1.pack(side=RIGHT,fill=Y)
        bar1.config(command=kk.yview)
        kk.place(x=20,y=120,relwidth=0.9,relheight=0.6)
        #获取热评
        
        getcomment(key,kk,top1)

        #添加水平滚动条
        
        bar = Scrollbar(kk,orient=HORIZONTAL)
        bar.pack(side=BOTTOM,fill=X)
        bar.config(command=kk.xview)
        def progressit(text):
            '''global badgirl
            nonlocal which
            if pygame.mixer.music.get_busy():
                pygame.mixer.init()
                ratio = scale2.get()
                timy = badgirl[4][which]
                pygame.mixer.music.rewind()
                pygame.mixer.music.set_pos(ratio*timy)'''
        v=DoubleVar()
        scale2 = Scale(top1,from_=0,to=1,resolution=0.01,orient=HORIZONTAL,variable=v,length= 300,command = progressit)
        scale2.place(x = 140, y=440)

        

        #path = 'D:\hanpididi\\' + ho+ '.mp3'
        path = ho+ '.mp3'
        if not os.path.exists(path):
                r = requests.get(urll)
                with open(path,'wb') as f:
                    f.write(r.content)
                    f.close()
        sm = "{}.mp3".format(ho)  
        pygame.init()
        pygame.mixer.init()
        q=pygame.mixer.music.load(sm)
        pygame.mixer.music.play()
        
        def ha():
            global badgirl
            timy = badgirl[4][which]
            gan = int(timy/100)
            if pygame.mixer.music.get_busy():
                scale2.set(pygame.mixer.music.get_pos()/timy)
            else:
                scale2.set(0)
            print(pygame.mixer.music.get_pos(),'saf')
            top.after(gan,ha)
        global badgirl
        timy = badgirl[4][which]
        gan = int(timy/100)
        top1.after(gan,ha)
        top1.mainloop()

        print(pygame.mixer.music.get_pos())
        nonlocal ass
        key1 = sid[which+ass]
        mp3_name1,songer1=mp3_name[which+ass],songers[which+ass]
        urll = 'http://music.163.com/song/media/outer/url?id=%d.mp3'%key1
        ho1=mp3_name1+"-"+songer1
        #path = 'D:\hanpididi\\' + ho+ '.mp3'
        path11 = ho1+ '.mp3'
        if not os.path.exists(path11):
                r = requests.get(urll)
                with open(path11,'wb') as f:
                    f.write(r.content)
                    f.close()
        pygame.mixer.music.queue(path11)
        pygame.mixer.music.set_volume(0.5)
        #play = time.time()
        
        print(pygame.mixer.music.get_pos())
        
        
        print(pygame.mixer.music.get_pos())
        #图片





        
    top = Tk()
    top.geometry('400x250')
    top.resizable(0,0)
    
    so=Text(top,width=25, height=1)
    so.place(x=70,y=105)
    button=ttk.Button(top,text="搜  索",command=lambda:hey(top))
    button.place(x=260,y=100)



    #取得歌曲的信息(名字，MP3地址)
    def hey(top1):
        #try:

        #清理文本框
        
        ido = so.get(1.0,END)

        #新建窗口
        top = Toplevel()
        top.geometry('800x600')
        top.resizable(0,0)

        #新建listbox
        a =Listbox(top,width=40,height=14,selectmode = EXTENDED)
        bar1 = Scrollbar(a)
        bar1.pack(side=RIGHT,fill=Y)
        a.bind("<Double-Button-1>", lambda event:playit(lb = a , data = gedan))
        bar1.config(command=a.yview)
        a.config(yscrollcommand=bar1.set)
        a.place(x=40,y=180,relwidth=0.9,relheight=0.6)
        a.delete(0,END)

        def down(lb):
            down = Toplevel()
            down.geometry('350x250')
            down.resizable(0,0)

            s=lb.curselection()
            print(s)

            com=Text(down,width=25, height=1)
            com.insert(INSERT,'请输入下载路径')
            com.place(x=70,y=105)
            com1=Text(down,width=25, height=1)
            com1.insert(INSERT,'起个名字？用空格隔开每个名字')
            com1.place(x=70,y=145)
            button=ttk.Button(down,text="完成啦",command=lambda:downd())
            button.place(x=260,y=100)
            def downd():
                comd = com.get(1.0,END)
                comd=comd[:-1]
                comd1 = com1.get(1.0,END)
                comd1=comd1[:-1]
                comd1= comd1.split()
                
                for i in s:
                  global mp3_name
                  global songers
                  global sid
                  print(i)
                  #try:
                  print(i)
                  path1 = comd + comd1[i]+'.mp3'
                  print(path1)
                  kfc = sid[i]
                  print(kfc)
                  url = 'http://music.163.com/song/media/outer/url?id=%d.mp3'%kfc
                  if not os.path.exists(comd):
                        os.mkdir(comd)
                  if not os.path.exists(path1):
                        r = requests.get(url)
                        with open(path1,'wb') as f:
                              f.write(r.content)
                              f.close()
                              print('下载好了')
                  else:
                        print('文件已存在')
                  #except:
                  #  mb.showinfo('似乎下载错地方了呢','啊呀，好像出错了了\n你再看看路?')
        def cost():
            app = wx.App()
            dialog = MyBrowser(None,-1)
            dialog.browser.LoadURL("https://music.163.com/style/swf/widget.swf?sid=%s&type=0&auto=1&width=310&height=430" %ido)
            dialog.Show()
        b = Button(top,text = '下载',command=lambda:down(lb = a))
        b.pack(side = BOTTOM)
        c = Button(top,text = '想要个更好看的版本',command=lambda:cost())
        c.pack(side = BOTTOM)

        
        #设定变量
        global sid
        iddd=[]
        global mp3_name
        global songers
        global gedan
        global badgirl

        #获取歌单信息
        api="http://music.163.com/api/playlist/detail?id=%s"%ido
        response=requests.get(api)
        data=response.text
        data=json.loads(data)
        gedan=data['result']['tracks']
        for i in range(len(data['result']['tracks'])):
            mp3_name.append(gedan[i]['name'])
            sid.append(gedan[i]['id'])
            songer=''
            for j in range(len(gedan[i]['artists'])):
                songer+='/'+gedan[i]['artists'][j]['name']
            album = gedan[i]['album']['name']
            songers.append(songer[1:])
            time1 = int(gedan[i]['bMusic']['playTime'])//1000
            sfkd = int(time1//60)
            b = int(time1%60) if len(str(int(time1%60))) >1 else '0' + str(int(time1%60))
            timee= str(sfkd)+':'+str(b)
            redu = gedan[i]['popularity']
            ge=mp3_name[i]+" "*(35-2*len(mp3_name[i]))+songers[i]+" "*(35-2*len(songers[i]))+album+" "*(35-2*len(album))+timee+" "*(35-2*len(timee))+str(redu)
            a.insert(i+1,str(ge)+'\n')
            badgirl[0].append(gedan[i]['name'])
            badgirl[1].append(songer[1:])
            badgirl[2].append(album)
            badgirl[3].append(redu)
            badgirl[4].append(int(gedan[i]['bMusic']['playTime']))

       # 歌单封面
        picurl = data['result']['coverImgUrl']
        r = requests.get(picurl)
        #path1 = 'D:\hanpididi\\' + str(ido)[:-1] +'.jpg'
        path1 = str(ido)[:-1] +'.jpg'
        with open(path1,'wb') as f:
            f.write(r.content)
            f.close()
        global imgg 
        im=Image.open(str(ido)[:-1]+".jpg")
        img=im.resize((128,128),Image.ANTIALIAS)
        imgg=ImageTk.PhotoImage(img)
        imLabel=Label(top,image=imgg)
        imLabel.place(x=40,y=30)

        #歌单描述
        desc=data['result']['description']
        lab =scrolledtext.ScrolledText(top,width=70,height=8,wrap=WORD)
        lab.insert(1.0,desc)
        lab.place(x = 200,y = 30)
        #except:
        #   mb.showinfo('似乎走错路了呢','啊呀，好像走错了\n你再找找路?')
        
    #实现热评
    def getcomment(idd,s,a):
        scomment='http://music.163.com/api/v1/resource/comments/R_SO_4_%s?limit=20&offset=0'%idd
        response=requests.get(scomment)
        commen=response.text
        comment=json.loads(commen)['hotComments']
        la = Label(a,text='热门评论')
        for i in range(len(comment)):
            s.insert(i+1,str(comment[i]['content']+'\n'))


#欢迎界面

start = Tk()
start.geometry('600x450')
start.title('绿绮万壑松')
start.update()
start.resizable(0, 0)

song = tkFont.Font(family = 'simsunnsimsun', size = 14)
img_1 = PhotoImage(file = 'sss.png')
label_start = Label(start,
                   width = 300,
                   image = img_1)
label_start.place(x = 300, y = 0, width = 300, height = 450)
label_back = Label(start,
                   bg = '#3e4145')
label_back.place(x = 0, y = 0, width = 300, height = 450)
label_c = Label(start,
                text = '客心洗流水，余响入霜钟。\n\n\n欢迎来到音乐的殿堂  ',
                bg = '#3e4145',
                fg = 'white',
                font = song,
                justify = CENTER)
label_c.place(x = 40, y = 90)
button=ttk.Button(start,text='开启一段旅程',command=main,width = 30)
button.place(x = 40, y = 290)


badgirl=[[] for i in range(5)]
