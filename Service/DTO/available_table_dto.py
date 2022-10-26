class AvailableTableDTO:
    def __init__(self, reservation):
        self.one = 0 if reservation.one != 0 else 1
        self.two = 0 if reservation.two != 0 else 1
        self.three = 0 if reservation.three != 0 else 1
        self.four = 0 if reservation.four != 0 else 1
        self.five = 0 if reservation.five != 0 else 1
        self.six = 0 if reservation.six != 0 else 1
        self.seven = 0 if reservation.seven != 0 else 1
        self.eight = 0 if reservation.eight != 0 else 1
        self.nine = 0 if reservation.nine != 0 else 1
        self.ten = 0 if reservation.ten != 0 else 1
        self.eleven = 0 if reservation.eleven != 0 else 1
        self.twelve = 0 if reservation.twelve != 0 else 1