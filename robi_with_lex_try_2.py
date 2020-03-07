import os
import string




def Symb(Symbol, Code):
    #symbol and code will be strings
    #symbol is the key that you search the table with
    #if the table doesn't have the symbol, the symbol will be added next in the table with the respective code and return the position of the sybmol
    #if the symbol exists in the table, the program will just return its position
    if Symbol not in arr:
        arr.append(Symbol)
        codes.append(Code)
        return arr.index(Symbol)
    else:
        return arr.index(Symbol)

arr = []
codes = []
clear = lambda: os.system('cls')

WS = [' ','\t']
alphabet = list(string.ascii_letters)
digits = list('1234567890')
operators = ['=','+','-',';','>','<','<>',':','*']

inputz="ana:=Milsugi+merge+4*labe;"
low = list(inputz)
list1 = iter(low)
Ch = list1

def Recognise_Identifier():
    global Ch
    buffer = ''
    init = Ch
    while Ch in alphabet or Ch in digits:
        buffer += Ch
        #print("identif. is " + Ch)
        Ch = next(list1,'end')
        if Ch == 'end':
            break
    if buffer!='':
        #print(buffer)
        return Symb(buffer,1)


def Recognise_Number():
    global Ch
    buffer = ''
    init = Ch
    while Ch in digits:
        buffer += Ch
        #print("number is " + Ch)
        Ch = next(list1,'end')
        if Ch == 'end':
            break
    if buffer!='':
        return Symb(buffer,2)

def Recognise_Operators():
    global Ch
    buffer = ''
    while Ch in operators:
        buffer += Ch
        Ch = next(list1,'end')
        if Ch == 'end':
            break
    if buffer!='':
        return Symb(buffer,3)
    

def Lex():    
    global Ch
    Ch = next(list1,'end')
    while(1):
        if Ch == 'end':
            break
        while Ch in WS:
            Ch = next(list1,'end')
            if Ch == 'end':
                break
        if Ch in alphabet:
            Recognise_Identifier()
        if Ch in operators:
            Recognise_Operators()
        if Ch in digits:
            Recognise_Number()

Lex()
print(arr)


#problema e ca dupa ce nu mai gaseste nimic in lista, Ch e deja la urmatorul element din cauza while-urilor (?)