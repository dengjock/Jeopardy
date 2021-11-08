from functions import enter_display, answer_decision
from colorama import Fore, Back, Style

points = 0
enter_display()
player_1 = 0
player_2 = 0

print()
game_board = [

    ["100S", "100H", "100G", "100M", "100V"],
    ["200S", "200H", "200G", "200M", "200V"],
    ["300S", "300H", "300G", "300M", "300V"],
    ["400S", "400H", "400G", "400M", "400V"],
    ["500S", "500H", "500G", "500M", "500V"]

    ]

i = 0
labels = ["Science", "History", "Geography", "Music", "Variety"]


for subject in labels:
    print("{:12}".format(subject), end = "")
print()
attempts = 0

# print('\n'.join(['\t\t'.join([str(cell) for cell in row]) for row in game_board]))
for row in game_board:
    for item in row:
        print("{:12}".format(item), end = "")
    print()

answers = {
    "Science" : [
        {"question" : "How many bones are there in a adult human body?", "answer" : "206"},
        {"question" : "How many planets are in the solar system?", "answer" : "8"},
        {"question" : "What does DNA stand for?", "answer"  : "Deoxyribonucleic acid"},
        {"question" : "What is the formula for water?", "answer"  : "H20"},
        {"question" : "How many elements are on the periodic table?", "answer"  : "118"}
    ],
    "History" : [
        {"question" : "When did the Roman Empire end?", "answer"  : "395 AD"},
        {"question" : "When did the French revolution begin?", "answer"  : "1789"},
        {"question" : "How many times was Julius Caesar stabbed?", "answer"  : "23 times"},
        {"question" : "What was the largest empire in history?", "answer"  : "British Empire"}, 
        {"question" : "What is the longest river in the world?", "answer"  : "Nile" or "Nile river" or "nile river"}
    ],

    "Geography": [
        {"question" : "What is the largest continent?", "answer"  : "Asia" or "asia"},
        {"question" : "What continent has the most countries in it?", "answer"  : "Africa" or "africa"},
        {"question" : "What is the largest US state?", "answer"  : "Alaska" or "alaska"},
        {"question" : "What is France's largest border neighbor?", "answer"  : "Brazil" or "brazil"},
        {"question" : "Which country has the most lakes?", "answer"  : "Canada" or "canada"}

    ],
    "Music" :[
        {"question" : "What is the most expensive instrument sold?", "answer"  : "Violin" or "violin"},
        {"question" : "What band played on all continents?", "answer"  : "Metallica" or "metallica"},
        {"question" : "When will the longest performance end?", "answer"  : "2640"},
        {"question" : "What is the most sold album of all time?", "answer"  : "Thriller" or "thriller"},
        {"question" : "Who has the most #1 hits of all time?", "answer"  : "The Beatles" or "the beatles" or "The beatles"} 
    ],
    "Variety":[
        {"question" : "Who is the lead singer of Pearl Jam?", "answer"  : "Eddie Vedder"},
        {"question" : "Who turned evil in Star Wars?", "answer"  : "Anakin" or "Anakin Skywalker"},
        {"question" : "What element makes up 25% of the Earth's crust?", "answer"  : "Silicon"},
        {"question" : "What Greek god is called Jupiter in Rome?", "answer"  : "Zeus"},
        {"question" : "Who created the Apple II?", "answer"  : "Steve Wozniak"}

    ]
}

game_status = 3
science_1 = False
science_2 = False 
science_3 = False
science_4 = False
science_5 = False
history_1 = False
history_2 = False
history_3 = False
history_4 = False
history_5 = False
geography_1 = False
geography_2 = False
geography_3 = False
geography_4 = False
geography_5 = False
music_1 = False
music_2 = False
music_3 = False
music_4 = False
music_5 = False
variety_1 = False
variety_2 = False
variety_3 = False
variety_4 = False
variety_5 = False


