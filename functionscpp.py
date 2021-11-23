#Functions
import record
import pandas as pd
import pyttsx3
eng = pyttsx3.init()
eng.say("This is the Funtions module")
eng.runAndWait()
import_file_path="functions.xlsx"
voice_input=record.recorder().lower()
print(voice_input)
df=pd.read_excel(import_file_path)
print(df)
variable_commands_list=df['function_Declaration'].tolist()
print(type(variable_commands_list[0]))
for element in variable_commands_list:
    ele=element.lower()
    print("Function command detected")
    if "function" in ele:
        if "define a function" in voice_input:
            print(voice_input[19:])
            input_list=voice_input.split()
            function_ind=input_list.index("function")
            type_ind=input_list.index("type")
            function_name=input_list[type_ind+1]+" "+input_list[function_ind+1]
        print("function command detected")
    else:
        print("Nothing related to function")
print("Code Block: ")
print(function_name)

