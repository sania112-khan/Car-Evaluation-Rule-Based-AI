
# Algorithm 2: Weighted Scoring Rule-Based System

def classify_car(buying, maint, doors, persons, lug_boot, safety):

    score = 0

    # Safety score
    if safety == "high":
        score += 30
    elif safety == "med":
        score += 15

    # Passenger capacity score
    if persons == "more":
        score += 25
    elif persons == "4":
        score += 15

    # Buying price score
    if buying == "low":
        score += 15
    elif buying == "med":
        score += 10
    elif buying == "high":
        score += 5

    # Maintenance cost score
    if maint == "low":
        score += 15
    elif maint == "med":
        score += 10
    elif maint == "high":
        score += 5

    # Luggage boot score
    if lug_boot == "big":
        score += 10
    elif lug_boot == "med":
        score += 5

    # Number of doors score
    if doors in ["4", "5more"]:
        score += 5
    elif doors == "3":
        score += 3

    # Final classification
    if score <= 40:
        return "unacc"
    elif score <= 60:
        return "acc"
    elif score <= 80:
        return "good"
    else:
        return "vgood"


# Test the algorithm
if __name__ == "__main__":

    test_cars = [
        ("low", "low", "4", "4", "big", "low"),
        ("low", "med", "4", "2", "small", "high"),
        ("low", "low", "4", "4", "big", "high"),
        ("med", "med", "4", "4", "med", "med"),
        ("high", "high", "2", "4", "small", "high")
    ]

    print("ALGORITHM 2: WEIGHTED SCORING SYSTEM")
    print("-----------------------------------")

    for car in test_cars:

        prediction = classify_car(*car)

        print("Car features:", car)
        print("Predicted classification:", prediction)
        print()
