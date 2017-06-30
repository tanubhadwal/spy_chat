# test = []
# def demo():
#     a = raw_input("enter")
#     b = raw_input("Enter B")
#     test.append(a)
#     test.append(b)
#     print test
# demo()
friends=[]
def add_friend():
    friends_name = []

    friends_age = []

    friends_rating = []
    friends_is_online = []

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

def select_a_friend():
    item_number= int(0)
    for temp in friends:
        print("%d %s"%(item_number+1,friends['name']))
        item_number= item_number+1
    friend_choice=raw_input("choose your friend")
    friend_choice_position=int(friend_choice)-1
    return friend_choice_position