from datetime import datetime

current_time = datetime.now().hour
if 7 < current_time < 10:
    print("wake up")
elif 7 >= current_time >= 0:
    print("yet sleeping")
else:
    print("hard work")

today = datetime.now().weekday()
if today in [1, 2, 3, 4, 5]:
    print("working day")
else:
    print("weekend")