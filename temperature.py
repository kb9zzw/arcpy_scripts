#Name: temperature.py
#Purpose: Converts temperature
#Author: Jon Burroughs (jdburrou)
#Date: 1/25/2012
#Usage:  temperature.py [temperature] {scale}
#Example:  temperature.py 32 F

# Function to convert fahrenheit to celsius
def f2c(temp_f) :
    return 5.0 / 9.0 * (temp_f - 32)

# Function to convert celsius to fahrenheit
def c2f(temp_c) :
    return 1.8 * temp_c + 32

# Main program
if __name__ == '__main__' :
    # Get temperature value
    temp = float(sys.argv[1])
    
    # Check if scale is provided
    if (len(sys.argv) == 3 ) :
        scale = sys.argv[2].upper()
    else :
        print "Since you didn't specify a scale, I'm assuming F to C."
        scale = 'F'

    # Convert temperature
    if scale == 'F' :
        # Convert to celsius
        print '%.1f Fahrenheit is equivalent to %.1f Celsius.' % (temp, f2c(temp))
    elif scale == 'C' :
        # Convert to fahrenheit
        print '%.1f Celsius is equivalent to %.1f Fahrenheit.' % (temp, c2f(temp))
    else :
        # Unknown scale
        print "I don't know how to convert %.1f %s." % (temp, scale)