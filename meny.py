def show_menu():
    print("\nVälkommen till huvudmenyn!")

    while True:
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
            print("Tack för att du använder Quick Park. Välkommen åter!")
            return
        else:
            print("⚠️ Ogiltigt val, försök igen.")


        

