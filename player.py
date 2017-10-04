import tkinter as tk
import tkinter.messagebox
import urllib.request
import json
import os
import threading
import time
root= tk.Tk()
root.title("my fist project")
root.geometry('300x200+200+200')
entry=tk.Entry(root)
entry.pack()
def music():
    text=entry.get()
    text=urllib.request.quote(text)
    if not text:
        tkinter.messagebox.showinfo(title='温馨提示',message='您可以输入以下内容进行搜索:\n1,歌手名\n2,歌曲名\n3,部分歌词')
    else:
        html=urllib.request.urlopen("http://s.music.163.com/search/get/?type=1&s=%s&limit=9"%text).read()
        html=html.decode("utf-8")
        texts=json.loads(html)
        list_s=texts["result"]["songs"]
        global m_list
        m_list=[]

        listbox.delete(0,listbox.size())
        for i in range(len(list_s)):
            listbox.insert(i,list_s[i]['album']['name']+"("+list_s[i]['artists'][0]['name']+')')
            m_list.append(list_s[i]['audio'])

var=tk.StringVar()
def play():
    sy=listbox.curselection()[0]
    urllib.request.urlretrieve(m_list[sy],'2.mp3')
    os.system('2.mp3')
    time.sleep(10)

def th(event):
    t=threading.Thread(target=play)
    t.start()
tk.Button(root,text='搜索歌曲',command=music).pack()
listbox=tk.Listbox(root,width=50,listvariable=var)
listbox.bind('<Double-Button-1>',th)
listbox.pack()
tk.mainloop()
