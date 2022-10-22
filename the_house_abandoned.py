user_name = ""
next_location = ""
house_power = False
have_key = False
have_note = False
cellar_note = False
eaten_dinner = False
drunk_drink = False
user_sick = False


def get_user_selection(valid_options):
    options_to_show_user = " | ".join(valid_options)
    waiting_for_user_selection = True
    while waiting_for_user_selection:
        print(options_to_show_user)
        user_input = input("")
        if user_input in valid_options:
            waiting_for_user_selection = False
            return user_input
        else:
            print("Invalid option")


def scary_game_soq():
    global user_name
    print("The House Abandoned")
    user_sure_name = False
    while user_sure_name == False:
        print("What is your name?")
        user_name = input("")
        print("Are you sure")
        user_sure = input("")
        user_sure = user_sure.lower()
        if user_sure == "yes":
            user_sure_name = True
        elif user_sure == "no":
            user_sure_name = False
    print("start or quit")
    valid_options = ["start", "quit"]
    scary_soq = get_user_selection(valid_options)
    if scary_soq == "start":
        return
    elif scary_soq == "quit":
        exit()


def start_of_game():
    print(
        "As you drive down the street, your anxiety creeps up. You are terrified of what you will find in this house, but it is too late now. You've already signed yourself up for whatever will greet you.")
    user_response = input("")
    print(
        "You pull up to the driveway and are reminded of what this house used to be. You remember the white railing that went along the front porch. The blue siding of the house with the complementary red door. The two chairs that Ma and Pa used to read every Saturday morning in. The grass could never grow no matter what Ma's friends put on it. All tied together with a fence that used to keep Charlie, your old dog, inside.")
    return "inside car"


def in_car():
    global next_location
    global have_key
    global have_note
    valid_options = ["look around", "get out of car"]
    user_car = get_user_selection(valid_options)
    if user_car is "look around":
        print("You see a glovebox, the car keys, and you can also see the generator on the side of the house.")
        valid_options = ["open glovebox", "get out of car"]
        user_look_car = get_user_selection
        if user_look_car is "open glovebox":
            print("You open the glovebox and see 'keys' on a key ring along a 'note' with some napkins and documents.")
            print("Take the:")
            valid_options = ["keys", "note", "none"]
            user_take_key = get_user_selection(valid_options)
            if user_take_key is "keys":
                return "keys"
            elif user_take_key is "note":
                return "car note"
            elif user_take_key is "none":
                return "inside car"
        elif user_look_car is "get out of car":
            return "outside"
    elif user_car is "get out of car":
        return "outside"


def get_keys():
    global next_location
    global have_key
    while have_key is False:
        have_key = True
        print("You take the keys hoping they're the keys for the house, you don't remember for some reason")
        print("Would you like to take the 'note'?")
        valid_options = ["yes", "no"]
        take_note = get_user_selection(valid_options)
        if take_note is "yes":
            return "car note"
        elif take_note is "no":
            print("You decide not to take the note as it makes you uncomfortable.")
            print("Get out of the car?")
            valid_options = ["yes", "no"]
            get_out_of_car = get_user_selection(valid_options)
            if get_out_of_car is "yes":
                return "outside"
            elif get_out_of_car is "no":
                return "inside car"
    while have_key:
        print("You've already taken the keys. Would you like to take the note?")
        valid_options = ["yes", "no"]
        take_note = get_user_selection(valid_options)
        if take_note is "yes":
            return "car note"
        elif take_note is "no":
            return "inside car"


