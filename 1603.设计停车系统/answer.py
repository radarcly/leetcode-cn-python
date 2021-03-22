class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.capacity = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.capacity[carType - 1]:
            self.capacity[carType - 1] -= 1
            return True
        else:
            return False