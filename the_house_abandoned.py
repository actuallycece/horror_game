user_name = ""
next_location = ""
house_power = False
have_key = False
have_note = False

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
    soq = False
    while soq == False:
        print("start or quit")
        scary_soq = input("")
        scary_soq = scary_soq.lower()
        if scary_soq == "start":
            soq = True
            return
        elif scary_soq == "quit":
            exit()
        else:
            print("Invalid Option")

def in_car():
    global next_location
    global have_key
    global have_note

    print("As you drive down the street, your anxiety creeps up. You are terrified of what you will find in this house, but it is too late now. You've already signed yourself up for whatever will greet you.")
    user_response = input("")
    print("You pull up to the driveway and are reminded of what this house used to be. You remember the white railing that went along the front porch. The blue siding of the house with the complementary red door. The two chairs that Ma and Pa used to read every Saturday morning in. The grass would never grow no matter what Ma's friends put on it. All tied together with a fence that used to keep Charlie, your old dog, inside.")
    print("look around | get out of car")
    user_next_move = False
    while user_next_move == False:
        user_car = input("")
        user_car = user_car.lower()
        if user_car == "look around":
            user_next_move = True
            print("You see a glovebox, the car keys, and you can also see the generator on the side of the house.")
            print("open glovebox | get out of car")
            user_in_car = False
            while user_in_car == False:
                user_look_car = input("")
                user_look_car = user_look_car.lower()
                if user_look_car == "open glovebox":
                    user_in_car = True
                    print("You open the glovebox and see keys on a key ring along a note with some napkins and documents.")
                    print("Take the Keys?")
                    user_take_key = input("")
                    if user_take_key == "yes":
                        print("You take the keys hoping they're the keys for the house, you don't remember for some reason")
                        have_key = True
                        print("Would you like to take the note?")
                        take_note = input("")
                        user_take_note = False
                        while user_take_note == False:
                            if take_note == "yes":
                                user_take_note = True
                                have_note = True
                                print("You take the 'Note' it feels weird in your hands")
                                print("Read note?")
                                read_note = input("")
                                if read_note == "yes":
                                    print("You open the old crumbled note and it reads:")
                                    print("Hey Son, welcome back, weve missed you! Theres still Thanksgiving dinner out for you along with your favorite game in your room. Dont forget to turn the generator on the side of the side. We love you - Ma and Pa")
                                    print("You crumble the note into your pocket")
                                    user_response = input("")
                                    print("Get out of the car?")
                                    get_out_of_car = input("")
                                    if get_out_of_car == "yes":
                                        return "outside"
                                elif read_note == "no":
                                    print("You decide not to read the note as it already makes you uncomfertable.")
                                    print("Get out of the car?")
                                    get_out_of_car = input("")
                                    if get_out_of_car == "yes":
                                        return "outside"
                            elif take_note == "no":
                                user_take_note = True
                                have_note = False
                                print("Get out of the car?")
                                get_out_of_car = input("")
                                if get_out_of_car == "yes":
                                    return "outside"
                                else:
                                    print("you have to progress.")
                                    print("Get out of the car?")
                                    needs_too_get_out = False
                                    while needs_too_get_out == False:
                                        print ("Get out of the car?")
                                        get_out_of_car = input("")
                                        get_out_of_car = get_out_of_car.lower()
                                        if get_out_of_car == "yes":
                                            needs_too_get_out = True
                                            return "outside"
                                        elif get_out_of_car == "no":
                                            needs_too_get_out = False
                                            print("invalid response")
                                        else:
                                            print("invalid response")
                            else:
                                user_take_note = False
                                print("invalid response")
                                print("Would you like to take the note?")
                    elif user_take_key == "no":
                        print("you dont take the keys for some reason hoping they arent important and continue to do what you were doing.")
                        have_key = False
                        print("Would you like to take the note?")
                        take_note = input("")
                        if take_note == "yes":
                            have_note = True
                            print("You take the 'Note' it feels weird in your hands")
                            print("Read note?")
                            read_note = input("")
                            if read_note == "yes":
                                print("You open the old crumbled note and it reads:")
                                print("Hey Son, welcome back, weve missed you! Theres still Thanksgiving dinner out for you along with your favorite game in your room. Dont forget to turn the generator on the side of the side. We love you - Ma and Pa")
                                user_response = input("")
                                print("You cumble the note into your pocket")
                                print("Go inside the house?")
                                user_response = input("")
                                if user_response == "yes":
                                    return "inside house"
                                elif user_response == "no":
                                    return "outside"
                            elif read_note == "no":
                                print("You decide not to read the note as it already makes you uncomfertable.")
                                print("Get out of the car?")
                                get_out_of_car = input("")
                                if get_out_of_car == "yes":
                                    return "outside"
                                elif get_out_of_car == "no":
                                    return "inside car"
                elif user_look_car == "get out of car":
                    user_in_car = True
                    return "outside"
                else:
                    user_in_car = False
                    print("invalid response")
                    print("open glovebox | get out of car")
        elif user_car == "get out of car":
            user_next_move = True
            return "outside"
        else:
            user_next_move = False
            print("invalid response")
            print("look around | get out of car")


