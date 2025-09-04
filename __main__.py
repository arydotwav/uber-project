from .ui.trip_ui import TripUi
from .auth.auth_manager import AuthManager

def main():
   auth_manager = AuthManager()
   ui = TripUi(auth_manager)
   ui.start_trip()

if __name__ == "__main__":
    main()



##va para el trip ui, el trip_ui es el que tiene que heredar el controller.