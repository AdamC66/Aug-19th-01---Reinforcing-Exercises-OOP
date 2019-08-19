# Create a Location class with a name.

# Create a Trip class with a list of Location instances (called stops or destinations or something similar). Define a method that lets you add locations to the trip's list of destinations.

# Make several instances of Locations and add them to an instance of Trip.

# Define a method in the Trip class that iterates through the list of locations and prints something similar to the following:
# "Began trip."
# "Travelled from Toronto to Ottawa."
# "Travelled from Ottawa to Montreal."
# "Travelled from Montreal to Quebec City."
# "Travelled from Quebec City to Halifax."
# "Travelled from Halifax to St. John's."
# "Ended trip."

class Location:
    def __init__(self, name):
        self.name = name

class Trip:
    def __init__(self):
        self.stops = []
    
    def add_stop (self, stop):
        self.stops.append(stop)

    def describe_trip(self):
        print("Began trip")
        for i in range(len(self.stops)-1):
            print(f'Travelled from {self.stops[i].name} to {self.stops[i+1].name}')
        print('Finished trip')


toronto = Location('Toronto')
halifax = Location('Halifax')
montreal = Location('Montreal')
winnipeg = Location('Winnipeg') 

my_trip = Trip()
my_trip.add_stop(toronto)
my_trip.add_stop(halifax)
my_trip.add_stop(montreal)
my_trip.add_stop(winnipeg)
my_trip.describe_trip()