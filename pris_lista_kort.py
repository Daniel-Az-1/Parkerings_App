pris_list = {1:20, 24:450}

def show_pris_short_time():
    line_number = 1
    print("Observera att du debiteras per minut om du parkerar kortare eller längre än en timme.")
    print("\nPrislista för kortvarig parkering:")
    for time, pris in pris_list.items():
        if time == 1:
            time_text = "timme"
        else:
            time_text = "timmar"
        print(f"{line_number}) {time} {time_text} = {pris} Kr")
        line_number += 1
