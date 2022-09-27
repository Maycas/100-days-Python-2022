# LEAP YEAR

## Instructions

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this [video](https://www.youtube.com/watch?v=xX96xng7sAE) does it more justice.

This is how you work out whether if a particular year is a leap year.

&emsp; on every year that is evenly divisible by 4 

&emsp; **except** every year that is evenly divisible by 100 

&emsp; **unless** the year is also evenly divisible by 400

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap... but we need to check the last condition)

2000 ÷ 400 = 5 (Leap! As it's also divisible by 400)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

## Examples

### Example 1
```
2400
```
```
Leap year.
```

### Example 2
```
1989
```
```
Not leap year.
```