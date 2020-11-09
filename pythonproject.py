from tkinter  import*

score1=0
wickets=0
score3=0

class cricket:
    def __init__(self,root):
        self.root=root
        self.root.title("online crickrt score board")
        self.root.geometry('')
        self.root.config(bg="black")
        title=Label(self.root,text="Score Board")

#*************frame1*********************
        frame1=Frame(self.root)
        frame1.place(x=300,y=100,width=700,height=50)

        #**************Team-Lable****************
        self.t_name=StringVar()
        self.t_name.set("Ind")
        self.teamlbl=Label(frame1,text="",textvariable=self.t_name,font=("",15,"bold"))
        self.teamlbl.pack(side=LEFT)

        #**************Score-Lable****************
        self.scr=StringVar()
        self.scr.set("0")
        self.scorelbl=Label(frame1,text="",textvariable=self.scr,font=("",15,"bold"))
        self.scorelbl.pack(side=LEFT,padx=(10,0))

        #**************wickets-Lable****************
        self.wkt=StringVar()
        self.wkt.set("- 0")
        self.wktlbl=Label(frame1,text="",textvariable=self.wkt,font=("",15,"bold"))
        self.wktlbl.pack(side=LEFT)

        #**************over-6-boll-Lable****************
        self.ovr=StringVar()
        self.ovr.set("0")
        self.ovrlbl=Label(frame1,text="",textvariable=self.ovr,font=("",15,"bold"))
        self.ovrlbl.pack(side=LEFT,padx=(10,0))

        #**************balls-Lable****************
        self.balls=StringVar()
        self.balls.set(".0")
        self.balllbl=Label(frame1,text="",textvariable=self.balls,font=("",15,"bold"))
        self.balllbl.pack(side=LEFT)

        #**************Total-overs-Lable****************
        self.over=StringVar()
        self.over.set("/ 0")
        self.overlbl=Label(frame1,text="",textvariable=self.over,font=("",15,"bold"))
        self.overlbl.pack(side=LEFT)
        self.scr.set("0")

#****************************BATSMAN-1-Lable************************************
        self.B1=StringVar()
        self.B1.set("Sparsh")
        self.B1balllbl=Label(frame1,text="",textvariable=self.B1,font=("",15,"bold"))
        self.B1balllbl.pack(side=LEFT,padx=(15,0))

        self.B1scr=StringVar()
        self.B1scr.set("0")
        self.B1scrlbl=Label(frame1,text="",textvariable=self.B1scr,font=("",15,"bold"))
        self.B1scrlbl.pack(side=LEFT,padx=(5,0))

        self.B1ball=StringVar()
        self.B1ball.set("(0)")
        self.B1balllbl=Label(frame1,text="",textvariable=self.B1ball,font=("",15,"bold"))
        self.B1balllbl.pack(side=LEFT,padx=(15,0))

#****************************BATSMAN-2-Lable************************************
        self.B2=StringVar()
        self.B2.set("Gurdit")
        self.B2balllbl=Label(frame1,text="",textvariable=self.B2,font=("",15,"bold"))
        self.B2balllbl.pack(side=LEFT,padx=(20,0))

        self.B2scr=StringVar()
        self.B2scr.set("0")
        self.B2scrlbl=Label(frame1,text="",textvariable=self.B2scr,font=("",15,"bold"))
        self.B2scrlbl.pack(side=LEFT,padx=(5,0))

        self.B2ball=StringVar()
        self.B2ball.set("(0)")
        self.B2balllbl=Label(frame1,text="",textvariable=self.B2ball,font=("",15,"bold"))
        self.B2balllbl.pack(side=LEFT,padx=(15,0))

#*************frame2*********************
        frame2=Frame(self.root)
        frame2.place(x=300,y=300,width=700,height=300)

#**************Buttons*******************************
        totalscrlbl=Label(frame2,text="Add Score",font=("",15,"bold")).place(x=0,y=5)

        scr1btn=Button(frame2,text="+1",font=("",15,'bold'),command=scr1)
        scr1btn.place(x=0,y=40)

        scr2btn=Button(frame2,text="+2",font=("",15,'bold'),command=scr2)
        scr2btn.place(x=40,y=40)

        scr3btn=Button(frame2,text="+3",font=("",15,'bold'),command=scr3)
        scr3btn.place(x=80,y=40)

        scr4btn=Button(frame2,text="+4",font=("",15,'bold'),command=scr4)
        scr4btn.place(x=0,y=80)

        scr5btn=Button(frame2,text="+5",font=("",15,'bold'),command=scr5)
        scr5btn.place(x=40,y=80)

        scr6btn=Button(frame2,text="+6",font=("",15,'bold'),command=scr6)
        scr6btn.place(x=80,y=80)

        scrminusbtn=Button(frame2,text="-1",font=("",15,'bold'),command=scrminus)
        scrminusbtn.place(x=40,y=120)

