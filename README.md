# Shipping Route Finder
In this assignment, you will implement a shipping route finder program that utilizes the A* search algorithm to determine the optimal path between two shipping points.


## Inputs:
You will be provided with a simplified map of cities. Each shipping route connects two points (cities or ports) and has an associated cost (distance).

## Example of the input data:

```python
Start,StartLatitude,StartLongitude,End,EndLatitude,EndLongitude,Distance
New York,40.7128,-74.0060,Boston,42.3601,-71.0589,215
New York,40.7128,-74.0060,Chicago,41.8781,-87.6298,790
New York,40.7128,-74.0060,Miami,25.7617,-80.1918,1305
Boston,42.3601,-71.0589,Chicago,41.8781,-87.6298,983
Boston,42.3601,-71.0589,San Francisco,37.7749,-122.4194,2704
Chicago,41.8781,-87.6298,Denver,39.7392,-104.9903,1003
Chicago,41.8781,-87.6298,San Francisco,37.7749,-122.4194,2134
Denver,39.7392,-104.9903,Los Angeles,34.0522,-118.2437,1015
Denver,39.7392,-104.9903,Seattle,47.6062,-122.3321,1307
San Francisco,37.7749,-122.4194,Los Angeles,34.0522,-118.2437,381
Los Angeles,34.0522,-118.2437,Seattle,47.6062,-122.3321,1151
Los Angeles,34.0522,-118.2437,Miami,25.7617,-80.1918,2734
Miami,25.7617,-80.1918,Houston,29.7604,-95.3698,1183
Houston,29.7604,-95.3698,New Orleans,29.9511,-90.0715,348
New Orleans,29.9511,-90.0715,Miami,25.7617,-80.1918,732
Houston,29.7604,-95.3698,Chicago,41.8781,-87.6298,1085
Miami,25.7617,-80.1918,Atlanta,33.7490,-84.3880,661
Atlanta,33.7490,-84.3880,New York,40.7128,-74.0060,936
New Orleans,29.9511,-90.0715,Atlanta,33.7490,-84.3880,462
Seattle,47.6062,-122.3321,Chicago,41.8781,-87.6298,2064
Seattle,47.6062,-122.3321,Miami,25.7617,-80.1918,3258
San Francisco,37.7749,-122.4194,Seattle,47.6062,-122.3321,808
```

The input data is provided in a CSV file. The code for reading the CSV is provided. Your task is to implement the A* search algorithm to find the optimal path from a given starting city to a destination city.

# Your task:
Implement the `function find_path_astar` in the main.py file.

The find_path_astar method should return a Python list of the city names that represent the path. For example, if the start city is New York and the destination city is Los Angeles, the method should return ['New York', 'Chicago', 'Denver', 'Los Angeles'].

**Don't** change the `function find_path_astar` function name because this name is being used by the test files. Changing it will make the test cases fail.

# Running your code:
To run your code locally and try different sample files, use the following command:

`python3 main.py sample_routes/us.csv "New York" "Los Angeles"`

The second command line argument, sample_routes/us.csv, is the input file name. You can use different files provided in the sample_routes directory to test your code.

# Testing your code
To run the tests, simply execute the test_main.py file like this: `python3 test_main.py`.

# Rubric
- All test cases pass, demonstrating a correct implementation of the A* search algorithm. **[100%]**
- Partial Test Cases Passed: The score is based on the number of test cases passed.
