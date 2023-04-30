from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("460x550")
root.title("Muslim Simulator")

point = 0 # Player's final score

global fn # f(n) = h(n) + g(n) // path cost
fn = 0

global hn # Number of CHOICES made
hn = 0

global gn # Number of BAD CHOICES made
gn = 0

morningScene = Frame(root, padx=5, pady=5)
morningScene.grid(row=1, columnspan=3)

afternoonScene = Frame(root, padx=5, pady=5)
afternoonScene.grid(row=1, columnspan=3)

nightScene = Frame(root, padx=5, pady=5)
nightScene.grid(row=1, columnspan=3)

def intro():
    global point
    point = 0
    greet = Label(morningScene, text="Welcome to Muslim Simulator 2023!")
    introduction = Label(morningScene, text="In this journey, we will decide whether you're a good Muslim or otherwise." +
                         "\n Be aware that all your choices are meaningful and will decide your fate!", justify=CENTER)

    greet.grid(column=1,row=0)
    introduction.grid(columnspan=3, row=1)

def morning():
    temp = 0

    morningGreet = Label(morningScene, text="\nThis is just another normal day for a Muslim. To start the day you decided to wakeup: ")
    early = Button(morningScene, text="Early", padx=20, pady=10, command=lambda: goEarly(temp))
    onTime = Button(morningScene, text="On Time", padx=20, pady=10, command=lambda: goOnTime(temp))
    late = Button(morningScene, text="Late", padx=20, pady=10, command=lambda: goLate())

    morningGreet.grid(columnspan=3, row=2)
    early.grid(column=0,row=3)
    onTime.grid(column=1, row=3)
    late.grid(column=2, row=3)

def goEarly(temp):
    global hn
    earlyGreet = Label(morningScene ,text="\n\n[4:30 AM]\nGreat! You decided to wake up early.\nDo you want to "
                  + "perform tahajjud prayer ? or do you want to go back to sleep ?")
    tahajjud = Button(morningScene, text="Tahajjud", padx=20, pady=10, command=lambda: goTahajjud(temp))
    sleep = Button(morningScene, text="Sleep", padx=20, pady=10, command=lambda: goOnTime(temp))

    earlyGreet.grid(columnspan=3, row=4)
    tahajjud.grid(column=0, columnspan=2, row=5)
    sleep.grid(column=1, columnspan=2, row=5)

    hn += 1


def goTahajjud(temp):
    global point
    point += 1
    temp = 1
    goOnTime(temp)
    
def goOnTime(temp):
    global hn
    if temp == 0:
        onTimeGreet = Label(morningScene, text="\n\n[6:00 AM]\nGood! You decided to wake up on time. \nDo you want to perform Subuh" +
                  " prayer ? or do you want to go back to sleep ?")
    
    else:
        onTimeGreet = Label(morningScene, text="\n\n[6:00 AM]\nGood! Do you want to perform Subuh" +
                  " prayer ?\nor do you want to go back to sleep ?")
    
    subuh = Button(morningScene, text="Subuh", padx=20, pady=10, command=lambda: goAfternoon())
    sleep = Button(morningScene, text="Sleep", padx=20, pady=10, command=lambda: goSleep())

    onTimeGreet.grid(columnspan=3, row=6)
    subuh.grid(column=0, columnspan=2, row=7)
    sleep.grid(column=1, columnspan=2, row=7)

    hn += 1

def goSleep():
    global point
    point -= 1
    goLate()

def goLate():
    global hn
    global gn
    lateGreet = Label(morningScene, text="\n\n[7:30 AM]\nAstaghfirullahalazim... You woke up late and did not perform Subuh prayer." +
          "\nDo you want to peform Qada' prayer ?")
    yesQada = Button(morningScene, text="Yes", padx=20, pady=10, command=lambda: goQada(1))
    noQada = Button(morningScene, text="No", padx=20, pady=10, command=lambda: goQada(2))

    lateGreet.grid(columnspan=3, row=8)
    yesQada.grid(column=0, columnspan=2, row=9)
    noQada.grid(column=1, columnspan=2, row=9)

    hn += 1
    gn += 1

