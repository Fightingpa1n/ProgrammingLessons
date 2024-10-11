from time import sleep
#this is the solver file it contains the code for the solver functions that automatically checks exersises

def boolean(exersise): #check boolean exersises
    correct = 0 #set correct Total to 0
    for i in range(len(exersise)): #loop through all exersises
        question = exersise[i] #get the current question
        if question["value"] is None: #if the value is None
            _warning(f"[{i}] Question was not answered")
            sleep(0.2)
            continue
        if question["value"] == question["expected"]:
            correct += 1
        else:
            _wrong(f"[{i}] Wrong. [given: {question['expected']}| correct: {question['value']}]")
            sleep(0.2)
        
    evaluate(correct, len(exersise)) #evaluate the results

def math(exercise):  # check math exercises
    correct = 0  # set correct total to 0
    for i in range(len(exercise)):  # loop through all exercises
        question = exercise[i]  # get the current question

        if question['expected'] is None:  # if the value is None (i.e., not answered)
            _warning(f"[{i}] Question was not answered")
            sleep(0.2)
            continue
        
        try:
            result = eval(str(question['operation']))  # evaluate the operation
        except Exception as e:
            _warning(f"[{i}] Error evaluating operation: {e}")
            sleep(0.2)
            continue

        if isinstance(result, float) and isinstance(question['expected'], float):
            # If both result and expected are floats, check if they match within 2 decimal places
            if round(result, 2) == round(question['expected'], 2):
                correct += 1  # full point for correct answer
            else:
                _wrong(f"[{i}] Wrong. [given: {question['expected']} | expected: {result}]")
                sleep(0.2)

        elif isinstance(result, float) and isinstance(question['expected'], int):
            # If the result is a float but the expected is an int, check if rounding would make them equal
            if round(result) == question['expected']:
                correct += 0.5  # half point for correct answer but wrong type
                _warning(f"[{i}] Wrong type, but correct value. [given: {question['expected']} | expected: {result}]")
                sleep(0.2)
            else:
                _wrong(f"[{i}] Wrong. [given: {question['expected']} | expected: {result}]")
                sleep(0.2)

        elif isinstance(result, int) and isinstance(question['expected'], float):
            # If the result is an int but the expected is a float, check if they match
            if float(result) == round(question['expected'], 2):
                correct += 0.5  # half point for wrong type but correct answer
                _warning(f"[{i}] Wrong type, but correct value. [given: {question['expected']} | expected: {result}]")
                sleep(0.2)
            else:
                _wrong(f"[{i}] Wrong. [given: {question['expected']} | expected: {result}]")
                sleep(0.2)

        else:
            # If both are of the same type and correct
            if result == question['expected']:
                correct += 1  # full point for correct answer
            else:
                _wrong(f"[{i}] Wrong. [given: {question['expected']} | expected: {result}]")
                sleep(0.2)
    
    evaluate(correct, len(exercise))  # evaluate the results


def evaluate(correct, total): #evaluate the results
    score = correct / total * 100 #calculate the score (percentage)
    _info(f"Score: {correct}/{total} ({score}%)") #show the score
    sleep(0.2)
    if score == 100: #if the score is 100%
        _correct("Congratulations! Perfect score!\n"+IMAGE_PERFECT)
    elif score >= 80: #if score is above 80%
        _correct("POG!\n"+IMAGE_GOOD)
    elif score >= 30: #if score is above 30% 
        _warning("aRe YOu SeRioUs RiGhT nOw?\n"+IMAGE_NOTGOOD)
    elif score > 0: #if score is above 0%
        _wrong("No Programming Skill?!?\n"+IMAGE_BAD)
    else: #if score is 0%
        _wrong(IMAGE_TERRIBLE)

def _wrong(message):
    print(f"\033[31m{message}\033[0m")
def _correct(message):
    print(f"\033[32m{message}\033[0m")
def _warning(message):
    print(f"\033[33m{message}\033[0m")
def _info(message):
    print(f"\033[34m{message}\033[0m")

