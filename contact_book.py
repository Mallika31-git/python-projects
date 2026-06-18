contacts={"rebca":"9573267896","rinky":"1234567890","mallika":"8976542098"}
options=f"""
1. Add Contact
2. Search Contact
3. Delete Contact
4. Display Contacts
5. count contacts
6. update
7. Exit
"""
 
choice=''
while choice!=7:
    print(options)
    choice=int(input("enter your choice:"))
    if choice ==1:
       key=input("enter your contact name:")
       
       if key in contacts:
           print("entered name is already in contacts")
       elif key not in contacts:
           value=input("enter your number:")
           if value in contacts.values():
            print("entered number is already in contacts")
      
           elif len(value)!=10 or not value.isdigit():
             print("entered number will not fit for contact")

           else:
            contacts[key]=value
            print(contacts)
           
       
 
    elif choice==2:
        menu=f"""
        1.search contact with name
        2.search contact with number
        3.exit
        """
        choose=''
        while choose!=3:
           print(menu)
           choose=int(input("choose any one:"))
           if choose==1:
             key=input("enter key:")
             if key in contacts.keys():
               print(key,":",contacts[key])
             else:
               print("sorry! entered key is not available")
           elif choose==2:
               
             num=input("enter a number:")
             if num in contacts.values():
                for i in contacts:
                    if num==contacts[i]:
                        print(i,":",contacts[i])
                        break
             else:
               print("entered number is not in contacts")
           elif choose==3:
                print("returning to main menu")
           else:
            print("you choose wrong number")
     
    elif choice==3:
        key=input("eneter name to delete:")
        if key in contacts:
            del contacts[key]
            print(contacts)
        else:
            print("sorry! entered name is not available")
            
    elif choice==4:
        for i in contacts:
         print(i,":",contacts[i])
          
         
        
    elif choice==5:
         print("number of contacts are:",len(contacts))
 
    elif choice==6:
        choose=f"""
       1.update  number
       2.update name
       3.exit
       """
        pick=''
        while pick!=3:
         print(choose)
         pick=int(input("pick one:"))
         if pick ==1:
             name=input("enter name:")
   
             if name in contacts:
                 number=input("enter number:")
                 if number not in contacts.values():
                    if len(number)==10 and number.isdigit() :
                     
                     contacts.update({name:number})
                     print(contacts)
                    else:
                     print("sorry! entered detailes or wrong")
                 else:
                      print("sorry! entered number is already in contacts")
             else:
                 print("sorry! entered name is wrong")
         elif pick==2:
          num=input("enter number:")    
          if num in contacts.values():
             
                new_name = input("enter new name:")
                if new_name not in contacts:
                    old_name=''
                    for i in contacts:
                     if contacts[i] == num:
                      old_name = i
                   
                      break
                    contacts[new_name]=contacts[old_name]
                    del contacts[old_name]
                

                    print(contacts)
                else:
                   print("sorry! entered name is alredy in contacts")

          else:
            print(" sorry! number not found")
         elif pick==3:
             print("returning to main menu")
        
         else:
           print("sorry! you picked wrong number")
              
    elif choice==7:
        print("signing out")
    else:
        print("sorry! your choice is wrong")