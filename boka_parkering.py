import visa_kortvariga_str
import visa_langvariga_str
import visa_tid_datum
import hantera_bokning_long
import hantera_bokning_kort
import pris_lista_long
import pris_lista_kort

def book_parking():
    print("Välj typ av parkering:")
    
    while True:
        user_choice = input("Tryck 1 för att hyra en långvarig parkeringsplats eller 2 för kortvarig parkering: ")

        if user_choice == "1":
            print("\nLångvarig parkering:")
            pris_lista_long.show_pris_long_time()
            visa_langvariga_str.show_available_parking_long()
            visa_tid_datum.datetime()
            hantera_bokning_long.manage_booking()
            return
        elif user_choice == "2":
            print("\nKortvarig parkering:")
            pris_lista_kort.show_pris_short_time()
            visa_kortvariga_str.show_available_parking_short()
            visa_tid_datum.show_time_and_date()
            hantera_bokning_kort.manage_booking()
            return
        else:
            print("Ogiltigt val. Vänligen välj ett giltigt alternativ.")
            while True:
                print("Välj ett av alternativen:")
                print("1) Försöka igen")
                print("2) Avsluta")
                user_choice_2 = input("Ange ditt val: ")

                if user_choice_2 == "1":
                    break
                elif user_choice_2 == "2":
                    print("Tack för att du använde Quick Park! \nHej då!")
                    return
                else:
                    print("Ogiltigt val, försök igen.")
