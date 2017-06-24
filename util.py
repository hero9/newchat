def createSocket(socketName, ip, port):
    socketName.bind((ip, port))
    socketName.listen(1)


def connect(socketName):
    return socketName.accept()
