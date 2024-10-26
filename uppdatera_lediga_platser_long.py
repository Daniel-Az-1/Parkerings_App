
def update_available_parking_spaces(space_nummer, ny_status, confirmed_number_of_months=None, regnummer=None):

    if ny_status == "upptagen" and regnummer:
        import visa_langvariga_str
        visa_langvariga_str.parking_spaces[space_nummer] = [ny_status, regnummer]
        print(f"Du har hyrt parkeringsplatsen {space_nummer} för {confirmed_number_of_months} månad/månader. \nTack för att du har använt Quick Park, hejdå!")
        return visa_langvariga_str.parking_spaces
    elif ny_status == "ledig":
        import visa_langvariga_str
        visa_langvariga_str.parking_spaces[space_nummer] = [ny_status]
        print("Uppdatering av listan av långa parkeringsplatser har lyckats !")
        return
    else:
        print("Ett tekniskt fel har inträffat! vänligen kontakta kundtjänsten med telefonnummer 0737826801 för att få hjälp")


