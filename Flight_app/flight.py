# id, flight_number, airline, source, destination, departure_time, arrival_time, seats, price
class Flight:
    def __init__(self, id, flight_number, airline, source, destination, departure_time, arrival_time, seats, price):
        self.id = id
        self.flight_number = flight_number
        self.airline = airline
        self.source = source
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.seats = seats
        self.price = price

    def __str__(self):
        return f'[id={self.id}, flight_number={self.flight_number}, airline={self.airline}, source={self.source}, destination={self.destination}, departure={self.departure_time}, arrival={self.arrival_time}, seats={self.seats}, price={self.price}]'

    def __repr__(self):
        return self.__str__()
