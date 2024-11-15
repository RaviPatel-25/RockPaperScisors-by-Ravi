from tkinter import*
from PIL import ImageTk, Image
import random

class Game:
	def __init__(self,root):
		self.root = root
		self.root.geometry("1080x2129+0+0")
		self.root.resizable(False,False)
		self.root.overrideredirect(True)
		self.root.config(bg="white")
		
		self.ptext = StringVar()
		
		path = "/storage/emulated/0/RockPaperScissor/"
		
		self.rock = path + "Rock.jpg"
		self.paper = path + "Paper.jpg"
		self.scissor = path + "Scissor.jpg"
		self.blank = path + "Blank.jpg"
		
		self.rock = Image.open(self.rock)
		self.paper = Image.open(self.paper)
		self.scissor = Image.open(self.scissor)
		self.blank = Image.open(self.blank)
		
		self.rock = self.rock.resize((300, 300))
		self.paper = self.paper.resize((300, 300))
		self.scissor = self.scissor.resize((300, 300))
		self.blank = self.blank.resize((300, 300))
		
		self.rockcom = self.rock.rotate(90)
		self.papercom = self.paper.rotate(90)
		self.scissorcom = self.scissor.rotate(90)
		
		self.rockcom = ImageTk.PhotoImage(self.rockcom)
		self.papercom = ImageTk.PhotoImage(self.papercom)
		self.scissorcom = ImageTk.PhotoImage(self.scissorcom)
		
		self.rock = self.rock.rotate(270)
		self.paper = self.paper.rotate(270)
		self.scissor = self.scissor.rotate(270)
		
		self.rock = ImageTk.PhotoImage(self.rock)
		self.paper = ImageTk.PhotoImage(self.paper)
		self.scissor = ImageTk.PhotoImage(self.scissor)
		self.blank = ImageTk.PhotoImage(self.blank)
		
		self.label = Label(self.root, text = " Rock Paper Scissor ", bg="#00FF0A",font = ("Arial",18,"bold"))
		
		self.turnlabel = Label(self.root,text ="Let's Play",bg="white",font=("Arial",10,"bold","italic"))
		
		self.you = Label(self.root,text="You",bg="white")
		self.comp = Label(self.root,text="Comp",bg="white")
		
		self.rockbtn = Button(self.root,bd=7,text="Rock",bg="#00A0E8",font=("Arial",8,"bold"),command=self.prock)
		self.paperbtn = Button(self.root,bd=7,text="Paper",bg="yellow",font=("Arial",8,"bold"),command=self.ppaper)
		self.scissorbtn = Button(self.root,bd=7,text="Scissor",bg="red",font=("Arial",8,"bold"),command=self.pscissor)
		
		self.info = Label(self.root,text=" Choose and Press any one Button ",bg="white")
		
		self.plrlabel = Label(self.root,image=self.blank)
		self.plabel = Label(self.root,text="",bg="white",textvariable=self.ptext,font=("Arial",10,"bold"))
		
		self.comlabel = Label(self.root,image=self.blank)
		self.clabel = Label(self.root,text="",bg="white",font=("Arial",10,"bold"))
		
		self.result = Label(self.root,text="",bg="white",font=("Arial",10,"bold"))
		
		self.resetbtn = Button(self.root,bd=7,text="Reset",bg="gray",font=("Arial",10,"bold"),command=self.reset)
		
	def main(self):
		self.label.place(x=60,y=50)
		self.turnlabel.place(x=400,y=250)
		self.you.place(x=190,y=340)
		self.comp.place(x=780,y=340)
		self.rockbtn.place(x=150,y=1000,width=200,height=100)
		self.paperbtn.place(x=450,y=1000,width=200,height=100)
		self.scissorbtn.place(x=750,y=1000,width=200,height=100)
		
		self.info.place(x=200,y=900)
		
		self.plrlabel.place(x=80,y=400)
		self.plabel.place(x=100,y=720)
		self.comlabel.place(x=700,y=400)
		self.clabel.place(x=730,y=720)
		
		self.result.place(x=370,y=1200)
		
		self.resetbtn.place(x=440,y=1300)
	
	def prock(self):
		self.plrlabel.config(image=self.rock)
		self.ptext.set("Rock")
		self.computer()
		
	def ppaper(self):
		self.plrlabel.config(image=self.paper)
		self.ptext.set("Paper")
		self.computer()
		
	def pscissor(self):
		self.plrlabel.config(image=self.scissor)
		self.ptext.set("Scissor")
		self.computer()
		
	def crock(self):
		self.comlabel.config(image=self.rockcom)
		self.clabel.config(text="Rock")
		
	def cpaper(self):
		self.comlabel.config(image=self.papercom)
		self.clabel.config(text="Paper")
		
	def cscissor(self):
		self.comlabel.config(image=self.scissorcom)
		self.clabel.config(text="Scissor")
		
	def computer(self):
		self.choose = ["rock","paper","scissor"]
		choice = random.choice(self.choose)
		
		if choice=="rock":
			self.crock()
		elif choice=="paper":
			self.cpaper()
		else:
			self.cscissor()
			
		ply = self.ptext.get()
		
		if ply=="Rock" and choice=="scissor":
			self.result.config(text="You Win")
		elif ply=="Paper" and choice=="rock":
			self.result.config(text="You Win")
		elif ply=="Scissor" and choice=="paper":
			self.result.config(text="You Win")
		elif ply=="Rock" and choice=="rock":
			self.result.config(text="Game Draw")
		elif ply=="Paper" and choice=="paper":
			self.result.config(text="Game Draw")
		elif ply=="Scissor" and choice=="scissor":
			self.result.config(text="Game Draw")
		else:
			self.result.config(text="Computer Win")
		
	def reset(self):
		self.plrlabel.config(image=self.blank)
		self.comlabel.config(image=self.blank)
		self.result.config(text="")
		self.ptext.set("")
		self.clabel.config(text="")
		
root = Tk()
obj = Game(root)
obj.main()
root.mainloop()