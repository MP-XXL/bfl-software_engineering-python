import ticketting_logic



user1 = ticketting_logic.Tickets("Lucky", 90)
user2 = ticketting_logic.Tickets("Lucky", 5)
user3 = ticketting_logic.Tickets("Lucky", 10)

user1.buy_Ticket(90)
print(user2.buy_Ticket(30))
user1.display_bought()
user1.remaining_Tickets()
