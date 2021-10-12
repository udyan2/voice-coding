#variable
import record
import pandas as pd
import pyttsx3
eng = pyttsx3.init()
eng.say("This is the Variables module")
eng.runAndWait()
import_file_path="variables.xlsx"
voice_input=record.recorder().lower()
print(voice_input)
df=pd.read_excel(import_file_path)
print(df)
variable_commands_list=df['Var_Declaration'].tolist()
#print(type(variable_commands_list[0]))
for element in variable_commands_list:
    ele=element.lower()
    if "variable" in ele:
        if "initialise a variable" in voice_input:
            print(voice_input[19:])
            input_list=voice_input.split()
            var_ind=input_list.index("variable")
            type_ind=input_list.index("type")
            command=input_list[type_ind+1]+" "+input_list[var_ind+1]
            print("\nCode Block: ")
            print(command)
            break
    else:
        print("Nothing related to variable")
        eng.say("Nothing related to variable")
        eng.runAndWait()
            


    
