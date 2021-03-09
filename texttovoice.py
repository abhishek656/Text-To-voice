# today we will do one mini project 
# step 1:  install module pywin32 
from win32com.client import Dispatch


    
if __name__ == "__main__":
    text = Dispatch(("SAPI.Spvoice"))
    text.speak("" )


    