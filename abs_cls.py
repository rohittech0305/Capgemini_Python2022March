from abc import ABC , abstractmethod  #abstract base class
class Car(ABC):
    @abstractmethod
    def breaks(self):
        pass
    @abstractmethod
    def seats(self):
        pass
    @abstractmethod
    def tyres(self):
        pass
    @abstractmethod
    def mirror(self):
        pass
    @abstractmethod
    def clutch(self):
        pass
    @abstractmethod
    def acceralator(self):
        pass
    @abstractmethod
    def audio(self):
        pass

    def car_price(self):
        print("car price is :1400000")

class EcoSport(Car):
    def __init__(self,model,yr):
        self.model=model
        self.year=yr

    def breaks(self):
        self.break_applied=True

    def seats(self):
        self.seat_capacity="7 seater"

    def tyres(self):
        self.tire="4 tyres"

    def mirror(self):
        self.mirror="fitted"

    def clutch(self):
        self.clutch="fitted"

    def acceralator(self):
        print("Applied")

    def audio(self):
        print("Special device attached")

c1=EcoSport('ES-o',2022)
c1.car_price()
c1.audio()