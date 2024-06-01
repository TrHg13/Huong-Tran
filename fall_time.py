# Import the required modules
import math
import constants

# Get the height from the user
height = int(input('Height in meters: '))  # Meters from planet

# Calculate and print the time values
if __name__ == '__main__':
    print('Earth:', math.sqrt(2 * height / constants.earth_g), 'seconds')
    print('Mars:', math.sqrt(2 * height / constants.mars_g), 'seconds')
