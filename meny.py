def show_menu():
    while True:
        print("\nVälkommen till huvudmenyn!")
        print("1. Visa lediga platser")
        print("2. Boka parkering")
        print("3. Avsluta")
        user_choice = input("Ange ditt val (1-3): ")
        if user_choice == "1":
            import visa_lediga_platser
            visa_lediga_platser.show_parking_spaces()
            return
        elif user_choice == "2":
            import boka_parkering
            boka_parkering.book_parking()
            return
        elif user_choice == "3":
            print("Programmet avslutas. Tack för att du använde Quick Park!")
            return
        else:
            print("Ogiltigt val, försök igen.")
