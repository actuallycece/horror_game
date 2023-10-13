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
        return "start game"
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
    if user_car == "look around":
        print("You see a glovebox, the car keys, and you can also see the generator on the side of the house.")
        valid_options = ["open glovebox", "get out of car"]
        user_look_car = get_user_selection(valid_options)
        if user_look_car == "open glovebox":
            print("You open the glovebox and see 'keys' on a key ring along a 'note' with some napkins and documents.")
            print("Take the:")
            valid_options = ["keys", "note", "none"]
            user_take_key = get_user_selection(valid_options)
            if user_take_key == "keys":
                return "keys"
            elif user_take_key == "note":
                return "car note"
            elif user_take_key == "none":
                return "inside car"
        elif user_look_car == "get out of car":
            return "outside"
    elif user_car == "get out of car":
        return "outside"


def get_keys():
    global next_location
    global have_key
    while have_key == False:
        have_key = True
        print("You take the keys hoping they're the keys for the house, you don't remember for some reason")
        print("Would you like to take the 'note'?")
        valid_options = ["yes", "no"]
        take_note = get_user_selection(valid_options)
        if take_note == "yes":
            return "car note"
        elif take_note == "no":
            print("You decide not to take the note as it makes you uncomfortable.")
            print("Get out of the car?")
            valid_options = ["yes", "no"]
            get_out_of_car = get_user_selection(valid_options)
            if get_out_of_car == "yes":
                return "outside"
            elif get_out_of_car == "no":
                return "inside car"
    while have_key:
        print("You've already taken the keys. Would you like to take the note?")
        valid_options = ["yes", "no"]
        take_note = get_user_selection(valid_options)
        if take_note == "yes":
            return "car note"
        elif take_note == "no":
            return "inside car"


def note_in_car():
    global next_location
    global have_note
    while have_note == False:
        have_note = True
        print("You take the 'Note' it feels weird in your hands.")
        print("Read note?")
        valid_options = ["yes", "no"]
        read_note = get_user_selection(valid_options)
        if read_note == "yes":
            print("You open the old, crumbled, alcohol-smelling note, and it reads:")
            print(
                "Hey Son, welcome back; we've missed you! There's Thanksgiving dinner out for you, along with your favorite game in your room. Don't forget to turn the generator on the side of the side. We love you - Ma and Pa")
            user_response = input("")
            print("You crumble the note into your pocket")
            user_response = input("")
            print("Get out of the car?")
            valid_options = ["yes", "no"]
            get_out_of_car = get_user_selection(valid_options)
            if get_out_of_car == "yes":
                return "outside"
            elif get_out_of_car == "no":
                return "inside car"
        elif read_note == "no":
            print("You decide not to read the note as it already makes you uncomfortable.")
            print("Get out of the car?")
            valid_options = ["yes", "no"]
            get_out_of_car = get_user_selection(valid_options)
            if get_out_of_car == "yes":
                return "outside"
            elif get_out_of_car == "no":
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
        if user_next_move == "house":
            print(
                "You walk up the old and forgotten stairs to the front door, you can see that it still has Ma and Pa's old engravings in it, this reminds you of when they did it, you miss those days.")
            return "inside house"
        elif user_next_move == "car":
            print("You go back into the car as though you forgot something")
            return "inside car"
    while house_power == False:
        print(
            "The house is dark and dim in a way that makes you extremely anxious and this takes over you, you can not enter without turning on the generator.")
        print("Turn on the Generator?")
        valid_options = ["yes", "no"]
        tog_again = get_user_selection(valid_options)
        if tog_again == "yes":
            return "generator"
        elif tog_again == "no":
            return "outside"


