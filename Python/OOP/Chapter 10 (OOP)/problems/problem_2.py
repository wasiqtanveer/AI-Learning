class train:
    tickets = 0
    @staticmethod
    def get_ticket():
        train.tickets += 1
        print(f"ticket number {train.tickets} is booked")
        return train.tickets
    
    @staticmethod
    def status():
        print(f"Total tickets booked are {train.tickets}")    
        
    @staticmethod
    def get_fare():
        print("Ticket fare is 1000")

train.status()
train.get_fare()
train.get_ticket()
train.get_ticket()
train.get_ticket()
train.get_ticket()
train.get_ticket()
train.get_ticket()
train.get_ticket()
train.status()