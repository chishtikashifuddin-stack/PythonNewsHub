import os
a = os.open("news.txt",0)
b = os.read(a, 89990)
lines = b.splitlines()
title = []
desc= []

def fun():
    print("         |---------------------------------------------------|")
    print("         |        ENTER 1 FOR INTERNATION NEWS               |")
    print("         |        ENTER 2 FOR INDIAN NEWS                    |")
    print("         |---------------------------------------------------|\n")
    a = input("ENTER YOU NUMBER :")
    if a == "1":
        print("---------------THIS IS YOURE INTERNATION NEWS --------------\n")
        t()
    if a == "2":
        print("---------------THIS IS YOURE INDIAN NEWS TITLE--------------\n")
        t1()

    else:
        print("PLEASE ENTER CORRECT OPTION")
        print("----------------------------\n")
        fun()


def t():
    global line
    for line in lines:
        e = line.decode('utf-8') 
        parts = e.split(",")
        for d2 in parts:
            if "title" in d2:
                title.append(d2)            
        title1 = title.pop(14)
        for title1 in title:
            if "title" in title1:
                title3,title4 = title1.split(":")
                print(title4)
            
                print("-------------------------------------------------------------------\n")
    print("  ----------------------------------------------  ")
    print(f" | THERE ARE {len(title)} INTERNATION TOP NEWS AVAILABLE  | ")
    print("  ----------------------------------------------  \n")
    opt()
  
def opt():
    r = input("YOU WANT TO READ NEWS DESCRIPTION (Y/N):")
    if r == "n" or r == "N":
        print("THANK FOR READING NEWS")
        print("----------------------\n")
        fun()
        
    if r == "y" or r == "Y":
        des()
    else:
        print("PLEASE ENTER ONLY Y/N")
        print("---------------------\n")
        opt()
 
 
