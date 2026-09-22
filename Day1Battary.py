import psutil
import time
from winotify import Notification

notified = False 

while True:
    battary = psutil.sensors_battery()
    percent = battary.percent
    plugged = battary.power_plugged

    print(f"Battery percentage: {percent}%")
    print(f"Plugged in: {plugged}")

    if percent <= 30 and not plugged:

        if not notified :
            notification = Notification(
            app_id= "Battary Monitor",
            title= "Battary Low" ,
            msg=f"{percent}% Battary remaining!"
            )

            notification.show()
            notified= True


    else:
        notified=False    

    time.sleep(60)    