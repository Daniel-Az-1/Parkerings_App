def log_in():
    import shelve 
    with shelve.open("programs_database_shelve.db") as db: 
        user_data = db["user_data"] 

        while True:
            user_name = input("Ange ditt användarnamn : ")
            password = input("Ange ditt lösenord: ")

            if user_name in user_data and password == user_data[user_name]:
                print("Du är inloggat nu.")
                import meny
                meny.show_menu()
                return 
            else:
                print("⚠️ Fel användarnamn eller lösenord")

                while True:
                    print("Välj ett av alternativen nedan:")
                    print("Tryck '1' för att försöka logga in igen.")
                    print("Tryck '2' för att avsluta.")
                    user_choice = input("Ange ditt val: ")

                    if user_choice == "1":
                     break
                    elif user_choice == "2":
                        print("Tack för att du har använt Quick Park, hejdå!")
                        return
                    else:
                        print("⚠️ Ogiltigt val, försök igen.")
                    