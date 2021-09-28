#variable
import record
import pandas as pd

import_file_path="variables.xlsx"
voice_input=record.recorder().lower()
print(voice_input)
df=pd.read_excel(import_file_path)
print(df)
variable_commands_list=df['Var_Declaration'].tolist()
print(type(variable_commands_list[0]))
for element in variable_commands_list:
    ele=element.lower()
    print("Variable command detected")
    if "variable" in ele:
        if "initialize a variable" in voice_input:
            print(voice_input[19:])
            input_list=voice_input.split()
            print(lst)
            var_ind=input_list.index("variable")
            type_ind=input_list.index("type")
            val_ind=
            var_name=input_list[type_ind+1]+" "+input_lst[var_ind+1]
            
        print("Variable command detected")
    else:
        print("Nothing related to variable")
    
print("Code Block: ")

print(command)