def user_outside():
    global next_location
    global house_power
    print("You are outside you can see the 'car' and the 'generator to the left of the house.")
    print("Go to:")
    valid_options = ["car", "generator"]
    car_or_gen = get_user_selection(valid_options)
    if car_or_gen == "car":
        return "inside car"
    elif car_or_gen == "generator":
        print("Turn on the Generator?")
        valid_options = ["yes", "no"]
        turn_on_gen = get_user_selection(valid_options)
        if turn_on_gen == "yes":
            house_power = True
            return "generator"
        elif turn_on_gen == "no":
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
    if open_the_door == "yes" and have_key:
        print("It works! You you twist the key and creek open the old rusty door and take in what you see.")
        print("Look around?")
        valid_options = ["yes"]
        user_inside_house = get_user_selection(valid_options)
        if user_inside_house == "yes":
            return "inside entryway"
    elif open_the_door == "yes" and have_key == False:
        print("You try to open the door but its locked you think that you may have left the keys in the glovebox")
        return "outside"
    elif open_the_door == "no":
        print("Where would you like to go?")
        print("car | generator")
        valid_options = ["car", "generator"]
        cog = get_user_selection(valid_options)
        if cog == "car":
            return "inside car"
        elif cog == "generator":
            return "outside"


def entryway():
    global next_location
    print(
        "You look around and are in the entryway with the stairs directly to your left. In front of you, you can see the 'living room' with the old brown couch and TV that you're surprised aren't stolen directly in front of a tv stand. In the 'living room' is the 'kitchen' and 'dining room' with an open entryway to see straight into the dirty, abandoned kitchen.")
    print("go into:")
    valid_options = ["living room", "dining room", "upstairs"]
    go_into_lkd = get_user_selection(valid_options)
    if go_into_lkd == "living room":
        return "inside living room"
    elif go_into_lkd == "dining room":
        return "inside dining room"
    elif go_into_lkd == "upstairs":
        return "going upstairs"


def living_room():
    global next_location
    print(
        "You walk into the dirty and dingy living room. Red liquid seeped into the carpet everywhere, along with old bottles and plates of food on the coffee table. Aside from the dishes are the TV remote and two coasters with cups on them. The cups are filled with a thick black, tar-like liquid... and smell. This place is nothing like it used to be. ")
    print("go inside:")
    valid_options = ["entryway", "dining room", "kitchen"]
    edk_response = get_user_selection(valid_options)
    if edk_response == "entryway":
        return "inside entryway"
    elif edk_response == "dining room":
        return "inside dining room"
    elif edk_response == "kitchen":
        return "inside kitchen"


def dining_room():
    global next_location
    global eaten_dinner
    print(
        "The dining room has the same carpet as the living room, with a long table, five chairs, and six placemats. There's a Turkey in the middle of the table, along with some greens, sweet potato pie, ham, mashed potatoes, corn, and candy yams.")
    user_response = input("")
    return "eat dinner"


def eat_dinner():
    global next_location
    global eaten_dinner
    if eaten_dinner == False:
        print("Eat Thanksgiving dinner?")
        valid_options = ["yes", "no"]
        user_etd = get_user_selection(valid_options)
        if user_etd == "yes":
            eaten_dinner = True
            print("You take a bite of the ham; it's gross. It tastes like roadkill. ")
            user_response = input("")
            print("You think you have to vomit and would prefer to do it in the cellar.")
            print("go into:")
            valid_options = ["living room", "kitchen", "cellar"]
            user_lok = get_user_selection(valid_options)
            if user_lok == "living room":
                return "inside living room"
            elif user_lok == "kitchen":
                return "inside kitchen"
            elif user_lok == "cellar":
                return "inside cellar"
        elif user_etd == "no":
            print("You decide not to eat the rotten food, it looks like its been a couple years anyways.")
            print("go into: living room | kitchen")
            valid_options = ["living room", "kitchen"]
            user_lok = get_user_selection(valid_options)
            if user_lok == "living room":
                return "inside living room"
            elif user_lok == "kitchen":
                return "inside kitchen"
    elif eaten_dinner:
        user_response = input("")
        print("go into: living room | kitchen")
        valid_options = ["living room", "kitchen"]
        user_lok = get_user_selection(valid_options)
        if user_lok == "living room":
            return "inside living room"
        elif user_lok == "kitchen":
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
        if go_into_dr == "dining room":
            return "inside dining room"
    elif drunk_drink == False:
        return "drink drink"