while game_status != 0 and points < 3500 and attempts < 25:
    user_selection = input()
    if user_selection ==  "100S" and science_1 == False:
        print(answers["Science"][0]["question"])
        user_answer = input()
        if user_answer == answers["Science"][0]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 100!" + Style.RESET_ALL)
            points = points + 100
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        science_1 = True
        print()
        game_board[0][0] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1 
    
    elif user_selection == "200S" and science_2 == False:
        print(answers["Science"][1]["question"])
        user_answer = input()
        if user_answer == answers["Science"][1]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 200!" + Style.RESET_ALL)
            points = points + 200
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        science_2 = True
        print()
        game_board[1][0] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "300S" and science_3 == False:
        print(answers["Science"][2]["question"])
        user_answer = input()
        if user_answer == answers["Science"][2]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 300!" + Style.RESET_ALL)
            points = points + 300
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        science_3 = True
        print()
        game_board[2][0] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "400S" and science_4 == False:
        print(answers["Science"][3]["question"])
        user_answer = input()
        if user_answer == answers["Science"][3]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 400!" + Style.RESET_ALL)
            points = points + 400
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        science_4 = True
        print()
        game_board[3][0] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "500S" and science_5 == False:
        print(answers["Science"][4]["question"])
        user_answer = input()
        if user_answer == answers["Science"][4]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 400!" + Style.RESET_ALL)
            points = points + 400
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        science_5 = True
        print()
        game_board[4][0] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "100H" and history_1 == False:
        print(answers["History"][0]["question"])
        user_answer = input()
        if user_answer == answers["History"][0]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 100!" + Style.RESET_ALL)
            points = points + 100
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        history_1 = True
        print()
        game_board[0][1] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "200H" and history_2 == False:
        print(answers["History"][1]["question"])
        user_answer = input()
        if user_answer == answers["History"][1]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 200!" + Style.RESET_ALL)
            points = points + 200
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        history_2 = True
        print()
        game_board[1][1] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "300H" and history_3 == False:
        print(answers["History"][2]["question"])
        user_answer = input()
        if user_answer == answers["History"][2]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 300!" + Style.RESET_ALL)
            points = points + 300
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        history_3 = True
        print()
        game_board[2][1] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "400H" and history_4 == False:
        print(answers["History"][3]["question"])
        user_answer = input()
        if user_answer == answers["History"][3]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 400!" + Style.RESET_ALL)
            points = points + 400
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        history_4 = True
        print()
        game_board[3][1] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "500H" and history_5 == False:
        print(answers["History"][4]["question"])
        user_answer = input()
        if user_answer == answers["History"][4]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 500!" + Style.RESET_ALL)
            points = points + 500
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        history_5 = True
        print()
        game_board[4][1] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "100G" and geography_1 == False:
        print(answers["Geography"][0]["question"])
        user_answer = input()
        if user_answer == answers["Geography"][0]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 100!" + Style.RESET_ALL)
            points = points + 100
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        geography_1 = True
        print()
        game_board[0][2] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "200G" and geography_2 == False:
        print(answers["Geography"][1]["question"])
        user_answer = input()
        if user_answer == answers["Geography"][1]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 200!" + Style.RESET_ALL)
            points = points + 200
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        geography_2 = True
        print()
        game_board[1][2] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "300G" and geography_3 == False:
        print(answers["Geography"][2]["question"])
        user_answer = input()
        if user_answer == answers["Geography"][2]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 300!" + Style.RESET_ALL)
            points = points + 300
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        geography_3 = True
        print()
        game_board[2][2] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1
        
    elif user_selection == "400G" and geography_4 == False:
        print(answers["Geography"][3]["question"])
        user_answer = input()
        if user_answer == answers["Geography"][3]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 400!" + Style.RESET_ALL)
            points = points + 400
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        geography_4 = True
        print()
        game_board[3][2] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "500G" and geography_5 == False:
        print(answers["Geography"][4]["question"])
        user_answer = input()
        if user_answer == answers["Geography"][4]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 500!" + Style.RESET_ALL)
            points = points + 500
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        geography_5 = True
        print()
        game_board[4][2] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "100M" and music_1 == False:
        print(answers["Music"][0]["question"])
        user_answer = input()
        if user_answer == answers["Music"][0]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 100!" + Style.RESET_ALL)
            points = points + 100
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        music_1 = True
        print()
        game_board[0][3] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "200M" and music_2 == False:
        print(answers["Music"][1]["question"])
        user_answer = input()
        if user_answer == answers["Music"][1]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 200!" + Style.RESET_ALL)
            points = points + 200
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        music_2 = True
        print()
        game_board[1][3] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "300M" and music_3 == False:
        print(answers["Music"][2]["question"])
        user_answer = input()
        if user_answer == answers["Music"][2]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 300!" + Style.RESET_ALL)
            points = points + 300
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        music_3 = True
        print()
        game_board[2][3] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "400M" and music_4 == False:
        print(answers["Music"][3]["question"])
        user_answer = input()
        if user_answer == answers["Music"][3]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 400!" + Style.RESET_ALL)
            points = points + 400
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        music_4 = True
        print()
        game_board[3][3] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "500M" and music_5 == False:
        print(answers["Music"][4]["question"])
        user_answer = input()
        if user_answer == answers["Music"][4]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 500!" + Style.RESET_ALL)
            points = points + 500
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        music_5 = True
        print()
        game_board[4][3] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "100V" and variety_1 == False:
        print(answers["Variety"][0]["question"])
        user_answer = input()
        if user_answer == answers["Variety"][0]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 100!" + Style.RESET_ALL)
            points = points + 100
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        variety_1 = True
        print()
        game_board[0][4] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "200V" and variety_2 == False:
        print(answers["Variety"][1]["question"])
        user_answer = input()
        if user_answer == answers["Variety"][1]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 200!" + Style.RESET_ALL)
            points = points + 200
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        variety_2 = True
        print()
        game_board[1][4] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "300V" and variety_3 == False:
        print(answers["Variety"][2]["question"])
        user_answer = input()
        if user_answer == answers["Variety"][2]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 300!" + Style.RESET_ALL)
            points = points + 300
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        variety_3 = True
        print()
        game_board[2][4] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "400V" and variety_4 == False:
        print(answers["Variety"][3]["question"])
        user_answer = input()
        if user_answer == answers["Variety"][3]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 400!" + Style.RESET_ALL)
            points = points + 400
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        variety_4 = True
        print()
        game_board[3][4] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "500V" and variety_5 == False:
        print(answers["Variety"][4]["question"])
        user_answer = input()
        if user_answer == answers["Variety"][4]["answer"]:
            print(Fore.GREEN + "Correct, your points have increased by 500!" + Style.RESET_ALL)
            points = points + 500
        else:
            print(Fore.RED + "Your response was incorrect." + Style.RESET_ALL)
            game_status = game_status - 1
        variety_5 = True
        print()
        game_board[4][4] = "   X"
        for subject in labels:
            print("{:12}".format(subject), end = "")
        print()
        for row in game_board:
            for item in row:
                print("{:12}".format(item), end = "")
            print()
        attempts = attempts + 1

    elif user_selection == "End":
        game_status = 0
    elif user_selection == "100S" and science_1 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "200S" and science_2 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "300S" and science_3 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "400S" and science_4 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "500S" and science_5 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "100H" and history_1 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "200H" and history_2 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "300H" and history_3 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "400H" and history_4 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "500H" and history_5 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "100G" and geography_1 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "200G" and geography_2 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "300G" and geography_3 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "400G" and geography_4 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "500G" and geography_5 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "100M" and music_1 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "200M" and music_2 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "300M" and music_3 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "400M" and music_4 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "500M" and music_5 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "100V" and variety_1 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "200V" and variety_2 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "300V" and variety_3 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "400V" and variety_4 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    elif user_selection == "500V" and variety_5 == True:
        print(Fore.RED + "You already answered this question." + Style.RESET_ALL)
    
    elif user_selection not in game_board:
        print(Fore.RED + "Selection not found in gameboard try again."  + Style.RESET_ALL)

if game_status == 0:
    print("Your final score was {} points.".format(points))
if points >= 3500:
    print(Fore.GREEN + "Congrats you have {} points which is the max".format(points)  + Style.RESET_ALL)
if attempts > 25:
    print(Fore.RED + "You have exceeded the amount of attempts."  + Style.RESET_ALL)