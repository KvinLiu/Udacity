def jungle_animal(animal, my_speed):
    # YOUR CODE HERE
    if "zebra, cheetah".find(animal) == 7:
        if my_speed > 115:
            r = "Run!"
        else:
            r = "Stay calm and wait!"
    elif animal == "zebra":
        r = "Try to ride a zebra!"
    else:
        r = "Introduce yourself!"
    print r
