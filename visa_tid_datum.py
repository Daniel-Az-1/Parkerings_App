import datetime

def show_time_and_date():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M") 
    print(f"Dagens datum och aktuella tid:\n{current_time}")