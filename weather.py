import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    return (f"{temp}{DEGREE_SYMBOL}")

def convert_date(iso_string):
    date = datetime.fromisoformat(iso_string)
    return(date.strftime("%A %d %B %Y"))
    
    

def convert_f_to_c(temp_in_farenheit):
    #temp_in_celcius = round((float(temp_in_farenheit) - 32) * 5/9, 1)
    #return temp_in_celcius

    return(round(float((temp_in_farenheit - 32) / 1.8), 1))


def calculate_mean(weather_data):
    total = 0
    for data in weather_data:
        total = total + float(data)
    return total/len(weather_data)
    

def load_data_from_csv(file):
    weather_data = []
    with open(file) as csv_file:
        results = csv.reader(csv_file)
        count = 0
        for line in results:
            if line == []:
                pass
            
            elif count != 0:
                updated_line = line
                updated_line[1]= int(line[1])
                updated_line[2]= int(line[2])
                weather_data.append(updated_line)
            count += 1
    return weather_data



def find_min(weather_data):
    if len(weather_data) == 0:
        return () 

    min_temp = 999999999999
    min_index = 0 
    index = 0
    for element in weather_data:
        if int(element) <= int(min_temp):
            min_temp = float(element)
            min_index = index 
        index += 1

    return(min_temp, min_index)
  

def find_max(weather_data):
    if len(weather_data) == 0:
        return () 

    max_temp = 0
    max_index = 0 
    index = 0
    for element in weather_data:
        if int(element) >= int(max_temp):
            max_temp = float(element)
            max_index = index 
        index += 1

    return(max_temp, max_index)
    


def generate_summary(weather_data):

    days = len(weather_data)

    min_array = []
    for row in weather_data:
        min_array.append(row[1])
    min_temp, min_index = find_min(min_array)

    max_array = []
    for row in weather_data:
        max_array.append(row[2])
    max_temp, max_index = find_max(max_array)

    min_date = weather_data[min_index][0]
    max_date = weather_data[max_index][0]

    avg_min = calculate_mean(min_array)
    avg_max = calculate_mean(max_array)

    out  = f'{days} Day Overview\n'
    out += f'  The lowest temperature will be {format_temperature(convert_f_to_c(min_temp))}, and will occur on {convert_date(min_date)}.\n' 
    out += f'  The highest temperature will be {format_temperature(convert_f_to_c(max_temp))}, and will occur on {convert_date(max_date)}.\n' 
    out += f'  The average low this week is {format_temperature(convert_f_to_c(avg_min))}.\n'
    out += f'  The average high this week is {format_temperature(convert_f_to_c(avg_max))}.\n'

    return(out)

    
    
    


def generate_daily_summary(weather_data):

    daily_summary = ""
    for day in weather_data:
        date = convert_date(day[0])
        min = format_temperature(convert_f_to_c(day[1]))
        max = format_temperature(convert_f_to_c(day[2]))
        daily_summary += f"---- {date} ----"
        daily_summary += "\n  "
        daily_summary += f"Minimum Temperature: {min}"
        daily_summary += "\n  "
        daily_summary += f"Maximum Temperature: {max}"
        daily_summary += "\n\n"
    return daily_summary
