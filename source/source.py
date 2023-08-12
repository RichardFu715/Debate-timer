from ast import Slice
import time, datetime
import ctypes
import tkinter as tk

versionNo='''v2.0.
Formal version for Windows 10/11.'''

# Main window

ctypes.windll.shcore.SetProcessDpiAwareness(1)

root=tk.Tk()
root.attributes('-alpha',0.01)
root.attributes('-fullscreen',1)
root.update()

if root.winfo_height()/720>root.winfo_width()/1280: ScaleFactor=root.winfo_width()*100/1280
else: ScaleFactor=root.winfo_height()*100/720

root.tk.call('tk','scaling',ScaleFactor/75)
root.config(bg='#000000')
root.attributes('-topmost',0)
root.title('Debate Timer')
root.update()

# Common values

SCALEFACTOR=ScaleFactor*0.01

SCREENHEIGHT=root.winfo_height()
SCREENWIDTH=root.winfo_width()
FRAMEWIDTH=(SCREENWIDTH-int(1280*SCALEFACTOR))//2+int(SCALEFACTOR*1280)
FRAMEHEIGHT=SCREENHEIGHT-int(SCALEFACTOR*84)

TITLETEXTWIDTH=int((SCREENWIDTH-132*SCALEFACTOR)/(35*SCALEFACTOR))
TEAMNAMEWIDTH=int((FRAMEWIDTH//2-100*SCALEFACTOR)/(18*SCALEFACTOR))

LISTLEN=1
PAGENO=0

DISPLAYPAGENO=0
STANDARDQUARTERSECOND=0

LEFTTIME=0
RIGHTTIME=0
PUBLICTIME=0
LEFTQUARTERSECOND=0
RIGHTQUARTERSECOND=0
PUBLICQUARTERSECOND=0
LEFTTIMERSTATE=0
RIGHTTIMERSTATE=0
PUBLICTIMERSTATE=0
SPEAKERMODE=0

TIMERPAGENO=0

BELLMARK1=True
BELLMARK2=True
BELLMARK3=True

LISTFIRSTOPENMARK=True
TIMERFIRSTOPENMARK=True

# Debate settings

TimeList1=[]
SegmentList1=[]
SpeakerModeList=[]

# Public color values

BACKGROUNDCOLOR=[['#1F1F1F','#F7F7F7'],['#000000','#FFFFFF']]
FOREGROUNDCOLOR=[['#FFFFFF','#0F0F0F'],['#FFFFFF','#000000']]
FOREGROUNDACCENTCOLOR=[['#80C6FF','#004680'],['#80C6FF','#004680']]
BACKGROUNDACCENTCOLOR=[['#008CFF','#008CFF'],['#000000','#FFFFFF']]
BUTTONOUTLINECOLOR=[['#1F1F1F','#F7F7F7'],['#FFFFFF','#000000']]
ENTRYOUTLINECOLOR=[['#FFFFFF','#000000'],['#FFFFFF','#000000']]
ENTRYOUTLINEBACKGROUND=[['#7F7F7F','#7F7F7F'],['#80C6FF','#005FAB']]

'''Colors
#004680 Dark Blue
#008cff Blue
#80c6ff Light Blue
'''

# Public page elements

minimizebutton=tk.Button(root,text='\u2500',command=root.iconify,bd=0,bg='#3f3f3f',fg='#ffffff',relief='flat',width=3,font=('Microsoft YaHei UI',9))
minimizebutton.place(x=int(SCREENWIDTH-59*SCALEFACTOR),y=0)

closebutton=tk.Button(root,text='\u2573',command=root.destroy,bd=0,bg='#3f3f3f',fg='#ffffff',activebackground='#ff0000',activeforeground='#ffffff',relief='flat',width=3,font=('Microsoft YaHei UI',9))
closebutton.place(x=int(SCREENWIDTH-27*SCALEFACTOR),y=0)

titletext1=tk.StringVar()
title1=tk.Label(root,textvariable=titletext1,fg='#ffffff',bg='#000000',font=('Consolas',48,'bold'),width=TITLETEXTWIDTH)
title1.place(x=int(64*SCALEFACTOR+((SCREENWIDTH-132*SCALEFACTOR-TITLETEXTWIDTH*35*SCALEFACTOR)//2)),y=int(4*SCALEFACTOR))

# Welcome

frame0=tk.Frame(root,height=FRAMEHEIGHT,width=FRAMEWIDTH,bg='#000000')

versioninfo=tk.Label(root,text='%s'%versionNo,fg='#5f5f5f',bg='#000000',font=('Microsoft YaHei UI',9),justify='left')

button01=tk.Button(frame0,text='Get ready!',font=('Microsoft JhengHei UI',24),fg='#ffffff',bg='#0078d7',relief='flat',bd=0,width=24)
button01.place(x=int(SCREENWIDTH-472*SCALEFACTOR)//2,y=SCREENHEIGHT//4)

# List

frame1=tk.Frame(root,height=FRAMEHEIGHT,width=FRAMEWIDTH,bg='#000000')
frame10=tk.Frame(frame1,height=int(600*SCALEFACTOR),width=int(440*SCALEFACTOR+TITLETEXTWIDTH*8*SCALEFACTOR),bg='#000000',highlightbackground='#3f3f3f',highlightcolor='#3f3f3f',highlightthickness=int(SCALEFACTOR))
frame10.place(x=(FRAMEWIDTH-(496+(TITLETEXTWIDTH+TEAMNAMEWIDTH)*8)*SCALEFACTOR)//2,y=0)

labellist10=[tk.Label(frame10,text='No.',fg='#ffffff',bg='#000000',font=('Microsoft YaHei UI',9),height=2,anchor='center'),tk.Label(frame10,text='Segment title',fg='#ffffff',bg='#000000',font=('Microsoft YaHei UI',9),height=2,anchor='center'),tk.Label(frame10,text='''Time/sec
For each team''',fg='#ffffff',bg='#000000',font=('Microsoft YaHei UI',9),justify='center'),tk.Label(frame10,text='''Time for:
Both  Pro  Con Public''',fg='#ffffff',bg='#000000',font=('Microsoft YaHei UI',9),justify='center'),tk.Label(frame10,text='Options',fg='#ffffff',bg='#000000',font=('Microsoft YaHei UI',9))]
labellist10[0].place(x=4*SCALEFACTOR,y=0)
labellist10[1].place(x=52*SCALEFACTOR,y=0)
labellist10[2].place(x=int(40*SCALEFACTOR+TITLETEXTWIDTH*8*SCALEFACTOR),y=0)
labellist10[3].place(x=int(132*SCALEFACTOR+TITLETEXTWIDTH*8*SCALEFACTOR),y=0)
labellist10[4].place(x=int(284*SCALEFACTOR+TITLETEXTWIDTH*8*SCALEFACTOR),y=0)

frame101=tk.Frame(frame10,height=int(512*SCALEFACTOR),width=int(280*SCALEFACTOR+TITLETEXTWIDTH*8*SCALEFACTOR),bg='#000000')
frame102=tk.Frame(frame101,height=int(32*SCALEFACTOR),width=int(280*SCALEFACTOR+TITLETEXTWIDTH*8*SCALEFACTOR),bg='#000000')
frame103=tk.Frame(frame10,height=int(32*SCALEFACTOR),width=int(48*SCALEFACTOR),bg='#000000')
frame104=tk.Frame(frame10,height=int(64*SCALEFACTOR),width=int(96*SCALEFACTOR),bg='#000000')
frame101.place(x=int(4*SCALEFACTOR),y=int(44*SCALEFACTOR))
frame102.place(x=0,y=0)
frame103.place(x=int((288+TITLETEXTWIDTH*8)*SCALEFACTOR),y=int(44*SCALEFACTOR))
frame104.place(x=int((340+TITLETEXTWIDTH*8)*SCALEFACTOR),y=int(28*SCALEFACTOR))

frame11=tk.Frame(frame1,bg='#000000',height=int(464*SCALEFACTOR),width=int(40*SCALEFACTOR+TEAMNAMEWIDTH*8*SCALEFACTOR),highlightbackground='#3f3f3f',highlightcolor='#3f3f3f',highlightthickness=int(SCALEFACTOR))
frame11.place(x=int(SCALEFACTOR*452+SCALEFACTOR*TITLETEXTWIDTH*8+(FRAMEWIDTH-SCALEFACTOR*(496+(TITLETEXTWIDTH+TEAMNAMEWIDTH)*8))//2),y=0)

labeltextlist11=[tk.IntVar()]
labellist11=[]

labellist12=[tk.Label(frame11,text='Pro',font=('Microsoft JhengHei UI',32),fg='#66ccff',bg='#000000'),tk.Label(frame11,text='Con',font=('Microsoft JhengHei UI',32),fg='#66ccff',bg='#000000')]
labellist13=[tk.Label(frame11,text='Team name',font=('Microsoft YaHei UI',9),fg='#ffffff',bg='#000000'),tk.Label(frame11,text='Team name',font=('Microsoft Yahei UI',9),fg='#ffffff',bg='#000000')]
labellist14=[tk.Label(frame11,text='Viewpoint',font=('Microsoft YaHei UI',9),fg='#ffffff',bg='#000000'),tk.Label(frame11,text='Viewpoint',font=('Microsoft YaHei UI',9),fg='#ffffff',bg='#000000')]
labellist12[0].place(x=int(16*SCALEFACTOR),y=int(8*SCALEFACTOR))
labellist12[1].place(x=int(16*SCALEFACTOR),y=int(224*SCALEFACTOR))
labellist13[0].place(x=int(16*SCALEFACTOR),y=int(64*SCALEFACTOR))
labellist13[1].place(x=int(16*SCALEFACTOR),y=int(280*SCALEFACTOR))
labellist14[0].place(x=int(16*SCALEFACTOR),y=int(128*SCALEFACTOR))
labellist14[1].place(x=int(16*SCALEFACTOR),y=int(344*SCALEFACTOR))

entrytextlist11=[]
entrylist11=[]
entrytextlist12=[]
entrylist12=[]
entrytextlist13=[]
entrylist13=[]
texttextlist11=[]
textlist11=[]

checkvaluelist11=[]
checklist11=[]

buttonlist11=[]
buttonlist12=[]
buttonlist13=[]
buttonlist14=[tk.Button(frame10,text='< Prev',fg='#ffffff',bg='#3f3f3f',font=('Microsoft YaHei UI',9),disabledforeground='#7f7f7f',relief='flat',bd=0), tk.Button(frame10,text='Next >',fg='#ffffff',bg='#3f3f3f',font=('Microsoft YaHei UI',9),disabledforeground='#7f7f7f',relief='flat',bd=0)]
button15=tk.Button(frame1,text='Begin!',font=('Microsoft JhengHei UI',12),fg='#ffffff',bg='#0078d7',relief='flat',width=(40+TEAMNAMEWIDTH*8)//10,bd=0)

checkbuttonvalue11and21=tk.IntVar()
checkbutton11=tk.Checkbutton(frame1,text='Always on top',font=('Microsoft YaHei UI',9),fg='#ffffff',bg='#000000',selectcolor='#000000',activebackground='#000000',activeforeground='#ffffff',variable=checkbuttonvalue11and21)

# Time

frame2=tk.Frame(root,height=FRAMEHEIGHT,width=FRAMEWIDTH,bg='#000000')
frame21=tk.Frame(frame2,height=int(100*SCALEFACTOR),width=int(200*SCALEFACTOR),bg='#000000')
frame22=tk.Frame(frame21,height=int(100*SCALEFACTOR),width=int(400*SCALEFACTOR),bg='#000000')

labeltextlist21=[]
labeltextlist22=[]
labeltextlist23=[]
labeltext24=tk.StringVar()
labellist21=[]
labellist22=[]
labellist23=[]
label24=tk.Label(frame2,textvariable=labeltext24,font=('Microsoft YaHei UI',9),fg='#7f7f7f',bg='#000000')

entrytextlist21=[]
entrylist21=[]

buttonlist21=[]
buttonlist22=[]
buttonlist23=[]

checkbutton21=tk.Checkbutton(frame2,text='Always on top',font=('Microsoft YaHei UI',9),fg='#ffffff',bg='#000000',selectcolor='#000000',activebackground='#000000',activeforeground='#ffffff',variable=checkbuttonvalue11and21)

# Check before timing

frame3=tk.Frame(root,height=FRAMEHEIGHT,width=FRAMEWIDTH,bg='#000000')

labeltext31=tk.StringVar()
label31=tk.Label(frame3,textvariable=labeltext31,fg='#ff0000',bg='#000000',font=('Microsoft JhengHei UI',16),wraplength=FRAMEWIDTH-64,justify='left')
label31.place(x=32,y=16)

button31=tk.Button(frame3,text='Go back to settings',font=('Microsoft JhengHei UI',12),fg='#ffffff',bg='#3f3f3f',relief='flat',bd=0)

# End

frame4=tk.Frame(root,height=FRAMEHEIGHT,width=FRAMEWIDTH,bg='#000000')

button41=tk.Button(frame4,text='Start a new round',font=('Microsoft JhengHei UI',24),relief='flat',bd=0,fg='#ffffff',bg='#0078d7',width=24)
button42=tk.Button(frame4,text='Exit',font=('Microsoft JhengHei UI',24),relief='flat',bd=0,fg='#ffffff',bg='#3f3f3f',width=24)
button41.place(x=(FRAMEWIDTH-472*SCALEFACTOR)//2,y=FRAMEHEIGHT//4)
button42.place(x=(FRAMEWIDTH-472*SCALEFACTOR)//2,y=FRAMEHEIGHT//4+int(96*SCALEFACTOR))

# Check before entering program

frame5=tk.Frame(root,height=SCREENHEIGHT,width=SCREENWIDTH,bg='#000000')
labeltext51=tk.StringVar()
label51=tk.Label(frame5,textvariable=labeltext51,font=('Microsoft JhengHei UI',16),fg='#ff0000',bg='#000000',wraplength=SCREENWIDTH-8,justify='left')
button51=tk.Button(frame5,text='Close',font=('Microsoft JhengHei UI',16),fg='#ffffff',bg='#3f3f3f',command=root.destroy,relief='flat',bd=0)
label51.place(x=4,y=int(4*SCALEFACTOR))
button51.place(x=4,y=int(240*SCALEFACTOR))

# Manage

def SetCurrentFrame(frameno):
    global SCREENWIDTH,FRAMEWIDTH
    for i in range(0,6):
        if i==frameno:
            if frameno==5: frame5.place(x=0,y=84)
            else: eval("frame{}.place(x={},y=int(84*SCALEFACTOR))".format(i,int((SCREENWIDTH-FRAMEWIDTH)//2)))
        else:
            eval("frame{}.place(x={},y=int(84*SCALEFACTOR))".format(i,SCREENWIDTH+1))

def BackToSettings():
    PreDebate()

def ChangeTopMost():
    root.attributes('-topmost',checkbuttonvalue11and21.get())
    root.update()

def FadeWindow():
    for i in range(10,-1,-1):
        time.sleep(0.01)
        root.attributes('-alpha',round(i/10,1))

def ShowWindow():
    for i in range(0,11,1):
        time.sleep(0.01)
        root.attributes('-alpha',round(i/10,1))

def SleepQuarterSecond():
    st=time.monotonic()
    time.sleep(0.15)
    while time.monotonic()<.25+st:
        pass
    return

def CloseProgram():
    FadeWindow()
    root.destroy()

def EndDebate():
    SetCurrentFrame(4)
    titletext1.set('The end!')
    button41.config(command=BackToSettings)
    button42.config(command=CloseProgram)

def TimerPageUp():
    TimerMgr(1)

def TimerPageDown():
    TimerMgr(2)

def TimerBackToSettings():
    Stop1()
    Stop2()
    Stop3()
    BackToSettings()

def TimerRestart():
    TimerMgr(4)

def TimerAbort():
    TimerMgr(5)

def Countdown1():
    global LEFTTIME, LEFTQUARTERSECOND, LEFTTIMERSTATE, BELLMARK1, STANDARDQUARTERSECOND
    while (LEFTTIME!=0 or LEFTQUARTERSECOND!=0) and LEFTTIMERSTATE==1:
        LEFTQUARTERSECOND-=1
        if LEFTQUARTERSECOND==-1:
            LEFTQUARTERSECOND+=4
            LEFTTIME-=1
            entrytextlist21[0].set(LEFTTIME)
        root.update()
        SleepQuarterSecond()
    if LEFTTIME==0 and LEFTQUARTERSECOND==0:
        entrylist21[0].config(fg='#ff0000',disabledforeground='#ff0000')
        if BELLMARK1==True:
            root.bell()
            BELLMARK1=False
        LEFTTIMERSTATE=0
        buttonlist21[0].config(state='disabled')
        buttonlist22[0].config(state='disabled')
    return

def Countdown2():
    global RIGHTTIME, RIGHTQUARTERSECOND, RIGHTTIMERSTATE, BELLMARK2, STANDARDQUARTERSECOND
    while (RIGHTTIME!=0 or RIGHTQUARTERSECOND!=0) and RIGHTTIMERSTATE==1:
        RIGHTQUARTERSECOND-=1
        if RIGHTQUARTERSECOND==-1:
            RIGHTQUARTERSECOND+=4
            RIGHTTIME-=1
            entrytextlist21[1].set(RIGHTTIME)
        root.update()
        SleepQuarterSecond()
    if RIGHTTIME==0 and RIGHTQUARTERSECOND==0:
        entrylist21[1].config(fg='#ff0000',disabledforeground='#ff0000')
        if BELLMARK2==True:
            root.bell()
            BELLMARK2=False
        RIGHTTIMERSTATE=0
        buttonlist21[1].config(state='disabled')
        buttonlist22[1].config(state='disabled')
    return

def Countdown3():
    global PUBLICTIME, PUBLICQUARTERSECOND, PUBLICTIMERSTATE, BELLMARK3, STANDARDQUARTERSECOND
    while (PUBLICTIME!=0 or PUBLICQUARTERSECOND!=0) and PUBLICTIMERSTATE==1:
        PUBLICQUARTERSECOND-=1
        if PUBLICQUARTERSECOND==-1:
            PUBLICQUARTERSECOND+=4
            PUBLICTIME-=1
            entrytextlist21[2].set(PUBLICTIME)
        root.update()
        SleepQuarterSecond()
    if PUBLICTIME==0 and PUBLICQUARTERSECOND==0:
        entrylist21[2].config(fg='#ff0000',disabledforeground='#ff0000')
        if BELLMARK3==True:
            root.bell()
            BELLMARK3=False
        PUBLICTIMERSTATE=0
        buttonlist21[2].config(state='disabled')
        buttonlist22[2].config(state='disabled')
    return

def Start1():
    global LEFTTIMERSTATE, RIGHTTIMERSTATE, RIGHTTIME, RIGHTQUARTERSECOND
    LEFTTIMERSTATE, RIGHTTIMERSTATE=1,0
    buttonlist21[0].config(state='disabled')
    buttonlist22[0].config(state='normal')
    if SPEAKERMODE==0 and (RIGHTTIME!=0 or RIGHTQUARTERSECOND!=0):
        buttonlist21[1].config(state='normal')
        buttonlist22[1].config(state='disabled')
    Countdown1()

def Start2():
    global RIGHTTIMERSTATE, LEFTTIMERSTATE, LEFTTIME, LEFTQUARTERSECOND
    LEFTTIMERSTATE, RIGHTTIMERSTATE=0,1
    buttonlist21[1].config(state='disabled')
    buttonlist22[1].config(state='normal')
    if SPEAKERMODE==0 and (LEFTTIME!=0 or LEFTQUARTERSECOND!=0):
        buttonlist21[0].config(state='normal')
        buttonlist22[0].config(state='disabled')
    Countdown2()

def Start3():
    global PUBLICTIMERSTATE
    PUBLICTIMERSTATE=1
    buttonlist21[2].config(state='disabled')
    buttonlist22[2].config(state='normal')
    Countdown3()

def Stop1():
    global LEFTTIMERSTATE
    LEFTTIMERSTATE=0
    buttonlist21[0].config(state='normal')
    buttonlist22[0].config(state='disabled')

def Stop2():
    global RIGHTTIMERSTATE
    RIGHTTIMERSTATE=0
    buttonlist21[1].config(state='normal')
    buttonlist22[1].config(state='disabled')

def Stop3():
    global PUBLICTIMERSTATE
    PUBLICTIMERSTATE=0
    buttonlist21[2].config(state='normal')
    buttonlist22[2].config(state='disabled')

def TimerSetup():
    global SPEAKERMODE, FRAMEHEIGHT, FRAMEWIDTH, SCALEFACTOR, TEAMNAMEWIDTH
    for i in range(2):
        labeltextlist21.append(tk.StringVar())
        labeltextlist22.append(tk.StringVar())
        labeltextlist23.append(tk.StringVar())
        labellist22.append(tk.Label(frame2,textvariable=labeltextlist22[i],fg='#66ccff',bg='#3f3f3f',font=('Consolas',24,'bold'),anchor='n'))
        labellist23.append(tk.Label(frame2,textvariable=labeltextlist23[i],fg='#ffffff',bg='#000000',font=('Consolas',24),anchor='n',justify='center',height=3))
    for i in range(3):
        entrytextlist21.append(tk.StringVar())
        entrylist21.append(tk.Entry(frame2,textvariable=entrytextlist21[i],fg='#ffffff',bg='#000000',font=('Bahnschrift',108),disabledforeground='#ffffff',disabledbackground='#000000',bd=0,relief='flat',width=4,justify='center',state='disabled'))
        buttonlist21.append(tk.Button(frame22,text='Start',font=('Microsoft JHengHei UI',12),fg='#ffffff',bg='#3f3f3f',disabledforeground='#7f7f7f',width=5,relief='flat',bd=0))
        buttonlist22.append(tk.Button(frame22,text='Stop',font=('Microsoft JHengHei UI',12),fg='#ffffff',bg='#3f3f3f',disabledforeground='#7f7f7f',width=5,relief='flat',bd=0))
    labellist21.append(tk.Label(frame2,textvariable=labeltextlist21[0],fg='#ffffff',bg='#0078d7',font=('Consolas',24,'bold'),anchor='n',justify='center',width=TEAMNAMEWIDTH))
    labellist21.append(tk.Label(frame2,textvariable=labeltextlist21[1],fg='#ffffff',bg='#0078d7',font=('Consolas',24,'bold'),anchor='n',justify='center',width=TEAMNAMEWIDTH))
    frame21.place(x=(FRAMEWIDTH-200*SCALEFACTOR)//2,y=FRAMEHEIGHT-int(128*SCALEFACTOR))
    labellist21[0].place(x=int(SCALEFACTOR*16),y=int(14*SCALEFACTOR))
    labellist21[1].place(x=int(FRAMEWIDTH-(FRAMEWIDTH//2-100*SCALEFACTOR)//int(18*SCALEFACTOR)*int(18*SCALEFACTOR)-int(SCALEFACTOR*22)),y=int(SCALEFACTOR*14))
    labellist22[0].config(width=TEAMNAMEWIDTH)
    labellist22[1].config(width=TEAMNAMEWIDTH)
    labellist22[0].place(x=int(SCALEFACTOR*16),y=int(SCALEFACTOR*54))
    labellist22[1].place(x=int(FRAMEWIDTH-(FRAMEWIDTH//2-100*SCALEFACTOR)//int(18*SCALEFACTOR)*int(18*SCALEFACTOR)-int(SCALEFACTOR*22)),y=int(SCALEFACTOR*54))
    labellist23[0].config(width=TEAMNAMEWIDTH,wraplength=int((FRAMEWIDTH//2-100*SCALEFACTOR)//int(SCALEFACTOR*18)*int(SCALEFACTOR*18)))
    labellist23[1].config(width=TEAMNAMEWIDTH,wraplength=int((FRAMEWIDTH//2-100*SCALEFACTOR)//int(SCALEFACTOR*18)*int(SCALEFACTOR*18)))
    labellist23[0].place(x=int(SCALEFACTOR*16),y=int(SCALEFACTOR*120))
    labellist23[1].place(x=int(FRAMEWIDTH-((FRAMEWIDTH//2-SCALEFACTOR*100)//int(SCALEFACTOR*18)*int(SCALEFACTOR*18))-int(SCALEFACTOR*22)),y=int(SCALEFACTOR*120))
    label24.place(x=int(SCALEFACTOR*16),y=FRAMEHEIGHT-int(SCALEFACTOR*32))
    entrylist21[0].place(x=int((TEAMNAMEWIDTH*18-322)*SCALEFACTOR//2+int(SCALEFACTOR*16)),y=int(SCALEFACTOR*240))
    entrylist21[1].place(x=int(FRAMEWIDTH-int(SCALEFACTOR*16)-int(TEAMNAMEWIDTH*18*SCALEFACTOR)+SCALEFACTOR*(TEAMNAMEWIDTH*18-322)//2),y=int(SCALEFACTOR*240))
    entrylist21[2].place(x=int((FRAMEWIDTH-322*SCALEFACTOR)//2),y=int(SCALEFACTOR*240))
    labeltextlist21[0].set('Pro')
    labeltextlist21[1].set('Con')
    buttonlist21[0].config(command=Start1)
    buttonlist21[1].config(command=Start2)
    buttonlist21[2].config(command=Start3)
    buttonlist22[0].config(command=Stop1)
    buttonlist22[1].config(command=Stop2)
    buttonlist22[2].config(command=Stop3)
    buttonlist21[0].place(x=int(SCALEFACTOR*20),y=int(SCALEFACTOR*16))
    buttonlist21[1].place(x=int(SCALEFACTOR*124),y=int(SCALEFACTOR*16))
    buttonlist21[2].place(x=int(SCALEFACTOR*272),y=int(SCALEFACTOR*16))
    buttonlist22[0].place(x=int(SCALEFACTOR*20),y=int(SCALEFACTOR*56))
    buttonlist22[1].place(x=int(SCALEFACTOR*124),y=int(SCALEFACTOR*56))
    buttonlist22[2].place(x=int(SCALEFACTOR*272),y=int(SCALEFACTOR*56))
    for i in range(5):
        buttonlist23.append(tk.Button(frame2,font=('Microsoft YaHei UI',12),fg='#ffffff',bg='#3f3f3f',disabledforeground='#7f7f7f',relief='flat',bd=0))
    buttonlist23[0].config(text='Prev')
    buttonlist23[1].config(text='Next')
    buttonlist23[2].config(text='Edit settings')
    buttonlist23[3].config(text='Restart')
    buttonlist23[4].config(text='Abort')
    buttonlist23[0].place(x=FRAMEWIDTH-int(SCALEFACTOR*337),y=FRAMEHEIGHT-int(SCALEFACTOR*36))
    buttonlist23[0].config(command=TimerPageUp)
    buttonlist23[1].place(x=FRAMEWIDTH-int(SCALEFACTOR*287),y=FRAMEHEIGHT-int(SCALEFACTOR*36))
    buttonlist23[1].config(command=TimerPageDown)
    buttonlist23[2].place(x=FRAMEWIDTH-int(SCALEFACTOR*234),y=FRAMEHEIGHT-int(SCALEFACTOR*36))
    buttonlist23[2].config(command=TimerBackToSettings)
    buttonlist23[3].place(x=FRAMEWIDTH-int(SCALEFACTOR*124),y=FRAMEHEIGHT-int(SCALEFACTOR*36))
    buttonlist23[3].config(command=TimerRestart)
    buttonlist23[4].place(x=FRAMEWIDTH-int(SCALEFACTOR*54),y=FRAMEHEIGHT-int(SCALEFACTOR*36))
    buttonlist23[4].config(command=TimerAbort)
    checkbutton21.config(command=ChangeTopMost)
    checkbutton21.place(x=FRAMEWIDTH-int(SCALEFACTOR*450),y=FRAMEHEIGHT-int(SCALEFACTOR*32))
    root.update()

def TimerRefreshPage():
    global LEFTTIME, RIGHTTIME, PUBLICTIME, SPEAKERMODE, BELLMARK1, BELLMARK2, BELLMARK3, TIMERPAGENO, LISTLEN, TimeList1, SpeakerModeList, SegmentList1
    Stop1()
    Stop2()
    Stop3()
    labeltextlist22[0].set(entrytextlist13[0].get())
    labeltextlist22[1].set(entrytextlist13[1].get())
    labeltextlist23[0].set(textlist11[0].get(1.0,'end').strip())
    labeltextlist23[1].set(textlist11[1].get(1.0,'end').strip())
    titletext1.set(SegmentList1[TIMERPAGENO])
    labeltext24.set("Segment {} of {}.".format(TIMERPAGENO+1,LISTLEN))
    LEFTTIME=TimeList1[TIMERPAGENO]
    RIGHTTIME=TimeList1[TIMERPAGENO]
    PUBLICTIME=TimeList1[TIMERPAGENO]
    SPEAKERMODE=SpeakerModeList[TIMERPAGENO]
    BELLMARK1=BELLMARK2=BELLMARK3=True
    if SPEAKERMODE==3:
        frame22.place(x=int(-200*SCALEFACTOR),y=0)
    else:
        frame22.place(x=0,y=0)
    if SPEAKERMODE==0 or SPEAKERMODE==1:
        entrytextlist21[0].set(LEFTTIME)
        buttonlist21[0].config(state='normal')
    else:
        entrytextlist21[0].set('')
        buttonlist21[0].config(state='disabled')
    buttonlist22[0].config(state='disabled')
    if SPEAKERMODE==0 or SPEAKERMODE==2:
        entrytextlist21[1].set(RIGHTTIME)
        buttonlist21[1].config(state='normal')
    else:
        entrytextlist21[1].set('')
        buttonlist21[1].config(state='disabled')
    buttonlist22[1].config(state='disabled')
    if SPEAKERMODE==3:
        entrytextlist21[2].set(PUBLICTIME)
    else:
        entrytextlist21[2].set('')
    for i in range(3):
        entrylist21[i].config(fg='#ffffff',disabledforeground='#ffffff')
    if TIMERPAGENO==0:
        buttonlist23[0].config(state='disabled')
    else:
        buttonlist23[0].config(state='normal')
    root.update()

def TimerMgr(buttonstate):
    global TIMERPAGENO, LISTLEN, TIMERFIRSTOPENMARK
    '''
    buttonstate=0: Setup
    buttonstate=1: Page up
    buttonstate=2: Page down
    buttonstate=3: Back to settings
    buttonstate=4: Restart
    buttonstate=5: Abort
    '''
    SetCurrentFrame(2)
    if buttonstate==0:
        if TIMERFIRSTOPENMARK==True:
            TIMERFIRSTOPENMARK=False
            TimerSetup()
        TIMERPAGENO=0
        TimerRefreshPage()
    elif buttonstate==1:
        if TIMERPAGENO>0:
            TIMERPAGENO-=1
            TimerRefreshPage()
        else:
            pass
    elif buttonstate==2:
        if TIMERPAGENO<LISTLEN-1:
            TIMERPAGENO+=1
            TimerRefreshPage()
        else:
            EndDebate()
    elif buttonstate==4:
        Stop1()
        Stop2()
        Stop3()
        CheckBeforeTiming()
    elif buttonstate==5:
        Stop1()
        Stop2()
        Stop3()
        EndDebate()

def CheckBeforeTiming():
    global TimeList1,SegmentList1,SpeakerModeList,texttextlist11,LISTLEN
    TimeList1=[]
    SpeakerModeList=[]
    SegmentList1=[]
    for i in range(LISTLEN):
        SegmentList1.append(entrytextlist11[i].get())
    errormark=False
    labeltext31.set('Loading...')
    button31.place(x=int(SCALEFACTOR*16),y=int(SCALEFACTOR*128))
    button31.config(command=BackToSettings)
    SetCurrentFrame(3)
    root.update()
    for i in range(LISTLEN):
        for j in entrytextlist12[i].get().strip():
            if j<'0' or j>'9':
                labeltext31.set('''Error! 
Line {} (Segment "{}"): Please enter an integar between 1 and 9999 as the time. 
The string you have entered includes char(s) besides NUMBERS.'''.format(i+1,SegmentList1[i]))
                errormark=True
                break
        if entrytextlist12[i].get().strip()=='':
            errormark=True
            labeltext31.set('''Error! 
Line {} (Segment "{}"): Please enter an integar between 1 and 9999 as the time. 
The string you have entered is empty.'''.format(i+1,SegmentList1[i]))
        if errormark==True:
            break
        TimeList1.append(int(entrytextlist12[i].get().strip()))
        if TimeList1[i]<1 or TimeList1[i]>9999:
            if TimeList1[i]<1: labeltext31.set('''Error!
Line {} (Segment "{}"): Please enter an integar between 1 and 9999 as the time.
The number you have entered is too small.'''.format(i+1,SegmentList1[i]))
            else: labeltext31.set('''Error! 
Line {} (Segment "{}"): Please enter an integar between 1 and 9999 as the time. 
The number you have entered is too large.'''.format(i+1,SegmentList1[i]))
            errormark=True
            break
    if errormark==False:
        tottime=0
        datetime1=datetime.datetime.today()
        time.sleep(0.25)
        datetime2=datetime.datetime.today()
        interval1=(datetime2.microsecond-datetime1.microsecond-250000)%1000000/1000000
        tottime+=interval1
        STANDARDQUARTERSECOND=0.25-tottime
        for i in range(LISTLEN):
            SegmentList1.append(entrytextlist11[i].get())
            SpeakerModeList.append(checkvaluelist11[i].get())
        TimerMgr(0)

def PageButtonManage():
    global PAGENO, LISTLEN
    if PAGENO==0:
        buttonlist14[0].config(state='disabled')
    else:
        buttonlist14[0].config(state='normal')
    if PAGENO==(LISTLEN-1)//16:
        buttonlist14[1].config(state='disabled')
    else:
        buttonlist14[1].config(state='normal')

def SwapButtonManage():
    global LISTLEN, PAGENO
    if LISTLEN<17:
        buttonlist13[0].config(state='disabled')
        buttonlist13[LISTLEN].config(state='disabled')
        for i in range(1,LISTLEN):
            buttonlist13[i].config(state='normal')
    else:
        if PAGENO==0:
            for i in range(1,17):
                buttonlist13[i].config(state='normal')
            buttonlist13[0].config(state='disabled')
        elif PAGENO==(LISTLEN-1)//16:
            if LISTLEN%16==0:
                for i in range(16):
                    buttonlist13[i].config(state='normal')
                buttonlist13[16].config(state='disabled')
            else:
                for i in range(0,LISTLEN%16):
                    buttonlist13[i].config(state='normal')
                buttonlist13[LISTLEN%16].config(state='disabled')
        else:
            for i in range(17):
                buttonlist13[i].config(state='normal')

def DeleteButtonManage():
    global LISTLEN
    if LISTLEN==1:
        buttonlist11[0].config(state='disabled')
    else:
        buttonlist11[0].config(state='normal')

def FrameHeightManage():
    global PAGENO, LISTLEN
    if PAGENO==(LISTLEN-1)//16:
        if LISTLEN%16==0:
            frame103.config(height=int(SCALEFACTOR*512))
            frame104.config(height=int(SCALEFACTOR*544))
        else:
            frame103.config(height=int(SCALEFACTOR*(LISTLEN%16)*32))
            frame104.config(height=int(SCALEFACTOR*((LISTLEN%16)*32+32)))
    else:
        frame103.config(height=int(SCALEFACTOR*512))
        frame104.config(height=int(SCALEFACTOR*544))
    frame102.config(height=int(SCALEFACTOR*LISTLEN*32))
    PageButtonManage()
    SwapButtonManage()
    DeleteButtonManage()

def PageUp1():
    global PAGENO
    if PAGENO>0:
        PAGENO-=1
        frame102.place(x=0,y=int(SCALEFACTOR*(-512)*PAGENO))
    PageButtonManage()
    FrameHeightManage()

def PageDown1():
    global PAGENO
    if PAGENO<(LISTLEN-1)//16:
        PAGENO+=1
        frame102.place(x=0,y=int(SCALEFACTOR*(-512)*PAGENO))
    PageButtonManage()
    FrameHeightManage()

def ListDelPublic(lineno):
    global PAGENO, LISTLEN
    for i in range(16*PAGENO+lineno,LISTLEN-1):
        entrytextlist11[i].set(entrytextlist11[i+1].get())
        entrytextlist12[i].set(entrytextlist12[i+1].get())
        checkvaluelist11[i].set(checkvaluelist11[i+1].get())
    labellist11[LISTLEN-1].destroy()
    del labellist11[LISTLEN-1]
    del labeltextlist11[LISTLEN-1]
    entrylist11[LISTLEN-1].destroy()
    del entrylist11[LISTLEN-1]
    del entrytextlist11[LISTLEN-1]
    entrylist12[LISTLEN-1].destroy()
    del entrylist12[LISTLEN-1]
    del entrytextlist12[LISTLEN-1]
    for i in range(4):
        checklist11[LISTLEN-1][0].destroy()
    del checklist11[LISTLEN-1]
    del checkvaluelist11[LISTLEN-1]
    LISTLEN-=1
    if LISTLEN==PAGENO*16:
        PageUp1()
    FrameHeightManage()
    SwapButtonManage()
    DeleteButtonManage()

def ListInsPublic(lineno):
    global PAGENO, LISTLEN, TITLETEXTWIDTH
    labeltextlist11.append(tk.StringVar())
    labeltextlist11[LISTLEN].set(LISTLEN+1)
    labellist11.append(tk.Label(frame102,textvariable=labeltextlist11[LISTLEN],fg='#ffffff',bg='#000000'))
    labellist11[LISTLEN].place(x=0,y=int(SCALEFACTOR*(32*LISTLEN+4)))
    entrytextlist11.append(tk.StringVar())
    entrylist11.append(tk.Entry(frame102,textvariable=entrytextlist11[LISTLEN],font='consolas 11',width=TITLETEXTWIDTH,fg='#ffffff',bg='#000000',relief='flat',bd=0,highlightbackground='#7f7f7f',highlightcolor='#ffffff',highlightthickness=int(2*SCALEFACTOR),insertbackground='#ffffff'))
    entrylist11[LISTLEN].place(x=int(SCALEFACTOR*48),y=int(SCALEFACTOR*(32*LISTLEN+4)))
    entrytextlist12.append(tk.StringVar())
    entrylist12.append(tk.Entry(frame102,textvariable=entrytextlist12[LISTLEN],font='consolas 11',width=4,fg='#ffffff',bg='#000000',relief='flat',bd=0,highlightbackground='#7f7f7f',highlightcolor='#ffffff',highlightthickness=int(2*SCALEFACTOR),insertbackground='#ffffff'))
    entrylist12[LISTLEN].place(x=int(SCALEFACTOR*(60+TITLETEXTWIDTH*8)),y=int(SCALEFACTOR*(32*LISTLEN+4)))
    checkvaluelist11.append(tk.IntVar())
    checklist11.append([])
    for i in range(4):
        checklist11[LISTLEN].append(tk.Radiobutton(frame102,fg='#ffffff',bg='#000000',selectcolor='#000000',variable=checkvaluelist11[LISTLEN],value=i))
        checklist11[LISTLEN][i].place(x=int(SCALEFACTOR*(i*32+132+TITLETEXTWIDTH*8)),y=int(SCALEFACTOR*(LISTLEN*32+4)))
    for i in range(LISTLEN,PAGENO*16+lineno,-1):
        entrytextlist11[i].set(entrytextlist11[i-1].get())
        entrytextlist12[i].set(entrytextlist12[i-1].get())
        checkvaluelist11[i].set(checkvaluelist11[i-1].get())
    entrytextlist11[16*PAGENO+lineno].set('')
    entrytextlist12[16*PAGENO+lineno].set('')
    checkvaluelist11[16*PAGENO+lineno].set(0)
    LISTLEN+=1
    if lineno==16:
        PageDown1()
    FrameHeightManage()
    SwapButtonManage()
    DeleteButtonManage()

def ListSwpPublic(lineno):
    global PAGENO, LISTLEN
    tempstring=entrytextlist11[16*PAGENO+lineno].get()
    entrytextlist11[16*PAGENO+lineno].set(entrytextlist11[16*PAGENO+lineno-1].get())
    entrytextlist11[16*PAGENO+lineno-1].set(tempstring)
    tempstring=entrytextlist12[16*PAGENO+lineno].get()
    entrytextlist12[16*PAGENO+lineno].set(entrytextlist12[16*PAGENO+lineno-1].get())
    entrytextlist12[16*PAGENO+lineno-1].set(tempstring)
    tempint=checkvaluelist11[16*PAGENO+lineno].get()
    checkvaluelist11[16*PAGENO+lineno].set(checkvaluelist11[16*PAGENO+lineno-1].get())
    checkvaluelist11[16*PAGENO+lineno-1].set(tempint)

def ListDel0():
    #ListDel
    ListDelPublic(0)

def ListDel1():
    #ListDel
    ListDelPublic(1)

def ListDel2():
    #ListDel
    ListDelPublic(2)

def ListDel3():
    #ListDel
    ListDelPublic(3)

def ListDel4():
    #ListDel
    ListDelPublic(4)

def ListDel5():
    #ListDel
    ListDelPublic(5)

def ListDel6():
    #ListDel
    ListDelPublic(6)

def ListDel7():
    #ListDel
    ListDelPublic(7)

def ListDel8():
    #ListDel
    ListDelPublic(8)

def ListDel9():
    #ListDel
    ListDelPublic(9)

def ListDel10():
    #ListDel
    ListDelPublic(10)

def ListDel11():
    #ListDel
    ListDelPublic(11)

def ListDel12():
    #ListDel
    ListDelPublic(12)

def ListDel13():
    #ListDel
    ListDelPublic(13)

def ListDel14():
    #ListDel
    ListDelPublic(14)

def ListDel15():
    #ListDel
    ListDelPublic(15)

#--------

def ListIns0():
    #ListIns
    ListInsPublic(0)

def ListIns1():
    #ListIns
    ListInsPublic(1)

def ListIns2():
    #ListIns
    ListInsPublic(2)

def ListIns3():
    #ListIns
    ListInsPublic(3)

def ListIns4():
    #ListIns
    ListInsPublic(4)

def ListIns5():
    #ListIns
    ListInsPublic(5)

def ListIns6():
    #ListIns
    ListInsPublic(6)

def ListIns7():
    #ListIns
    ListInsPublic(7)

def ListIns8():
    #ListIns
    ListInsPublic(8)

def ListIns9():
    #ListIns
    ListInsPublic(9)

def ListIns10():
    #ListIns
    ListInsPublic(10)

def ListIns11():
    #ListIns
    ListInsPublic(11)

def ListIns12():
    #ListIns
    ListInsPublic(12)

def ListIns13():
    #ListIns
    ListInsPublic(13)

def ListIns14():
    #ListIns
    ListInsPublic(14)

def ListIns15():
    #ListIns
    ListInsPublic(15)

def ListIns16():
    #ListIns
    ListInsPublic(16)

#--------

def ListSwp0():
    #ListSwp
    ListSwpPublic(0)

def ListSwp1():
    #ListSwp
    ListSwpPublic(1)

def ListSwp2():
    #ListSwp
    ListSwpPublic(2)

def ListSwp3():
    #ListSwp
    ListSwpPublic(3)

def ListSwp4():
    #ListSwp
    ListSwpPublic(4)

def ListSwp5():
    #ListSwp
    ListSwpPublic(5)

def ListSwp6():
    #ListSwp
    ListSwpPublic(6)

def ListSwp7():
    #ListSwp
    ListSwpPublic(7)

def ListSwp8():
    #ListSwp
    ListSwpPublic(8)

def ListSwp9():
    #ListSwp
    ListSwpPublic(9)

def ListSwp10():
    #ListSwp
    ListSwpPublic(10)

def ListSwp11():
    #ListSwp
    ListSwpPublic(11)

def ListSwp12():
    #ListSwp
    ListSwpPublic(12)

def ListSwp13():
    #ListSwp
    ListSwpPublic(13)

def ListSwp14():
    #ListSwp
    ListSwpPublic(14)

def ListSwp15():
    #ListSwp
    ListSwpPublic(15)

def ListSwp16():
    #ListSwp
    ListSwpPublic(16)

def ListSetup():
    global TITLETEXTWIDTH
    labeltextlist11.append(tk.StringVar())
    labeltextlist11[0].set(1)
    labellist11.append(tk.Label(frame102,textvariable=labeltextlist11[0],fg='#ffffff',bg='#000000'))
    labellist11[0].place(x=0,y=int(SCALEFACTOR*4))
    entrytextlist11.append(tk.StringVar())
    entrylist11.append(tk.Entry(frame102,textvariable=entrytextlist11[0],font='consolas 11',width=TITLETEXTWIDTH,fg='#ffffff',bg='#000000',relief='flat',bd=0,highlightbackground='#7f7f7f',highlightcolor='#ffffff',highlightthickness=int(SCALEFACTOR*2),insertbackground='#ffffff'))
    entrylist11[0].place(x=int(SCALEFACTOR*48),y=int(SCALEFACTOR*4))
    entrytextlist12.append(tk.StringVar())
    entrylist12.append(tk.Entry(frame102,textvariable=entrytextlist12[0],font='consolas 11',width=4,fg='#ffffff',bg='#000000',relief='flat',bd=0,highlightbackground='#7f7f7f',highlightcolor='#ffffff',highlightthickness=int(SCALEFACTOR*2),insertbackground='#ffffff'))
    entrylist12[0].place(x=int(SCALEFACTOR*(60+TITLETEXTWIDTH*8)),y=int(SCALEFACTOR*4))
    checkvaluelist11.append(tk.IntVar())
    checklist11.append([])
    for i in range(4):
        checklist11[0].append(tk.Radiobutton(frame102,fg='#ffffff',bg='#000000',selectcolor='#000000',variable=checkvaluelist11[0],value=i))
        checklist11[0][i].place(x=int(SCALEFACTOR*(i*32+132+TITLETEXTWIDTH*8)),y=int(SCALEFACTOR*4))
    for i in range(16):
        buttonlist11.append(tk.Button(frame103,text='Delete',fg='#ffffff',bg='#3f3f3f',font=('Microsoft YaHei UI',9),disabledforeground='#7f7f7f',relief='flat',bd=0))
        eval('buttonlist11[{}].config(command=ListDel{})'.format(i,i))
        buttonlist11[i].place(x=0,y=int(SCALEFACTOR*(i*32+4)))
    for i in range(17):
        buttonlist12.append(tk.Button(frame104,text='Insert',fg='#ffffff',bg='#3f3f3f',font=('Microsoft YaHei UI',9),disabledforeground='#7f7f7f',relief='flat',bd=0))
        buttonlist12[i].place(x=0,y=int(SCALEFACTOR*(i*32+4)))
        buttonlist13.append(tk.Button(frame104,text='Swap',fg='#ffffff',bg='#3f3f3f',font=('Microsoft YaHei UI',9),disabledforeground='#7f7f7f',relief='flat',bd=0))
        buttonlist13[i].place(x=int(SCALEFACTOR*48),y=int(SCALEFACTOR*(i*32+4)))
        eval('buttonlist12[{}].config(command=ListIns{})'.format(i,i))
        eval('buttonlist13[{}].config(command=ListSwp{})'.format(i,i))
    buttonlist14[0].place(x=int(SCALEFACTOR*8),y=int(SCALEFACTOR*568))
    buttonlist14[1].place(x=int(SCALEFACTOR*80),y=int(SCALEFACTOR*568))
    buttonlist14[0].config(command=PageUp1)
    buttonlist14[1].config(command=PageDown1)
    button15.config(command=CheckBeforeTiming)
    button15.place(x=int(SCALEFACTOR*452)+int(SCALEFACTOR*TITLETEXTWIDTH*8)+(FRAMEWIDTH-SCALEFACTOR*(496+(TITLETEXTWIDTH+TEAMNAMEWIDTH)*8))//2,y=int(SCALEFACTOR*500))
    entrylist13[0].place(x=int(SCALEFACTOR*16),y=int(SCALEFACTOR*88))
    entrylist13[1].place(x=int(SCALEFACTOR*16),y=int(SCALEFACTOR*304))
    textlist11[0].place(x=int(SCALEFACTOR*16),y=int(SCALEFACTOR*152))
    textlist11[1].place(x=int(SCALEFACTOR*16),y=int(SCALEFACTOR*368))
    checkbutton11.config(command=ChangeTopMost)
    checkbutton11.place(x=int(SCALEFACTOR*452)+int(SCALEFACTOR*TITLETEXTWIDTH*8)+(FRAMEWIDTH-SCALEFACTOR*(496+(TITLETEXTWIDTH+TEAMNAMEWIDTH)*8))//2,y=int(SCALEFACTOR*472))
    PageButtonManage()
    DeleteButtonManage()
    SwapButtonManage()

def PreDebate():
    global LISTFIRSTOPENMARK, TEAMNAMEWIDTH, FRAMEWIDTH
    versioninfo.place(x=SCREENWIDTH,y=SCREENHEIGHT)
    for i in range(2):
        entrytextlist13.append(tk.StringVar())
        texttextlist11.append("")
        entrylist13.append(tk.Entry(frame11,textvariable=entrytextlist13[i],font=('Consolas',11),width=TEAMNAMEWIDTH,fg='#ffffff',bg='#000000',relief='flat',bd=0,highlightbackground='#7f7f7f',highlightcolor='#ffffff',highlightthickness=int(SCALEFACTOR*2),insertbackground='#ffffff'))
        textlist11.append(tk.Text(frame11,font=('Consolas',11),height=3,width=TEAMNAMEWIDTH,fg='#ffffff',bg='#000000',relief='flat',bd=0,highlightbackground='#7f7f7f',highlightcolor='#ffffff',highlightthickness=int(SCALEFACTOR*2),insertbackground='#ffffff',wrap='word'))
    if LISTFIRSTOPENMARK==True:
        LISTFIRSTOPENMARK=False
        ListSetup()
    titletext1.set('Debate settings')
    SetCurrentFrame(1)

def WelcomePageMgr():
    SetCurrentFrame(0)
    global FRAMEHEIGHT
    checkbuttonvalue11and21.set(0)
    ChangeTopMost()
    frame0.place(x=0,y=int(SCALEFACTOR*120))
    titletext1.set('Debate Timer')
    versioninfo.place(x=int(SCALEFACTOR*4),y=int(SCREENHEIGHT-40*SCALEFACTOR))
    button01.config(command=PreDebate)
    closebutton.config(command=CloseProgram)

def Main():
    global SCREENHEIGHT, SCREENWIDTH
    tottime=0
    SetCurrentFrame(5)
    ShowWindow()
    labeltext51.set('Loading...')
    root.update()
    if SCREENHEIGHT<720 or SCREENWIDTH<1280:
        labeltext51.set('''Ooops! Something went wrong!
        The valid resolution of your monitor has not met the minium requirement of this program.
        Your valid resolution: {}x{}. Minium requirement: 1280x720.
        Perhaps you can try the ways below and restart this program.
        - Connect your PC to a monitor with higher resolution.
        '''.format(int(SCREENWIDTH),int(SCREENHEIGHT)))
    elif SCREENHEIGHT>SCREENWIDTH:
        labeltext51.set('''Ooops! Something went wrong!
        Your display mode is protrait.
        Please go to your system settings to change display mode.
        ''')
    else:
        WelcomePageMgr()

if __name__=="__main__":
    Main()
    tk.mainloop()