def drink_drink():
    global next_location
    global user_sick
    print("Would you like to drink the drink?")
    valid_options = ["yes", "no"]
    drink_the_drink = get_user_selection(valid_options)
    if drink_the_drink == "yes":
        user_sick = True
        print("You drink a sip of some alcohol left in bottle. It taste like watered down acid.")
        user_response = input("")
        print("Where would you like to go:")
        valid_options = ["living room"]
        go_into_lr = get_user_selection(valid_options)
        if go_into_lr == "living room":
            return "inside living room"
    elif drink_the_drink == "no":
        print("You decide not to drink the drink as that sounds disgusting and you dont know what you even thought to do that.")
        user_response = input("")
        print("Where would you like to go?")
        valid_options = ["living room"]
        go_into_lr = get_user_selection(valid_options)
        if go_into_lr == "living room":
            return "inside living room"


def cellar():
    global next_location
    global cellar_note
    print("You walk down the stairs and into the cellar. Suddenly you dont feel sick anymore, you do have headache though. Inside the cellar you can see old boxes and an opened gift alongside a note.")
    if cellar_note:
        print("Look at 'gift'?")
        valid_options = ["yes", "no"]
        look_at_gift = get_user_selection(valid_options)
        if look_at_gift == "yes":
            print("You think it was a bottle; all left is a box, an elegant red ribbon, and a note.")
            user_response = input("")
            print("Go back upstairs?")
            valid_options = ["yes", "no"]
            go_back_us = get_user_selection(valid_options)
            if go_back_us == "yes":
                return "inside dining room"
            elif go_back_us == "no":
                return "inside cellar"
        elif look_at_gift == "no":
            print("Go back upstairs?")
            valid_options = ["yes", "no"]
            go_back_us = get_user_selection(valid_options)
            if go_back_us == "yes":
                return "inside dining room"
            elif go_back_us == "no":
                return "inside cellar"
    elif cellar_note == False:
        print("Get the note?")
        valid_options = ["yes", "no"]
        get_note = get_user_selection(valid_options)
        if get_note == "yes":
            cellar_note = True
            print("You pick the note up off the floor.")
            print("Read the note?")
            valid_options = ["yes", "no"]
            read_cellar_note = get_user_selection(valid_options)
            if read_cellar_note == "yes":
                print("Hey son, it's Pa. I just want you to know how genuinely proud of you I am. You are doing everything I know you would, and you haven't failed me yet, and I know you won't. ")
                user_response = input("")
                print("What would you like to do?")
                valid_options = ["look at gift", "go upstairs"]
                gift_or_upstairs = get_user_selection(valid_options)
                if gift_or_upstairs == "look at gift":
                    print("You think it was a bottle; all left is a box, an elegant red ribbon, and a note.")
                    user_response = input("")
                    print("Go back upstairs?")
                    valid_options = ["yes", "no"]
                    go_back_us = get_user_selection(valid_options)
                    if go_back_us == "yes":
                        return "inside dining room"
                    elif go_back_us == "no":
                        return "inside cellar"
                elif gift_or_upstairs == "go upstairs":
                    return "inside dining room"
            elif read_cellar_note == "no":
                print("You decide not to read the note as it makes you uncomfortable.")
                user_response = input("")
                print("What would you like to do?")
                valid_options = ["look at gift", "go upstairs"]
                gift_or_upstairs = get_user_selection(valid_options)
                if gift_or_upstairs == "look at gift":
                    print("You think it was a bottle; all left is a box, an elegant red ribbon, and a note.")
                    user_response = input("")
                    print("Go back upstairs?")
                    valid_options = ["yes", "no"]
                    go_back_us = get_user_selection(valid_options)
                    if go_back_us == "yes":
                        return "inside dining room"
                    elif go_back_us == "no":
                        return "inside cellar"
                elif gift_or_upstairs == "go upstairs":
                    return "inside dining room"
        elif get_note == "no":
            print("You decide not to get the note as it makes you uncomfortable.")
            user_response = input("")
            print("Look at 'gift'?")
            valid_options = ["yes", "no"]
            look_at_gift = get_user_selection(valid_options)
            if look_at_gift == "yes":
                print("You think it was a bottle; all left is the box, an elegant red ribbon, and the note.")
                user_response = input("")
                print("Go back upstairs?")
                valid_options = ["yes", "no"]
                go_back_us = get_user_selection(valid_options)
                if go_back_us == "yes":
                    return "inside living room"
                elif go_back_us == "no":
                    return "inside cellar"
            elif look_at_gift == "no":
                print("Go back upstairs?")
                valid_options = ["yes", "no"]
                go_back_us = get_user_selection(valid_options)
                if go_back_us == "yes":
                    return "inside living room"
                elif go_back_us == "no":
                    return "inside cellar"


