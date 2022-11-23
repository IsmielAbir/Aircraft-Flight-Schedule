from TravelAgent import TravelAgent

def main():
    travel_agent = TravelAgent('Blue Sky')
    trip_info1 = travel_agent.set_trip_one_city_one_way('DAC', 'PRA', '05/04/2026')
    #print('aircraft', trip_info1.aircraft)
    #print('price', trip_info1.cost)
    
    
    trip_cities = ['DUB', 'LHR','ORD', 'SYD', 'JFK']
    trip_info2 = travel_agent.set_trip_multi_city_flexible_round(trip_cities, '05/11/2100')
    
    print('price', trip_info2[1])
    for trip in trip_info2[0]:
        print(trip)
        
    

if __name__ == '__main__':
    main()