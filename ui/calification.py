import time

class Calification:

    def __init__(self):
        self.calification: int = None

    
    def calificate(self):

        self.calification = input("Califica tu viaje (1 a 5 estrellas)")

        message = self.send_calification()

        return message


    def send_calification(self):

        time.sleep(0.5)

        return f"Viaje calificado con exito con {self.calification} estrellas"



calification = Calification()

print(calification.calificate())
    
        