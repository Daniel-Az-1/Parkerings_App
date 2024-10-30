# exempel på ordlistan user_data={"Daniel":"820610"}
def register():
    import shelve
    with shelve.open("programs_database_shelve.db") as db:
        user_data = db.get("user_data", {})

        while True:
            print("Registrera dig:")
            user_name = input("Ange ett användarnamn: ")
            
            if user_name in user_data:
                print("⚠️ Användarnamnet är redan taget. Försök med ett annat.")
            else:
                password = input("Ange ett lösenord: ")
                user_data[user_name] = password
                db["user_data"] = user_data
                print("Din registrering har lyckats ✔️")
                break 

    while True:
        user_choice = input("Tryck 'ja' för att logga in eller 'nej' för att avsluta: ").lower()

        if user_choice == "ja":
            import logga_in
            logga_in.log_in()
            return
        elif user_choice == "nej":
            print("Tack för att du använder Quick Park. Välkommen åter!")
            return 
        else:
            print("⚠️ Ogiltigt val, försök igen.")