def upstairs():
    global next_location
    print("Walking up the stairs, you can see the old drawings you and your siblings did as kids on the walls. One that you know *** did in particular. This makes you sad, but you keep walking. ")
    user__response = input("")
    return "top of stairs"


def top_of_the_stairs():
    global next_location
    print("You're at the top of the stairs, here are all of the rooms. You can see 'your room', '01101101 01101001 01100001's room', 'michael and brayan's room', 'ma and pa's room', and a 'bathroom'")
    print("Where would you like to go?")
    valid_options = ["my room", "01101101 01101001 01100001's room", "michael and brayan's room", "ma and pa's room", "bathroom"]
    where_upstairs = get_user_selection(valid_options)
    if where_upstairs == "my room":
        return "my room"
    elif where_upstairs == "01101101 01101001 01100001's room":
        return "mias room"
    elif where_upstairs == "michael and brayan's room":
        return "brothers room"
    elif where_upstairs == "ma and pa's room":
        return "parents room"
    elif where_upstairs == "bathroom":
        return "upstairs bathroom"


def my_room():
    global next_location
    print("You step into your room and its exatly like you left it, this calms you. You look around and see your desk and computer in front of you, your bed to the right side of the room agaisnt the wall with you night stands on both side of it, and to the left is your old dirty laudry and closet which is all pack up in boxes...things are not how you left them.")
    user__response = input("")
    print("You start to notice you bed is covered in a blood like substance but its very tar like in texture. The floor is covered in alocohol and theres a note on the nightstand.")
    user__response = input("")
    print("Where would you like to go?")
    valid_options = ["bed", "computer"]
    in_my_room = get_user_selection(valid_options)
    if in_my_room == "bed":
        print("You start walking up to the bed and you start feeling tipsy, and then drunk, and then...you stumble. ")
        user__response = input("")
        print("You start thinking that taking a rest in bed might be good for you.")
        print("Rest in bed?")
        valid_options = ["yes"]
        rest = get_user_selection(valid_options)
        if rest == "yes":
            print("You lay down in the bed and begin dreaming...'Im sorry Mia' 'Im so sorry Mia' you begin saying over and over again")
            user__response = input("")
            print("Wake up?")
            valid_options = ["yes"]
            wake_up = get_user_selection(valid_options)
            if wake_up == "yes":
                print("She cant wake up")
                user__response = input("")
                print("....")
                user__response = input("")
                print("........")
                user__response = input("")
                print("...")
                user__response = input("")
                return "new game"
    elif in_my_room == "computer":
        print("You walk up to the computer and notice your favorite game is still inside of it.")
        user__response = input("")
        print("Play game?")
        valid_options = ["yes", "no"]
        play_game = get_user_selection(valid_options)
        if play_game == "yes":
            return "new game"
        elif play_game == "no":
            print("Go the bed?")
            valid_options = ["yes"]
            go_to_bed = get_user_selection(valid_options)
            if go_to_bed == "yes":
                print("You get up for the computer and walk up to the bed you can see a 'note' on the bedside table.")
                user__response = input("")
                print("Read the note?")
                valid_options = ["yes", "no"]
                read_room_note = get_user_selection(valid_options)
                if read_room_note == "yes":
                    print("You have to wake up.")
                    user__response = input("")
                    print("This note makes you weary you decide to take a nap on the bed.")
                    user__response = input("")
                    return "new game"
                elif read_room_note == "no":
                    print("You decide not to read the room note, bute you decide to take a nap on the bed")
                    user__response = input("")
                    return "new game"


