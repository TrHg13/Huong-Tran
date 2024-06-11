# measurements.py

# Import the required modules
import math
from constants import earth_g, mars_g

# Input: Height in meters
height = int(input('Height in meters: '))

# Main code to calculate and print the time to fall from the given height on Earth and Mars
if __name__ == '__main__':
    print('Earth:', math.sqrt(2 * height / earth_g), 'seconds')
    print('Mars:', math.sqrt(2 * height / mars_g), 'seconds')
