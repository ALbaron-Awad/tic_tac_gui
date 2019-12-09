from tkinter import *
import tkinter.messagebox

btn_clicked = True


def main():

    global btn_clicked, root, count
    count = 0
    root = Tk()

    root.title("Tic Tac Toe")
    info_msg="#Game__Instruction\n" \
             "******************************************" \
             "*-This game has two player\n" \
             "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" \
             "actually  you are  Playing with yourself (*~^)!"" \
             ""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    window = Label(root, text="Tic Tac Toe!", bg='#F3BE2F', font=("Times New Roman Bold", 18))
    window.grid(column=0, row=1)
    info = Message(root, text=info_msg)
    info.config(bg='#B6AD88', font=("Times New Roman ", 10))
    info.grid(row=5, column=0)



    def start(button):
        global btn_clicked, root, count
        if button["text"] == " " and btn_clicked:

            button["text"] = "X"
            count += 1
            btn_clicked = False

        elif button["text"] == " ":

            button['text'] = "O"
            count += 1
            btn_clicked = True

        if (button1["text"] == button2["text"] == button3["text"] == "X" or

            button4["text"] == button5["text"] == button6["text"] == "X" or

            button7["text"] == button8["text"] == button9["text"] == "X" or

            button1["text"] == button4["text"] == button7["text"] == "X" or

            button2["text"] == button5["text"] == button8["text"] == "X" or

            button3["text"] == button6["text"] == button9["text"] == "X" or

            button1["text"] == button5["text"] == button9["text"] == "X" or

            button3["text"] == button5["text"] == button7["text"] == "X"):

            answer = tkinter.messagebox.askquestion('X Player wins!', 'Do you want to play again')

            root.destroy()

            if answer == 'yes':
                main()

        elif (count == 9):
            tkinter.messagebox.showinfo("Tic Tac Toe", "Sorry, It is a Tie!")
            answer = tkinter.messagebox.askquestion('Sorry,but the Game dead !', 'Do you want to play again')

            root.destroy()

            if answer == 'yes':
                main()

        elif (button1["text"] == button2["text"] == button3["text"] == "O" or

            button4["text"] == button5["text"] == button6["text"] == "O" or

            button7["text"] == button8["text"] == button9["text"] == "O" or

            button1["text"] == button4["text"] == button7["text"] == "O" or

            button2["text"] == button5["text"] == button8["text"] == "O" or

            button3["text"] == button6["text"] == button9["text"] == "O" or

            button1["text"] == button5["text"] == button9["text"] == "O" or

            button3["text"] == button5["text"] == button7["text"] == "O"):

            answer = tkinter.messagebox.askquestion('O Player wins!!!', 'Do you want to play again')

            root.destroy()

            if answer == 'yes':
                main()

    button1 = Button(root, text=" ",  bg='#CFC082', height=6, width=6, command=lambda: start(button1))
    button1.grid(row=4, column=4)

    button2 = Button(root, text=" ", bg='#CFC082', height=6, width=6, command=lambda: start(button2))
    button2.grid(row=4, column=5)

    button3 = Button(root, text=" ",  bg='#CFC082', height=6, width=6, command=lambda: start(button3))
    button3.grid(row=4, column=6)

    button4 = Button(root, text=" ",   bg='#CFC082',height=6, width=6, command=lambda: start(button4))
    button4.grid(row=5, column=4)

    button5 = Button(root, text=" ",  bg='#CFC082',height=6, width=6, command=lambda: start(button5))
    button5.grid(row=5, column=5)

    button6 = Button(root, text=" ", bg='#CFC082',height=6, width=6, command=lambda: start(button6))
    button6.grid(row=5, column=6)

    button7 = Button(root, text=" ",  bg='#CFC082', height=6, width=6, command=lambda: start(button7))
    button7.grid(row=6, column=4)

    button8 = Button(root, text=" ", bg='#CFC082', height=6, width=6, command=lambda: start(button8))
    button8.grid(row=6, column=5)

    button9 = Button(root, text=" ", bg='#CFC082', height=6, width=6, command=lambda: start(button9))
    button9.grid(row=6, column=6)

    root.geometry("500x400+600+500")
    root.config(background='#6E6E6E')
    root.mainloop()
    
    
main()