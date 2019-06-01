"""
Containers:
    Data to send
    Data that has been read
    Errors
Functions:
    Create sockets
    Connect to a server
    Send data
    Read data

    UI functions
        Prints to UI
        Read from UI

Exceptions:
    Errors from server-side
    Invalid data type received
    Invalid data type to send
    Connection broken

Create a read socket, write socket
Connect to the server
Send usrname
Loop
    create list of sockets ready to write and read
    if data to send:
        send data
    if data to read:
        read data
        decrypt data
        display data
"""
