from datetime import datetime

def obtenir_temps():
    return "Helloo ! Il est {}.".format(datetime.now().strftime("%H:%M:%S"))