def des():
    global line
    for line in lines:
        e = line.decode("utf-8") 
        parts = e.split(",")
        for d2 in parts:
            if "description" in d2:
                desc.append(d2)
    f = input("ENTER THE NUMBER WHICH NEWS YOU WANT READ IN DETAIL : ")
    if f == "1":
        print(desc[0])
        print("-----------------------------------------------------------------\n")
        b = input("YOU WANT READ MORE NEWS OR LEAVE (Y/N) : ")
        if b == "y" or b == "Y":
            des()
        if b == "n" or b == "N":
            print("THANK FOR READING NEWS")
            print("-----------------------\n")
            fun()
        else:
            print("PLEASE ENTER ONLY Y or N")
            print("-------------------------\n")
            fun()
    if f == "2":
        print(desc[1])
        print("-----------------------------------------------------------------\n")
        b = input("YOU WANT READ MORE NEWS OR LEAVE (Y/N) : ")
        if b == "y" or b == "Y":
            des()
        if b == "n" or b == "N":
            print("THANK FOR READING NEWS")
            print("-----------------------\n")
            fun()
            
        else:
            print("PLEASE ENTER ONLY Y or N")
            print("-------------------------\n")
            fun()
            
    if f == "3":
        print(desc[2])
        print("-----------------------------------------------------------------\n")
        b = input("YOU WANT READ MORE NEWS OR LEAVE (Y/N) : ")
        if b == "y" or b == "Y":
            des()
        if b == "n" or b == "N":
            print("THANK FOR READING NEWS")
            print("-----------------------\n")
            fun()
        else:
            print("PLEASE ENTER ONLY Y or N")
            print("-------------------------\n")
            fun()
            
    if f == "4":
        print(desc[3])
        print("-----------------------------------------------------------------\n")
        b = input("YOU WANT READ MORE NEWS OR LEAVE (Y/N) : ")
        if b == "y" or b == "Y":
            des()
        if b == "n" or b == "N":
            print("THANK FOR READING NEWS")
            print("-----------------------\n")
            fun()

        else:
            print("PLEASE ENTER ONLY Y or N")
            print("-------------------------\n")
            fun()

    if f == "5":
        print(desc[4])
        print("-----------------------------------------------------------------\n")
        b = input("YOU WANT READ MORE NEWS OR LEAVE (Y/N) : ")
        if b == "y" or b == "Y":
            des()
        if b == "n" or b == "N":
            print("THANK FOR READING NEWS")
            print("-----------------------\n")
            fun()
        else:
            print("PLEASE ENTER ONLY Y or N")
            print("-------------------------\n")
            fun()

    if f == "6":
        print(desc[5])
        print("-----------------------------------------------------------------\n")
        b = input("YOU WANT READ MORE NEWS OR LEAVE (Y/N) : ")
        if b == "y" or b == "Y":
            des()
        if b == "n" or b == "N":
            print("THANK FOR READING NEWS")
            print("-----------------------\n")
            fun()
        else:
            print("PLEASE ENTER ONLY Y or N")
            print("-------------------------\n")
            fun()
    
    if f == "7":
        print(desc[6])
        print("-----------------------------------------------------------------\n")
        b = input("YOU WANT READ MORE NEWS OR LEAVE (Y/N) : ")
        if b == "y" or b == "Y":
            des()
        if b == "n" or b == "N":
            print("THANK FOR READING NEWS")
            print("-----------------------\n")
            fun()
        else:
            print("PLEASE ENTER ONLY Y or N")
            print("-------------------------\n")
            fun()

    if f == "8":
        print(desc[7])
        print("-----------------------------------------------------------------\n")
        b = input("YOU WANT READ MORE NEWS OR LEAVE (Y/N) : ")
        if b == "y" or b == "Y":
            des()
        if b == "n" or b == "N":
            print("THANK FOR READING NEWS")
            print("-----------------------\n")
            fun()
        else:
            print("PLEASE ENTER ONLY Y or N")
            print("-------------------------\n")
            fun()
            
    if f == "9":
        print(desc[8])
        print("-----------------------------------------------------------------\n")
        b = input("YOU WANT READ MORE NEWS OR LEAVE (Y/N) : ")
        if b == "y" or b == "Y":
            des()
        if b == "n" or b == "N":
            print("THANK FOR READING NEWS")
            print("-----------------------\n")
            fun()
        else:
            print("PLEASE ENTER ONLY Y or N")
            print("-------------------------\n")
            fun()
            
    if f == "10":
        print(desc[9])
        print("-----------------------------------------------------------------\n")
        b = input("YOU WANT READ MORE NEWS OR LEAVE (Y/N) : ")
        if b == "y" or b == "Y":
            des()
        if b == "n" or b == "N":
            print("THANK FOR READING NEWS")
            print("-----------------------\n")
            fun()
        else:
            print("PLEASE ENTER ONLY Y or N")
            print("-------------------------\n")
            fun()
    
    if f == "11":
        print(desc[10])
        print("-----------------------------------------------------------------\n")
        b = input("YOU WANT READ MORE NEWS OR LEAVE (Y/N) : ")
        if b == "y" or b == "Y":
            des()
        if b == "n" or b == "N":
            print("THANK FOR READING NEWS")
            print("-----------------------\n")
            fun()
        else:
            print("PLEASE ENTER ONLY Y or N")
            print("-------------------------\n")
            fun()
            
    if f == "12":
        print(desc[11])
        print("-----------------------------------------------------------------\n")
        b = input("YOU WANT READ MORE NEWS OR LEAVE (Y/N) : ")
        if b == "y" or b == "Y":
            des()
        if b == "n" or b == "N":
            print("THANK FOR READING NEWS")
            print("-----------------------\n")
            fun()
        else:
            print("PLEASE ENTER ONLY Y or N")
            print("-------------------------\n")
            fun()
   
    if f == "13":
        print(desc[12])
        print("-----------------------------------------------------------------\n")
        b = input("YOU WANT READ MORE NEWS OR LEAVE (Y/N) : ")
        if b == "y" or b == "Y":
            des()
        if b == "n" or b == "N":
            print("THANK FOR READING NEWS")
            print("-----------------------\n")
            fun()
        else:
            print("PLEASE ENTER ONLY Y or N")
            print("-------------------------\n")
            fun()
            
    if f == "14":
        print(desc[13])
        print("-----------------------------------------------------------------\n")
        b = input("YOU WANT READ MORE NEWS OR LEAVE (Y/N) : ")
        if b == "y" or b == "Y":
            des()
        if b == "n" or b == "N":
            print("THANK FOR READING NEWS")
            print("-----------------------\n")
            fun()
        else:
            print("PLEASE ENTER ONLY Y or N")
            print("-------------------------\n")
            fun()
     
    else:
        print("PLEASE ENTER CORRECT NEWS !")
        print("---------------------------\n")
        des()


def t1():
    for line in lines:
        s = str(line)
        e = s.dncode("utf-8")
        c = e.split(",")
        for d2 in c:
            if "title" in d2:
                title.append(d2)
    print(title[14])
    print("---------------------------------------\n")
    print("IF YOU WANT TO READ THE DESCRIPTION OF THE TITLE ")
    go()

def go():
    f = input("ENTER (Y/N)")
    if f == "y" or f == "Y":
        print("---------------THIS IS INDIAN NEWS DESCRIPTION--------------\n")
        des1()
    if f == "N" or f == "n":
        print("THANK YOU FOR READING NEWS")
        print("--------------------------\n")
        fun()
        
    else:
        print("ENTER ONLY (Y/N)")
        print("-----------------\n")
        go()


def go2():    
    g = input("ENTER (Y) FOR EXIST :")
    if g == "Y" or g == "y":
        print("THANK FOR READING NEWS")
        print("--------------------------\n")
        fun()
    else:
        print("PLEASE ENTER CORRECT OPTION")
        print("---------------------------\n")
        go2()


def des1():
    for line in lines:
        s = str(line)
        e = s.encode("utf-8")
        c = e.split(b",")
        for d2 in c:
            if b"description" in d2:
                desc.append(d2)
        print(desc[14])
        print("------------------------------------------------------------------------------------------------------------------------\n")
        go2()
fun()