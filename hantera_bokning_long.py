
def manage_booking():
    while True:
        print("Ange hur många månader du vill hyra parkeringsplatsen:")
        user_choice = input("Välj mellan 1, 3, 6 eller 12 månader: ")

        
        if user_choice.isdigit() and int(user_choice) in [1, 3, 6, 12]:
            user_choice = int(user_choice) 
            print(f"Du har valt att hyra parkeringen i {user_choice} månad/månader.")
            import bekrafta_tiden_long
            bekrafta_tiden_long.confirm_the_time(user_choice)
            return user_choice 
        else:
            print("Ogiltigt val. Du kan välja 1, 3, 6 eller 12 månader.")
        
        while True:
            print("Välj ett av följande alternativ:")
            print("1) Ange ett nytt antal månader")
            print("2) Avsluta bokningen")
            retry_choice = input("Ange ditt val: ")

            if retry_choice == "1":
                break
            elif retry_choice == "2":
                print("Bokningen har avslutats. Tack för att du använde Quick Park!")
                return
            else:
                print("Ogiltigt val, försök igen.")
