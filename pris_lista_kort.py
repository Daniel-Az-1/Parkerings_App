pris_list = {"En timme": 20}

def show_pris_short_time():
    line_number = 1
    print("Observera att du debiteras per minut om du parkerar kortare eller längre än en timme.")
    print("\nPrislista för kortvarig parkering:")
    for time, pris in pris_list.items():
        print(f"{line_number}) {time} = {pris} Kr")
        line_number += 1
