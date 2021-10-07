#Classes
import record
import pandas as pd

import_file_path="classes.xlsx"
voice_input=record.recorder().lower()
print(voice_input)
df=pd.read_excel(import_file_path)
print(df)
variable_commands_list=df['class_Declaration'].tolist()
print(type(variable_commands_list[0]))
for element in variable_commands_list:
    ele=element.lower()
    print("class command detected")
    if "class" in ele:
        if "create a class" in voice_input:
            print(voice_input[19:])
            input_list=voice_input.split()
            print(lst)
            var_ind=input_list.index("class")
            type_ind=input_list.index("type")
            val_ind=
            var_name=input_list[type_ind+1]+" "+input_lst[var_ind+1]
            
        print("Class command detected")
    else:
        print("Nothing related to Class")
    
print("Code Block: ")

print(command)

