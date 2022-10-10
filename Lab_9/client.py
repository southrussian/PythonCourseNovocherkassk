from socket import *
from threading import *
from tkinter import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

host = '127.0.0.1'
port = 9090

client_socket.connect((host, port))

window = Tk()
window.title("Connected to: " + host + ':' + str(port))

txt_messages = Text(window, width=50)
txt_messages.grid(row=0, column=0, padx=10, pady=10)

txt_your_message = Entry(window, width=50)
txt_your_message.insert(0, 'Your message')


def send_message():
    client_message = txt_your_message.get()
    txt_messages.insert(END, '\n' + 'You: ' + client_message)
    client_socket.send(client_message.encode('utf-8'))


send_button = Button(window, text='Send', width=20, command=send_message)
send_button.grid(row=2, column=0, padx=10, pady=10)


def recv_message():
    while True:
        server_message = client_socket.recv(1024).encode('utf-8')
        print(server_message)
        txt_messages.insert(END, '\n' + server_message)


recv_thread = Thread(target=recv_message)
recv_thread.daemon = True
recv_thread.start()

window.mainloop()