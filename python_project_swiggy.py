import time,threading
print("\n"*5,"-"*20)
restaurent_dict = {"THE WAVES":0, "VINTAGE CAFE":0, "PET POOJA":0,"PUNJABI DHABA":0,\
    "KHANA KHAJANA":0}
menu_restaurent = {
    "THE WAVES" : {"SALAD":835, "DAHI ":940, "CHICKEN TIKKA": 850,\
    "PANEER MASALA ":885, "LACCHA PRATHA ":985},\
    "VINTAGE CAFE" : {"SANDWICH" : 350,"PANEER TIKKA" : 370, "LACCHA PRATHA" : 450,\
    "GRILLED PANEER" : 390, "BUTTER CHICKEN" : 540},\
    "PET POOJA" : {"ALOO PRATHA ":695, "PAYAJ PARATHA ":650, "LACCHA PRATHA":1150, "STUFF PRATHA":1095,\
    "ANDAA PRATHA":750},\
    "PUNJABI DHABA" : {"MAKKI ROTTI ":1190, "CHICKEN BUTTER MASALA":560, "PANEER TIKKA":350, "LASSI":850,\
    "CHICKEN LOLLIPOP":350},\
    "KHANA KHAJANA" : {"DAL": 50, "CHAWAL":55}
}

queueList = []  



class Service:

    def joinService(self):
        print("*"*25,"JOIN SWIGGY AND SPREAD HAPPINESS","*"*25)
        print("\n"*3)
        print("-"*80)
        print("(1) NEW USER")
        print("(2) EXISTING USER")
        print("\n"*5)
        print("(M) BACK TO MAIN MENU")
        print("="*80)
        join_input = input("SELECT YOUR CHOICE----  ")
        if join_input.upper() == 'M':
            Swiggy.mainMenu(self)
        elif join_input == '1':
            Service.SignUp(self)
        elif join_input == '2':
            Service.SignIn(self)
        else:
            print("WRONG INPUT PLEASE SELECT CORRECT CHOICE ")
            Service.joinService(self)


    def SignUp(self):
        print(" "*35,"COMPLETE YOUR REGISTRATION PROCESS")
        print("\n"*2)
        print("(J) BACK TO JOIN SERVICE ")
        u_name = input("PLEASE SELECT YOUR RESTURANT NAME OR PRESS 'J' TO GO BACK-----  ")
        if u_name.upper() == 'J':
            Service.joinService(self)
        elif u_name.upper() != 'J':
            Service.addMenu(self,u_name)
        else:
            print("WRONG INPUT PLEASE SELECT CORRECT CHOICE")
            Service.SignUp(self)



    def addMenu(self,u_name):
        restaurent_dict[u_name] = 0
        meal_name = input("PLEASE ENTER NAME OF MEAL----  ")
        meal_price = input("PLEASE ENTER THE PRICE FOR YOUR DISH----  ")
        price_check1 = []
        for _i_ in meal_price:
            if ord(_i_)>=48 and ord(_i_)<=57:
                price_check1.append("True")
            else:
                price_check1.append("False")
        if "False" in price_check1:
            print("WRONG PRICE INPUT PLEASE GIVE CORRECT INPUT")
            Service.addMenu(self,u_name)
        else:
            if u_name in menu_restaurent:

                menu_restaurent[u_name][meal_name] = meal_price
            else:
                menu_restaurent[u_name]={meal_name:meal_price}
        print("\n"*2)
        print("(A) ADD MORE ITEMS")
        print("(D) DONE ADDING ITEMS ")
        add_items = input("PLEASE SELECT YOUR OPTION----  ")
        if add_items.upper() == 'A':
            Service.addMenu(self,u_name)
        elif add_items.upper() == 'D':
            Swiggy.mainMenu(self)
        else:
            print("WRONG INPUT PLEASE GIVE CORRECT INPUT")
            Service.addMenu(self,u_name)


    def SignIn(self):
        print("*"*70)
        res_name = input("ENTER YOUR RESTURANT NAME----  ")
        if res_name in menu_restaurent:
            print(" "*30,"MENU OF HOTEL ",res_name)
            print("-"*70)
            print("ITEMS"," "*40,"PRICE")
            print("-"*70)
            i = 0
            for k,v in menu_restaurent[res_name].items():
                i += 1
                print("(",i,")"," ",k,"\t"*7,v,sep="")
            print("-"*89)
            print("(A) ADD NEW DISH","\t"*2,"(M) BACK TO MAIN MENU","\t"*2)
            print("-"*89)
            update_menu_input = input("PLEASE ENTER DISH NAME TO BE UPDATED OR SELECT ANY OPERATION TO BE PERFORMED: ")
            if update_menu_input.upper() == "M":
                Swiggy.mainMenu(self)
            elif update_menu_input.upper() == 'A':
                meal_name1 = input("PLEASE ENTER NAME OF MEAL----  ")
                meal_price1 = input("PLEASE ENTER THE PRICE FOR YOUR DISH----  ")
                price_check = []
                for _i in meal_price1:
                    if ord(_i)>=48 and ord(_i)<=57:
                        price_check.append("True")
                    else:
                        price_check.append("False")
                if "False" in price_check:
                    print("WRONG PRICE INPUT PLEASE GIVE CORRECT INPUT")
                    Service.SignIn(self)
                else:
                    menu_restaurent[res_name][meal_name1] = meal_price1
            print("(A) ADD MORE DISH")
            print("(D) DONE WITH UPDATION")
            print("\n"*2)
            sel_input = input("SELECT YOUR OPTION----  ")
            if sel_input.upper() == 'A':
                Service.SignIn(self)
            elif sel_input.upper() == 'D':
                Swiggy.mainMenu(self)
            else:
                print("WRONG INPUT")
                Swiggy.mainMenu(self)

        else:
            print("WRONG RESTURANT NAME INPUT PLEASE GIVE CORRECT INPUT")
            Service.SignIn(self)









