# python-formation

## Poker table implementation
This is a simple repo for trainees to learn how to use python.
I personally feel like testing is a part of implementation, so we will use pytest to test our code.
We can divide this exercise in several steps
Trainees will install pytest in their venv with command
    pip install pytest

## Step 1 - Create Cards - Implementation
This first exercise will show the syntax needed to create a simple class and enums
1. Create enums for Color and CardValues
2. Create the Card class
    - 2 attributes: color and value (value name is a bit tricky because of enums, maybe rename that)
    - A representation

## Step 2 - Create Cards - Testing
In this exercise we will use pytest for the first time.
It will learn trainees to use import, as well as the whole pytest framework
1. Create a first test that just asserts (False then True)
2. Create a test to check that Card class exists, that it has 2 attributes color and value

## Step 3 - Create Hand - Implementation
Hand is a class that has one attribute: cards
It must have one method: compute_value
Following steps will be implemented
1. Create enum for hand value
2. Create Hand class, with initializer
3. Create compute_value, we can use different steps
   1. give the combination
   2. think on what we have to output to be able to compare two hands


## Step 3 - Create Hand - Testing
1. Create a test to check that Hand exists, that it has one attribute, and one method
2. Create testcases for each combination



