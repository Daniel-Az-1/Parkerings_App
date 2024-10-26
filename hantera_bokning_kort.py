
def manage_booking():
    while True:
        print("Ange den tid du önskar parkera i minuter:")
        user_choice = input("Vänligen ange ett positivt heltal för antalet minuter (t.ex. 30, 60, 90): ")

        
        if user_choice.isdigit() and int(user_choice) > 0:
            user_choice = int(user_choice) 
            print(f"Du har valt att parkera i {user_choice} minuter.") #måste ändras
            import  bekrafta_tiden_kort
            bekrafta_tiden_kort.confirm_the_time(user_choice)
            return user_choice
        else:
            print("Ogiltig inmatning. Vänligen ange ett positivt heltal för att fortsätta.")
            
            while True:
                print("Välj ett av följande alternativ:")
                print("1) Ange ny parkeringstid")
                print("2) Avsluta bokningen")
                retry_choice = input("Ange ditt val: ")

                if retry_choice == "1":
                    break
                elif retry_choice == "2":
                    print("Bokningen har avslutats. Tack för att du använde Quick Park! Välkommen åter!")
                    return
                else:
                    print("Ogiltigt val, försök igen.")