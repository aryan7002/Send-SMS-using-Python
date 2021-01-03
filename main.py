#imprt module requests using pip install
#you also need a sms provider i have use fast2sms
#you need to genrate an api authencation key in sms provider
#you also need an tkinter module
import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo,showerror

def send_sms(number,message):
    url='https://www.fast2sms.com/dev/bulk'
    params={
        'authorization':' ',#your api key here
        'sender_id':'FSTSMS',#it is given by an sms provider
        'message':message,
        'language':'english',
        'route':'p',#p for promational and t for transctional
        'numbers':number
    }
    response=requests.get(url,params=params)
    dic=response.json()
    print(dic)
    return dic.get('return')

def btn_click():
    num=textNumber.get()
    msg=textMsg.get("1.0",END)
    r=send_sms(num,msg)
    if r== True:
        showinfo("Send Success","Successfully Sent")
    else:
        showerror("Error","Something Went Wrong!")


#creating Gui
top=Tk()
top.title("Message Sender")
top.geometry("400x550")
font=("Helvetica",22,"bold")
lable=Label(top,text="Enter phone number",font=("Helvetica",18))
lable.pack()

textNumber=Entry(top,font=font)
textNumber.pack(fill=X,pady=20)

lable2=Label(top,text="Enter your message",font=("Helvetica",18))
lable2.pack()

textMsg=Text(top)
textMsg.pack(fill=X)

sendBtn=Button(top,text="SEND SMS",command=btn_click)
sendBtn.pack()

top.mainloop()
