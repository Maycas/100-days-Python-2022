# TREASURE MAP

# Instructions

You are going to write a program that will mark a spot with an `X`.

In the starting code, you will find a variable called `map`.

This `map` contains a nested list. When `map` is printed this is what the nested list looks like:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code `print(f"{row1}\n{row2}\n{row3}"` to format the 3 lists to be printed as a 3 by 3 square, each on a new line. 

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

Now it looks a bit more like the coordinates of a real map:

![Map](https://codingrooms-user-uploads-us-west-2.s3-us-west-2.amazonaws.com/dcf3f486-3ca7-40e2-8c2c-3e7ed90ea071/Co-ordinates_oggjzg+copy.png)

Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical location and the second digit is the horizontal location. So an input of 23 should place an X at the position shown below:

![Accessing coordinates in a map](https://codingrooms-user-uploads-us-west-2.s3-us-west-2.amazonaws.com/6e21e893-12cc-4ebb-9fcb-600b87a719b0/map.png)

First, your program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an `"X"`. Remember that your nested list map actually looks like this: [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']].

# Example

Column 2, row 3 would be entered as:
```
23
```
```
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
```

Column 3, row 1 would be entered as:
```
31
```
```
['⬜️', '⬜️', 'X']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
```