# The client program connects to server and sends data to other connected 
# clients through the server
import socket
import thread
import sys


def recv_data():
    "Receive data from other clients connected to server"
    while 1:
        try:
            recv_data = client_socket.recv(4096)            
        except:
            #Handle the case when server process terminates
            print ("Server closed connection, thread exiting.")
            thread.interrupt_main()
            break
        if not recv_data:
                # Recv with no data, server closed connection
                print ("Server closed connection, thread exiting.")
                thread.interrupt_main()
                break
        else:
                print '{}'.format(recv_data)

def send_data():
    "Send data from other clients connected to server"
    while 1:

        send_data_1 = str(raw_input(''))
        
        send_data=name_id+': '+send_data_1
       
        if send_data_1 == "q" or send_data == "Q":
            client_socket.send(send_data)
            thread.interrupt_main()
            break
        else:
           client_socket.send(send_data)
            
if __name__ == "__main__":

    print ('\t\t******* Socket Programming Using Python ********')
    print ('\t\t*******        TCP/IP Chat Client       ********')
    print ('\nConnecting to server at 173.253.224.102:5000')

    global name_id
    name_id= str(raw_input('Enter Username: '))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('173.253.224.102', 5000))

    print ('Connected to server at 173.253.224.102:5000')
    
    thread.start_new_thread(send_data,())
    thread.start_new_thread(recv_data,())
    

    try:
        while 1:
            continue
    except:
        print ("Client program quits....")
        client_socket.close()       