#image for 100%
IMAGE_PERFECT = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣶⣤⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⡿⠋⠉⠛⠛⠛⠿⣿⠿⠿⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⡀⢀⣽⣷⣆⡀⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣷⠶⠋⠀⠀⣠⣤⣤⣉⣉⣿⠙⣿⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠁⠀⠀⠴⡟⣻⣿⣿⣿⣿⣿⣶⣿⣦⡀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⠟⡿⠻⣿⠃⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠏⢹⣿⣿⣿⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣼⣷⡶⣿⣄⠀⠀⠀⠀⠀⢉⣿⣿⣿⡿⠀⠸⣿⣿⡿⣷⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡿⣦⢀⣿⣿⣄⡀⣀⣰⠾⠛⣻⣿⣿⣟⣲⡀⢸⡿⡟⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠞⣾⣿⡛⣿⣿⣿⣿⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⣿⡽⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⠿⣍⣿⣧⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⣽⣿⣷⣙⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣹⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡆⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣾⣿⣿⣿⣿⣿⣿⡶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⡴⠞⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⣿⣿⣿⠿⣿⣿⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣠⣤⠶⠚⠉⠉⠀⢀⡴⠂⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⢀⣿⣿⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠞⠋⠁⠀⠀⠀⠀⣠⣴⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⣾⣿⠋⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡀⠀⠀⢀⣷⣶⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣆⣼⣿⠁⢠⠃⠈⠓⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⡛⠛⠿⠿⠿⠿⠿⢷⣦⣤⣤⣤⣦⣄⣀⣀⠀⢀⣿⣿⠻⣿⣰⠻⠀⠸⣧⡀⠀⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠛⢿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠿⣦⣼⡏⢻⣿⣿⠇⠀⠁⠀⠻⣿⠙⣶⣄⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣐⠀⠀⠀⠈⠳⡘⣿⡟⣀⡠⠿⠶⠒⠟⠓⠀⠹⡄⢴⣬⣍⣑⠢⢤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢀⣀⠐⠲⠤⠁⢘⣠⣿⣷⣦⠀⠀⠀⠀⠀⠀⠙⢿⣿⣏⠉⠉⠂⠉⠉⠓⠒⠦⣄⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠈⣿⣿⣷⣯⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢦⣷⡀⠀⠀⠀⠀⠀⠀⠉⠲⣄⠀
⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⠀⢹⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢻⣷⣄⠀⠀⠀⠀⠀⠀⠈⠳
⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣸⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣽⡟⢶⣄⠀⠀⠀⠀⠀
⠯⠀⠀⠀⠒⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⠈⠳⠀⠀⠀⠀
⠀⠀⢀⣀⣀⡀⣼⣤⡟⣬⣿⣷⣤⣀⣄⣀⡀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡄⣉⡀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⣿⣿⣄⠀⣀⣀
"""

#image for above 80%
IMAGE_GOOD = """
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⣀⣄⣶⡶⣦⣀⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⢠⡦⡟⠻⠛⠙⠉⠈⠄⠄⠈⠻⠛⣾⣦⣤⣀⠄⠄
⠄⠄⠄⣰⡿⠟⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠋⠽⢿⣧⠄
⠄⢀⣴⠞⠂⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢼⠆⠄
⠄⣼⠇⠄⠄⠄⠄⠄⠄⠄⠄⣀⣠⣤⣶⣿⣶⣦⣤⣀⠄⣻⡃⠄
⠄⡿⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⢸⣧⠄
⠄⢿⡀⠄⠄⠄⠄⠄⠄⠄⢠⣾⣿⣿⣋⣩⣭⣝⣿⣿⠛⢰⡇⠄
⠄⢸⡇⠄⠄⢀⠄⠄⠄⠄⣾⣿⣿⣿⣟⣯⠉⢉⣿⠋⣟⢻⡇⠄
⠄⠄⢹⡀⢳⡗⠂⣠⠄⠄⣿⣿⣿⣿⣿⣭⣽⣿⣿⣿⣉⣸⠇⠄
⠄⠄⠈⣷⠄⢳⣷⣿⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄
⠄⠄⠄⠘⣧⠄⠈⠙⠄⠄⠄⠉⠙⠛⠛⣿⣿⣷⣤⣄⢿⡿⠃⠄
⠄⠄⠄⠄⠉⠳⣄⡀⠄⠄⠄⢢⣦⣾⣿⠿⠿⠛⠉⢉⣽⠇⠄⠄
⠄⠄⠄⠄⠄⠄⠘⠿⣄⢀⠄⣀⣝⢻⣿⡿⠒⣀⣀⣸⠁⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠈⠳⣤⠁⠙⠎⢻⣄⠄⠄⣸⠋⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠙⠶⢦⣄⣀⣣⠴⠃⠄⠄⠄⠄⠄
"""

#image for above 10%
IMAGE_NOTGOOD = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿
⣿⣿⡏⠁⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣦⣤⡄⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿
⣿⣿⣷⣄⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡧⠇⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣾⣮⣭⣿⡻⣽⣒⠀⣤⣜⣭⠐⢐⣒⠢⢰⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿⣿⣿⣿⣿⡟⣾⣿⠂⢈⢿⣷⣞⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣷⣶⣾⡿⠿⣿⠗⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠋⠉⠑⠀⠀⢘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠟⢹⣿⣿⡇⢀⣶⣶⠴⠶⠀⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠀⠀⢸⣿⣿⠀⠀⠣⠀⠀⠀⠀⠀⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠹⣿⣧⣀⠀⠀⠀⠀⡀⣴⠁⢘⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿
⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⠗⠂⠄⠀⣴⡟⠀⠀⡃⠀⠉⠉⠟⡿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠾⠛⠂⢹⠀⠀⠀⢡⠀⠀⠀⠀⠀⠙⠛⠿⢿⣿⣿
"""

