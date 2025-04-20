from pet import Pet

def test_pet():
    print("Creating pet named Buddy...")
    buddy = Pet("Buddy")

    print("\nInitial Status:")
    buddy.get_status()

    print("\nBuddy eats...")
    buddy.eat()
    buddy.get_status()

    print("\nBuddy plays...")
    buddy.play()
    buddy.get_status()

    print("\nBuddy sleeps...")
    buddy.sleep()
    buddy.get_status()

    print("\nTraining Buddy to roll over...")
    buddy.train("roll over")
    print("Training Buddy to fetch...")
    buddy.train("fetch")

    print("\nTricks learned:")
    buddy.show_tricks()

    print("\nPlaying until energy goes too low:")
    for _ in range(5):
        buddy.play()
        buddy.get_status()

    print("\nTrying to overfeed Buddy:")
    for _ in range(5):
        buddy.eat()
        buddy.get_status()

    print("\nTrying to over-sleep Buddy:")
    for _ in range(3):
        buddy.sleep()
        buddy.get_status()

# Run the test
test_pet()

