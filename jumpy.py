#Python program for Jumbled game concept
from tkinter import*
global p1
global p2
global pp1
global pp2

def ques():
    global ans
    global question
    import random
    words =["rainbow","orange","apple","banana","sugarcane"]
    ans=random.choice(words)
    question="".join(random.sample(ans,len(ans)))
    return question
def close1():
    root1.destroy()

def thank():
    p1=name.get()
    p2=name2.get()
    global root1
    root1=Tk()
    root1.title("FINAL SCORES ")
    root1.geometry("300x250")
    l1 =Label(root1,text=p1,fg="black",bg="red").pack(fill="x")
    l2 =Label(root1,text=pp1,fg="black",bg="red").pack(fill="x")
    l3 =Label(root1,text=p2,fg="black",bg="green").pack(fill="x")
    l4 =Label(root1,text=pp2,fg="black",bg="green").pack(fill="x")
    l5 =Label(root1,text="Thank You for playing the game",fg="black",bg="red").pack(fill="x")
    b_0 =Button(root1,text="CLOSE",command=close1).pack()
    root1.mainloop()
    

    
def play():
    root.destroy()
    p1=name.get()
    p2=name2.get()
    turn=0
    global pp1
    global pp2
    pp1=0
    pp2=0
    
    while 1:
        if (turn%2==0):
            print(p1,"turn")
            print("The question is ",ques())
            player_ans=input("Your ans = ")
            if (player_ans==ans):
                pp1=pp1+1
                print("Congratulations ur score is =",pp1)                                    
            else:
                print("oops the ans is =",ans)
            print("press 1 to continue or 0 to exit")
            c=int(input())
            if (c==0):
                thank()
                break
        else:
            print(p2,"turn")
            print("The question is ",ques())
            player_ans=input("Your ans = ")
            if (player_ans==ans):
                pp2=pp2+1
                print("Congratulations ur score is =",pp2)                                    
            else:
                print("oops the ans is =",ans)
            print("press 1 to continue or 0 to exit")
            c=int(input())
            if (c==0):
                thank()
                break
        turn+=1
def close():
    window.destroy()



window=Tk()
window.title("JUMBLED GAME")
window.geometry("300x250")
Label(window,text="JUMBLED GAME",fg="black",bg="red").pack(fill="x")
Label(window,text="",bg="red").pack(fill="x")
Button(window,text="CLICK TO PLAY",fg="black",command=close).pack()
Button(window,text="CLOSE",command=close).pack()
window.mainloop()

global root
root=Tk()
root.geometry("350x100")
root.title("ENTER THE PLAYER NAMES")
name =StringVar()
label_1 =Label(root,text="Player1",fg="black").pack()
entry_1=Entry(root,textvariable=name).pack()
name2 =StringVar()
label_2 =Label(root,text="Player2",fg="black").pack()
entry_2=Entry(root,textvariable=name2).pack()
b =Button(root,text="Ok",command=play).pack()
root.mainloop()
