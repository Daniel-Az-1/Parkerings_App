pris_list = {1:500, 3:1400, 6:2800, 12: 5500}

def show_pris_long_time():
    line_number = 1
    print("Observera att du hyr en specifik parkeringsplats med ett nummer och du får endast parkera på den platsen.")
    print("\nPrislista för långvarig parkering:")
    for time, pris in pris_list.items():
        if time == 1:
            time_text = "månad"
        else:
            time_text = "månader"
        print(f"{line_number}) {time} {time_text} = {pris} Kr")
        line_number += 1
