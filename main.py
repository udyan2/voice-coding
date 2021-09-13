#variable
import record
import pandas as pd

import_file_path="variables.xlsx"
voice_input=record.recorder().lower()
print(voice_input)
df=pd.read_excel(import_file_path)
print(df)
variables_list=df['Var_Declaration'].tolist()
print(type(variables_list[0]))
for element in variables_list:
    ele=element.lower()
    print("Variable command detected")
    if "variable" in ele:
        
        if "declare a variable" in voice_input:
            print(voice_input[19:])
            lst=voice_input.split()
            print(lst)
            var_ind=lst.index("variable")
            type_ind=lst.index("type")
            command=lst[type_ind+1]+" "+lst[var_ind+1]
        print("Variable command detected")
    else:
        print("Nothing related to variable")
    
print("Code Block: ")
print(command)
