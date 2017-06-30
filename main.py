from spy_details import spy, Spy,friends,ChatMessage
from steganography.steganography import Steganography
from datetime import datetime
from colorama import init,Fore,Style

init(autoreset=True)

print (Fore.GREEN + spy.name)
### Default Message../////
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

# friends_name = []
#
# friends_age = []
#
# friends_rating = []
#
# friends_is_online = []




print "Hello! welcome to spy chat"

question = "Do you want to continue as " + spy.salutation+ " " + spy.name+ " (Y/N)?"

existing = raw_input(question)


def select_a_friend():
    item_number = 0
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number + 1, friend.salutation, friend.name,friend.age,friend.rating)
        item_number = item_number + 1

    friend_choice=raw_input("choose your friend")
    friend_choice_position=int(friend_choice)-1
    return friend_choice_position


####   Add status and update new status.//////
def add_status(current_status_message):
    updated_status_message = None

    if current_status_message != None:
        print 'Your current status message is %s \n' % (current_status_message())
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':
        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)

            item_position = item_position + 1
        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:

        print 'The option you chose is not valid! Press either y or n.'
    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You did not update your status message'
    return updated_status_message

# friends lisstttt.//
friends_name = []

friends_age = []

friends_rating = []
friends_is_online = []
### add function  for friend//////
def add_friend():
    new_name = raw_input("Please add your friend's name: ")

    new_salutation = raw_input("Are they Mr. or Ms.?: ")

    new_name = new_name + " " + new_salutation

    new_age = raw_input("Age?")

    new_age = int(new_age)

    new_rating = raw_input("Spy rating?")

    new_rating = float(new_rating)

    if len(new_name) > 0 and new_age > 12 :

        friends_name.append(new_name)

        friends_age.append(new_age)

        friends_rating.append(new_rating)

        friends_is_online.append(True)

        print 'Friend Added!'

    else:

        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'


    return len(friends_name)

    return friend_choice_position
###### SEND AN SECRET MESSAGE//....////

def send_message():

    friend_choice = select_a_friend()
    original_image = "k.png"

    output_path = "kk.png"
    text = "i am ready for marriage but i dont want to go"

    Steganography.encode(original_image, output_path, text)
    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)
    print "Your secret message image is ready!"
######READ A SECRET MESSAAGE..////

def read_message():
    sender = select_a_friend()
    output_path = 'kk.png'
    get= Steganography.decode(output_path)
    print get
    new_chat = ChatMessage(get,False)

    friends[sender].chats.append(new_chat)
    print "Your secret message has been saved!"

#def start_chat(spy):
 #   spy.name = spy.salutation + " " + spy.name
  #  print "tanu"
def read_chat_history():
    read_for = select_a_friend()
    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            init(autoreset=True)
            msg_date = Fore.BLUE + chat.time.strftime("%d %B %Y") + Style.RESET_ALL

            print '[%s] %s: %s' % (msg_date, 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (msg_date, friends[read_for].name, chat.message)

def start_chat(spy):
    spy_name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:
        print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True
######## show the menu..//////
        while show_menu:

            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"

            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:

                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    current_status_message = raw_input()
                    add_status(current_status_message)
                elif menu_choice == 2:

                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)

                elif menu_choice == 3:
                 send_message()

                elif menu_choice == 4:
                 read_message()

                elif menu_choice==5:
                 read_chat_history()

            else:

                show_menu = False

    else:

        print 'Sorry you are not of the correct age to be a spy'






if existing.upper() == "Y":
    start_chat(spy)
elif existing.upper() == "N":

    spy = Spy("","", 0,0)
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:

        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")
        if(spy.salutation== "Mr."):
            print(spy.salutation+spy.name)
        elif(spy.salutation=="Ms"):
            print(spy.salutation+spy.name)
        elif(spy.salutation=="O"):
            print (spy.salutation+spy.name)
        else:
            print("please enter a specifiy you are MR., Ms ,O ")

        spy.age = raw_input("What is your age?")

        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")

        spy.rating = float(spy.rating)
        start_chat(spy)
    else:
        print 'Please add a valid spy name'
else:
    print "you entered an invalid value."