cmds = ["add","sub","gz","ez","gez","g","e","l","ge","le","copy","set","jump","stop"]
codes = [0,268435456,536870912,805306368,1073741824,1342177280,1610612736,1879048192,2147483648,2415919104,2684354560,2952790016,3221225472,3489660928]
regs = ["reg0","reg1","reg2","reg3","reg4","reg5","reg6","reg7"]
from_reg_codes = [0,33554432,67108864,100663296,134217728,167772160,201326592,234881024]
to_reg_codes = [0,4194304,8388608,12582912,16777216,20971520,25165824,29360128]

def read_file(name):
    file = open(name,"r",encoding="utf-8")
    file = file.readlines()
    liste = []
    for i in file:
        if i[-1::]=="\n":
            i = i[0:-1]
        liste.append(i)
    return liste

def read_code(code):
    liste = []
    for i in code:
        value = 0
        string = i.split(" ")
        if len(string)==0:
            continue
        value = value | codes[cmds.index(string[0])]
        if string[0]=="copy":
            value = value | from_reg_codes[regs.index(string[1])]
            value = value | to_reg_codes[regs.index(string[2])]
        elif string[0]=="set":
            value = value | to_reg_codes[regs.index(string[1])]
            value = value | int(string[2])
        elif string[0]=="gz" or string[0]=="ez" or string[0]=="gez" or string[0]=="g" or string[0]=="g" or string[0]=="e" or string[0]=="l" or string[0]=="ge" or string[0]=="le" or string[0]=="jump":
            value = value | int(string[1])
        value = hex(value)[2::].upper()
        liste.append(value)
    return liste

def compile_code(name,to):
    code = read_file(name)
    write = read_code(code)
    file = open(to,"w",encoding="utf-8")
    for index,i in enumerate(write):
        file.write(i)
        if index!=len(write)-1:
            file.write(" ")
    file.close()

compile_code("code.txt","code")
