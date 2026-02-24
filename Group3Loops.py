# -----------------------------
# SENSOR LOOP
# -----------------------------
def Sensor_Loop():
    global SensorCount

    while True:
        print("\n--- Sensor Loop Running ---")

        if not IsDoorClosed:
            print("Door is open.")
            SensorCount += 1

        elif Temperature > 100:
            print("Temperature above 100°C.")
            SensorCount += 1

        elif Humidity > 60:
            print("Humidity exceeds 60%.")
            SensorCount += 1

        elif Watts > 1500:
            print("Watt value exceeds 1500.")
            SensorCount += 1

        else:
            print("All sensors normal.")
            break

        print("Increase Sensor +1 =", SensorCount)
        break


# -----------------------------
# START LOOP
# -----------------------------
while True:

    print("\n--- Start Loop ---")

    # Simulated sensor read
    Sensors = [IsDoorClosed, Temperature, Humidity, Watts]

    # Check if sensors are valid
    if IsDoorClosed and Time > 0:
        print("Sensors OK. Start cooking.")
        Cooking = True

        # Start cooking
        while Cooking and Time > 0:

            if IsPaused:
                print("Cooking paused.")
                break

            print(f"Cooking... Time left: {Time} seconds")
            Time -= 1

            # Run sensor check during cooking
            Sensor_Loop()

        if Time <= 0:
            print("Cooking complete.")
            break

    else:
        print("Cannot start. Check door or time.")
        break


print("\n--- End ---")