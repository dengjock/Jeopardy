def answer_decision(user_selection):
    if user_selection in "100" or "200" or "300" or "400" or "500":
        if user_selection in "100":
            if user_selection[-1] == "S":
                return "100S"
            if user_selection[-1] == "H":
                return "100H"
            if user_selection[-1] == "G":
                return "100G"
            if user_selection[-1] == "M":
                return "100M"
            if user_selection[-1] == "V":
                return "100V"
        
        if user_selection in "200":
            if user_selection[-1] == "S":
                return "200S"
            if user_selection[-1] == "H":
                return "200H"
            if user_selection[-1] == "G":
                return "200G"
            if user_selection[-1] == "M":
                return "200M"
            if user_selection[-1] == "V":
                return "200V"
        
        if user_selection in "300":
            if user_selection[-1] == "S":
                return "300S"
            if user_selection[-1] == "H":
                return "300H"
            if user_selection[-1] == "G":
                return "300G"
            if user_selection[-1] == "M":
                return "300M"
            if user_selection[-1] == "V":
                return "300V"
        
        if user_selection in "400":
            if user_selection[-1] == "S":
                return "400S"
            if user_selection[-1] == "H":
                return "400H"
            if user_selection[-1] == "G":
                return "400G"
            if user_selection[-1] == "M":
                return "400M"
            if user_selection[-1] == "V":
                return "400V"

        if user_selection in "500":
            if user_selection[-1] == "S":
                return "500S"
            if user_selection[-1] == "H":
                return "500H"
            if user_selection[-1] == "G":
                return "500G"
            if user_selection[-1] == "M":
                return "500M"
            if user_selection[-1] == "V":
                return "500V"
def enter_display():
    return
print("Welcome to Jeopardy!")
print()
print("Choose your categories and points in the input.")
print()
print("Choose ONLY from the gameboard selection")
print()
print("Enter End exactly if you want to end the game")
print()
print("After each response to the question, type in another category.")


