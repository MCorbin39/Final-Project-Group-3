# get input from user
def userInput():
    modes = ["Popcorn", "ReheatPizza", "Defrost", "Reheat", "Start", "Stop", "Open", "Close", "Manual"]
    timeDict = {"Popcorn": 180, "ReheatPizza": 40, "Reheat": 30, "Start": 30}  
    powerDict = {"Popcorn":"High", "ReheatPizza":"Medium", "Reheat":"Medium", "Start":"High"}

    while True:

        user_input = input("Select a Mode: \nPopcorn\nReheatPizza\nDefrost\nReheat\nStart\nStop\nOpen\nClose\nManual\n").strip()
        if user_input in modes:
            print("you chose: ", user_input)   
            if user_input == "Manual":
                cookTime = int(input("Enter the time in seconds: "))
                power = input("Enter the power level (Low, Medium, High): ")
            else:
                cookTime = timeDict.get(user_input, "Something went wrong with time")
                power = powerDict.get(user_input, "Something went wrong with power")
            print(f"Time: {cookTime} seconds, Power: {power}")
            return cookTime, power
        else:
             print("That number is not a valid mode. Try again.")
    





userInput()
