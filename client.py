import socket
 
IP = socket.gethostbyname(socket.gethostname()) 
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024


def main():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    """ Connecting to the server. """
    client.connect(ADDR)
 
    """ Opening and reading the file data. """
    file = open("sample.txt", "r") # ***************U can use any txt file but make sure about it's path********
    data = file.read()
    
    """ Sending the filename to the server. """
    client.send("sample.txt".encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
    print(data)
    new_data=""
    new_data=input("Enter the text: ")
    """ Sending the file data to the server. """
    client.send(new_data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
    file.seek(0)
    data2=file.read()
    file.seek(0)
    print(data2)
  
    client.close()
 
 
if __name__ == "__main__":
    main()
