print(" *** Wind classification ***")

wind_speed = float(input("Enter wind speed (km/h) : "))

if wind_speed >= 0 and wind_speed <= 51.99:
    print("Wind classification is Breeze.")
elif wind_speed >= 52.00 and wind_speed <= 55.99:
    print("Wind classification is Depression.")
elif wind_speed >= 56.00 and  wind_speed <= 101.99:
    print("Wind classification is Tropical Storm.")
elif wind_speed >= 102.00 and wind_speed <= 208.99:
    print("Wind classification is Typhoon.")
elif wind_speed >= 209:
    print("Wind classification is Super Typhoon.")
else:
    print("!!!Wrong value can't classify.")


