def confirm_the_time(antal_timmar):
    print(f"Du har valt att parkera i {antal_timmar} timme/timmar.")
    confirm = input("Bekräfta ditt val? (ja/nej): ")
    
    if confirm.lower() == "ja":
        print("Tiden har bekräftats.")
        return antal_timmar  
    else:
        print("Bokningen har avbrutits.")
        return None  
