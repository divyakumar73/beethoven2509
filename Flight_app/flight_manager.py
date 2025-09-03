flights = []

def create_flight(flight):
    global flights
    if len(flights) == 0:
        flight.id = 1
    else:
        flight.id = flights[-1].id + 1
    flights.append(flight)

def read_all():
    return flights

def read_by_id(id):
    for flight in flights:
        if flight.id == id:
            return flight
    return None

def update(flight):
    old_flight = read_by_id(flight.id)
    if old_flight is None:
        return
    old_flight.flight_number = flight.flight_number
    old_flight.airline = flight.airline
    old_flight.source = flight.source
    old_flight.destination = flight.destination
    old_flight.departure_time = flight.departure_time
    old_flight.arrival_time = flight.arrival_time
    old_flight.seats = flight.seats
    old_flight.price = flight.price

def delete_by_id(id):
    flight = read_by_id(id)
    if flight:
        flights.remove(flight)