class OrderMeal:
    
    def orderFood(self):
        quantity_list = []
        food_list = []
        price_list = []
        input_check = []
        print("\n"*3)
        print("#"*40," ORDER FOOD ","#"*40)
        print(" (1) SLECTE OPTION FROM RESTURANTS\n "
        "(2) SEARCH DISH  ")
        print(" (B) BACK ")
        print(" (E) EXIT ")
        print("\n"*2)
        or_input = input("  SELECT OPTION -----")
        if or_input == '1':
            print("PLEASE SELECT THE RESTAURENT OF YOUR CHOICE FROM BELOW OPTIONS: \n")
            for i in range (0,len(restaurent_dict)):
                print(f"({i+1}){(list(restaurent_dict.keys())[i])}",sep='')
            print()
            print("(M) MAIN MENU\n "
            "(P) PREVIOUS MENU\n"
            "(E) EXIT   ")
            of_input = input("PLEASE SELECT YOUR CHOICE----- ")
            if of_input.upper() == 'M':
                Swiggy.mainMenu(self)
            elif of_input.upper() == 'E':
                exit()
            elif of_input.upper() == 'P':
                OrderMeal.orderFood(self)
            elif of_input != "M" and of_input != "S" and of_input != 'P':
                for i in of_input:
                    if ord(i) >= 48 and ord(i) <= 57:
                        input_check.append("True")
                    else:
                        input_check.append("False")
            if "False" in input_check:
                print("\n" + "ERROR: Invalid Input (",of_input,"). Try again!",sep='')
                OrderMeal.orderFood(self)
            elif int(of_input)<= len(restaurent_dict):
                OrderMeal.resturantMenu(self,list(restaurent_dict.keys())[int(of_input)-1],food_list,price_list,quantity_list)
            else:
                print("WRONG INPUT PLEASE SELECT CORRECT OPTION")
                OrderMeal.orderFood(self)
        elif or_input == '2':    
            OrderMeal.search_Menu(self)
        elif or_input.upper() == 'B':
            Swiggy.mainMenu(self)
        elif or_input.upper() == 'E':
            exit()
        else:
            print("wrong input please select correct input")
            OrderMeal.orderFood(self)





    def search_Menu(self):
        l = []
        flag = 0
        while True:
            print("\n")
            print("#"*35,"SEARCH MENU","#"*35)
            print("\n"*2)
            print("-"*89)
            print("(B) BACK TO ORDER FOOD PAGE")
            print("-"*89)
            dish = (input("PLEASE ENTER DISH NAME : ").upper())
            sr_no = 1
            for i,j in menu_restaurent.items():
                for k,v in j.items():
                    if k.startswith(dish):
                        print("\n")
                        print("-"*89)
                        print("(",sr_no,")"," ",i,sep="")
                        sr_no += 1
                        l.append(i)
                        print("DISH NAME: ",k,"\t"*6,"PRICE: ",v)
                        print("-"*89)
                        flag = 1
                    else:
                        continue
            if flag == 0:
                print("ENTER DISH NOT FOUND ")
                OrderMeal.search_Menu(self)
                break
            while True:
                try:
                    search_menu_input = input("PLEASE SELECT RESTAURANT: ")
                    search_menu_input = int(search_menu_input)
                    break
                except ValueError:
                    print("NO VALID INPUT!! PLEASE TRY AGAIN ...")
            if l != []:
                OrderMeal.resturantMenu(self,l[search_menu_input-1],[],[],[])
                break
            else:
                print("\n" + "ENTERED DISH (",dish,") NOT FOUND. TRY AGAIN!",sep='')
        




    def resturantMenu(self,res,food_list,price_list,quantity_list):
        if restaurent_dict[res]>1:
            print("********SORRY WE ARE NOT ACCEPTING MORE ORDER PLEASE TRY AFTER SOME TIME********")
            OrderMeal.orderFood(self)
        input_check1 = []
        print("*."*80)
        print("="*79)
        print("-"*40,res,"-"*40)
        print("MEAL"," "*70, "PRICE", "\n"*3)
        k = 0
        for i, j in menu_restaurent.items():
            if i == res:
                for meal,price in j.items():
                    print("(",k+1,")  ",meal," "*55,price)
                    k +=1
                break
        print("\n"*3)
        print("(M) MAIN MENU\n (R) BACK TO RESTURANT LIST\n (V) VIEW CART ","\n"*3)
        dish_input = input("PLEASE SELECT YOUR CHOICE------ ")
        if dish_input.upper()== 'M':
            Swiggy.mainMenu(self)
        elif dish_input.upper() == 'R':
            OrderMeal.orderFood(self)
        elif dish_input.upper() == 'V': 
            if food_list != [] and price_list != []:
                OrderMeal.cart(self,food_list,price_list,quantity_list,res)
        elif dish_input != "V" or dish_input != "R" or dish_input != "M":
            for i in dish_input:
                if ord(i) >= 48 and ord(i) <= 57:
                        input_check1.append("True")
                else:
                    input_check1.append("False")
            if "False" in input_check1:
                print("\n" + "ERROR: Invalid Input (",dish_input,"). Try again!",sep='')
                OrderMeal.resturantMenu(self,res,food_list,price_list,quantity_list)
            elif int(dish_input)> len(menu_restaurent[res]):
                print("WRONG INPUT PLEASE SELECT CORRECT OPTION ")
                OrderMeal.resturantMenu(self,res,food_list,price_list,quantity_list)
            else:
                f=(list(menu_restaurent[res].keys())[int(dish_input)-1])
                food_list.append(f)
                p=list((menu_restaurent[res]).values())[int(dish_input)-1]
                price_list.append(p)
                q= input("ENTER QUANTITY----- ")
                quantity_list.append(q)
                OrderMeal.resturantMenu(self,res,food_list,price_list,quantity_list)
        else:
            print("wrong input please select correct input")
            OrderMeal.resturantMenu(self, res, food_list, price_list, quantity_list)

    
    def cart(self,food_list,price_list,quantity_list,res):
        tp = 0
        total_price = []
        for j in range (len(price_list)):
            total_price.append(int(quantity_list[j])*(price_list[j]))
        print("-"*80)
        print("ITEMS", " "*30,"QUANTITY"," "*30,"PRICE")
        print("="*80)
        for i in range (len(food_list)):
            print(f"({i+1}) {food_list[i]}"," "*20,quantity_list[i]," "*20,total_price[i])
            tp += total_price[i]
        gst = (tp*18)//100
        print("  GST"," "*50,gst)
        print("="*80)
        print("TOTAL"," "*50,tp+gst)
        print("\n"*3)
        print("(P) PAYMENT\n"
        "(B) BACK TO MENU LIST")
        print("\n"*3)
        cart_input = input("SELECT YOUR CHOICE----  ")
        if cart_input.upper() == "B":
            OrderMeal.resturantMenu(self,res,food_list,price_list,quantity_list)
        elif cart_input.upper() == 'P':
            OrderMeal.Payment(self,food_list,price_list,quantity_list,res)
        else:
            print("WRONG INPUT PLEASE SELECT CORRECT CHOICE ")
            OrderMeal.cart(self,food_list, price_list, quantity_list, res)



    

    def Payment(self,food_list,price_list,quantity_list,res):
        print("#"*80)
        print(" "*20, "MODE OF PAYMENT")
        print("(1)"," "*10,"CASH ON DELIVERY")
        print("(2)"," "*10,"CREDIT CARD/DEBIT CARD")
        print("(3)"," "*10,"UPI")
        print("(4)"," "*10,"EMI")
        print("="*80)
        print("(C)"," "*10,"CANCEL PAYMENT")
        pay_input = input("PLEASE SELECT YOUR CHOICE----   ")
        if pay_input.upper() == 'C':
            OrderMeal.cart(self, food_list, price_list, quantity_list, res)
        elif pay_input == '1' or pay_input == '2' or pay_input == '3' or pay_input == '4':
            restaurent_dict[res] = restaurent_dict[res]+1
            OrderMeal.Payment_success(self,res)
        else:
            print("WRONG INPUT PLEASE SELECT CORRECT CHOICE ")
            OrderMeal.Payment(self, food_list, price_list, quantity_list, res)



    def Payment_success(self,res):
        print("#"*39,"PAYMENT STATUS","#"*39)
        print("\n"*3)
        print("\t"*4,"PAYMENT SUCCESSFUL")
        print("\n"*3)
        print("="*89)
        print("(M)","\t","BACK TO MAIN MENU")
        print("\n"*2)
        print("(E)","\t","EXIT")
        print("="*89)
        def endHotelProcess(self,res):
            while(restaurent_dict[res]!=0):
                time.sleep(40)
                restaurent_dict[res] -= 1
        t1 = threading.Thread(target=endHotelProcess,args=(self,res,))
        queueList.append(t1)
        queueList[-1].start()
        pay_in = input("PLEASE SELECT YOUR CHOICE-----  ")
        if pay_in.upper() == 'M':
            Swiggy.mainMenu(self)
        elif pay_in.upper() == 'E':
            exit()
        



class Swiggy(OrderMeal,Service):

    def mainMenu(self):
        print("*"*40,"MAIN MENU","*"*40)
        print("*"*35,"SELECT YOUR CHOICE","*"*37)
        print("(O) ORDER FOOD" + "\n"
                    "(J) JOIN SERVICES\n"
                    "(E) EXIT\n")
        print("->"*50)
        mm_input=input("PRESS 'O' FOR ORDER FOOD------- 'J' FOR JOIN\
SERVICES-------- 'E' FOR EXIT----  ").upper()
        if mm_input == "O":
            OrderMeal.orderFood(self)
        elif mm_input == 'J':
            Service.joinService(self)
        elif mm_input == 'E':
            print("THANKING YOU FOR USING SWIGGY\n"
            "HAVE A HEALTHY MEAL")
            exit()
        else:
            print("WRONG INPUT PLEASE SLECTE CORRECT INPUT")
            self.mainMenu()
            
if __name__ == "__main__":
    o = Swiggy()
    o.mainMenu()