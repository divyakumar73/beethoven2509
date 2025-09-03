from flight_manager import create_flight, read_all, read_by_id, update, delete_by_id
from flight import Flight

def menu():
    message = '''
The menu choices are
1 - Create Flight
2 - Read All Flights
3 - Read By Id
4 - Update Flight
5 - Delete Flight
6 - Exit / Logout
Your choice: '''
    choice = int(input(message))

    if choice == 1:
        flight_number = input('Flight Number: ')
        airline = input('Airline: ')
        source = input('Source: ')
        destination = input('Destination: ')
        departure_time = input('Departure Time: ')
        arrival_time = input('Arrival Time: ')
        seats = int(input('Seats Available: '))
        price = float(input('Price: '))

        flight = Flight(-1, flight_number, airline, source, destination, departure_time, arrival_time, seats, price)
        create_flight(flight)
        print('Flight created successfully.')

    elif choice == 2:
        flights = read_all()
        print('Flights:')
        for flight in flights:
            print(flight)

    elif choice == 3:
        id = int(input('Flight ID: '))
        flight = read_by_id(id)
        if flight is None:
            print('Flight not found')
        else:
            print(flight)

    elif choice == 4:
        id = int(input('Flight ID: '))
        old_flight = read_by_id(id)
        if old_flight is None:
            print('Flight Not Found.')
        else:
            print(old_flight)
            flight_number = input('Flight Number: ')
            airline = input('Airline: ')
            source = input('Source: ')
            destination = input('Destination: ')
            departure_time = input('Departure Time: ')
            arrival_time = input('Arrival Time: ')
            seats = int(input('Seats Available: '))
            price = float(input('Price: '))
            new_flight = Flight(id, flight_number, airline, source, destination, departure_time, arrival_time, seats, price)
            update(new_flight)
            print('Flight Updated Successfully.')

    elif choice == 5:
        id = int(input('Flight ID: '))
        old_flight = read_by_id(id)
        if old_flight is None:
            print('Flight Not Found.')
        else:
            print(old_flight)
            if input('Are you sure to delete (y/n)? ') == 'y':
                delete_by_id(id)
                print('Flight Deleted Successfully')
    return choice

def menus():
    print('Flight Management App')
    choice = menu()
    while choice != 6:
        choice = menu()
    print('Thank you for using the app')

menus()
