import time

class Calification:

    def __init__(self):
        self.calification: int = None

    
    def calificate(self):
        while True:
            try:
                rating = int(input("Rate your trip (1 to 5 stars): "))
                if 1 <= rating <= 5:
                    self.calification = rating
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        self.send_calification()



    def send_calification(self):

        time.sleep(0.5)

        print(f"Trip successfully rated with {self.calification} stars")

        return self.calification

    
        