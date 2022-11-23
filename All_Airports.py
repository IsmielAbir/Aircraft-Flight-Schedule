import csv
from Airport import Airport
class AllAirports:
    def __init__(self) -> None:
        self.airports = None
        self.load_airport_data('./data/airport.csv')
    
    def load_airport_data(self, file_path):
        airports = {}
        currency_rates = {}
        country_currency = {}
        
        # get currency name<---> rate
        with open('./data/currencyrates.csv', 'r') as file:
            lines = csv.reader(file)
            for line in lines:
                currency_rates[line[1]] = line[2]
                
        file.close()     
                
        # dict country <---> currency name
        
        with open('./data/countrycurrency.csv', 'r') as file:
            lines = csv.reader(file)
            for line in lines:
                country_currency[line[0]] = line[1]
        file.close()
        
        
        # create airport
        with open(file_path, 'r', encoding="utf8") as file:
            lines = csv.reader(file)
            
            for line in lines:
                country = line[3]
                airports[line[4]] = Airport(line[4], line[1], line[2], line[3], line[6], line[7], 0)
                
            self.airports = airports
            for airport in airports.items():
                print(airport)    
                
AllAirports()
    