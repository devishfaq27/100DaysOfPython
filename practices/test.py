import math


def compute_HRV(interval1: float, interval2: float, interval3: float) -> float:
    return math.sqrt(((interval1 - interval2) ** 2 + (interval2 - interval3) ** 2) / 2)

def temperature_is_fever(temperature: float, site: str) -> bool:
    return (site == 'O' and temperature >= 37.8) or (site == 'U' and temperature >= 37.2)


def has_fever() -> bool:
    temperature = float(input("Enter your temperature (°C) : "))
    site = input("Was the temperature measured Orally (O) or Underarm (U)? (enter O or U): ").upper()

    return temperature_is_fever(temperature, site)


def has_nausea() -> bool:
    nausea = input("Are you experiencing nausea? (enter y or n): ").lower()
    return nausea == 'y'


def has_low_HRV() -> bool:
    print("Please enter 3 heartbeat intervals in ms...")
    interval1 = float(input("Enter first interval: "))
    interval2 = float(input("Enter second interval: "))
    interval3 = float(input("Enter third interval: "))

    hrv = compute_HRV(interval1, interval2, interval3)
    return hrv < 50


def has_high_cortisol() -> bool:
    cortisol_level = float(input("Enter cortisol level in mcg/dL: "))
    return cortisol_level < 50


def main():
    if has_fever():
        if has_nausea():
            diagnosis = "Flu"
        else:
            diagnosis = "Infection"

    else:
        if has_low_HRV():
            if has_high_cortisol():
                diagnosis = "Stress"
            else:
                diagnosis = "healthy"

    print(f"diagnosis: {diagnosis}")


main()
