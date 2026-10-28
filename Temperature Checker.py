#Input a temperature in Celsius. Print Cold if it is below 15, Warm if it is from 15 to 30, and Hot if it is above 30.
tem=int(input("Enter the tamperature in celsius:"))
if tem<15:
    print("Cold")
elif tem>=15 and tem<=30:
    print("Waram")
elif tem>30:
    print("Hot")