def house_has_power():
    global house_power
    global have_key

    if house_power == True:
            print("The house makes a loud 'whirling' sound and boots up like a Windows Home Vista")
            print("go inside house | go inside car")
            user_next_move = input("")
            if user_next_move == "go inside car":
                print("You go back into the car as though you forgot something")
                return "inside car"
            elif user_next_move == "go inside house":
                print(
                    "You walk up the old and forgotten stairs to the front door, you can see that it still has Ma and Pa's old engravings in it, this reminds you of when they did it, you miss those days.")
                return "inside house"
    elif house_power == False:
            print("The house is dark and dim in a way that makes you extremly anxious and this takes over you, you can not enter without turning on the generator.")
            print("Turn on the Generator?")
            tog_again = input("")
            if tog_again == "yes":
                house_power = True
                print("You walk along side the high weeds that youve never seen before. Couple of scratches on your shins from the bushes but other than that you continue on to what your doing.")
                print("go inside house | go inside car")
                user_next_move = input("")
                if user_next_move == "go inside house":
                    return "inside house"
            if user_next_move == "go inside car":
                print("You go back into the car as though you forgot something")
                return "inside car"

def inside_house():
    global have_key
    global house_power
    global have_note
    
    print("Open the door?")
    opened_door = False
    while opened_door == False:
        if have_key == True:
            opened_door = True
            user_response = input("")
            print("It works! You you twist the key and creek open the old rusty door and take in what you see.")
            print("look around")
            go_lkd = False
            while go_lkd == False:
                user_inside_house = input("")
                if user_inside_house == "look around":
                    go_lkd = True
                    return "inside entryway"
                elif have_key == False:
                    opened_door = True
                print("You try to open the door but its locked you think that you may have left the keys in the glovebox")
                while go_back_car == False:
                    print("Go back to car?")
                go_back_car = input("")
                if go_back_car == "yes":
                    return "inside car"
            else:
                print("invalid response")
                print("Open the door?")


def entryway():
    print("You look around and are in the entryway with the stairs directly to your left. In front of you, you can see the 'living room' with the old brown couch and TV that you're surprised aren't stolen directly in front of a tv stand. In the 'living room' is the 'kitchen' and 'dining room' with an open entryway to see straight into the dirty abandoned kitchen.")
    print("go into: living room | dining room | upstairs")
    lkd = False
    while lkd == False:
        go_into_lkd = input("")
        if go_into_lkd == "living room":
            lkd = True
            return "inside living room"
        elif go_into_lkd == "dining room":
            lkd = True
            return "inside dining room"
        elif go_into_lkd == "upstairs":
            lkd = True
            return "going upstairs"
        else:
            lkd = False
            print("invalid respone")
            print("go into: living room | dining room | upstairs")
    else:
        go_lkd = False
        print("invalid repsonse")
        print("look around")


def living_room():
    print("You walk into the dirty and dingy living room. Red liquid seeped into the carpet everywhere, along with old bottles and plates of food on the coffee table. Aside from the dishes are the TV remote and two coasters with cups on them. The cups are filled with a thick black, tar-like liquid... and smell. This place is nothing like it used to be. ")
    print("go inside: entryway | dining room | kitchen")
    edk = False
    while edk == False:
        edk_response = input("")
        if edk_response == "entryway":
            edk = True
            return "inside entryway"
        elif edk_response == "dining room":
            edk = True
            return "inside dining room"
        elif edk_response == "kitchen":
            edk = True
            return "inside kitchen"
        else:
            edk = False
            print("invalid response")


def dining_room():
    print("")


def kitchen():
    print("")


def upstairs():
    print()


def user_outside():
    global house_power
    global have_key

    print("You get out of the car and see the generator to the left of the house.")
    print("Turn on the Generator?")
    turn_on_gen = input("")
    if turn_on_gen == "yes":
        house_power = True
        return "generator"
    elif turn_on_gen == "no":
        house_power = False
        return "generator"

def main():
    game_running = True
    next_location = ""
    scary_game_soq()
    next_location = in_car()
    while game_running == True:
        if next_location == "inside car":
            next_location = in_car()
        elif next_location == "generator":
            next_location = house_has_power()
        elif next_location == "outside":
            next_location = user_outside()
        elif next_location == "inside house":
            next_location = inside_house()
        elif next_location == "inside entryway"
        next_location = entryway()
        elif next_location == "inside living room":
            next_location = living_room()
        elif next_location == "inside kitchen":
            next_location = kitchen()
        elif next_location == "inside dining room":
            next_location = dining_room()
        elif next_location == "go upstairs":
            next_location = upstairs()
        else:
            print("Error")
            game_running = False


main()
