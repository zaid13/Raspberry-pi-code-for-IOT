
#pip3 install pyrebase
#pip3 install gpiozero


import pyrebase
from gpiozero import LED

l = LED(5)


config = {
    "apiKey": "AIzaSyDPuL913r0ynfeaAbxKC9FauFNIk0STiyQ",
    "authDomain": "i-o-t-5dbbe.firebaseapp.com",
    "databaseURL": "https://i-o-t-5dbbe.firebaseio.com",
    "storageBucket": "i-o-t-5dbbe.appspot.com"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()


def stream_handler(message):
    print(message["event"])  # put
    print(message["path"])  # /-K7yGTTEp7O549EzTYtI
    print(message["data"])# {'title': 'Pyrebase', "body": "etc..."}
    if(message["data"]=='1'):
        print("is equal")
        l.on()
    else:
        print("not equal")
        l.off()


my_stream = db.child("posts").stream(stream_handler) #checks for data at child "posts"
