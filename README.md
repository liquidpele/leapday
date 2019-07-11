# Leapday

System to manually calculate the name of the weekday for the leap day in a given year.  

## Usage

python -m flake8 passes, run tests with py.test

Example usage:  ./leapday.py 2000 2004 -f shortname -m json

For full options, use -h

## Details 

For this project, it was specified this would be used by a lot of things, 
so I made the script handle multiple years at a time as well as gave it the ability to 
output the results in various machine-readable formats for easy integration.  
I also separated the core logic into methods which can be used directly if another python 
program wanted to import use them.  Lastly, it runs on both python 2 and 3. 

Assumptions that were made:
1. No BCE years are supported
2. Gregorian calendar is used

Didn't have time to create a setup.py with a entry point for system executable, but that could easily be done. 