def mias_room():
    global next_location
    print("What have you done")
    user__response = input("")
    print("Your a terrible person")
    user__response = input("")
    print("How could you she was your sister")
    user__response = input("")
    print("....")
    user__response = input("")
    return "top of stairs"


def brothers_room():
    global next_location
    print("You walk into your Brothers old room, you feel like you should be in here but you see a 'note' on the bed")
    user__response = input("")
    print("Read the note?")
    valid_options = ["yes", "no"]
    read_brothers_note = get_user_selection(valid_options)
    if read_brothers_note == "yes":
        print("When he wakes up we're gonna tear him limb from limb")
        user__response = input("")
        print("You decide to leave the room as this note terrifies you")
        return "top of stairs"
    elif read_brothers_note == "no":
        print("You decide not to read the note as being in this room already makes you feel weird, you decide to leave.")
        return "top of stairs"


def parents_room():
    global next_location
    global user_sick
    print("You walk into your parents room, in the middle on the room you can see their bed and to the left the bathroom.")
    user__response = input("")
    if user_sick:
        print("You start feeling sick and run straight to the bathroom.")
        user__response = input("")
        print("As you are vomiting you vomit up a note.")
        user__response = input("")
        print("Read the note?")
        valid_options = ["yes", "no"]
        read_sick_note = get_user_selection(valid_options)
        if read_sick_note == "yes":
            print("Mia was closest to us, our only daughter, how could you. Please were begging you to wake up.")
            user__response = input("")
            print("This note makes you terrified so you decide to leave the room")
            user__response = input("")
            return "top of stairs"
        elif read_sick_note == "no":
            print("You decide not to read the note as its covered in puke.")
            user__response = input("")
            print("When you are done you decide the coming in here was the wrong idea and decide to leave.")
            user__response = input("")
            return "top of stairs"
    elif user_sick == False:
        print("You feel a strong urge to leave this room as you start to remember what you did.")
        user__response = input("")
        return "top of stairs"


def new_game():
    global next_location
    print("As you drive down the street, your happiness creeps up. You are excited to see the house. You've signed yourself up for whatever will greet you.")
    user__response = input("")
    print("You pull up to the driveway and are excited to join the party. Its your 25th birthday, what gifts will you get, whos going to be there, all these questions arise in your head. ")
    user__response = input("")
    return "in car party"


def in_car_party():
    global next_location
    valid_options = ["look around", "get out of car"]
    car_options = get_user_selection(valid_options)
    if car_options == "look around":
        print("You look around, theres balloons and and streamers everywhere and a banner that reads out 'Happy 25th Birthday Ian!'")
        user__response = input("")
        print("You get out of the car and start walking to the door.")
        user__response = input("")
        return "inside party"
    elif car_options == "get out of car":
        print("You get out of the car and start walking to the door.")
        user__response = input("")
        return "inside party"


