def show_parking_spaces():
    while True:
        print("\nVill du se långvariga eller kortvariga parkeringsplatser?\n")
        print("1. Långvariga")
        print("2. Kortvariga")
        print("3. Återgå till huvudmenyn")
        choice = input("\nVälj ett alternativ (1, 2 eller 3): ")
        
        if choice == "1":
            import visa_langvariga_str
            visa_langvariga_str.show_available_parking_long()

            while True:
                back_to_menu_1 = input("\nVill du återgå till huvudmenyn? Välj 'nej' för att avsluta programmet. (ja/nej): ")
                
                if back_to_menu_1.lower() == "ja":
                    import meny
                    meny.show_menu()
                    return
                elif back_to_menu_1.lower() == "nej":
                    print(f"\nTack för att du använder Quick Park. Välkommen åter 👋")
                    return
                else:
                    print(f"\n⚠️ Ogiltigt svar. Försök igen")

        elif choice == "2":
            import visa_kortvariga_str
            visa_kortvariga_str.show_available_parking_short()

            while True:
                back_to_menu_2 = input("\nVill du återgå till huvudmenyn? Välj 'nej' för att avsluta programmet. (ja/nej): ")
                
                if back_to_menu_2.lower() == "ja":
                    import meny 
                    meny.show_menu()
                    return
                elif back_to_menu_2.lower() == "nej":
                    print(f"\nTack för att du använder Quick Park. Välkommen åter 👋")
                    return
                else:
                    print(f"\n⚠️ Ogiltigt svar. Försök igen")
            
        elif choice == "3":
            import meny
            meny.show_menu()
            return
        else:
            print("\n⚠️ Ogiltigt val, försök igen.")