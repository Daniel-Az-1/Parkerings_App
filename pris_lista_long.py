pris_list = {"1 månad": 500, "3 månader": 1400, "6 månader": 2800, "12 månader": 5500}

def show_pris_long_time():
    
    line_number = 1
    print("Observera att du hyr en specifik parkeringsplats med ett nummer och du får endast parkera på den platsen.")
    print("\nPrislista för långvarig parkering:")
    for time, pris in pris_list.items():
        print(f"{line_number}) {time} = {pris} Kr")
        line_number += 1
