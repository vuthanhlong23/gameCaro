from tkinter import* 
from math import*
from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import ttk
import tkinter


def info():
    six=tkinter.Tk()
    six.geometry('200x200+200+200')
    text = Label(six, text="Leader:Dao \n Secretary: An \n Developer: Minh, Phuc, Long")
    text.grid(column=10,row=10)

def Setting():
    new=tkinter.Tk()
    new.geometry('400x400')
    bar=Scale(new,orient=HORIZONTAL,from_=0,to =10,tickinterval=1,sliderlength=15,length=150)
    bar.place(x=20,y=10)

two=Tk()
three=Canvas(two,width =900, height = 630,background="#f4bc42")
three.pack()

label = Label(two,text="GAME\nCARO",bg="#f4bc42",font="none 60 bold")
label.place(x=350,y=100)
blue=Button(two,text="New Game",font="none 10 bold",width=15,height=3,command=two.destroy)
blue.place(x=400,y=350)
red=Button(two,text="Group Informaton",font="none 10 bold",width=15,height=3,command=info)
red.place(x=400,y=430)
Sett=Button(two,text="Settings",font="none 10 bold",width=15,height=3,command=Setting)
Sett.place(x=400,y=510)
two.mainloop()

class Example(Frame):
   def __init__(self, parent):
       Frame.__init__(self, parent)
       self.parent = parent
       self.initUI()

   def initUI(self):
       self.parent.title("Colors")
       self.pack(fill=BOTH, expand=1)

       canvas = Canvas(self)
       canvas.create_rectangle(30, 10, 900, 800, outline="#00ffff", fill="#00ffff")
       canvas.pack(fill=BOTH, expand=1)
       green=ttk.Button(canvas,text="Quit",command=lambda:[f() for f in[caro.destroy]])
       green.pack()
       yellow=ttk.Button(canvas,text="2 player :)",command=reset)
       yellow.pack()

def reset():
    board.delete("all")
    x1.clear()
    y1.clear()
    x2.clear()
    y2.clear()
    Arrayx.clear()
    Arrayy.clear()
    dem=0
    veBanCo()



caro=Tk()
board = Canvas( caro, width = 630, height = 630,background="#f4bc42")
board.pack(side = LEFT)

ex = Example(caro)

for i in range(0,21):
	board.create_line(i*30,30,i*30,600)
	board.create_line(30,i*30,600,i*30)

count=0	#turn
stop=0

x1=[]		#x_cross
y1=[]		#y_cross
x2=[]		#x_circle
y2=[]		#y_circle
x3=[]		#x1'=630-x1
y3=[]		#y1'=630-y1
x4=[]		#x2'=630-x2
y4=[]		#y2'=630-y2
Arrayx=[] 	#incoincidence
Arrayy=[]	#incoincidence

def save_cross(x,y):
	x1.append(x)
	y1.append(y)
	x3.append(630-x)
	y3.append(630-y)
	
def save_circle(x,y):
	x2.append(x)
	y2.append(y)
	x4.append(630-x)
	y4.append(630-y)
	
def save(x,y):
	Arrayx.append(x)
	Arrayy.append(y)
	
def check(x,y):
	for i in range (len(Arrayx)):
		if x==Arrayx[i] and y==Arrayy[i]:
			return 1
	return 0
	
def check_cross(x,y):
	for i in range(len(x1)):
		if x==x1[i] and y==y1[i]:
			return 1
	return 0
	
def check_circle(x,y):
	for i in range(len(x2)):
		if x==x2[i] and y==y2[i]:
			return 1
	return 0

def draw_cross(x,y):
	board.create_line(x-10,y-10,x+10,y+10,fill="red",width=3)
	board.create_line(x+10,y-10,x-10,y+10,fill="red",width=3)
	
def draw_circle(x,y):
	board.create_oval(x-10,y-10,x+10,y+10,outline="green",width=3)

