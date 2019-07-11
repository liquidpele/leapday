#!/usr/bin/python
import pytest
import leapday


yeardata = [
    (504, True),
    (505, False),
    (1000, False),
    (2000, True),
    (2001, False),
    (2002, False),
    (2003, False),
    (2004, True),
    (2005, False),
    (2006, False),
    (2007, False),
    (2008, True),
    (3000, False),
    (4000, True),
]


dow_data = [
    (2016, 'Monday'),
    (2012, 'Wednesday'),
    (2008, 'Friday'),
    (2004, 'Sunday'),
    (2000, 'Tuesday'),
    (1996, 'Thursday'),
    (1992, 'Saturday'),
]


class TestLeapYear(object):
    @pytest.mark.parametrize("year,expected_result", yeardata)
    def test_is_leapyear(self, year, expected_result):
        result = leapday.is_leap_year(year)
        err = 'Got {}, expected {}'.format(result, expected_result)
        assert result == expected_result, err

    def test_invalid_years(self):
        with pytest.raises(ValueError):
            leapday.is_leap_year('a')
        with pytest.raises(ValueError):
            leapday.is_leap_year(-1)


class TestLeapDay(object):
    @pytest.mark.parametrize("year,expected_result", dow_data)
    def test_is_leapyear(self, year, expected_result):
        result = leapday.dow_to_name(leapday.leapday_day_of_week(year))
        err = 'Got {}, expected {}'.format(result, expected_result)
        assert result == expected_result, err