def note_in_car():
    global next_location
    global have_note
    while have_note is False:
        have_note = True
        print("You take the 'Note' it feels weird in your hands.")
        print("Read note?")
        valid_options = ["yes", "no"]
        read_note = get_user_selection(valid_options)
        if read_note is "yes":
            print("You open the old, crumbled, alcohol-smelling note, and it reads:")
            print(
                "Hey Son, welcome back; we've missed you! There's Thanksgiving dinner out for you, along with your favorite game in your room. Don't forget to turn the generator on the side of the side. We love you - Ma and Pa")
            user_response = input("")
            print("You crumble the note into your pocket")
            user_response = input("")
            print("Get out of the car?")
            valid_options = ["yes", "no"]
            get_out_of_car = get_user_selection(valid_options)
            if get_out_of_car is "yes":
                return "outside"
            elif get_out_of_car is "no":
                return "inside car"
        elif read_note is "no":
            print("You decide not to read the note as it already makes you uncomfortable.")
            print("Get out of the car?")
            valid_options = ["yes", "no"]
            get_out_of_car = get_user_selection(valid_options)
            if get_out_of_car is "yes":
                return "outside"
            elif get_out_of_car is "no":
                return "inside car"


def house_has_power():
    global house_power
    global next_location
    while house_power:
        print(
            "You walk along side the high weeds that you've never seen before. Couple of scratches on your shins from the bushes but other than that you continue on to turn on the generator.")
        print("go inside:")
        valid_options = ["house", "car"]
        user_next_move = get_user_selection(valid_options)
        if user_next_move is "house":
            print(
                "You walk up the old and forgotten stairs to the front door, you can see that it still has Ma and Pa's old engravings in it, this reminds you of when they did it, you miss those days.")
            return "inside house"
        elif user_next_move is "car":
            print("You go back into the car as though you forgot something")
            return "inside car"
    while house_power is False:
        print(
            "The house is dark and dim in a way that makes you extremely anxious and this takes over you, you can not enter without turning on the generator.")
        print("Turn on the Generator?")
        valid_options = ["yes", "no"]
        tog_again = get_user_selection(valid_options)
        if tog_again is "yes":
            return "generator"
        elif tog_again is "no":
            return "outside"


def user_outside():
    global next_location
    global house_power
    print("You are outside you can see the 'car' and the 'generator to the left of the house.")
    print("Go to:")
    valid_options = ["car", "generator"]
    car_or_gen = get_user_selection(valid_options)
    if car_or_gen is "car":
        return "car"
    elif car_or_gen is "generator":
        print("Turn on the Generator?")
        valid_options = ["yes", "no"]
        turn_on_gen = get_user_selection(valid_options)
        if turn_on_gen is "yes":
            house_power = True
            return "generator"
        elif turn_on_gen is "no":
            house_power = False
            return "generator"


def inside_house():
    global have_key
    global house_power
    global have_note
    global next_location
    print("Open the door?")
    valid_options = ["yes", "no"]
    open_the_door = get_user_selection(valid_options)
    if open_the_door is "yes" and have_key:
        print("It works! You you twist the key and creek open the old rusty door and take in what you see.")
        print("Look around?")
        valid_options = ["yes"]
        user_inside_house = get_user_selection(valid_options)
        user_inside_house = input("")
        if user_inside_house is "yes":
            return "inside entryway"
    elif open_the_door is "yes" and have_key is False:
        print("You try to open the door but its locked you think that you may have left the keys in the glovebox")
        return "outside"
    elif open_the_door is "no":
        print("Where would you like to go?")
        print("car | generator")
        valid_options = ["car", "generator"]
        cog = get_user_selection(valid_options)
        if cog is "car":
            return "inside car"
        elif cog is "generator":
            return "outside"


def entryway():
    global next_location
    print(
        "You look around and are in the entryway with the stairs directly to your left. In front of you, you can see the 'living room' with the old brown couch and TV that you're surprised aren't stolen directly in front of a tv stand. In the 'living room' is the 'kitchen' and 'dining room' with an open entryway to see straight into the dirty, abandoned kitchen.")
    print("go into:")
    valid_options = ["living room", "dining room", "upstairs"]
    go_into_lkd = get_user_selection(valid_options)
    if go_into_lkd is "living room":
        return "inside living room"
    elif go_into_lkd is "dining room":
        return "inside dining room"
    elif go_into_lkd is "upstairs":
        return "going upstairs"


