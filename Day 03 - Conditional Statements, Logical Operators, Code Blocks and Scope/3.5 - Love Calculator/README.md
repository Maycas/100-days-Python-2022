# LOVE CALCULATOR

## Instructions

You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

&emsp; Take both people's names and check for the number of times the letters in the word TRUE occurs.

&emsp; Then check for the number of times the letters in the word LOVE occurs.

&emsp; Then combine these numbers to make a 2 digit number.

For Love Scores less than **10 or greater than 90**, the message should be:

```
"Your score is **x**, you go together like coke and mentos."
```

For Love Scores **between 40 and 50**, the message should be:

```
"Your score is **y**, you are alright together."
```

Otherwise, the message will just be their score. e.g.:

```
"Your score is **z**."
```

e.g.

```python
name1 = "Angela Yu"
name2 = "Jack Bauer"
```

T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times

Total = 5

L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

## Example 1

```python
name1 = "Kanye West"
name2 = "Kim Kardashian"
```

```
Your score is 42, you are alright together.
```

## Example 2

```python
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"
```

```
Your score is 73.
```
