# game-of-greed-V1

## Description

* This program simulate The game of Greed, this game is a dice game. ... When a player passes (that is, rolls zero dice on their turn) the machene gets one more turn to roll, and then the game is over. If at that point neither player has gone over 100, the player with the higher score wins.
  
___

## **Live PR URL** [link1](https://github.com/jariryyousef/game_of_greed/pull/1)

## **Live PR URL** [link2](https://github.com/jariryyousef/game_of_greed/pull/2)

## **Live PR URL** [link3](https://github.com/jariryyousef/game_of_greed/pull/4)

## **Live PR URL** [link4](https://github.com/jariryyousef/game_of_greed/pull/5)
---

## Feature Tasks

*version 1 & 2*_______

 >[x] Application should implement all features from previous version

>[x] Application should simulate rolling between 1 and 6 dice

>[x] Application should allow user to set aside dice each roll

>[x] Application should allow “banking” current score or rolling again.

>[x] Application should keep track of total score

>[x] Application should keep track of current round

>[x] Application should have automated tests to ensure proper operation

*version 3*_______

>[x] Application should implement features from versions 1 and 2

>[x] Should handle setting aside scoring dice and continuing turn with remaining dice.
Should handle when cheating occurs.
 - >Or just typos.
 - >**E.g.** roll = [1,3,5,2] and user selects 1, 1, 1, 1, 1, 1

>[x] Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.

>[x] Handle **zilch** No points for round, and round is over

## Requirment

```javascript
poetry
python 3.9.7
pytest
```

## Getting started

```bash
poytry install
poetry shell
pytest
python -m Modules_and_Testing.math_series
```

## Algorithm

<img src = "Game of Greed.jpg">

## This game-of-greed

* Define a GameLogic class in game_of_greed/game_logic.py file.
* Handle calculating score for dice roll:

  [x] Add calculate_score static method to GameLogic class

  [x] The input to calculate_score is a tuple of integers that represent a dice roll.

  [x] The output from calculate_score is an integer representing the roll’s score according to rules of game.

  Handle rolling dice:

  [x] Add roll_dice static method to GameLogic class.

  [x] The input to roll_dice is an integer between 1 and 6.

  [x] The output of roll_dice is a tuple with random values between 1 and 6.
  
  [x] The length of tuple must match the argument given to roll_dice method.
  Handle banking points:
  
  [x] Define a Banker class
  
  [x]Add a shelf instance method
  
  [x]Input to shelf is the amount of points (integer) to add to shelf.
  
  [x]shelf should temporarily store unbanked points.
  Add a bank instance method:
  
  [x]bank should add any points on the shelf to total and reset shelf to 0.
  
  [x]bank output should be the amount of points added to total from shelf.
  Add a clear_shelf instance method:
  
  [x]clear_shelf should remove all unbanked points

## Testing Details

---

### Calculate Score

  [x] zilch - roll with no scoring dice should return 0

  [x] ones - rolls with various number of 1s should return correct score

  [x] twos - rolls with various number of 2s should return correct score

  [x] threes - rolls with various number of 3s should return correct score

  [x] fours - rolls with various number of 4s should return correct score

  [x] fives - rolls with various number of 5s should return correct score

  [x] sixes - rolls with various number of 6s should return correct score

  [x] straight - 1,2,3,4,5,6 should return correct score

  [x] three_pairs - 3 pairs should return correct score

  [x] two_trios - 2 sets of 3 should return correct score

  [x] leftover_ones - 1s not used in set of 3 (or greater) should return correct score

  [x] leftover_fives - 5s not used in set of 3 (or greater) should return correct score

---

### Banker

* shelf:
  
  [x] should properly track unbanked points

* bank:
  
  [x] should properly add unbanked points to total and return the deposited amount

* clear_shelf:
  
  [x] should remove any unbanked points, resetting to zeroant it should not affect previously banked points

---

### User Acceptance Tests

  [x] quitter.sim test

  [x] one_and_done.sim tests

  [x] bank_one_roll_then_quit.sim tests

  [x] bank_one_roll_then_quit.sim test

---
___
**Collaboratores:**

* Bashar Taamneh
* Aseel Al-Saqer
* Haneen Hashlmoun
* Yousef Jariri
