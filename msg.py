# for code msg function...//
from steganography.steganography import Steganography
from test import friends
from test import select_a_friend
from datetime import datetime, timedelta
from spy import spy
print (friends)
def send_message():
    friend_choice = select_a_friend()


    original_image = raw_input('what is your image name')
    output_path='output.jpg'
    text = raw_input('secret message')
    new_chat = {

        "message": text,

        "time": datetime.now(),

        "sent_by_me": True
    }
    friends[friend_choice]['chats'].append(new_chat)

    print "Your secret message image is ready!"

    #secret_msg = Steganography.encode

    Steganography.encode = (original_image,output_path,text)


# to read a msg./////
def read_message():
    sender =  select_a_friend()
    output_path=raw_input('what is your name of the file')
    secret_text= Steganography.decode(output_path)


    new_chat = {

    "message": secret_text,

    "time": datetime.now(),

    "sent_by_me": False

     }

    friends[sender]['chats'].append(new_chat)

print "Your secret message has been saved!"

send_message()