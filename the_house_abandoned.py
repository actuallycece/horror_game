user_name = ""
next_location = ""
house_power = False
have_key = False
have_note = False


def scary_game_soq():
    global user_name

    print(f"The House Abandoned")
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
            soq = False
            exit()
        print("Invalid Option")


def scary_game_start():
    print(
        "As you drive down the street, your anxiety creeps up. You are terrified of what you will find in this house, but it is too late now. You've already signed yourself up for whatever will greet you.")
    user_response = input("")
    print(
        "You pull up to the driveway and are reminded of what this house used to be. You remember the white railing that went along the front porch. The blue siding of the house with the complementary red door. The two chairs that Ma and Pa used to read every Saturday morning in. The grass would never grow no matter what Ma's friends put on it. All tied together with a fence that used to keep Charlie, your old dog, inside.")
    print("look around | get out of car")
    user_car = input("")
    user_car = user_car.lower()
    if user_car == "look around":
        next_location = "inside car"
        return
    elif user_car == "get out of car":
        next_location = "outside"
        return

def in_car():
    global next_location
    global have_key
    global have_note

    print("You see a glovebox, the car keys, and you can also see the generator on the side of the house.")
    print("open glovebox | get out of car")
    user_look_car = input("")
    if user_look_car == "open glovebox":
        print("You open the glovebox and see keys on a key ring along a note with some napkins and documents.")
        print("Take the Keys?")
        user_take_key = input("")
        if user_take_key == "yes":
            print("You take the keys hoping they're the keys for the house, you don't remember for some reason")
            have_key = True
            print("Would you like to take the note?")
            take_note = input("")
            if take_note == "yes":
                have_note = True
                print("You take the 'Note' it feels weird in your hands")
                print("Read note?")
                read_note = input("")
                if read_note == "yes":
                    print("You open the old crumbled note and it reads:")
                    print(
                        "Hey Son, welcome back, weve missed you! Theres still Thanksgiving dinner out for you along with your favorite game in your room. Dont forget to turn the generator on the side of the side. We love you - Ma and Pa")
                    user_response = input("")
                    print("Get out of the car?")
                    get_out_of_car = input("")
                    if get_out_of_car == "yes":
                        next_location = "outside"
                        return
                elif read_note == "no":
                    print("You decide not to read the note as it already makes you uncomfertable.")
                    print("Get out of the car?")
                    get_out_of_car = input("")
                    if get_out_of_car == "yes":
                        next_location = "outside"
                        return

            elif take_note == "no":
                have_note = False
                print("Get out of the car?")
                get_out_of_car = input("")
                if get_out_of_car == "yes":
                    next_location = "outside"
                    return
                else:
                    print("you have to progress.")
                    print("Get out of the car?")
                    get_out_of_car = input("")
                    if get_out_of_car == "yes":
                        next_location = "outside"
                        return
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
                    print(
                        "Hey Son, welcome back, weve missed you! Theres still Thanksgiving dinner out for you along with your favorite game in your room. Dont forget to turn the generator on the side of the side. We love you - Ma and Pa")
                    user_response = input("")
                    print("You cumble the note into your pocket")
                    print("Go inside the house?")
                    user_response = input("")
                    if user_response == "yes":
                        next_location = "inside house"
                        return
                    elif user_response == "no":
                        next_location = "outside"
                        return
                elif read_note == "no":
                    print("You decide not to read the note as it already makes you uncomfertable.")
                    print("Get out of the car?")
                    get_out_of_car = input("")
                    if get_out_of_car == "yes":
                        next_location = "outside"
                        return
                    elif get_out_of_car == "no":
                        next_location = "inside car"
                        return
    elif user_look_car == "get out of car":
        next_location = "outside"
        return

def house_has_power():
    global house_power
    global have_key

    if house_power == True:
            print("The house makes a loud 'whirling' sound and boots up like a Windows Home Vista")
            print("go inside house | go inside car")
            user_next_move = input("")
            if user_next_move == "go inside car":
                print("You go back into the car as though you forgot something")
                next_location = "inside car"
                return
            elif user_next_move == "go inside house":
                print(
                    "You walk up the old and forgotten stairs to the front door, you can see that it still has Ma and Pa's old engravings in it, this reminds you of when they did it, you miss those days.")
                next_location = "inside house"
                return
    elif house_power == False:
            print("The house is dark and dim in a way that makes you extremly anxious and this takes over you, you can not enter without turning on the generator.")
            print("Turn on the Generator?")
            tog_again = input("")
            if tog_again == "yes":
                house_power = True
                print("go inside house | go inside car")
                user_next_move = input("")
                if user_next_move == "go inside house":
                    next_location = "inside house"
                    return
            if user_next_move == "go inside car":
                print("You go back into the car as though you forgot something")
                next_location = "inside car"
                return

def inside_house():
    global have_key
    global house_power
    global have_note

    if have_key == True:
        print("It works! You creek open the old rusty door and take in what you see.")
        print("look around")
        user_inside_house = input("")
        if user_inside_house == "look around":
            print("You look around and your in the entry with the stairs directly to the left of you. In front of you you can see the 'living room' with the old blue couch and TV that you're surprised is stolen directly in front on a tv stand. In the 'living room' is the 'kitchen' and 'dining room' with and open entryway so you can see straight into the dirty abandoned kitchen.")
            print("go into living room | go into kitchen | go into dining room")
            go_int_lkd = input("")
            if go_int_lkd == "go into living room":
                print("You walk straight into the living room")
    elif have_key == False:
            print("You try to open the door but its locked you think that you may have left the keys in the glovebox")
            while go_back_car == False:
                print("Go back to car?")
            go_back_car = input("")
            if go_back_car == "yes":
                next_location = "inside car"
                return

def user_outside():
    global house_power
    global have_key

    print("You get out of the car and see the generator to the left of the house.")
    print("Turn on the Generator?")
    turn_on_gen = input("")

    if turn_on_gen == "yes":
        house_power = True
        next_location = "generator"
        return
    elif turn_on_gen == "no":
        house_power = False
        next_location = "generator"
        return

def main():
    game_running = True
    next_location = ""
    scary_game_soq()
    scary_game_start()
    while game_running == True:
        if next_location == "inside car":
            next_location = in_car()
        elif next_location == "generator":
            next_location = house_has_power()
        elif next_location == "outside":
            next_location = user_outside()
        elif next_location == "inside house":
            next_location = inside_house()
        else:
            print("Error")
            game_running = False


main()
