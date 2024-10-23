def show_long_term_parking():
    # Ordlista över långvariga parkeringsplatser
    long_term_parking = {
        "Parkering 1": "upptagen",
        "Parkering 2": "tillgänglig",
        "Parkering 3": "tillgänglig",
        "Parkering 4": "upptagen",
        "Parkering 5": "tillgänglig",
        "Parkering 6": "upptagen",
        "Parkering 7": "tillgänglig"
    }
    
    while True:  # Loop för att återgå till huvudmenyn efter att ha visat platser
        print("\nTillgängliga långvariga parkeringsplatser:\n")
        available = False  # sätts till false först så att om alla är upptagen, meddelandet inga långvariga parkeringar är tillgängliga
        for key in long_term_parking:
            if long_term_parking[key] == "tillgänglig":
                print(f"{key}: {long_term_parking[key]}")
                available = True  # Om minst en plats är tillgänglig så kommer available = true, går till menu

        if available == False:
            print("Inga långvariga parkeringsplatser är tillgängliga.")
        
        # Fråga användaren om de vill gå tillbaka till huvudmenyn
        back_to_menu = input("\nVill du gå tillbaka till huvudmenyn? (ja/nej): ")
        if back_to_menu.lower() == "ja":
            from meny import show_menu
            show_menu()
            return
        elif back_to_menu.lower() == "nej":
            print(f"\nTack för att du använde Quick Park!")
            return
        else:
           print("\nOgiltigt val, försök igen.")
           