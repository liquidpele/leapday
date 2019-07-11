#!/usr/bin/python
from __future__ import print_function
import argparse
from collections import OrderedDict
import json


"""
Script to get the name of the day of the week of the leap day
on given years.  Manually calculate due to pretend bugs in stdlib.
Example:  ./leapday.py 2000 2004 -f shortname -m json

Assumptions:
1. No BCE years are supported
2. Gregorian calendar is used
"""


def is_leap_year(year):
    """Check if the given year is a leap year

    Parameters:
    year (int): Year to to check

    Returns:
    bool: True if the year is a leap year
    """
    if not isinstance(year, int) or year < 0:
        raise ValueError('Invalid year: {}'.format(year))
    # Logic from: https://support.microsoft.com/en-us/help/214019/
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True
    return False


def leapday_day_of_week(year):
    """Return the day of week of the leap day of a given year

    Parameters:
    year (int): Year to calculate the day of week for leap day

    Returns:
    int: Day of week, sun=0.  None for non-leapyear.
    """
    if not isinstance(year, int) or year < 0:
        raise ValueError('Invalid year: {}'.format(year))
    if not is_leap_year(year):
        return None
    # Use Gauss' algorithm
    # https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week
    # since we only ever want Feb 29th, simplify it a bit with jan1st algorithm
    jan1_dow = (1 + 5 * ((year - 1) % 4)
                + 4 * ((year - 1) % 100)
                + 6 * ((year - 1) % 400)) % 7
    return (jan1_dow + 59) % 7  # Feb 29th is 59 days from Jan 1st


def dow_to_name(dow, short=False):
    """Given a day of week integer, return the proper name

    Parameters:
    dow (int): Day of week as an integer, sun=0 sat=6

    Returns:
    string: Name of the given day
    """
    if not isinstance(dow, int) or dow < 0 or dow > 6:
        raise ValueError('Invalid day of week: {}'.format(dow))
    name = ['Sunday',
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday'][dow]
    return name[:3] if short else name


def main():
    parser = argparse.ArgumentParser(
        description="""Given a series of years, print the day of the week
        for the leap day on each year.
        If the year is not a leap year print blank.""")
    parser.add_argument('years', metavar='Year', type=int, nargs='+',
                        help='Year as YYYY')
    parser.add_argument('-f', dest='format', default=None,
                        help='Output format (Default is ints with Sun=0)',
                        choices=['name', 'shortname'])
    parser.add_argument('-m', dest='machine', default=None,
                        help='Output as machine readable',
                        choices=['json', 'xml'])
    args = parser.parse_args()

    machine_dict = OrderedDict()
    for year in args.years:
        # first generate the output format for the year
        dow = leapday_day_of_week(year)
        if args.format:
            if dow is None:
                name = ''
            else:
                short = args.format == 'shortname'
                name = dow_to_name(dow, short=short)
        else:
            name = '' if dow is None else '{}'.format(dow)
        # now output or save the data
        if args.machine is None:
            print(name)
        else:
            # this will de-duplicate years, which is nice for machine readable
            # but we can't do that for just stdout output
            machine_dict[year] = name or None
    # if doing machine readabe, process that now
    if args.machine == 'json':
        print(json.dumps(machine_dict, indent=4))
    elif args.machine == 'xml':
        # this is so simplistic, using a full xml lib is overkill
        print('<?xml version="1.0" encoding="utf-8"?>')
        print('<output>')
        for year, name in machine_dict.items():
            if name is None:
                print('  <item year="{}" />'.format(year))
            else:
                print('  <item year="{}">{}</item>'.format(year, name))
        print('</output>')


if __name__ == '__main__':
    main()