def inside_party():
    global next_location
    print("As you are walking up to the door your Ma and Pa greet you with huge smiles on their faces, 'Welcome home son, and Happy Birthday.' says Ma 'We love you' says Pa")
    user__response = input("")
    print("Pa begins pulling something from behind his back, its a gift!")
    user__response = input("")
    print("'We are so proud of you for finishing college and everything else youve done in this life, this is just for you' says Pa")
    user__response = input("")
    print("You open the gift, its a bottle of your favorite drink, 'Hennessy Timeless Cognac' your excited to have some.")
    user__response = input("")
    print("You walk inside and you are greeted by a few of your college peers, old highschool friends, along with the rest of your family of course. Ma, Pa, Bryan, Michael, and Mia.")
    user__response = input("")
    print("You thank Ma for all the cooking shes done, you can see ham and many other things she cooked just for you. You also take a couple shots of your new drink with friends.")
    user__response = input("")
    print("You decide to go down to the cellar to grab another bottle, you stumble a few times but never fall. You open the box from your gift one more time before Mia calls you from upstairs.")
    user__response = input("")
    print("Mia asks if you can take her home as you promised you would so she can get to class on time tomorrow.")
    user__response = input("")
    return "take mia"


def take_mia():
    global next_location
    print("Take Mia home?")
    valid_options = ["yes", "no"]
    take_mia = get_user_selection(valid_options)
    if take_mia == "yes":
        print("You tell Mia of course you can take her, and we should go right now so you can still enjoy the party.")
        user__response = input("")
        return "taking mia"
    elif take_mia == "no":
        return "take mia"


def taking_mia():
    global next_location
    print("You both head to the car, your feeling a little drunk but nothing a little water cant fix.")
    user__response = input("")
    print("About a minute down the road you begin opening your water bottle with one hand and fail miserably...")
    user__response = input("")
    print("..you hit a tree....")
    user__response = input("")
    print("Mia is impaled by a branch, not breathing.")
    user__response = input("")
    print("Your pretty much unscaved, you stare into the abyss for a second")
    user__response = input("")
    print("......")
    user__response = input("")
    print("..........")
    user__response = input("")
    print("You begin hearing sirens")
    user__response = input("")
    print("You grab the brandy bottle and throw it as far as possible")
    user__response = input("")
    print("You burst open the car door and get out and begin trying to walk but its hard, you collapse to the ground and hit you head and.....")
    user__response = input("")
    print("......")
    user__response = input("")
    print("........")
    user__response = input("")
    print("....")
    user__response = input("")
    print("'Hes waking up!' 'Get the nurse!'")
    user__response = input("")
    print("'Now tell us what happened' says Pa")
    user__response = input("")
    print("Game Over")


def main():
    game_running = True
    next_location = scary_game_soq()
    while game_running == True:
        if next_location == "start game":
            next_location = start_of_game()
        elif next_location == "inside car":
            next_location = in_car()
        elif next_location == "keys":
            next_location = get_keys()
        elif next_location == "car note":
            next_location = note_in_car()
        elif next_location == "generator":
            next_location = house_has_power()
        elif next_location == "outside":
            next_location = user_outside()
        elif next_location == "inside house":
            next_location = inside_house()
        elif next_location == "inside entryway":
            next_location = entryway()
        elif next_location == "inside living room":
            next_location = living_room()
        elif next_location == "inside kitchen":
            next_location = kitchen()
        elif next_location == "drink drink":
            next_location = drink_drink()
        elif next_location == "inside dining room":
            next_location = dining_room()
        elif next_location == "eat dinner":
            next_location = eat_dinner()
        elif next_location == "inside cellar":
            next_location = cellar()
        elif next_location == "go upstairs":
            next_location = upstairs()
        elif next_location == "top of stairs":
            next_location = top_of_the_stairs()
        elif next_location == "my room":
            next_location = my_room()
        elif next_location == "mias room":
            next_location = mias_room()
        elif next_location == "brothers room":
            next_location = brothers_room()
        elif next_location == "parents room":
            next_location = master_bed_bathroom()
        elif next_location == "upstairs bathroom":
            next_location = upstairs_bathroom()
        elif next_location == "new game":
            next_location = new_game()
        elif next_location == "in car party":
            next_location = in_car_party()
        elif next_location == "inside party":
            next_location = inside_party()
        elif next_location == "take mia":
            next_location = take_mia()
        elif next_location == "taking mia":
            next_location = taking_mia()
        else:
            print("Error")
            game_running = False


main()
