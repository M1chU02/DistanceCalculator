import math

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in kilometers

    # Convert latitude and longitude to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c

    return distance

def get_coordinate_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

print("Enter coordinates for the first location:")
lat1 = get_coordinate_input("Latitude 1: ")
lon1 = get_coordinate_input("Longitude 1: ")

print("\nEnter coordinates for the second location:")
lat2 = get_coordinate_input("Latitude 2: ")
lon2 = get_coordinate_input("Longitude 2: ")

distance = haversine_distance(lat1, lon1, lat2, lon2)
print(f"\nThe distance between the two points is {distance:.2f} kilometers.")