#*****************wickets-label-and batsman*******************
        totalwktlbl=Label(frame2,text="Add WICKETS",font=("",15,"bold")).place(x=0,y=170)

        wktbtn=Button(frame2,text="+1",font=("",15,'bold'),command=wicket)
        wktbtn.place(x=10,y=210)

        wktbtn=Button(frame2,text="-1",font=("",15,'bold'),command=_wicket)
        wktbtn.place(x=80,y=210)

#**************BATSMAN-1 SCORE INCREMENT BUTTONS*******************************
        B1scrlbl=Label(frame2,text="Add B1 Score",font=("",15,"bold")).place(x=200,y=5)

        B1scrbtn=Button(frame2,text="+1",font=("",15,'bold'))
        B1scrbtn.place(x=200,y=40)

        B1scrbtn=Button(frame2,text="+2",font=("",15,'bold'))
        B1scrbtn.place(x=240,y=40)

        B1scrbtn=Button(frame2,text="+3",font=("",15,'bold'))
        B1scrbtn.place(x=280,y=40)

        B1scrbtn=Button(frame2,text="+4",font=("",15,'bold'))
        B1scrbtn.place(x=200,y=80)

        B1scrbtn=Button(frame2,text="+5",font=("",15,'bold'))
        B1scrbtn.place(x=240,y=80)

        B1scrbtn=Button(frame2,text="+6",font=("",15,'bold'))
        B1scrbtn.place(x=280,y=80)

        B1scrbtn=Button(frame2,text="-1",font=("",15,'bold'))
        B1scrbtn.place(x=240,y=120)

#*****************batsman-1-balls played*******************

        B1ballplylbl=Label(frame2,text="B1 Balls Played",font=("",15,"bold")).place(x=200,y=170)

        B1ball1btn=Button(frame2,text="+1",font=("",15,'bold'))
        B1ball1btn.place(x=200,y=210)

        B1ball1minusbtn=Button(frame2,text="-1",font=("",15,'bold'))
        B1ball1minusbtn.place(x=280,y=210)


#**************BATSMAN-2 SCORE INCREMENT BUTTONS*******************************
        B2scrlbl=Label(frame2,text="Add B1 Score",font=("",15,"bold")).place(x=400,y=5)

        B2scrbtn=Button(frame2,text="+1",font=("",15,'bold'))
        B2scrbtn.place(x=400,y=40)

        B2scrbtn=Button(frame2,text="+2",font=("",15,'bold'))
        B2scrbtn.place(x=440,y=40)

        B2scrbtn=Button(frame2,text="+3",font=("",15,'bold'))
        B2scrbtn.place(x=480,y=40)

        B2scrbtn=Button(frame2,text="+4",font=("",15,'bold'))
        B2scrbtn.place(x=400,y=80)

        B2scrbtn=Button(frame2,text="+5",font=("",15,'bold'))
        B2scrbtn.place(x=440,y=80)

        B2scrbtn=Button(frame2,text="+6",font=("",15,'bold'))
        B2scrbtn.place(x=480,y=80)

        B2scrbtn=Button(frame2,text="-1",font=("",15,'bold'))
        B2scrbtn.place(x=440,y=120)

#*****************batsman-2-balls played*******************

        B2ballplylbl=Label(frame2,text="B2 Balls Played",font=("",15,"bold")).place(x=400,y=170)

        B2ball1btn=Button(frame2,text="+1",font=("",15,'bold'))
        B2ball1btn.place(x=400,y=210)

        B2ball1minusbtn=Button(frame2,text="-1",font=("",15,'bold'))
        B2ball1minusbtn.place(x=480,y=210)

