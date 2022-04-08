import tkinter
import PySimpleGUI as sg
import subprocess

def main():
    mainform = tkinter.Tk()

    def buttonclick():
        layout = [[sg.Text("Hello %s, What software are you going to use today?" % (txt1.get()))], [sg.Button("Calculator")], [sg.Button("Notepad")]]
        window = sg.Window("prototype program", layout)
        while True:
            event, values = window.read()
            if event == "Calculator":
                subprocess.Popen('C:\\Windows\\System32\\calc.exe')
                break
            elif event == "Notepad":
                subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
                break
            elif event == sg.WIN_CLOSED:
                break
        window.close()

    def close_window():
        mainform.destroy()

    lbl1 = tkinter.Label(mainform)
    lbl1['text'] = "Username"
    lbl1.grid(row=0, column=0, sticky=tkinter.E, padx=3, pady=3)

    lbl2 = tkinter.Label(mainform)
    lbl2['text'] = "Password"
    lbl2.grid(row=1, column=0, sticky=tkinter.E, padx=3, pady=3)

    txt1 = tkinter.Entry(mainform)
    txt1['width'] = 40
    txt1.grid(row=0, column=1, columnspan=2, padx=3, pady=3)

    txt2 = tkinter.Entry(mainform)
    txt2['width'] = 40
    txt2.grid(row=1, column=1, columnspan=2, padx=3, pady=3)

    chk = tkinter.Checkbutton(mainform)
    chk['text'] = "Remember me"
    chk.grid(row=2, column=0, padx=3, pady=3)

    btn1 = tkinter.Button(mainform, command=buttonclick)
    btn1['text'] = "Login"
    btn1.grid(row=2, column=1, sticky=tkinter.N+tkinter.E+tkinter.S+tkinter.W, padx=3, pady=3)

    btn2 = tkinter.Button(mainform, command=close_window)
    btn2['text'] = "Exit"
    btn2.grid(row=2, column=2, sticky=tkinter.N+tkinter.E+tkinter.S+tkinter.W, padx=3, pady=3)

    mainform.mainloop()

if __name__ == "__main__":
    main()
