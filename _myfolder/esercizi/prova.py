from random import choice 
import webbrowser
from datetime import datetime


def hourResponse():
    print(f"sono le ore {datetime.now().strftime("%H e %M")}")


hourResponse()