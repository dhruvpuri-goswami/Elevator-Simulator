class Elevator:
    def __init__(self, no, cur_floor, cur_weight, cur_direction, dir_floor):
        """
        Initialize the elevator with basic details.
        :param no: Elevator number
        :param cur_floor: Current floor of the elevator
        :param cur_weight: Current weight inside the elevator
        :param cur_direction: Current movement direction of the elevator (1: up, -1: down, 0: stationary)
        :param dir_floor: Target floor the elevator is heading towards
        """
        self.no = no
        self.cur_floor = cur_floor
        self.cur_weight = cur_weight
        self.cur_direction = cur_direction
        self.dir_floor = dir_floor
        self.served = [] # Tracks floors that the elevator has served

    def add_service(self, floor =  0):
        """
        Add a floor to the list of served floors if specified.
        :param floor: Floor to add to the service list
        """
        self.served.append(floor)
    
    def show_details(self):
        """
        Return the list of served floors.
        :return: List of floors served
        """
        return self.served

class Requests:
    def __init__(self, persons, weight, direction, floor):
        """
        Initialize a request.
        :param persons: Number of persons making the request
        :param weight: Total weight of the persons
        :param direction: Desired direction of travel
        :param floor: Target floor for the request
        """
        self.persons = persons
        self.weight = weight
        self.direction = direction
        self.floor = floor

def process_scheduling(elevators, requests):
    """
    Process all elevator requests based on the given logic.
    :param elevators: List of Elevator objects
    :param requests: List of Requests objects
    """
    requests = requests[:]  # Make a shallow copy of the requests list to modify it during processing
    
    while requests:  
        for elevator in elevators:  # Iterate over each elevator
            served = False  # Flag to check if a request has been served
            i = 0  # Index for iterating through the requests list
            while i < len(requests):
                request = requests[i]  # Current request being considered
                # Check if elevator can serve the request based on the direction and current floor
                if elevator.cur_direction == request.direction or elevator.cur_direction == 0:
                    # Check if adding the request's weight won't exceed the maximum weight capacity
                    if elevator.cur_weight + request.weight <= 480:
                        # Check if the request can be served based on the current and requested floor
                        if (elevator.cur_direction == 1 and request.floor >= elevator.cur_floor) or (elevator.cur_direction == -1 and request.floor <= elevator.cur_floor) or elevator.cur_direction == 0:
                            served = True  # Set served flag to True as the request will be served
                            elevator.add_service(request.floor)  # Add the floor to the elevator's service list
                            elevator.cur_weight += request.weight  # Update the elevator's current weight
                            # Set the elevator's direction if it's currently idle
                            if elevator.cur_direction == 0:
                                elevator.cur_direction = request.direction
                                elevator.dir_floor = request.floor
                            # Remove the served request from the list
                            requests.pop(i)
                            # Remove other requests for the same floor but opposite direction
                            requests = [r for r in requests if not (r.floor == request.floor and r.direction != request.direction)]
                            # Special condition to add service when the elevator starts at floor 0
                            if elevator.cur_floor == 0 and elevator.dir_floor == request.floor:
                                elevator.add_service()
                            continue  # Continue to the next iteration of the loop without incrementing i
                i += 1  # Increment i if no request is served in this iteration

            # If no requests were served in the current iteration, move the elevator to the direction floor and reset
            if not served:
                elevator.cur_floor = elevator.dir_floor  # Update the elevator's current floor to the direction floor
                elevator.cur_direction = 0  # Reset the elevator's direction
                elevator.cur_weight = 0  # Reset the elevator's weight


if __name__ == "__main__":
    # Initialize elevators and requests
    elevators = [
        Elevator(1, 12, 360, 1, 14),
        Elevator(2, 0, 0, 0, 0),
        Elevator(3, 10, 200, -1, 2)
    ]

    requests = [
        Requests(1, 50, 1, 5),
        Requests(1, 30, -1, 3),
        Requests(2, 110, -1, 11),
        Requests(1, 20, 1, 3),
        Requests(1, 90, -1, 7)
    ]

    process_scheduling(elevators, requests)

    for elevator in elevators:
        print(f"Elevator {elevator.no} served floors: {elevator.show_details()}")
