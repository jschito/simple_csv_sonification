# simple_csv_sonification
Sonify a CSV by using Parameter Mapping Sonification

The program loads a CSV file stored in the resources directory (res) and sonifies it by using the sonification method called **Parameter Mapping Sonification**. For this, the program first determines the range of the data values and then normalizes it to a octave, starting from the basic frequency. Thus, in this program, the pitch is used to sonify the data. 

## Files
- constants.py: Set the directory structure and the sonification settings
- sonify.py: Define the sonification function include the normalization of the data
