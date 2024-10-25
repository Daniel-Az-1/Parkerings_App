def confirm_payment(confirmed_number_of_months):
    # Importera pris_lista_long när vi behöver den
    import pris_lista_long
    prise = pris_lista_long.pris_list[confirmed_number_of_months]

    while True:
        print(f"Du ska betala {prise} kr för att hyra parkeringen i {confirmed_number_of_months} månad/månader.")
        user_choice = input("Tryck 'ja' för att acceptera debiteringen eller 'nej' för att avbryta och återgå till huvudmenyn: ").lower()

        if user_choice == "ja":
            print("Du kan betala med MasterCard eller Visa.")
            
            # Betalningsprocess med möjlighet att försöka igen vid fel
            while True:
                card_type = input("Välj 'Master' eller 'Visa': ").lower()
                if card_type in ["master", "visa"]:
                    card_number = input("Ange kortnummer (16 siffror, grupperat i 4-tal med mellanslag): ")

                    if len(card_number.replace(" ", "")) == 16 and card_number.replace(" ", "").isdigit():
                        card_cv = input("Ange kortets CVV-nummer (3 siffror): ")

                        if len(card_cv) == 3 and card_cv.isdigit():
                            print(f"Betalningen lyckades! Du har debiterats med {prise} kr.")
                            car_register_number = input("Ange bilens registreringsnummer: ")

                            # Visa lediga platser med möjlighet att välja rätt plats
                            while True:
                                import visa_langvariga_str
                                visa_langvariga_str.show_available_parking_long()

                                select_parking_space = input("Välj en ledig plats från listan: ")

                                # Kontrollera om vald plats är ledig
                                if select_parking_space in visa_langvariga_str.parking_spaces and visa_langvariga_str.parking_spaces[select_parking_space] == "ledig":
                                    new_status = "upptagen"
                                    import uppdatera_lediga_platser
                                    uppdatera_lediga_platser.update_available_parking_spaces(select_parking_space, new_status, confirmed_number_of_months, car_register_number)
                                    return select_parking_space, new_status, confirmed_number_of_months, car_register_number
                                else:
                                    print("Fel inmatning, du valde ett ogiltigt platsnummer. Försök igen.")
                        else:
                            print("Fel inmatning, CVV-nummer måste vara 3 siffror. Försök igen.")
                    else:
                        print("Fel inmatning, kortnummer måste bestå av 16 siffror och vara korrekt grupperat. Försök igen.")
                else:
                    print("Du måste välja mellan 'Master' eller 'Visa'. Försök igen.")
        
        elif user_choice == "nej":
            import meny
            meny.show_menu()
            return
        else:
            print("Ogiltigt val, svara med 'ja' eller 'nej'.")
