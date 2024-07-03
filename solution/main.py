import csv
import os
import sys
import math

## Helper functions
def read_csv_file(file_name):
    cities_data = []

    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            start = row["Start"]
            start_lat = float(row["StartLatitude"])
            start_lon = float(row["StartLongitude"])

            end = row["End"]
            end_lat = float(row["EndLatitude"])
            end_lon = float(row["EndLongitude"])

            distance = int(row["Distance"])

            cities_data.append((start, start_lat,
                               start_lon,  end, end_lat, end_lon, distance))

    return cities_data

def find_lat_lon(city, data):
    for start, start_lat, start_lon, end, end_lat, end_lon, _ in data:
        if city == start:
            return start_lat, start_lon
        elif city == end:
            return end_lat, end_lon
    return None, None

def heuristic_func(current_city, goal_city, data):
    current_lat, current_lon = find_lat_lon(current_city, data)
    goal_lat, goal_lon = find_lat_lon(goal_city, data)

    R = 6371.0

    lat1 = math.radians(current_lat)
    lon1 = math.radians(current_lon)
    lat2 = math.radians(goal_lat)
    lon2 = math.radians(goal_lon)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

def index_of_city(city, data):
    for i in range(len(data)):
        #print(data[i][0])
        if city == data[i][0]:
            return i
    return -1
def get_neighbors(city, data):
    neighbors = []
    for start, _, _, end, _, _, _ in data:
        if start == city:
            neighbors.append(end)
    return neighbors

def distance_between(city1, city2, data):
    for start, _, _, end, _, _, distance in data:
        if start == city1 and end == city2:
            return distance
    return None

def find_path_astar(start_city, end_city, data):
    open_set = set([start_city])
    closed_set = set()

    g = {start_city: 0}
    h = {start_city: heuristic_func(start_city, end_city, data)}
    f = {start_city: h[start_city]}

    parent_map = {start_city: None}

    while open_set:
        current_city = min(open_set, key=lambda city: f[city])

        if current_city == end_city:
            path = []
            while current_city:
                path.append(current_city)
                current_city = parent_map[current_city]
            return path[::-1]

        open_set.remove(current_city)
        closed_set.add(current_city)

        for neighbor in get_neighbors(current_city, data):
            if neighbor in closed_set:
                continue

            tentative_g_score = g[current_city] + distance_between(current_city, neighbor, data)

            if neighbor not in open_set:
                open_set.add(neighbor)
            elif tentative_g_score >= g.get(neighbor, float('inf')):
                continue

            parent_map[neighbor] = current_city
            g[neighbor] = tentative_g_score
            h[neighbor] = heuristic_func(neighbor, end_city, data)
            f[neighbor] = g[neighbor] + h[neighbor]

    return None



# Make sure to pass the 'data' variable to the heuristic_func when calling it
if __name__ == '__main__':

    arguments_count = len(sys.argv)
    if arguments_count < 4:
        print("Please provide the path to the csv file, the start city, and the end city.\
              \nExample: python main.py sample_routes/us.csv \"New York\" \"Los Angeles\"\
              \nDon't foget to add \" in the city name has spaces like New York or Los Angeles" )
        sys.exit(1)

    file_name = sys.argv[1]
    # print("Reading file: ", file_name)
    if not os.path.isfile(file_name):
        print("File does not exist: ", file_name)
        sys.exit(1)

    data = read_csv_file(file_name)

    for start_city, start_lat, start_lon, end_city, end_lat, end_lon, distance in data:
        # print(start_city, start_lat, start_lon,end_city, end_lat, end_lon, distance)
        pass
    start_city = sys.argv[2]
    end_city = sys.argv[3]

    if index_of_city(start_city, data) < 0:
        print("Start city not found in the data: ", start_city)
        sys.exit(1)
    if index_of_city(end_city, data) < 0:
        print("End city not found in the data: ", end_city)
        sys.exit(1)

    path = find_path_astar(start_city, end_city, data)

    print(path)
