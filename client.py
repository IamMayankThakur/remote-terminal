import socket
import sys
import tkinter as tk

print(sys.argv[1])
host = sys.argv[1]
port = 8880
s = socket.socket()
try:
    s.connect((host, port))
except:
    print("Server not reachable")
    exit(0)


def send_commands():
    global var
    cmd = entry.get()
    entry.delete(0, len(cmd))

    if cmd == 'quit':
        s.send(str.encode("qq"))
        s.close()
        sys.exit()

    if len(str.encode(cmd)) > 0:
        s.send(str.encode(cmd))
        client_response = str(s.recv(1024), 'utf-8')
        pwd = str(s.recv(1024), 'utf-8')
        print(client_response, end="")
        print("PWD:", pwd)
        var.set(pwd)
        list.insert(0.0, client_response)


top = tk.Tk()
frame = tk.Frame(top)
frame.pack()

sframe = tk.Frame(frame, borderwidth=1)
sframe.pack()
var = tk.StringVar()
label = tk.Label(sframe, textvariable=var)
var.set("")
label.grid(row=0, column=0)

entry = tk.Entry(sframe)
entry.grid(row=0, column=1, padx=20, pady=20)

button = tk.Button(sframe, text="Execute",
                   command=send_commands)
button.grid(row=0, column=2)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill=tk.Y)

# 000fff000
list = tk.Text(frame, yscrollcommand=scrollbar.set,
               wrap="word", fg="#00ffff", bg="black")
list.pack(side="left", fill="both")
scrollbar.config(command=list.yview)

top.mainloop()
