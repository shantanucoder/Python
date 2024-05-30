class Train:
    def __init__(self):
        self.seats = 78
        self.fare = 175

    def BookTickets(self):
        self.seats -= 1 

    def GetStatus(self):
        print("The status of the train with available seats:-", self.seats)

    def GetFareInfo(self):
        print("The fare of the train is:-", self.fare) 

tr = Train()
tr.GetFareInfo()
tr.GetStatus()
print("after booking one ticket")
tr.BookTickets()
tr.GetStatus()