def living_room():
    global next_location
    print(
        "You walk into the dirty and dingy living room. Red liquid seeped into the carpet everywhere, along with old bottles and plates of food on the coffee table. Aside from the dishes are the TV remote and two coasters with cups on them. The cups are filled with a thick black, tar-like liquid... and smell. This place is nothing like it used to be. ")
    print("go inside:")
    valid_options = ["entryway", "dining room", "kitchen"]
    edk_response = get_user_selection(valid_options)
    if edk_response is "entryway":
        return "inside entryway"
    elif edk_response is "dining room":
        return "inside dining room"
    elif edk_response is "kitchen":
        return "inside kitchen"


def dining_room():
    global next_location
    global eaten_dinner
    print(
        "The dining room has the same carpet as the living room, with a long table, five chairs, and six placemats. There's a Turkey in the middle of the table, along with some greens, sweet potato pie, ham, mashed potatoes, corn, and candy yams.")
    return "eat dinner"


def eat_dinner():
    if eaten_dinner is False:
        print("Eat Thanksgiving dinner?")
        valid_options = ["yes", "no"]
        user_etd = get_user_selection(valid_options)
        if user_etd is "yes":
            eaten_dinner = True
            print("You take a bite of the ham; it's gross. It tastes like roadkill. ")
            user_response = input("")
            print("You think you have to vomit and would prefer to do it in the cellar.")
            print("go into:")
            valid_options = ["living room", "kitchen", "cellar"]
            user_lok = get_user_selection(valid_options)
            if user_lok is "living room":
                return "inside living room"
            elif user_lok is "kitchen":
                return "inside kitchen"
            elif user_lok is "cellar":
                return "inside cellar"
        elif user_etd is "no":
            print("You decide not to eat the rotten food, it looks like its been a couple years anyways.")
            print("go into: living room | kitchen")
            valid_options = ["living room", "kitchen"]
            user_lok = get_user_selection(valid_options)
            if user_lok is "living room":
                return "inside living room"
            elif user_lok is "kitchen":
                return "inside kitchen"
    elif eaten_dinner:
        user_response = input("")
        print("go into: living room | kitchen")
        valid_options = ["living room", "kitchen"]
        user_lok = get_user_selection(valid_options)
        if user_lok is "living room":
            return "inside living room"
        elif user_lok is "kitchen":
            return "inside kitchen"


def kitchen():
    global next_location
    global drunk_drink
    print("The kitchen looks like it was once lively, with Ma running in and out, yelling at us to stay out. You can see all the pots and pans from that night, along with lots of opened bottles of alcohol.")
    if drunk_drink:
        user_response = input("")
        print("Where would you like to go?")
        valid_options = ["dining room"]
        go_into_dr = get_user_selection(valid_options)
        if go_into_dr is "dining room":
            return "inside dining room"
    elif drunk_drink is False:
        return "drink drink"

def drink_drink():
    global next_location
    global user_sick
    print("Would you like to drink a drink?")
    valid_options = ["yes", "no"]
    drink_the_drink = get_user_selection(valid_options)
    if drink_the_drink is "yes":
        user_sick = True
        print("You drink a sip of some alcohol left in bottle. It taste like watered down acid.")
        user_response = input("")
        print("Where would you like to go:")
        valid_options = ["living room"]
        go_into_lr = get_user_selection(valid_options)
        if go_into_lr is "living room":
            return "inside living room"
    elif drink_the_drink is "no":
        print("You decide not to drink the drink as that sounds disgusting and you dont know what you even thought to do that.")
        user_response = input("")
        print("Where would you like to go?")
        valid_options = ["living room"]
        go_into_lr = get_user_selection(valid_options)
        if go_into_lr is "living room":
            return "inside living room"


