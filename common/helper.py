from datetime import datetime

def getDatetimeFormat():
        ahora = datetime.now()
        return ahora.strftime("%Y-%m-%d %H:%M:%S")
