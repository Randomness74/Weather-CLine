#!/bin/bash

# remember to add this file to path.
# and chmod this file to 755, running "sudo chmod 755 ./weather.sh" from inside directory of file.
# and change to path to the weather.py file.
if ["$2" = ""]; then
	if ["$3" = ""]; then
		(python3 "/path/to/file/weather-linux.py" "$1") 
	else
		(python3 "/path/to/file/weather-linux.py" "$1" "$3" )
	fi
else 
	if ["$3" = ""]; then
		(python3 "/path/to/file/weather-linux.py" "$1" "$2") 
	else
		(python3 "/path/to/file/weather-linux.py" "$1" "$2" "$3")
	fi
fi
