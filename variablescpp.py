# variable
# import record
# import pandas as pd
import pyttsx3

def enter(msg):
    eng = pyttsx3.init()
    eng.say("This is the C plus plus Variables module")
    eng.runAndWait()
    import_file_path = "variables.xlsx"
    voice_input = msg
    print(voice_input)
    # df=pd.read_excel(import_file_path)
    # print(df)
    # variable_commands_list=df['Var_Declaration'].tolist()
    # print(type(variable_commands_list[0]))
    # for element in variable_commands_list:
    # ele=element.lower()
    if "variable" in voice_input:
        if "initialise a variable" or "declare a variable" or "write a variable" in voice_input:
            # print(voice_input[19:])
            input_list = voice_input.split()
            var_ind = input_list.index("variable")
            type_ind = input_list.index("type")
            if "value" in voice_input:
                value_ind = input_list.index("value")
                value = input_list[value_ind + 1]
                if input_list[type_ind + 1] == "string":
                    command = input_list[type_ind + 1] + " " + input_list[var_ind + 1] + '="' + value + '";'
                elif input_list[type_ind + 1] == "integer":
                    command = "int " + input_list[var_ind + 1] + "=" + value + ";"
                elif input_list[type_ind + 1] == "boolean":
                    command = "bool " + input_list[var_ind + 1] + "=" + value + ";"
            else:
                if input_list[type_ind + 1] == "string":
                    command = input_list[type_ind + 1] + input_list[var_ind + 1] + ";"
                elif input_list[type_ind + 1] == "integer":
                    command = "int " + input_list[var_ind + 1] + ";"
                elif input_list[type_ind + 1] == "boolean":
                    command = "bool " + input_list[var_ind + 1] + ";"

            eng.say("Your code block is ready!")
            eng.runAndWait()
            print("\nCode Block: ")
            print(command)
            return 1
    else:
        print("Nothing related to variables")
        eng.say("Nothing related to variables")
        eng.runAndWait()
        return 1