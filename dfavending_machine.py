class VendingMachineDFA:
    def __init__(self):
        # Initialize the state of the vending machine
        self.state = 0

    def insert_quarter(self):
        if self.state == 0:
            self.state = 1
        elif self.state == 1:
            self.state = 2
        elif self.state == 2:
            self.state = 3
        elif self.state == 3:
            self.state = 4
        elif self.state == 4:
            self.state = 5

        self.display_state()

    def insert_dollar(self):
        if self.state == 0:
            self.state = 4
        elif self.state == 1:
            self.state = 5
        elif self.state == 2:
            self.state = 5
        elif self.state == 3:
            self.state = 5
        elif self.state == 4:
            self.state = 5

        self.display_state()

    def display_state(self):
        # Display the amount of money inserted
        if self.state == 0:
            print("Current balance: $0.00")
        elif self.state == 1:
            print("Current balance: $0.25")
        elif self.state == 2:
            print("Current balance: $0.50")
        elif self.state == 3:
            print("Current balance: $0.75")
        elif self.state == 4:
            print("Current balance: $1.00")
        elif self.state == 5:
            print("Current balance: $1.25 (Soda dispensed)")

    def run(self):
        # Run the vending machine loop
        while self.state < 5:
            action = input("Insert 'q' for a quarter or 'd' for a dollar: ").lower()
            if action == 'q':
                self.insert_quarter()
            elif action == 'd':
                self.insert_dollar()
            else:
                print("Invalid input. Please insert 'q' for a quarter or 'd' for a dollar.")
        
        print("Transaction complete. Enjoy your soda!")


# Instantiate and run the DFA vending machine
vending_machine = VendingMachineDFA()
vending_machine.run()
