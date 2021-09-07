import sys 

def hex_calc(n): 
    # dictionary of letters if remainder is more than 9 
    hex_vals = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G'}

    # final string showing the hex value
    fin_str = ''

    # temp var to hold either the remainder or the quotient 
    temp_val = 0 

    #Constant val of 16 used for calculations
    DIV = 16 

    #var used to hold the remainder from division
    rem = 1 

    #var to hold the quotient 
    quot = 1 

    while n != 0: 

        #calculating remainder
        rem = n % DIV

        #calculating quotient
        quot = n // DIV

        #moving n to quot for the next round of calculations
        n = quot

        # if remainder and quot == 0, assign temp_val to quot and perform the final division
        if rem == 0 and quot == 0: 
            temp_val = quot
        else: 
            temp_val = rem 
        if temp_val <= 9: 
            temp_val = str(temp_val)
        else: 
            temp_val = hex_vals[temp_val]
    
        fin_str = fin_str + temp_val

    return ''.join(reversed(list(fin_str)))


#assign the argument from the command line using n: 
# sys.argv takes a list of arguments and passes it as a list to a py function
n = sys.argv[1] 
print(hex_calc(int(n)))