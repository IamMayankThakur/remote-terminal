# A remote terminal based on sockets

## Installation and usage

* Clone the project
* `cd remote-terminal`
* `pip3 install -r requirements.txt`
* Run the server using ``python3 server.py `server_ip` ``
* Run the client ``python3 client.py `server_ip` ``
* Type bash commands in the tkinter window.
* Type `quit` to close the connection

## Working

* This is based on simple socket programming.
* The client connects to the server, a UI window opens
* The client enters a command to be run on the server.
* The bash command is sent to the server.
* The command is executed and the output is sent back to the client.