def goQada(qada):
    global point
    global gn 

    if qada == 1:
        point += 1
        goAfternoon()

    else:
        point -= 1
        gn += 1
        goAfternoon()

def goAfternoon():
    global hn 
    morningScene.destroy()
    afternoonGreet = Label(afternoonScene, text="\n\n[12:00 PM]\nYou walk into the office and see your co-workers gossiping about the boss." +
                           "\nWhat are you going to do?")
    yesRant = Button(afternoonScene, text = "Join", padx=20, pady=10, command=lambda: goRant(1))
    noRant = Button(afternoonScene, text = "Walk\nAway", padx=20, pady=12, command=lambda: goRant(2))
    
    afternoonGreet.grid(columnspan=3, row=10)
    yesRant.grid(column=0, columnspan=2, row=11)
    noRant.grid(column=1, columnspan=2, row=11)

    hn += 1

def goRant(rant):
    global point
    global gn
    
    if rant == 1:
        point -= 1
        gn += 1
        goAzan()
    
    else:
        point += 1
        goAzan()

def goAzan():
    global hn 
    azanGreet = Label(afternoonScene, text="\n\n[1:12 PM]\nYou were in the middle of presentating your monthly report to your boss." +
                      "\nThen you heard the Zuhr call of prayer (Adzan)." +
                      "\nDo you want to continue with the presentation or respect the call of prayer?")
    noRespect = Button(afternoonScene, text="Continue\nMeeting", padx=20, pady=10, command=lambda: goRespect())
    respect = Button(afternoonScene, text="Respect\nAdzan", padx=20, pady=10, command=lambda: goRespect())

    azanGreet.grid(columnspan=3, row=12)
    noRespect.grid(column=0,columnspan=2, row=13)
    respect.grid(column=1, columnspan=2, row=13)

    hn += 1

def goRespect():
    global point
    global hn

    point += 1
    hn += 1
    goNight()

def goNight():
    global hn
    afternoonScene.destroy()
    nightGreet = Label(nightScene, text="\n\n[7:00 PM]\nIt is the end of the day, you are tired but still have obligations as a Muslim." +
                       "\nFor Maghrib, will you be going to the mosque?")
    prayMosque = Button(nightScene, text="Pray at\nMosque", padx=20, pady=10, command=lambda: goMosque(1))
    prayHome = Button(nightScene, text="Pray at\nHome", padx=20, pady=10, command=lambda: goMosque(2))

    nightGreet.grid(columnspan=3, row=16)
    prayMosque.grid(column=0, columnspan=2, row=17)
    prayHome.grid(column=1, columnspan=2, row=17)

    hn += 1

def goMosque(mosque):
    global point

    if mosque == 1:
        point += 1
        stayMosque()

    else:
        point -= 0
        endScene()

def stayMosque():
    global hn
    mosqueGreet = Label(nightScene, text="\n\n[8:00 PM]\nIt is not long until Isya'\nWill you go back home or stay to pray?")
    stayMosque = Button(nightScene, text="Stay at\nMosque", padx=20, pady=10, command=lambda: goIsya(1))
    goHome = Button(nightScene, text="Go Home", padx=20, pady=10, command=lambda: goIsya(2))

    mosqueGreet.grid(columnspan=3, row=18)
    stayMosque.grid(column=0, columnspan=2, row=19)
    goHome.grid(column=1, columnspan=2, row=19)

    hn += 1

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
    global hn
    global fn

    fn = gn + hn # final path cost
    
    if point >= 0:
        endGreet = Label(nightScene, text="\n\nYou have ended your day!\nTotal marks is: " + str(point) +
                         "\nYou are on the right path towards Rahmatan Lil Alamin!\n")

    else:
        endGreet = Label(nightScene, text="\n\nYou have ended your day!\nTotal marks is: " + str(point) +
                         "\nAllah SWT still loves you, return to the right path\n")

    endGreet.grid(columnspan=3, row=20)

intro()
morning()

root.mainloop()