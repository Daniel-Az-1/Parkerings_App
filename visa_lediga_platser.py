def show_parking_spaces():
    
    while True:  # Loop för att återgå till menyn
        # Visa valet till användaren
        print("\nVill du se långvariga eller kortvariga parkeringsplatser?\n")
        print("1. Långvariga")
        print("2. Kortvariga")
        print("3. Gå tillbaka till huvudmenyn")  # Möjlighet att avsluta programmet
        
        # Ta emot användarens val
        choice = input("\nVälj ett alternativ (1, 2 eller 3): ")
        
        # Kontrollera användarens val och visa rätt parkeringstyper
        if choice == "1":
            import visa_langvariga_str
            visa_langvariga_str.show_long_term_parking()
            return
        elif choice == "2":
            import visa_kortvariga_str
            visa_kortvariga_str.show_short_term_parking()
            return
        elif choice == "3":
            from meny import show_menu
            show_menu()
            break 
        else:
            print("\nOgiltigt val, försök igen.")