item_dict={}
f=open("D:\computer_hardware_shop\com_hardware_software.txt","r")

while True:
    item=f.readline()
    if item=='':
        break
    qntt=f.readline()
    uprc=f.readline()
    item=item[:len(item)-1]
    qntt=int(qntt[:len(item)-1])
    uprc=float(uprc[:len(item)-1])
    item_dict[item]=[qntt,uprc]
f.close()


m_length=50
def show_dict():
    print(m_length*"=")
    print("available item and quantity")
    print(m_length*"=")
    for x in item_dict: 
        print(x,(40-len(x))*" ",(6-len(str(item_dict[x][0])))*(" "),item_dict[x][0])
    print(m_length*"-")
    
def dec_quant(key,val):
    item_dict[key][0]-=val
    
def inc_quant(key,val):
    item_dict[key][0]+=val
def recive_order():
    print("Order Recived:")
    
    while True:
        item=input("Item(type 'x' to stop) :")
        if item=='x':
            break
        value=int(input("Enter quantity : "))
        
        if item not in item_dict:
            print("new item found")
            uprice=float(input("Unit price: "))
            item_dict[item]=[value,uprice]
            continue
            
        inc_quant(item,value)
        

def process_demand():
        print("Input Demand:")
        #demand_list is a empty list

        demand_list=[]
        
        
        while True:
            item=input("Item(type 'x' to stop) :")
            if item=='x':
                break
            if item not in item_dict:
                # Here f means formated string
                print(f"the item '{item}' is not available")
                continue
            value=int(input("Enter quantity : "))
            # we don't want to it will print negative number
            if value>item_dict[item][0]:
                print(f"total item of {item_dict[item][0]} pcs available")
                continue
            
            dec_quant(item,value)
            
            demand_list += [item,value,item_dict[item][1],value*item_dict[item][1]],

            # printing the payment recit
            print(40*"=")
            print("** Payment Recipt **".center(40))
            print(40*"=")
            print("Item",8*" ","Quant"," ","U.Price",2*" ","S.Price")
            print(40*"-")
            tprice=0
            for x in demand_list:
                tprice += x[3]
                print(x[0].title(),(11-len(x[0]))*" ",
                      (5-len(str(x[1])))*" ",x[1],
                      (8-len(str("%.2f"%x[2])))*" ","%.2f"%x[2],
                      (9-len(str("%.2f"%x[3])))*" ","%.2f"%x[3])
            print(40*"-")
            print("Total price:"," ",)
            print(40*"-")
        #show_dict()
        


# Home Work: add new item
    
#show_dict()

while True:
    show_dict()
    print("Choose an option : " )
    print("Type '1' To process demand")
    print("Type '2' to recive order")
    print("Type '3' to exit the program")
    choice= input("Choice: ")
    if choice == '1':
        process_demand()
    elif choice== '2':
        recive_order()
    elif choice== '3':
        break
    else:
        continue
    
f=open("D:\computer_hardware_shop\com_hardware_software2.txt","w")
for x in item_dict:
    f.write(x+"\n")
    f.write(str(item_dict[x][0])+"\n")
    f.write(str(item_dict[x][1])+"\n")
f.close()
    














    
