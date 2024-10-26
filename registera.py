user_data={"Daniel":"820610"}
def register():
    while True:
        print("Registera dig: ")
        user_name = input("Ange ett användarnamn: ")
        
        if user_name in user_data:
            print("användarnamnet är redan taget. Försök med ett annat")
        else:
            password = input("Ange ett lösenord: ")
            user_data[user_name]=password
            print("Din registering har lyckats")
            import meny
            meny.show_menu()
            return