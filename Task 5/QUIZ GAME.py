from tkinter import *
window=Tk()
window.title("Quiz App")
i=0
window.geometry("700x400")
ques_dict=dict()
ques_dict={"What is our national flower ?":["Rose","Lotus","Lily"],
"How many colors are there in our national flag ?":["Three","Four","Five"],
"Which among these is a neighbouring country ?":["USA","Switzerland","Nepal","Russia"],
"3+8 ?":["9","11"]
}

sol_list=["Lotus","Three","Nepal","11"]

ques_list=list(ques_dict.keys())
opt_list=list(ques_dict.values())

def clear_frame():
   for widgets in frame.winfo_children():
      widgets.destroy()

def show_score():
    global answers
    answers.append(optVal.get())
    clear_frame()
    score=0
    answers=answers[1:]
    for r,s in zip(answers,sol_list):
        if r==s:
            score+=1
    print(answers)
    message=f"Thanks for submitting.Your score is {score}"
    Label(frame,text=message,font="comicsans 19 bold",pady=20,fg="red",bg="yellow").place(relx=0.2,rely=0.4)
   

def start_quiz():
    global i
    global answers
    answers=[]
    i=0
    button.config(command=get_next_ques)
    get_next_ques()
def get_next_ques():
    global i
    clear_frame()
    answers.append(optVal.get())
    Label(frame,text=f"Q{i+1} {ques_list[i]}",font="Helventica 15 bold").place(rely=0.3)
    for j in range(0,len(opt_list[i])):
       Radiobutton(frame,text=opt_list[i][j],variable=optVal,value=opt_list[i][j],font="10").place(rely=0.4+j*0.1)
    i+=1
    btn=Button(frame,text="Next",command=get_next_ques,font="comicsans 15 bold",bg="light green")
    btn.place(rely=0.8,relx=0.4)
    if(i==len(ques_list)):
        btn.config(text="Submit Quiz")
        btn.config(command=show_score)
    
frame=Frame()
text=Label(text="ALL IN ONE QUIZ APP",pady=20,font="comicsans 25 bold",bg="red",fg="white")
text.place(relx=0.5,rely=0.1,anchor=CENTER)
optVal=StringVar(value=1)
button=Button(frame,text="Start Quiz",command=start_quiz,font="comicsans 30 bold",bg="yellow")
button.place(relx=0.5,rely=0.5,anchor=CENTER)
frame.pack(fill="both",expand=True)
window.mainloop()