#image for above 0%
IMAGE_BAD = """
⠀⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇
⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀
⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀
⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀
⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

#image for 0%
IMAGE_TERRIBLE = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡄⢠⡄⣠⠤⢤⡀⣤⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡏⠀⣿⠀⢨⡇⣿⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠈⠉⠉⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢠⠤⣄⢠⡄⠀⣤⢀⣠⢤⡀⢠⡄⠀⡄⢠⡀⠀⢠⣤⣤⡀ 
⠀⠀⠀⠀⣙⠲⢦⢸⡗⠒⣿⢸⡁⠀⣿⢸⡇⠀⡇⢸⡇⠀⢸⡇⠀⡷ 
⠀⠀⠀⠀⠈⠛⠋⠈⠃⠀⠋⠀⠙⠛⠁⠀⠙⠛⠁⠘⠛⠛⠘⠛⠋⠁ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⢀⡀⢀⠀⡀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⣯⠀⢸⠀⡇⠀⠀⣿⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠈⠓⠘⠀⠛⠒⠂⠛⠒⠂ 
⠀⣀⠀⢀⡀⢀⣀⡀⠀⡀⠀⣀⢀⣀⣀⡀⢀⣀⣀⠀⣀⣀⡀⣀⠀⠀⢀⣀⣀ 
⠀⠘⢷⠏⢰⡏⠀⢹⠄⡇⠀⣿⢸⣧⢤⡇⠘⠦⣬⡀⡧⠤⠄⣿⠀⠀⢸⠤⠄ 
⠀⠀⠘⠀⠀⠛⠒⠋⠀⠛⠒⠋⠘⠃⠀⠓⠘⠲⠚⠁⠓⠒⠂⠛⠒⠒⠘⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⢀⠀⢀⣀⠀⢀⠀⢀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⢆⣸⢠⡏⠉⢹⡈⣇⡼⣇⣼ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠈⠿⠀⠳⠶⠞⠀⠹⠇⠸⠇ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⢀⣀⣀⣀⡀⠄⢀⣠⡔⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣰⢿⣿⣿⣿⣿⣿⣿⣷⡆⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣻⣟⣿⣿⡿⣟⣛⣿⡃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣾⣿⣷⣿⣷⣿⣿⣿⣷⣽⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⡟⣟⣿⣿⠺⣟⣻⣿⣿⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡝⠻⠵⠿⠿⢿⣿⣿⢳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣧⠈⣛⣛⣿⣿⡿⣡⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠄⠙⠛⠛⢁⣴⣿⣿⣷⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⡿⠟⠉⠄⠄⢠⠄⣀⣠⣾⣿⣿⡿⠟⠁⠄⠈⠛⢿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⡟⠉⠄⠄⢀⠠⠐⠒⠐⠾⠿⢟⠋⠁⠄⢀⣀⠠⠐⠄⠂⠈⠻⢿⣿⣿ 
⣿⣿⣿⠋⠁⠄⢀⡈⠄⠄⠄⠄⠄⠄⠄⠄⠁⠒⠉⠄⢠⣶⠄⠄⠄⠄⠄⠈⠫⢿ 
⣿⣿⡟⠄⢔⠆⡀⠄⠈⢀⠄⠄⠄⠄⠄⠄⢄⡀⠄⠄⠈⡐⢠⠒⠄⠄⠄⠄⢀⣂ 
⣿⣿⠁⡀⠄⠄⢇⠄⠄⢈⠆⠄⠄⢀⠔⠉⠁⠉⠉⠣⣖⠉⡂⡔⠂⠄⢀⠔⠁⠄ 
⣿⡿⠄⠄⠄⠄⢰⠹⣗⣺⠤⠄⠰⡎⠄⠄⠄⠄⠄⠄⠘⢯⡶⢟⡠⠰⠄⠄⠄⠄
"""