def cellar():
    global next_location
    global cellar_note
    print("You walk down the stairs and into the cellar. You can see old boxes and an opened gift alongside a note.")
    if cellar_note:
        print("Look at 'gift'?")
        valid_options = ["yes", "no"]
        look_at_gift = get_user_selection(valid_options)
        if look_at_gift is "yes":
            print("You think it was a bottle; all left is the box, an elegant red ribbon, and the note.")
            user_response = input("")
            print("Go back upstairs?")
            valid_options = ["yes", "no"]
            go_back_us = get_user_selection(valid_options)
            if go_back_us is "yes":
                return "inside living room"
            elif go_back_us is "no":
                return "inside cellar"
        elif look_at_gift is "no":
            print("Go back upstairs?")
            valid_options = ["yes", "no"]
            go_back_us = get_user_selection(valid_options)
            if go_back_us is "yes":
                return "inside living room"
            elif go_back_us is "no":
                return "inside cellar"
    elif cellar_note is False:
        print("Get the note?")
        valid_options = ["yes", "no"]
        get_note = get_user_selection(valid_options)
        if get_note is "yes":
            cellar_note = True
            print("You pick the note up off the floor.")
            print("Read the note?")
            valid_options = ["yes", "no"]
            read_cellar_note = get_user_selection(valid_options)
            if read_cellar_note is "yes":
                print("Hey son, it's Pa. I just want you to know how genuinely proud of you I am. You are doing everything I know you would, and you haven't failed me yet, and I know you won't. ")
            elif read_cellar_note is "no":
                print("You decide not to read the note as it makes  you uncomfortable.")
                user_response = input("")
                print("What would you like to do?")
                valid_options = ["look at gift", "go upstairs"]
                gift_or_upstairs = get_user_selection(valid_options)
                if gift_or_upstairs is "look at gift":
                    print("You think it was a bottle; all left is the box, an elegant red ribbon, and the note.")
                    user_response = input("")
                    print("Go back upstairs?")
                    valid_options = ["yes", "no"]
                    go_back_us = get_user_selection(valid_options)
                    if go_back_us is "yes":
                        return "inside living room"
                    elif go_back_us is "no":
                        return "inside cellar"
                elif gift_or_upstairs is "go upstairs":
                    return "inside living room"
        elif get_note is "no":
            print("You decide not to get the note as it makes you uncomfortable.")
            user_response = input("")
            print("Look at 'gift'?")
            valid_options = ["yes", "no"]
            look_at_gift = get_user_selection(valid_options)
            if look_at_gift is "yes":
                print("You think it was a bottle; all left is the box, an elegant red ribbon, and the note.")
                user_response = input("")
                print("Go back upstairs?")
                valid_options = ["yes", "no"]
                go_back_us = get_user_selection(valid_options)
                if go_back_us is "yes":
                    return "inside living room"
                elif go_back_us is "no":
                    return "inside cellar"
            elif look_at_gift is "no":
                print("Go back upstairs?")
                valid_options = ["yes", "no"]
                go_back_us = get_user_selection(valid_options)
                if go_back_us is "yes":
                    return "inside living room"
                elif go_back_us is "no":
                    return "inside cellar"


def upstairs():
    global next_location
    print("")


def main():
    game_running = True
    scary_game_soq()
    next_location = start_of_game()
    while game_running is True:
        if next_location is "inside car":
            next_location = in_car()
        elif next_location is "keys":
            next_location = get_keys()
        elif next_location is "car note":
            next_location = note_in_car()
        elif next_location is "generator":
            next_location = house_has_power()
        elif next_location is "outside":
            next_location = user_outside()
        elif next_location is "inside house":
            next_location = inside_house()
        elif next_location is "inside entryway":
            next_location = entryway()
        elif next_location is "inside living room":
            next_location = living_room()
        elif next_location is "inside kitchen":
            next_location = kitchen()
        elif next_location is "drink drink":
            next_location = drink_drink()
        elif next_location is "inside dining room":
            next_location = dining_room()
        elif next_location is "eat dinner":
            next_location = eat_dinner()
        elif next_location is "inside cellar":
            next_location = cellar()
        elif next_location is "go upstairs":
            next_location = upstairs()
        else:
            print("Error")
            game_running = False


main()
