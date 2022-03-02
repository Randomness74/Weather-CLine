# Weather-CLine

A basic command line weather interface for Python. It provides the current weather for a specific location with support for metric units (Celsius, centimeters) and a five day forecast. The program requirements are the following:

- Python >3.4
- Pip3 package installer
- The packages: **requests**, **json**, **argparse**, **prettytable**, **colorama**, and **dateutil**.

First the batch/bash files must be added to the system path, and the "path/to/file" should be replaced with the path to the **.py** file. If you have your own Open Weather API Key (they're free!), please use it instead of the provided one to reduce load on the provided key. This program has been tested on both **Windows 10** and **Ubuntu 16**.

## Documentation

To find the current weather for a particular location, run:
```
weather *insert location here* [--c] [--f]
```
Adding the --f and --c flags adds the five day forecast and metric units respectively.
