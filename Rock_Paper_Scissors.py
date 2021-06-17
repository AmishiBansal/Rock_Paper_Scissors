from tkinter import *
from PIL import Image, ImageTk
from random import randint

# main window
root = Tk()
root.title("Rock Paper Scissors")
root.configure(background="#ffcccb")

# picture
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png"))
scissors_img_comp = ImageTk.PhotoImage(Image.open("scissors-user.png"))

# insert picture
user_label = Label(root, image=scissors_img, bg="#ffcccb")
comp_label = Label(root, image=scissors_img_comp, bg="#ffcccb")
comp_label.grid(row=1, column=4)
user_label.grid(row=1, column=0)

# scores
playerScore = Label(root, text=0, font=100, bg="#ffcccb", fg="black")
computerScore = Label(root, text=0, font=100, bg="#ffcccb", fg="black")
computerScore.grid(row=1, column=3)
playerScore.grid(row=1, column=1)


# indicators
user_indicator = Label(root, font=50, text="USER",
                       bg="#ffcccb", fg="black").grid(row=0, column=1)
computer_indicator = Label(
    root, font=50, text="COMPUTER", bg="#ffcccb", fg="black").grid(row=0, column=3)

# messages
msg = Label(root, font=50, bg="#ffcccb", fg="black")
msg.grid(row=3, column=2)

# update message
def updateMessage(x):
    msg['text'] = x

# update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("It is a tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif player == "scissor":
        if(computer == "rock"):
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    else:
        pass


# update choices
choices = ["rock", "paper", "scissor"]


def updateChoice(x):
    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissors_img_comp)


    # for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissors_img)
    checkWin(x, compChoice)


# buttons
rock = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda:updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda:updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda:updateChoice("scissor")).grid(row=2, column=3)

root.mainloop()



