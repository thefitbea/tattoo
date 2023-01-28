from datetime import datetime
import pytz
#print(pytz.all_timezones)

#fetching name

u_name=0
u_name=input("Enter Name:")

#fetch timezone
#https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

t_zone=input("Enter Timezone Option:\n Option 1: CST_AMNA\n Option 2 ECT_AME\n Option 3 IST_IND")


if t_zone=="1":
    CST_Tz = pytz.timezone("America/Chicago")
    timeInChicago = datetime.now(CST_Tz)
    currentTimeInCST = timeInChicago.strftime("%H:%M:%S")
    print(u_name+" on "+" at " + currentTimeInCST+" CST")
    # Output: The current time in New York is: 05:36:59

#add function and call it 2morrow

