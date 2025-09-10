class Tickets:



    tickets_available = 100
    bought_tickets = 0

    def __init__(self, name:str, tickets:int):
        self.name = name,
        self.tickets = tickets

    def buy_Ticket(self, tickets):
        if Tickets.tickets_available >= tickets:
            Tickets.tickets_available -= tickets
            print(f"You have {Tickets.tickets_available} available!")
            Tickets.bought_tickets += tickets
        else:
            return f"Insufficient tickets! You have {Tickets.tickets_available} tickets available and user needs {tickets}"

    def remaining_Tickets(self):
        print(f"You have {Tickets.tickets_available} remaining")

    def display_bought(self):
        print(f"Number of tickets bought were = {Tickets.bought_tickets}")



