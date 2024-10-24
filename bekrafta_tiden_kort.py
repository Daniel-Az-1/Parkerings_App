def confirm_the_time(antal_minuter):
    while True:
        print(f"Du har valt att parkera i {antal_minuter} minuter.")
        confirm = input("Bekräfta ditt val (ja/nej): ").lower()

        if confirm == "ja":
            print("Tiden har bekräftats.")
            import simulera_betalning_long  # här måste ämdras !
            simulera_betalning_long.confirm_payment(antal_minuter)  # här måste ändras 
            return antal_minuter

        elif confirm == "nej":
            print("Bokningen har avbrutits.")
            while True:
                user_choice = input("Tryck 1 för att återgå till huvudmenyn eller 2 för att logga ut: ")

                if user_choice == "1":
                    import meny  # Importera meny när användaren vill återgå till menyn
                    meny.show_menu()
                    return
                elif user_choice == "2":
                    print("Tack för att du använde Quick Park! Hejdå!")
                    return
                else:
                    print("Ogiltigt val, försök igen.")
