parking_spaces_long = {
        "1": "[ledig]",
        "2": "[ledig]",
        "3": "[ledig]",
        "4": "[upptagen, ABC678]",
        "5": "[ledig]",
        "6": "[ledig]",
        "7": "[ledig]"
    }
     

def show_available_parking_long():
    available = False
    result_str = "\nTillgängliga långvariga parkeringsplatser:\n"

    for key in parking_spaces_long:
            if parking_spaces_long[key] == "[ledig]":
                result_str += f"Parkerings plats: {key}\n"
                available = True

    if not available:
        return "Inga långvariga parkeringsplatser är lediga."
    else:
        return print(result_str)