parking_spaces = {
        "1":["ledig"],
        "2":["ledig"],
        "3":["ledig"],
        "4":["ledig"],
        "5":["upptagen","HJU531"],
        "6":["ledig"],
        "7":["ledig"]
    }
    
def show_available_parking_kort():
    available = False
    result_str = "\nLediga kortvariga parkeringsplatser:\n"
    
    for key in parking_spaces:
        if parking_spaces[key] == ["ledig"]:
            result_str += f"Parkerings plats: {key}\n"
            available = True

    if not available:
        return "Inga kortvariga parkeringsplatser är lediga."
    else:
        return print(result_str)
    