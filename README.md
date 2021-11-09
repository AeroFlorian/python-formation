# python-formation

## Poker table implementation
* This is a simple repo for trainees to learn how to use python.
* I personally feel like testing is a part of implementation, so we will use pytest to test our code.
* We can divide this exercise in several steps
* Trainees will install pytest in their venv with command
    pip install pytest

## Step 1 - Create Cards - Implementation
This first exercise will show the syntax needed to create a simple class and enums
1. Create enums for Color and CardValues
2. Create the Card class
    - 2 attributes: color and value (value name is a bit tricky because of enums, maybe rename that)
    - A representation

## Step 2 - Create Cards - Testing
* In this exercise we will use pytest for the first time.
* It will learn trainees to use import, as well as the whole pytest framework
1. Create a first test that just asserts (False then True)
2. Create a test to check that Card class exists, that it has 2 attributes color and value

## Step 3 - Create Hand - Implementation
* Hand is a class that has one attribute: cards
* It must have one method: compute_value
* Note that we will do only "Aces High" combination (Ace, 2, 3, 4, 5 is not a straight)
* Following steps will be implemented
1. Create enum for hand value
2. Create Hand class, with initializer
3. Create compute_value, we can use different steps
   1. give the combination
   2. think on what we have to output to be able to compare two hands


## Step 4 - Create Hand - Testing
1. Create a test to check that Hand exists, that it has one attribute, and one method
2. Create testcases for each combination

## Step 5 - Create Deck - Implementation
* A Deck is composed of all the cards that exists at the beginning.
* Trainees will choose the representation (attributes, methods)
* With a Deck, we want to be able to:
1. Start with all 52 cards
2. Pick x cards in the deck (that method must be a generator for the example)
3. Throw exception NoMoreCardsError when trying to pick 53 cards

## Step 6 - Create Deck - Testing
1. Test that a Deck has 52 Cards, and no Cards are equal 
2. Test that the pick_cards method is a generator
3. Test that Deck's cards is shrinking when picking cards
4. Test that we have a NoMoreCardsError exception when trying to pick 53 cards

## Step 7 - Create Table - Implementation
* A Table consists in having a deck at instantiation, from which we can pick x hands
* Then, it must have a method compute_best, that outputs the best hand that has been picked
* This method must throw exception NoHandsPickedError when trying to compute_best without picking a hand
* This method must throw exception NoMoreHandsError when trying to pick hands in an empty deck


## Step 8 - Create Table - Testing
1. Test that Table has one full deck and no hands picked at instantiation
2. Test that we can pick one hand
3. Test that picking 52//5 + 1 = 11 hands will throw NoMoreHandsError
4. Test that trying compute_best without picking hands throws NoHandsPickedError
5. Test that Table's deck is emptying itself when picking cards
