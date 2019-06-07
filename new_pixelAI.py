#fix infinite recommendation loop
def next_activity():
    print("What's the next thing you would like to do?")
    activity = input() 
    if "bored" in activity:
        recomendations()
    elif "recommendations" in activity:
        recomendations()
    elif "I don't know" or "i don't know" in activity:
        recomendations()
    elif "anything" in activity:
        recomendations()

    if "date" or "time" in activity:
        date()

    if "remind" or "remind me" in activity:
        toDo()

    if "websites" or "internet" in activity:
        websites()
    
    if "joke" or "jokes" in activity:
        jokes()
    elif "riddle" or "riddles" in activity:
        riddles()

    if "play" or "game" in activity:
        print("Which game?")
        game_type = input()
        if "rock" in game_type:
            rock_paper_scissors()
        elif "number" or "guessing" in game_type():
            guess_my_number()

def start():
    print("Hello! My name is Pixel. " + "What would you like help with today?")
    print("(Type 'What can you do?' to see what I can do)")
    wait = input("PRESS ENTER TO CONTINUE")
    next_activity()

def recomendations():
    print("I can...")
    print("Tell you a joke")
    wait = input("PRESS ENTER TO CONTINUE")
    print("Tell you the date")
    wait = input("PRESS ENTER TO CONTINUE")
    print("Show you interesting websites")
    wait = input("PRESS ENTER TO CONTINUE")
    print("Help you keep track of things")
    wait = input("PRESS ENTER TO CONTINUE")
    print("And I can also play games and tell jokes/riddles")
    wait = input("PRESS ENTER TO CONTINUE")
    print("After hearing that, what would you like to do?")
    next_activity()

def date():
    import datetime
    date = datetime.datetime.now()
    month = date.month
    day = date.day
    year = date.year
    print(month, day, year)
    print("That's today's date! What else would you like to do?")
    next_activity()

def websites():
    print("Before I can show you some interesting websites, I need to kno wwhat you like to do on the internet. " + 
    "Please, describe below. Then, the tabs will open in your default browser") 
    internet_activity = input()
    if "don't know" in internet_activity:
        print("Here are some general recomendations")
        Google = ("Google", "https://www.google.com")
        YouTube = ("YouTube", "https://www.youtube.com") 
        Reddit = ("Reddit", "https://www.reddit.com")
        Coding_Resources = ("Coding Resources", "https://www.w3schools.com")
        print(Google[0])
        print(YouTube[0])
        print(Reddit[0])
        print(Coding_Resources[0])
        import webbrowser
        webbrowser.open_new_tab(Google[1])
        webbrowser.open_new_tab(YouTube[1])
        webbrowser.open_new_tab(Reddit[1])
        webbrowser.open_new_tab(Coding_Resources[1])
    else:
        print("x")

    next_activity()

start() 