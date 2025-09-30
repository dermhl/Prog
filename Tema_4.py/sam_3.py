from datetime import datetime
import time

for i in range(5):
    now = datetime.now() #получить текущее время
    print(now.strftime("%H:%M:%S")) #вывод в формате чч:мм:сс
    time.sleep(1) #усыпить на 1 секунду