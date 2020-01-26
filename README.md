# Weather-CLine

A basic command line weather interface for python. Provides the current weather for a specific location, with metric support, along with a five day forecast option, with intervals of three hours. In order for it to work, you must have the following:

- Python >3.4
- Pip3 package installer
- The packages: **requests**, **json**, **argparse**, **prettytable**, **colorama**, and **dateutil**.

All you need to do is put the batch/bash file on your system path, and edit the file to replace the "path/to/file" with whatever the path is to the **.py** file. If you have your own Open Weather API Key (they're free!), please use it instead of the provided one, in order to reduce the load on the key. This program has been tested working on both **Windows 10** and **Debian/Ubuntu**. For reference, *--f* adds the forecast, and *--c* converts to metric units.