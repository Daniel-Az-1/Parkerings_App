def confirm_the_time(antal_manader):
    while True:
        print(f"\nDu har valt att hyra parkeringen i {antal_manader} månad/månader.")
        confirm = input("Bekräfta ditt val (ja/nej): ").lower()

        if confirm == "ja":
            print("Tiden har bekräftats.")
            import simulera_betalning_long 
            simulera_betalning_long.confirm_payment(antal_manader) 
            return antal_manader

        elif confirm == "nej":
            print("Bokningen har avbrutits.")
            while True:
                user_choice = input("Tryck 1 för att återgå till huvudmenyn eller 2 för att logga ut: ")

                if user_choice == "1":
                    import meny  
                    meny.show_menu()
                    return
                elif user_choice == "2":
                    print("Tack för att du använder Quick Park. Välkommen åter!")
                    return
                else:
                    print("⚠️ Ogiltigt val, försök igen.")
