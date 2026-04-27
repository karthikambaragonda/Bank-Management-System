vehicles = {
    'economy': 10,
    'premium': 18,
    'suv': 25
}
def calculate_fare(km, vehicle_type, hour):
    if vehicle_type not in vehicles:
        print("\nService Not Available\n")
        return
    base_fare = km * vehicles[vehicle_type]
    if 17 <= hour and hour<= 20:
        final_price = base_fare * 1.5
    else:
        final_price = base_fare
    return final_price
print("\n------------------FareCalc Ride Estimate------------------")
try:
    ride_distance = float(input("Enter distance (km): "))
    vehicle_type = input("Enter vehicle type (Economy/Premium/SUV): ").lower()
    ride_time = int(input("Enter hour (0-23): "))
    if ride_time<=0 or ride_time>23:
        print("Invalid Hour")
    else:
        fare = calculate_fare(ride_distance, vehicle_type, ride_time)
        if fare is not None:
            print("\n-------------Price Receipt------------------")
            print("Distance     :", ride_distance, "km")
            print("Vehicle Type :", vehicle_type)
            print("Ride Time    :", ride_time)
            print("Total Fare   : ₹", fare)
            print("--------------------------------------------")
except ValueError:
    print("Enter valid values")
    