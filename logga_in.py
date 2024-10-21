import registera
import meny
def log_in():

    while True:
        user_name = input("Ange ditt användarnamn : ")
        password = input("Ange ditt lösenord: ")

        if user_name in registera.user_data and password == registera.user_data[user_name]:
            meny.show_menu()
            return 
        else:
            print("Fel användarnamn eller lösenord")

            while True:
                print("Välj ett av alternativ:")
                print("1) Försöka igen")
                print("2) Avsluta")
                user_choice = input("Ange ditt val: ")

                if user_choice == "1":
                    break
                elif user_choice == "2":
                    print("Programmet har avslutas \nHej då ")
                    return
                else:
                    print("Ogiltigt val, försök igen.")

            

        
            
    
