# 1202_program_alarm.py

def continue_program(code):
    if (code == 99):
        print("Code <99> encountered. Ending program")
        return False
    elif (code != 1 and code != 2):
        print("Error!")
        print("Unrecognized code: <" + str(code) + "> encountered. Ending program.")
        return False
    return True

def run_intcode(i_code):
    position = 0

    while continue_program(i_code[position]):
        opt_code = i_code[position]

        if (opt_code == 1):
            print("Opt code is: " + str(opt_code))
        elif (opt_code == 2):
            print("Opt code is: " + str(opt_code))
        
        position += 4
        
    print(i_code)

Intcode = [1,9,10,3,2,3,11,0,99,30,40,50]

run_intcode(Intcode)