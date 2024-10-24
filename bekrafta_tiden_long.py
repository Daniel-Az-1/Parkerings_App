def confirm_the_time(antal_manader):
    print(f"Du har valt att parkera i {antal_manader} månad/månader.")
    confirm = input("Bekräfta ditt val? (ja/nej): ")
    
    if confirm.lower() == "ja":
        print("Tiden har bekräftats.")
        return antal_manader 
    else:
        print("Bokningen har avbrutits.")
        return None  
