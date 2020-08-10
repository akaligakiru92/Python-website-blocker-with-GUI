from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from datetime import datetime

hostsFile_path = r"C:\Windows\System32\drivers\etc\hosts"
localhost = "127.0.0.1"

def Response():
    result = myText.get()
    displayText.configure(state='normal')
    displayText.insert(END, result + ",")
    displayText.configure(state='disabled')
    User_Input.delete(0,END)

def checkNotEmpty():
    if(sTime=="" or eTime==""):
        return False
    else:
        return True

def blockNow():
    global timeNow
    now = datetime.now()
    timeNow = now.strftime("%H:%M")
    if (checkNotEmpty):
        sTime = start.get()
        eTime = end.get()
        while sTime!= timeNow:
            now = datetime.now()
            timeNow = now.strftime("%H:%M")
        getSiteFromTextAndBlock()
        while eTime!= timeNow:
            now = datetime.now()
            timeNow = now.strftime("%H:%M")
        unblockAll()
    else:
        mb.showwarning(title="None",message ="please fill the empty fields")
def unblockNow():
    global timeNow
    now = datetime.now()
    timeNow = now.strftime("%H:%M")    
    if (checkNotEmpty):
        sTime = start.get()
        eTime = end.get()
        while sTime!= timeNow:
            now = datetime.now()
            timeNow = now.strftime("%H:%M")
        unblockAll()
        while eTime!= timeNow:
            now = datetime.now()
            timeNow = now.strftime("%H:%M")
        getSiteFromTextAndBlock()
    else:
        mb.showwarning(title="None",message ="please fill the empty fields")
    
def getSiteFromTextAndBlock():
    global sites
    sites = [x.strip() for x in displayText.get("1.0",END).split(',')] 
    try:        
        with open(hostsFile_path,"r+") as file:
                content = file.read()
                for site in sites:
                    if site in content:
                        pass
                    else:
                        file.write( "\n" + localhost + " " + site)
                mb.showinfo(title="info",message = "all sites blocked ☺")
    except:
        mb.showinfo(title="Exception",message ="Error (⌣́_⌣̀)  ")
   
def unblockAll():
    with open(hostsFile_path,"r+") as file:
            contents = file.readlines()
            file.seek(0)
            for content in contents:
                if not any(website in content for website in sites):
                    file.write(content)
            file.truncate()
            displayText.configure(state='normal')
            displayText.delete('1.0', END)
            displayText.configure(state='disabled')
            mb.showinfo(title="unblock websites", message="Done ☺")

window = Tk()
window.title("WebSite-Blocker")
window.geometry("400x500")




myText = StringVar()
endText = StringVar()
startText = StringVar()
startLbl= StringVar()
endLbl= StringVar()
window.resizable(False, False)

User_Input = Entry(window, textvariable=myText, width=50)
User_Input.place(x=40, y=370)
start = Entry(window, textvariable=startText, width=5)
start.place(x=120 ,y=340)
end  = Entry(window, textvariable=endText, width=5)
end.place(x=250 ,y=340)
startLabel= Label(window, textvariable=startLbl)
endLabel= Label(window, textvariable=endLbl)
startLbl.set("start time:")
endLbl.set("end time:")
startLabel.place(x=50,y=340)
endLabel.place(x=180,y=340)
startLabel.pack
endLabel.pack



addButton = Button(window, text="Add to list", command=Response, bg="green", height=2, width=10).place(x =250, y=420)
blockButton = Button(window, text="Block site", command=blockNow, bg="red", height=2, width=10, ).place(x =150, y=420)
unblockButton = Button(window, text="Unblock site", command=unblockNow, bg="blue", height=2, width=10).place(x =50, y=420)
displayText = Text(window, height=20, width=40)
displayText.pack()
displayText.configure(state='disabled')

window.mainloop()









