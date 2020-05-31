# Simplified BlackJack Game (Python 3)
## Technologies used
- Python 3
- Unittest (TDD)
- Shell script
- pylint
## Rules of the game
## Playing the game
- Navigate to the main_package folder <br/>
```cd ~/{PATH}/SimplifiedBlackJackGame/python_code/main_package/```
- Make `playBlackJack.sh` executable by typing<br/>
```chmod +x playBlackJack.sh```
- Run `./playBlackJack.sh`<br/>
Once the game starts you will see this
![start_game](./images/start_game.png)
- Place your bet by entering an integer between 0 and the total number of chips that you have.
- The game starts and the dealer deals card to you and himself. 
- You are then asked if you want to hit (take another card) or stand (continue with your existing hand)
- If you choose hit, you will get another card. 
  - If the next card takes your score above 21 you lost the round.
  - If the next card takes you to score 21 you win the round.
  - otherwise you are asked for hit or stand again.
- When you choose to stand, now dealer will play his hand.
  - If his score goes over 21 you win.
  - If his score becomes 21 you lose.
  - Otherwise, you will go to the next step where both of your scores are compared.
- If at this point your score is higher than dealer you will win, otherwise you will lose.
- If you win your chips increase by the amount that you have bet and if you lose your chips reduce by the same amount.
- At the end of the round you are asked if you would like to play again.
  - If you choose to play again you start at the betting step.
  - If not, the game ends.
__Note__ if you don't have enough chips, the game will automatically end.

## Running the unit tests