def point(p):
	a=int((p/10))
	a=a*10
	i=0
	for i in range (0,15):
		if ((a-i)%30 ==0):
			a=a-i
			break
	if (i<15):
		for i in range (0,15):
			if ((a+i)%30 ==0):
				a=a+i
				break
	return a			
		
def Straight(x,y,x1,y1,x2,y2): #Done
	def Leftest(x,y,x1,y1,x2,y2):
		countLeft1=0
		countRight1=0
		block1=0
		for i in range(len(x1)):
			if y==y1[i]:
				for j in range (1,5): # 1,2,3,4
					if (x-j*30)==x1[i]: 
						countLeft1+=1 #max->4
				if (x+30)==x1[i]:
					countRight1+=1 #Right="wrong"
		for k in range(len(x2)):
			if y==y2[k]:
				if (x+30)==x2[k] or (x-5*30)==x2[k]:
					block1+=1
		if block1<2 and countLeft1==4 and countRight1==0:
			return 1
		return 0		
	
	def Mid(x,y,x1,y1,x2,y2):
		countmidleft=0
		countmidright=0
		blockmid=0
		sixthmid=0
		for i in range(len(x1)):
			if y==y1[i]:
				for j in range (1,3):# 1,2
					if (x-j*30)==x1[i]: 
						countmidleft+=1
					if (x+j*30)==x1[i]:
						countmidright+=1
				if (x-3*30)==x1[i] or (x+3*30)==x1[i]:
					sixthmid+=1		
		for k in range(len(x2)):
			if y==y2[k]:
				if (x+3*30)==x2[k] or (x-3*30)==x2[k]:
					blockmid+=1			
		if countmidleft==2 and countmidright==2 and blockmid<2 and sixthmid==0:
			return 1
		return 0	
	#3 and 1	
	def AnotherPlace(x,y,x1,y1,x2,y2):
		countLeft3 =0
		countRight3=0
		block3=0
		sixth3=0
		for i in range(len(x1)):
			if y==y1[i]:
				for j in range(1,4): #1,2,3
					if (x-j*30)==x1[i]:
						countLeft3+=1 #-->max=3
				if (x+30)==x1[i]:
					countRight3+=1
				if (x-4*30)==x1[i] or (x+2*30)==x1[i] :
					sixth3+=1		
		for k in range (len(x2)):				
			if y==y2[k]:				
				if (x+2*30)==x2[k] or (x-4*30)==x2[k]:
					block3+=1
		if countLeft3==3 and countRight3==1 and sixth3==0 and block3<2:
			return 1
		return 0	

	if AnotherPlace(x,y,x1,y1,x2,y2) or Mid(x,y,x1,y1,x2,y2) or Leftest(x,y,x1,y1,x2,y2):
		return 1
	return 0
		
