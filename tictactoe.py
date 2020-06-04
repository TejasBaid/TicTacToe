import readchar
pd = {'o_1' : " ",'o_2' : " ",'o_3' : " ",'o_4' : " ",'o_5' : " ",'o_6' : " ",'o_7' : " ",'o_8' : " ",'o_9' : " "}
current_piece = ""

def checker(n1,n2,n3,n4,n5,n6,n7,n8,n9):
    if n7 == n8 and n7 == n9 and n7 != " " and n8 != " " and n9 != " ":
        return True
    elif n4 == n5 and n4 == n6 and n4 != " " and n5 != " " and n6 != " ":
        return True
    elif n1 == n2 and n1 == n3 and n1 != " " and n2 != " " and n3 != " ":
        return True    
    elif n7 == n5 and n7 == n3 and n7 != " " and n5 != " " and n3 != " ":
        return True       
    elif n9 == n5 and n9 == n1 and n1 != " " and n5 != " " and n1 != " ":
        return True    
        #-----
    elif n7 == n4 and n7 == n1 and n7 != " " and n4 != " " and n1 != " ":
        return True
    elif n8 == n5 and n8 == n2 and n8 != " " and n5 != " " and n2 != " ":
        return True    
    elif n9 == n6 and n9 == n3 and n9 != " " and n6 != " " and n3 != " ":
        return True       

    else: 
        return False    
def turn(num):

    if num%2 == 0:
        return "o"
    else:
        return "x"    
def numerCheck(m_char):
    if m_char.isnumeric() == True:
        return True
    else:
        return False    

ticker = 0
msg = "Enter the key"
print("              ")
range_m = 10
mya = [1,2,3,4,5,6,7,8,9]
my_arr = ['1','2','3','4','5','6','7','8','9']
while True:
    if len(my_arr) != 0:
        print(msg)
        print("            ")
        print("      ")
        key = readchar.readkey()
        keya = str(key)
        if numerCheck(key) == True:
            if keya in my_arr:
                my_arr.remove(keya)
                myvar = "o_" + key
                ticker += 1
                myvar = str(myvar)
                pd[myvar] = turn(ticker)
                print(" {} | {} | {} ".format(pd['o_7'],pd['o_8'],pd['o_9']))
                print("-----------")
                print(" {} | {} | {} ".format(pd['o_4'],pd['o_5'],pd['o_6']))
                print("-----------")
                print(" {} | {} | {} ".format(pd['o_1'],pd['o_2'],pd['o_3']))
                print("              ")
                print("              ")

                if checker(pd['o_1'],pd['o_2'],pd['o_3'],pd['o_4'],pd['o_5'],pd['o_6'],pd['o_7'],pd['o_8'],pd['o_9']) == True:
                    print("{} wins".format(turn(ticker)))
                    print("              ")
                    print("              ")
                    break
            else:
                range_m += 1
                mya.append("x")
                print("The place is already taken")
                print("              ")
                print("              ")
                print("              ")
        else:
            print("Invalid input type")        
    else:
        print("      ")
        print("      ")
        print("ITS A TIE")
        print("      ")
        
        break   

    