#*****************TOTAL-BALLS INC-BUTTON*******************
        t_ballslbl=Label(frame2,text="Add tolal balls",font=("",15,"bold")).place(x=550,y=5)

        self.t_ballsbtn=Button(frame2,text="+1",font=("",15,'bold'))
        self.t_ballsbtn.place(x=550,y=40)

        self.t_ballsbtn=Button(frame2,text="-1",font=("",15,'bold'))
        self.t_ballsbtn.place(x=650,y=40)

#*******************Frame-3*************************************
        frame3=Frame(self.root)
        frame3.place(x=300,y=650,width=700,height=200)

        t_overlbl=Label(frame3,text="Enter total Overs",font=("",15,'bold')).place(x=10,y=20)
        self.t_overentry=Entry(frame3,font=("",10,'bold'))
        self.t_overentry.place(x=10,y=50)

        t_overbtn=Button(frame3,text="UPDATE",font=("",12,'bold'),command=update_over)
        t_overbtn.place(x=40,y=100)

        B1namelbl=Label(frame3,text="Enter BATSMAN-1",font=("",12,'bold')).place(x=190,y=20)

        self.B1name_entry=Entry(frame3,font=("",10,'bold'))
        self.B1name_entry.place(x=190,y=50)

        B1namebtn=Button(frame3,text="UPDATE",font=("",12,'bold'))
        B1namebtn.place(x=210,y=100)

        B2namelbl=Label(frame3,text="Enter BATSMAN-2",font=("",12,'bold')).place(x=360,y=20)
        self.B2name_entry=Entry(frame3,font=("",10,'bold'))
        self.B2name_entry.place(x=360,y=50)

        B2namebtn=Button(frame3,text="UPDATE",font=("",12,'bold'))
        B2namebtn.place(x=400,y=100)

        teamnamelbl=Label(frame3,text="Enter Team Name",font=("",12,'bold')).place(x=530,y=20)
        self.teamname_entry=Entry(frame3,font=("",10,'bold'))
        self.teamname_entry.place(x=530,y=50)

        teamnamebtn=Button(frame3,text="UPDATE",font=("",12,'bold'))
        teamnamebtn.place(x=590,y=100)



def scr1(self):
        global score1
        score1 +=1  
        self.scr.set(score1)

def scr2(self):
        global score1
        score1 +=2  
        self.scr.set(score1)

def scr3(self):
        global score1
        score1 +=3  
        self.scr.set(score1)

def scr4(self):
        global score1
        score1 +=4  
        self.scr.set(score1)

def scr5(self):
        global score1
        score1 +=5  
        self.scr.set(score1)

def scr6(self):
        global score1
        score1 +=6  
        self.scr.set(score1)

def scrminus(self):
        global score1
        score1 -=1  
        self.scr.set(score1)

def wicket(self):
        global wickets
        wickets+=1
        w=self.wkt.set("-"+str(wickets))
        if wicket==10:
                wktbtn.set(" ")
                wickets=0
def _wicket(self):
        global wickets
        wickets-=1
        self.wkt.set("-"+str(wickets)) 
def update_over(self):
        a=self.t_oversentry.get()
        self.over.set("/"+a)
        self.t_oversentry.delete(0,'end')


#B1-score**********
def B1scr1(self):
        global score2
        score2+=1
        self.B1scr.set(score2)


def B1scr2(self):
        global score2
        score2+=2
        self.B1scr.set(score2)

def B1scr3(self):
        global score2
        score2+=3
        self.B1scr.set(score2)

def B1scr4(self):
        global score2
        score2+=4
        self.B1scr.set(score2)

def B1scr5(self):
        global score2
        score2+=5
        self.B1scr.set(score2)

def B1scr6(self):
        global score2
        score2+=6
        self.B1scr.set(score2)

def B1scrminus(self):
        global score2
        score2-=1
        self.B1scr.set(score2)


#B1-score**************


def B2scr1(self):
        global score2
        score2+=1
        self.B1scr.set(score2)


def B2scr2(self):
        global score3
        score3+=2
        self.B1scr.set(score3)

def B2scr3(self):
        global score3
        score3+=3
        self.B1scr.set(score3)

def B2scr4(self):
        global score3
        score3+=4
        self.B1scr.set(score3)

def B2scr5(self):
        global score3
        score3+=5
        self.B1scr.set(score3)

def B2scr6(self):
        global score3
        score3+=6
        self.B1scr.set(score3)

def B2scrminus(self):
        global score3
        score3-=1
        self.B1scr.set(score3)




root=Tk()
obj=cricket(root)
root.mainloop()