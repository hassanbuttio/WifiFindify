import subprocess
from tkinter import *
import tkinter.messagebox
def getWifi():
   getUser=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split("\n")
   getUser=[a.split(":")[1][1:-1] for a in getUser if "All User Profile" in a]
   for a in getUser:
       results=subprocess.check_output(['netsh','wlan','show','profile',a,'key=clear']).decode('utf-8').split("\n")
       results=[b.split(":")[1][1:-1] for b in results if "Key" in b]
       answer=tkinter.messagebox.askquestion("Wifi Password --| | |--","Wifi Name: "+a+" Password: "+results[0]+"\n"+"Is This Key Working?")
       if answer=='yes':
           print("Thank You")
       elif answer=='no':
           print("Thank You")

getUser=input("Hello User Kindly Press Any Key To Continue.....")
print("Design & Developed By DevGen/DevCom")
root=Tk()
root.title("GetWifi Info")
root.geometry("300x300")
photo=PhotoImage(file="wifi.png")
thePhoto=Label(root,image=photo).pack()
labelinfo=Label(root,text="Wifi Key Finder",font=('arial',25,'bold')).pack()
getKey=Button(root,command=getWifi,text="Get Wifi Key")
getKey.pack()


root.mainloop()