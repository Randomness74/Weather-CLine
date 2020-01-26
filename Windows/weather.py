import requests, json, argparse, prettytable
from colorama import Fore, Style, init, Back
from datetime import datetime
from dateutil import tz

# the below line is for windows only. for linux and mac users, please remove the below line.
init(convert = True)
def current(city_name, c):
    advisory = []
    """ IF YOU HAVE YOUR OWN OPENWEATHER API KEY, PLEASE REPLACED APPID WITH YOUR API KEY 
        Thank you for doing this, as this reduces load on the api key.                      """
    complete_url = 'http://api.openweathermap.org/data/2.5/weather?appid=f538bf262cebc1969a94e4de6c0974e5&q=' + city_name
    response = requests.get(complete_url) 
    x = response.json()
    try:
        y = x['main']
        z = x['weather'][0]
        a = x['wind']
        b = x['sys']
    except KeyError:    # checks for error
        return Fore.WHITE + Back.RED + Style.BRIGHT + "That city does not exist!" + Style.RESET_ALL
    else:               # else go and add all options
        current = datetime.fromtimestamp(int(x['dt']), tz.tzlocal())
        current = current.strftime('%H:%M:%S')
        title = Fore.RED + Style.BRIGHT +  'Weather in ' + x['name'] + ', ' + b['country'] + ' at ' + str(current) + '\n'
        if int(int(y['temp'] - 273)*1.8 + 32) > 100:
            advisory.append('HEAT ADVISORY\n')
        temp_f = Fore.YELLOW + Style.DIM + 'Current Temperature: ' + Fore.BLUE + str(int(int(y['temp'] - 273)*1.8 + 32)) + '°F\n'
        temp_c = Fore.YELLOW + Style.BRIGHT + 'Current Temperature: ' + Fore.RED + str(int(y['temp'] - 273)) + '°C\n'
        humidity = Fore.GREEN + Style.BRIGHT + 'Humidity: ' + str(y['humidity']) + '%\n'
        pressure = Fore.WHITE + Style.DIM + 'Pressure: ' + str(y['pressure']) + ' mb\n'
        cloud = Fore.CYAN + 'Weather: ' + z['description'] + '\n'
        try:
            wind_speed = Fore.MAGENTA + Style.BRIGHT + 'Wind: ' + str(a['speed']) + ' mph at ' + str(a['deg']) + '° \n'
        except Exception:
            wind_speed = Fore.MAGENTA + Style.BRIGHT + 'Wind: ' + str(a['speed']) + ' mph\n'
        if c is True:
            return title + temp_c + humidity + pressure + cloud + wind_speed
        elif c is False:
            return title + temp_f + humidity + pressure + cloud + wind_speed
def forecast(city_name, c):
    """ IF YOU HAVE YOUR OWN OPENWEATHER API KEY, PLEASE REPLACED APPID WITH YOUR API KEY 
        Thank you for doing this, as this reduces load on the api key.                      """
    complete_url = 'http://api.openweathermap.org/data/2.5/forecast?appid=f538bf262cebc1969a94e4de6c0974e5&q=' + city_name
    response = requests.get(complete_url) 
    raw_json = response.json()
    days = 'lol'
    # grabs raw json request
    try:
        main = raw_json['list']
        info = raw_json['city']
    except Exception:
        print(Fore.WHITE + Back.RED + Style.BRIGHT + "That city does not exist!")
    # gets dateranges, by skipping days and organizing them properly.
    for attempt in range(0, 8):
        title = []
        temp_f = []
        temp_c = []
        humidity = []
        pressure = []
        cloud = []
        for num in range(attempt, 39, 8):
            try:
                x = main[num]
                y = x['main']
                z = x['weather'][0]
                a = x['wind']
                b = x['sys'] 
            except Exception:
                break
            else:
                # fixing broken time problems
                current = datetime.fromtimestamp(int(x['dt']), tz.tzlocal())
                current = current.strftime('%H:%M %m/%d/%Y')
                title.append(Fore.RED + Style.BRIGHT + str(current))
                temp_f.append(Fore.YELLOW + Style.DIM + 'Temperature: ' + Fore.BLUE + str(int(int(y['temp'] - 273)*1.8 + 32)) + '°F')
                temp_c.append(Fore.YELLOW + Style.BRIGHT + 'Current Temperature: ' + Fore.RED + str(int(y['temp'] - 273)) + '°C')
                humidity.append(Fore.GREEN + Style.BRIGHT + 'Humidity: ' + str(y['humidity']) + '%')
                pressure.append(Fore.WHITE + Style.DIM + 'Pressure: ' + str(y['pressure']) + ' mb')
                cloud.append(Fore.CYAN + 'Weather: ' + z['description'])
        # creates table
        table = prettytable.PrettyTable(title)
        if c is True:
            table.add_row(temp_c)
        elif c is False:
            table.add_row(temp_f)
        table.add_row(humidity)
        table.add_row(pressure)
        table.add_row(cloud)
        print(table)

parser = argparse.ArgumentParser()                                      
# adds argument parsing
parser.add_argument('city1', help="first city inputted", type=str)
parser.add_argument('--c', '--celsius', '-c', help = 'celsius/metric', action = 'store_true')
parser.add_argument('--f', '--forecast', '-f', help = 'forecast', action = 'store_true')
args = parser.parse_args()
# figures out flags.
if args.city1 == 'here' or args.city1 == '':
    # put your current city here, for convenience
    args.city1 = 'Manhattan'
if args.c:
    print(Fore.RED + current(args.city1, True))
    if args.f:
        forecast(args.city1, True)
else:
    print(Fore.BLUE + current(args.city1, False))
    if args.f:
        forecast(args.city1, False)