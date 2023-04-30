from tkinter import *
from tkinter import ttk

#Intro Scene
root = Tk()
root.geometry("500x1080")
root.title("Muslim Simulator")
point = 0

def intro():
    global point
    point = 0
    greet = Label(root, text="Welcome to Muslim Simulator 2023!")
    introduction = Label(root, text="In this journey, we will decide whether you're a good Muslim or otherwise." +
                         "\n Be aware that all your choices are meaningful and will decide your fate!", justify=CENTER)

    greet.grid(column=1,row=0)
    introduction.grid(columnspan=3, row=1)

def morning():
    temp = 0

    morningGreet = Label(root, text="\nThis is just another normal day for a Muslim. To start the day you decided to wakeup: ")
    early = Button(root, text="Early", padx=20, pady=10, command=lambda: goEarly(temp))
    onTime = Button(root, text="On Time", padx=20, pady=10, command=lambda: goOnTime(temp))
    late = Button(root, text="Late", padx=20, pady=10, command=lambda: goLate())

    morningGreet.grid(columnspan=3, row=2)
    early.grid(column=0,row=3)
    onTime.grid(column=1, row=3)
    late.grid(column=2, row=3)

def goEarly(temp):
    earlyGreet = Label(root ,text="\n\n[4:30AM]\nGreat! You decided to wake up early.\nDo you want to "
                  + "perform tahajjud prayer ? or do you want to go back to sleep ?")
    tahajjud = Button(root, text="Tahajjud", padx=20, pady=10, command=lambda: goTahajjud(temp))
    sleep = Button(root, text="Sleep", padx=20, pady=10, command=lambda: goOnTime(temp))

    earlyGreet.grid(columnspan=3, row=4)
    tahajjud.grid(column=0, columnspan=2, row=5)
    sleep.grid(column=1, columnspan=2, row=5)


def goTahajjud(temp):
    global point
    point += 1
    temp = 1
    goOnTime(temp)
    
def goOnTime(temp):
    if temp == 0:
        onTimeGreet = Label(root, text="\n\n[6:00AM]\nGood! You decided to wake up on time. \nDo you want to perform Subuh" +
                  " prayer ? or do you want to go back to sleep ?")
    
    else:
        onTimeGreet = Label(root, text="\n\n[6:00AM]\nGood! Do you want to perform Subuh" +
                  " prayer ?\nor do you want to go back to sleep ?")
    
    subuh = Button(root, text="Subuh", padx=20, pady=10, command=lambda: goAfternoon())
    sleep = Button(root, text="Sleep", padx=20, pady=10, command=lambda: goSleep())

    onTimeGreet.grid(columnspan=3, row=6)
    subuh.grid(column=0, columnspan=2, row=7)
    sleep.grid(column=1, columnspan=2, row=7)

def goSleep():
    global point
    point -= 1
    goLate()

def goLate():
    lateGreet = Label(root, text="\n\n[7:30AM]\nAstaghfirullahalazim... You woke up late and did not perform Subuh prayer." +
          "\nDo you want to peform Qada' prayer ?")
    yesQada = Button(root, text="Yes", padx=20, pady=10, command=lambda: goQada(1))
    noQada = Button(root, text="No", padx=20, pady=10, command=lambda: goQada(2))

    lateGreet.grid(columnspan=3, row=8)
    yesQada.grid(column=0, columnspan=2, row=9)
    noQada.grid(column=1, columnspan=2, row=9)

def goQada(qada):
    global point

    if qada == 1:
        point += 1
        goAfternoon()

    else:
        point -= 1
        goAfternoon()
    
def goAfternoon():
    afternoonGreet = Label(root, text="\n\n[12:00PM]\nYou walk into the office and see your co-workers gossiping about the boss" +
                           "\nwhat are you going to do?")
    yesRant = Button(root, text = "Join", padx=20, pady=10, command=lambda: goRant(1))
    noRant = Button(root, text = "Walk\nAway", padx=20, pady=12, command=lambda: goRant(2))
    
    afternoonGreet.grid(columnspan=3, row=10)
    yesRant.grid(column=0, columnspan=2, row=11)
    noRant.grid(column=1, columnspan=2, row=11)

def goRant(rant):
    global point
    
    if rant == 1:
        point -= 1
        goAzan()
    
    else:
        point += 1
        goAzan()

def goAzan():
    azanGreet = Label(root, text="\n\n[1:12PM]\nYou were in the middle of presentating your monthly report to your boss." +
                      "\nThen you heard the Zuhr call of prayer (Adzan)." +
                      "\nDo you want to continue with the presentation or respect the call of prayer?")
    noRespect = Button(root, text="Continue\nMeeting", padx=20, pady=10, command=lambda: goRespect())
    respect = Button(root, text="Respect\nAdzan", padx=20, pady=10, command=lambda: goRespect())

    azanGreet.grid(columnspan=3, row=12)
    noRespect.grid(column=0,columnspan=2, row=13)
    respect.grid(column=1, columnspan=2, row=13)

def goRespect():
    global point

    point += 1
    goNight()

def goNight():
    nightGreet = Label(root, text="\n\n[7:00PM]\nIt is the end of the day, you are tired but still have obligations as a muslim." +
                       "\nFor Maghrib, will you be going to the mosque?")
    prayMosque = Button(root, text="Pray at\nMosque", padx=20, pady=10, command=lambda: goMosque(1))
    prayHome = Button(root, text="Pray at\nHome", padx=20, pady=10, command=lambda: goMosque(2))

    nightGreet.grid(columnspan=3, row=16)
    prayMosque.grid(column=0, columnspan=2, row=17)
    prayHome.grid(column=1, columnspan=2, row=17)

def goMosque(mosque):
    global point

    if mosque == 1:
        point += 1
        stayMosque()

    else:
        point -= 0
        endScene()

def stayMosque():
    mosqueGreet = Label(root, text="\n\n[8:00]\nIt is not longer until Isya'\nWill you go back home or stay to pray?")
    stayMosque = Button(root, text="Stay at\nMosque", padx=20, pady=10, command=lambda: goIsya(1))
    goHome = Button(root, text="Go Home", padx=20, pady=10, command=lambda: goIsya(2))

    mosqueGreet.grid(columnspan=3, row=18)
    stayMosque.grid(column=0, columnspan=2, row=19)
    goHome.grid(column=1, columnspan=2, row=19)

def goIsya(Isya):
    global point

    if Isya == 1:
        point += 1
        endScene()

    else:
        point -= 0
        endScene()

def endScene():
    global point
    endGreet = Label(root, text="You have ended your day!\nTotal marks is: " + str(point))

    endGreet.grid(columnspan=3, row=20)

intro()
morning()

root.mainloop()