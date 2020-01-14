def start():
    bit1=input("enter first 8-bit binary string\n\t")
    bit2=input("enter second 8-bit binary string\n\t")
    bit1list=[]
    bit2list=[]
    outbit=['0','0','0','0','0','0','0','0']
    if len(bit1) and len(bit2)==8:
        if bit1.isdigit() and bit2.isdigit():
            output=""
            for i in bit1:
                bit1list.append(i)
            for i in bit2:
                bit2list.append(i)
            placevalue=0
            for item in bit1list:
                if item!=bit2list[placevalue]:
                    outbit[placevalue]='1'
                else:
                    pass
                placevalue+=1
            for item in outbit:
                output+=str(item)
                print(output)
        else:
            print("INVALID STRING SET set\n")
            start()
    else:
        print("INVALID STRING SET\n")
        start()
start()
