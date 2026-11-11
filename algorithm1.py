
# Algorithm 1: IF-THEN Rule-Based System

def classify_car(buying, maint, doors, persons, lug_boot, safety):

    # Rule 1: Low safety means unacceptable
    if safety == "low":
        return "unacc"

    # Rule 2: Cars for only two people are unacceptable
    elif persons == "2":
        return "unacc"

    # Rule 3: Conditions for a very good car
    elif (safety == "high" and
          persons in ["4", "more"] and
          buying == "low" and
          maint == "low" and
          lug_boot == "big"):
        return "vgood"

    # Rule 4: Conditions for a good car
    elif (safety == "high" and
          persons in ["4", "more"] and
          buying in ["low", "med"] and
          lug_boot in ["med", "big"]):
        return "good"

    # Rule 5: Conditions for an acceptable car
    elif safety == "med" and persons in ["4", "more"]:
        return "acc"

    # Default rule
    else:
        return "unacc"


# Test the algorithm using sample cars

if __name__ == "__main__":

    test_cars = [
        ("low", "low", "4", "4", "big", "low"),
        ("low", "med", "4", "2", "small", "high"),
        ("low", "low", "4", "4", "big", "high"),
        ("med", "med", "4", "4", "med", "med"),
        ("high", "high", "2", "4", "small", "high")
    ]

    print("ALGORITHM 1: IF-THEN RULE SYSTEM")
    print("--------------------------------")

    for car in test_cars:

        buying, maint, doors, persons, lug_boot, safety = car

        prediction = classify_car(
            buying, maint, doors, persons, lug_boot, safety
        )

        print("Car features:", car)
        print("Predicted classification:", prediction)
        print()
