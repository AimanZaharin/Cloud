from tkinter import *
from tkinter import ttk

#Intro Scene
root = Tk()
root.geometry("500x720")
root.title("Muslim Simulator")
#root.resizable(FALSE, FALSE)
point = 0

mainFrame = Frame(root)
mainFrame.pack(fill=BOTH, expand=1)

myCanvas = Canvas(mainFrame)
myCanvas.pack(side=LEFT, fill=BOTH, expand=1)


myScrollbar = ttk.Scrollbar(mainFrame, orient=VERTICAL, command=myCanvas.yview)
myScrollbar.pack(side=RIGHT, fill=Y)

myCanvas.configure(yscrollcommand=myScrollbar.set)
myCanvas.bind("<Configure>", lambda e: myCanvas.configure(scrollregion = myCanvas.bbox("all")))

secondFrame = Frame(myCanvas)

myCanvas.create_window((0,0), window=secondFrame, anchor="nw")

def intro():
    global point
    point = 0
    greet = Label(secondFrame, text="Welcome to Muslim Simulator 2023!")
    introduction = Label(secondFrame, text="In this journey, we will decide whether you're a good Muslim or otherwise." +
                         "\n Be aware that all your choices are meaningful and will decide your fate!", justify=CENTER)

    greet.pack()
    introduction.pack()

def morning():
    temp = 0

    morningGreet = Label(secondFrame, text="\nThis is just another normal day for a Muslim. To start the day you decided to wakeup: ")
    early = Button(secondFrame, text="Early", padx=40, pady=20, command=lambda: goEarly(temp))
    onTime = Button(secondFrame, text="On Time", padx=40, pady=20, command=lambda: goOnTime(temp))
    late = Button(secondFrame, text="Late", padx=40, pady=20, command=lambda: goLate())

    morningGreet.pack()
    early.pack()
    onTime.pack()
    late.pack()

def goEarly(temp):
    earlyGreet = Label(secondFrame ,text="\n\n[4:30AM]\nGreat! You decided to wake up early.\nDo you want to "
                  + "perform tahajjud prayer ? or do you want to go back to sleep ?")
    tahajjud = Button(secondFrame, text="Tahajjud", padx=40, pady=20, command=lambda: goTahajjud(temp))
    sleep = Button(secondFrame, text="Sleep", padx=40, pady=20, command=lambda: goOnTime(temp))

    earlyGreet.pack()
    tahajjud.pack()
    sleep.pack()


def goTahajjud(temp):
    global point
    point += 1
    temp = 1
    goOnTime(temp)
    
def goOnTime(temp):
    if temp == 0:
        onTimeGreet = Label(secondFrame, text="\n\n[6:00AM]\nGood! You decided to wake up on time. \nDo you want to perform Subuh" +
                  " prayer ? or do you want to go back to sleep ?")
    
    else:
        onTimeGreet = Label(secondFrame, text="\n\n[6:00AM]\nGood! Do you want to perform Subuh" +
                  " prayer ?\nor do you want to go back to sleep ?")
    
    subuh = Button(secondFrame, text="Subuh", padx=40, pady=20, command=lambda: goAfternoon())
    sleep = Button(secondFrame, text="Sleep", padx=40, pady=20, command=lambda: goSleep())

    onTimeGreet.pack()
    subuh.pack()
    sleep.pack()

def goSleep():
    global point
    point -= 1
    goLate()

def goLate():
    lateGreet = Label(secondFrame, text="\n\n[7:30AM]\nAstaghfirullahalazim... You woke up late and did not perform Subuh prayer." +
          "\nDo you want to peform Qada' prayer ?")
    yesQada = Button(secondFrame, text="Yes", padx=40, pady=20, command=lambda: goQada(1))
    noQada = Button(secondFrame, text="No", padx=40, pady=20, command=lambda: goQada(2))

    lateGreet.pack()
    yesQada.pack()
    noQada.pack()

def goQada(qada):
    global point

    if qada == 1:
        point += 1
        goAfternoon()

    else:
        point -= 1
        goAfternoon()
    
def goAfternoon():
    afternoonGreet = Label(secondFrame, text="\n\n[12:00PM]\nYou walk into the office and see your co-workers gossiping about the boss" +
                           "\nwhat are you going to do?")
    yesRant = Button(secondFrame, text = "Join", padx=40, pady=20, command=lambda: goRant(1))
    noRant = Button(secondFrame, text = "Walk\nAway", padx=40, pady=12, command=lambda: goRant(2))
    
    afternoonGreet.pack()
    yesRant.pack()
    noRant.pack()

def goRant(rant):
    global point
    
    if rant == 1:
        point -= 1
        goAzan()
    
    else:
        point += 1
        goAzan()

def goAzan():
    azanGreet = Label(secondFrame, text="\n\n[1:12PM]\nYou were in the middle of presentating your monthly report to your boss." +
                      "\nThen you heard the Zuhr call of prayer (Adzan)." +
                      "\nDo you want to continue with the presentation or respect the call of prayer?")
    noRespect = Button(secondFrame, text="Continue\nMeeting", padx=30, pady=20, command=lambda: goRespect())
    respect = Button(secondFrame, text="Respect\nAdzan", padx=30, pady=20, command=lambda: goRespect())

    azanGreet.pack()
    noRespect.pack()
    respect.pack()

def goRespect():
    global point

    point += 1
    goFlirting()

def goFlirting():
    flirtingGreet = Label(secondFrame, text="\n\n[6:00PM]\nYou arrived home from work." +
                          "\nWhile you were in the porch, your widowed neighbour next door greet you with a lustful intent." +
                          "\nShe then invite you to come into her house, what's your decision?")
    acceptFlirt = Button(secondFrame, text="accept", padx=40, pady=20, command=lambda: goImaan(1))
    declineFlirt = Button(secondFrame, text="decline", padx=40, pady=20, command=lambda: goImaan(2))

    flirtingGreet.pack()
    acceptFlirt.pack()
    declineFlirt.pack()

def goImaan(imaan):
    global point

    if imaan == 1:
        point -= 1
        goNight()
    
    else:
        point += 1
        goNight()

def goNight():
    nightGreet = Label(secondFrame, text="\n\n[7:00PM]\nIt is the end of the day, you are tired but still have obligations as a muslim." +
                       "\nFor Maghrib, will you be going to the mosque?")
    prayMosque = Button(secondFrame, text="Pray at\nMosque", padx=30, pady=20, command=lambda: goMosque(1))
    prayHome = Button(secondFrame, text="Pray at\nHome", padx=30, pady=20, command=lambda: goMosque(2))

    nightGreet.pack()
    prayMosque.pack()
    prayHome.pack()

def goMosque(mosque):
    global point
    
    if mosque == 1:
        point += 1

    else:
        point -= 0

intro()
morning()

root.mainloop()