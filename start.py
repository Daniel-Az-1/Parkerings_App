def start_program():
    import logo
    logo.show_logo()
    print("\nVi ser fram emot att hjälpa dig med parkeringen.")

    while True:
        print("\nVälj ett alternativ nedan:")
        user_choice = input("Ange '1' för att registrera dig eller '2' för att logga in: ")

        if user_choice == '1':
            print("\nDu har valt att registrera dig. Laddar registreringssidan...")
            import registera
            registera.register()
            return
        elif user_choice == '2':
            print("\nDu har valt att logga in. Laddar inloggningssidan...")
            import logga_in
            logga_in.log_in()
            return
        else:
            print("\n⚠️ Ogiltigt val. Vänligen välj ett giltigt alternativ.")

            while True:
                user_choice_2 = input("Ange '1' för att försöka igen eller '2' för att avsluta: ")
                if user_choice_2 == '1':
                    print("\nFörsöker igen...")
                    break
                elif user_choice_2 == '2':
                    print("\nTack för att du använder Quick Park. Välkommen åter 👋")
                    return
                else:
                    print("⚠️ Ogiltigt val. Vänligen ange '1' eller '2'.")

if __name__ == "__main__":
    start_program()

