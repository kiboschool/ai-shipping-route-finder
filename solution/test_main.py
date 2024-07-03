import unittest
import main

class TestFindPathAStar(unittest.TestCase):
    
    def setUp(self):
        self.data = main.read_csv_file("sample_routes/us.csv")

    def test_ny_to_la(self):
        result = main.find_path_astar("New York", "Los Angeles", self.data)
        expected = ['New York', 'Chicago', 'Denver', 'Los Angeles']
        self.assertEqual(result, expected)

    def test_boston_to_seattle(self):
        result = main.find_path_astar("Boston", "Seattle", self.data)
        expected = ['Boston', 'Chicago', 'Denver' , 'Seattle']
        self.assertEqual(result, expected)

    def test_denver_to_san_francisco(self):
        result = main.find_path_astar("Denver", "San Francisco", self.data)
        expected = ['Denver', 'Seattle', 'Chicago', 'San Francisco']
        self.assertEqual(result, expected)

    def test_new_york_to_san_francisco(self):
        result = main.find_path_astar("New York", "San Francisco", self.data)
        expected = ['New York', 'Chicago', 'San Francisco']
        self.assertEqual(result, expected)

    def test_new_york_to_houston(self):
        result = main.find_path_astar("New York", "Houston", self.data)
        expected = ['New York', 'Miami', 'Houston']
        self.assertEqual(result, expected)

    # Additional test cases can be added here for other city pairs

class TestFindPathAStarNigeria(unittest.TestCase):
    def setUp(self):
        self.data = main.read_csv_file("sample_routes/nigeria.csv")

    def test_lagos_to_abuja(self):
        result = main.find_path_astar("Lagos", "Abuja", self.data)
        expected = ['Lagos', 'Abuja']
        self.assertEqual(result, expected)

    def test_kano_to_port_harcourt(self):
        result = main.find_path_astar("Kano", "Port Harcourt", self.data)
        expected = ['Kano', 'Port Harcourt']
        self.assertEqual(result, expected)

    def test_ibadan_to_kaduna(self):
        result = main.find_path_astar("Ibadan", "Kaduna", self.data)
        expected = ['Ibadan', 'Kaduna']
        self.assertEqual(result, expected)

    def test_enugu_to_calabar(self):
        result = main.find_path_astar("Enugu", "Calabar", self.data)
        expected = ['Enugu', 'Calabar']
        self.assertEqual(result, expected)

class TestFindPathAStarRomania(unittest.TestCase):
    def setUp(self):
        self.data = main.read_csv_file("sample_routes/romania.csv")

    def test_arad_to_mehadia(self):
        result = main.find_path_astar("Arad", "Mehadia", self.data)
        expected = ['Arad', 'Timisoara', 'Lugoj', 'Mehadia']
        self.assertEqual(result, expected)

    def test_arad_to_drobeta_turnu_severin(self):
        result = main.find_path_astar("Arad", "Drobeta-Turnu Severin", self.data)
        expected = ['Arad', 'Timisoara', 'Lugoj', 'Mehadia', 'Drobeta-Turnu Severin']
        self.assertEqual(result, expected)

    def test_arad_to_craiova(self):
        result = main.find_path_astar("Arad", "Craiova", self.data)
        expected = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Craiova']
        self.assertEqual(result, expected)

    def test_arad_to_pitesti(self):
        result = main.find_path_astar("Arad", "Pitesti", self.data)
        expected = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti']
        self.assertEqual(result, expected)

    def test_arad_to_bucharest(self):
        result = main.find_path_astar("Arad", "Bucharest", self.data)
        expected = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
