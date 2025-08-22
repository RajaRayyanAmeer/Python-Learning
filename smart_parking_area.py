# A simple vehicle class to store basic information about each car, bike, or truck
class Vehicle:
    def __init__(self, plate, vtype, special=False):
        self.plate = plate  # License plate number
        self.vtype = vtype  # Type: bike, car, or truck
        self.special = special  # Whether it needs special parking (EV, VIP, etc.)


# Represents each individual parking spot in our system
class ParkingSpot:
    def __init__(self, number, area, floor, spot_type, reserved=False):
        self.number = number  # Unique spot number
        self.area = area  # Which parking area/zone (North, South)
        self.floor = floor  # Which floor the spot is on
        self.spot_type = spot_type  # What vehicle type fits here
        self.reserved = reserved  # If it's a special reserved spot
        self.taken = False  # Whether currently occupied
        self.current_vehicle = None  # Vehicle parked here (if any)


# The main brain of our parking system that manages everything
class ParkingManager:
    def __init__(self):
        # All parking spots we have
        self.all_spots = []

        # Available spots organized by vehicle type
        self.open_spots = {'bike': [], 'car': [], 'truck': []}

        # Currently taken spots with their vehicles
        self.taken_spots = {}

        # For future: vehicles waiting when parking is full
        self.waiting_list = []

    # Sets up our parking structure based on the building layout
    def setup_parking(self, areas):
        spot_counter = 1  # Start numbering spots from 1

        # Create spots for each area, floor, and spot position
        for area_name, details in areas.items():
            for floor_num in range(1, details['floors'] + 1):
                for i in range(details['spots_per_floor']):
                    # Determine spot type and if it's reserved
                    s_type = details['spot_types'][i]
                    is_reserved = i in details['reserved_spots']

                    # Create the new parking spot
                    new_spot = ParkingSpot(
                        spot_counter, area_name, floor_num, s_type, is_reserved
                    )

                    # Add to our tracking lists
                    self.all_spots.append(new_spot)
                    self.open_spots[s_type].append(new_spot)
                    spot_counter += 1

    # Parks a new vehicle in the appropriate spot
    def add_vehicle(self, vehicle):
        # First check for special vehicles (like electric cars)
        if vehicle.special:
            for spot in self.open_spots[vehicle.vtype]:
                if spot.reserved:
                    return self._take_spot(vehicle, spot)

        # For regular vehicles or if no special spots left
        if self.open_spots[vehicle.vtype]:
            return self._take_spot(vehicle, self.open_spots[vehicle.vtype][0])

        # If we get here, no spots are available
        return None

    # Helper method that actually assigns a vehicle to a spot
    def _take_spot(self, vehicle, spot):
        spot.taken = True
        spot.current_vehicle = vehicle
        self.open_spots[vehicle.vtype].remove(spot)
        self.taken_spots[vehicle.plate] = spot
        return spot

    # When a vehicle leaves, free up its spot
    def remove_vehicle(self, plate):
        if plate in self.taken_spots:
            spot = self.taken_spots[plate]
            spot.taken = False
            spot.current_vehicle = None
            self.open_spots[spot.spot_type].append(spot)
            del self.taken_spots[plate]
            return True
        return False

    # Shows the current parking situation
    def show_parking(self):
        print("\nParking Overview:")
        print(f"Total spots: {len(self.all_spots)}")
        print(f"Occupied spots: {len(self.taken_spots)}")

        # Show availability by vehicle type
        for vtype in self.open_spots:
            print(f"Open {vtype} spots: {len(self.open_spots[vtype])}")

        # List all parked vehicles
        print("\nVehicles parked:")
        for plate, spot in self.taken_spots.items():
            print(f"Area {spot.area}, Floor {spot.floor}, Spot {spot.number}: {plate}")

    # Shows spots reserved for electric vehicles
    def show_electric_spots(self):
        print("\nAvailable electric spots:")
        for spot in self.open_spots['car']:
            if spot.reserved:
                print(f"Area {spot.area}, Floor {spot.floor}, Spot {spot.number}")

    # Displays all special vehicles currently parked
    def show_special_vehicles(self):
        print("\nSpecial vehicles parked:")
        for plate, spot in self.taken_spots.items():
            if spot.current_vehicle and spot.current_vehicle.special:
                print(f"Area {spot.area}, Floor {spot.floor}, Spot {spot.number}: {plate}")


# The main interface that people interact with
def run_system():
    # Create our parking manager
    manager = ParkingManager()

    # Define our parking garage layout
    parking_areas = {
        'North': {
            'floors': 2,
            'spots_per_floor': 5,
            'spot_types': ['car', 'car', 'truck', 'bike', 'car'],
            'reserved_spots': [0, 4]  # First and last spots are special
        },
        'South': {
            'floors': 1,
            'spots_per_floor': 3,
            'spot_types': ['car', 'truck', 'bike'],
            'reserved_spots': [0]  # First spot is special
        }
    }

    # Set up the parking structure
    manager.setup_parking(parking_areas)

    # Main menu loop
    while True:
        print("\nCity Parking System")
        print("1. Park vehicle")
        print("2. Remove vehicle")
        print("3. View parking status")
        print("4. Check electric spots")
        print("5. View special vehicles")
        print("6. Quit")

        action = input("What would you like to do? ")

        # Park a new vehicle
        if action == '1':
            plate = input("Vehicle plate number: ")
            vtype = input("Vehicle type (bike/car/truck): ").lower()

            # Make sure they enter a valid vehicle type
            while vtype not in ['bike', 'car', 'truck']:
                print("Please enter bike, car, or truck")
                vtype = input("Vehicle type: ").lower()

            # Check if it's a special vehicle
            special = input("Special vehicle? (y/n): ").lower() == 'y'
            new_vehicle = Vehicle(plate, vtype, special)

            # Try to park the vehicle
            assigned_spot = manager.add_vehicle(new_vehicle)
            if assigned_spot:
                print(f"Park at: Area {assigned_spot.area}, Floor {assigned_spot.floor}, Spot {assigned_spot.number}")
            else:
                print("No spots available for this vehicle")

        # Remove a parked vehicle
        elif action == '2':
            plate = input("Enter plate to remove: ")
            if manager.remove_vehicle(plate):
                print("Vehicle removed")
            else:
                print("Vehicle not found")

        # Show current parking status
        elif action == '3':
            manager.show_parking()

        # Show available electric spots
        elif action == '4':
            manager.show_electric_spots()

        # Show special vehicles parked
        elif action == '5':
            manager.show_special_vehicles()

        # Exit the system
        elif action == '6':
            print("Goodbye!")
            break

        # Handle invalid choices
        else:
            print("Please choose 1-6")


# Start the parking system when we run this file
if __name__ == "__main__":
    run_system()