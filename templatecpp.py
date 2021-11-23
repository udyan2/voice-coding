#Templates
import record
import pandas as pd
import pyttsx3
eng = pyttsx3.init()
eng.say("This is the Templates module")
eng.runAndWait()

def enter(msg):
    def add():
        add_template="#include<iostream>int addition(int a, int b)\n{ \n\treturn (a+b);\n}"
        return add_template

    def subtract():
        subtract_template="int subtraction(int a, int b)\n{ \n\treturn (a-b);\n}"
        return subtract_template

    def multiply():
        multiply_template="int multiply(int a, int b)\n{ \n\treturn (a*b); \n}"
        return multiply_template

    def divide():
        divide_template="float division(int a, int b)\n{ \n\treturn (a/b); \n}"
        return divide_template

    def power():
        power_template="def division(int num, int pow)\n{ \n\treturn (num**pow); \n"
        return power_template

    def factorial(numval):
        factorial_template= 'int factorial(int n)\n{ \n\tif (n==1 or n==0)\n{\n\t\t return 1;\n}\n else\n{\n\t\t n * factorial(n - 1);\n}\n\t \nnum='+numval+'; \ncour<<"Factorial of"<<num<<"is"<<factorial(num));\n}'
        return factorial_template

    def armstrong():
        armstrong_template='num = int(input("Enter a number: "))\nsum = 0\ntemp = num\nwhile temp > 0:\n\tdigit = temp % 10\n\tsum += digit ** 3\n\ttemp //= 10\nif num == sum:\n\tprint(num,"is an Armstrong number")\nelse: \n\tprint(num,"is not an Armstrong number")'

        return armstrong_template

    def multiples():
        multiples_template='int multiples(int m, int count)\n{ \n\tfor(int i=0;i<count;i++)\n{ \n\t\tcout<<i*m;\n}'
        return multiples_template

    # import_file_path="templates.xlsx"
    voice_input=msg
    print(voice_input)
    # df=pd.read_excel(import_file_path)
    # variable_commands_list=df['template_Declaration'].tolist()
    # print(type(variable_commands_list[0]))
    if "template" in voice_input:
        if "create a template" in voice_input:
            print(voice_input[19:])
            input_list=voice_input.split()
            if "add" in voice_input:
                template=add()
            elif "subtract" in voice_input:
                template=subtract()
            elif "multiply" in voice_input:
                template=multiply()
            elif "divide" in voice_input:
                template=divide()
            elif "power" in voice_input:
                template=power()
            elif "armstrong" in voice_input:
                template=armstrong()
            elif "multiples" in voice_input:
                template=multiples()
            elif "factorial" in voice_input:
                input_list=voice_input.split()
                numval=input_list[input_list.index("number")+1]
                print(numval)
                template=factorial(numval)
        print("template command detected")
    else:
        print("Nothing related to object")
    print("\nCode Block:\n ")
    print(template)
    return 1