def Skew(x,y,x1,y1,x2,y2):	#Done
	#UptoRight
	def UR_First(x,y,x1,y1,x2,y2):
		UR_count1left=0
		UR_count1right=0
		UR_block1=0
		for i in range (len(x1)):
			for j in range(1,5): #1,2,3,4
				n1=y1[i]-y
				if (n1/30)==j:
					if n1==x-x1[i]:
						UR_count1left+=1
			if x1[i]-x==30 and y-y1[i]==30:
				UR_count1right+=1			
		for k in range (len(x2)):
			if (x2[k]-x)==30 and (y-y2[k])==30:
				UR_block1+=1
			if (x-x2[k])==5*30 and (y2[k]-y)==5*30:
				UR_block1+=1		
		if UR_count1left==4 and UR_block1<2 and UR_count1right==0:	
			return 1
		return 0	
			
	def UR_third(x,y,x1,y1,x2,y2):
		UR_count3left=0
		UR_count3right=0
		UR_block3=0
		UR_sixth3=0
		for i in range (len(x1)):
			for j in range(1,3): #1,2
				n3=y-y1[i]
				if abs(n3/30)==j:
					if (n3>0):
						if (x+abs(n3))==x1[i]:
							UR_count3right+=1
					if (n3<0):
						if (x-abs(n3))==x1[i]:
							UR_count3left+=1
			if (x1[i]-x)==3*30 and (y-y1[i])==3*30:
				UR_sixth3+=1
			if (x-x1[i])==3*30 and (y1[i]-y)==3*30:
				UR_sixth3+=1			
		for k in range (len(x2)):					
			if (x2[k]-x)==3*30 and (y-y2[k])==3*30:
				UR_block3+=1
			if (x-x2[k])==3*30 and (y2[k]-y)==3*30:
				UR_block3+=1			
		if UR_count3left==2 and UR_count3right==2 and UR_block3<2 and UR_sixth3==0:
			return 1
		return 0	
		
	def UR_second(x,y,x1,y1,x2,y2):
		UR_count2left=0
		UR_count2right=0
		UR_block2=0
		UR_sixth2=0
		for i in range(len(x1)):
			if y-y1[i]==30 and x1[i]-x==30: #1 upper right
				UR_count2right+=1
			for j in range(1,4): #1,2,3 lower left
				n2=(y1[i]-y)   
				if (n2/30)==j:
					if (x-n2)==x1[i]:
						UR_count2left+=1
			if x1[i]-x==2*30 and y-y1[i]==2*30:
				UR_sixth2+=1	
			if x-x1[i]==4*30 and y1[i]-y==4*30:
				UR_sixth2+=1
		for k in range(len(x2)):				
			if x2[k]-x==2*30 and y-y2[k]==2*30:
				UR_block2+=1
			if x-x2[k]==4*30 and y2[k]-y==4*30:
				UR_block2+=1
		if UR_count2left==3 and UR_count2right==1 and UR_block2<2 and UR_sixth2==0:
			return 1
		return 0		
	
	if UR_First(x,y,x1,y1,x2,y2) or UR_third(x,y,x1,y1,x2,y2) or UR_second(x,y,x1,y1,x2,y2):
		return 1
	return 0
	
def WinCondition(x,y,x1,y1,x2,y2,x3,y3,x4,y4): 
	if Straight(x,y,x1,y1,x2,y2) or Straight(630-x,630-y,x3,y3,x4,y4) or Straight(630-y,x,y3,x1,y4,x2) or Straight(y,630-x,y1,x3,y2,x4) or Skew(x,y,x1,y1,x2,y2) or Skew(y,x,y1,x1,y2,x2) or Skew(y,630-x,y1,x3,y2,x4) or Skew(630-y,x,y3,x1,y4,x2):
		return 1
	return 0	
				
def callback(event):
	global count
	global stop	
	if stop==0 and check(point(event.x), point(event.y))==0 and check_cross (point(event.x),point(event.y))==0 and check_cross (point(event.x),point(event.y))==0 and point(event.x)!=0 and point(event.y)!=0 and point(event.x)!=630 and point(event.y)!=630:
		if count % 2==0:
			draw_cross(point(event.x), point(event.y))
			save_cross(point(event.x), point(event.y))
		else:	
			draw_circle(point(event.x), point(event.y))
			save_circle(point(event.x), point(event.y))
		count+=1
		print(count)
		print (point(event.x),point(event.y))
		save (point(event.x),point(event.y))
		if count >=9:
			if WinCondition(point(event.x),point(event.y),x1,y1,x2,y2,x3,y3,x4,y4) and check_cross(point(event.x),point(event.y)):
				print ("Player1 Win!!!")
				stop=1
			else:		
				if WinCondition(point(event.x),point(event.y),x2,y2,x1,y1,x4,y4,x3,y3) and check_circle(point(event.x),point(event.y)):
					print ("Player2 Win!!!")
					stop=1
			
board.bind("<Button-1>", callback)	

caro.mainloop()
