#Switching to different modules
import pyttsx3
import variables
import classes
import functions
import template
import strings

eng = pyttsx3.init()

def shifter(voice_in):
    variables_list=["define a variable","write a variable", "create a variable", "initialize a variable", "take input in a variable"]
    functions_list=["declare a function", "create a function", "write a function"]
    classes_list=["create a class","make a class","define a class"]
    templates_list=["predefined template","predefined codeblock","write a whole code"]
    strings_list=["string processing","string manipulation","string slicing"]
    exit_list=["exit program","exit","close program","close voice coding","stop voice coding"]
    if voice_in.lower() in variables_list:
        eng.say("Entering variables module")
        eng.runAndWait()
        check=variables.enter()
        return check
    if voice_in.lower() in functions_list:
        eng.say("Entering variables module")
        eng.runAndWait()
        check=functions.enter()
        return check
    if voice_in.lower() in classes_list:
        eng.say("Entering variables module")
        eng.runAndWait()
        check=classes.enter()
        return check
    if voice_in.lower() in templates_list:
        eng.say("Entering variables module")
        eng.runAndWait()
        check=template.enter()
        return check
    if voice_in.lower() in strings_list:
        eng.say("Entering variables module")
        eng.runAndWait()
        check=strings.enter()
        return check
    elif voice_in.lower() in exit_list:
        print("Bye, have a great day!")
        eng.say("Bye, have a great day!")
        eng.runAndWait()
    else:
        print("This functionality will be available soon!")
        eng.say("This functionality will be available soon!")
        eng.runAndWait()
        return 1