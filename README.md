# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Constraint propagation check for naked twins repeatedly until no further reduce can be achieved. 

Naked twins means in every unit of a Sudoku, if two boxes has identical two possible digits, those two digits has to be in the two boxes. It means no other boxes in the same unit can have those two digits. 

Here are the details:

Step 1: find all units in the Sudoku. It includes rows, columns, squares and two diagonal regions.

Step 2: for each unit, go through all boxes. For each box, if there are two possible digits in it, check all other boxes in this unit and see if there is different box which has identical two possible values.

Step 3: when a twin box is found, it means no other boxes in the unit should have the two digits in the naked twins. So we should go through all other boxes in the unit and remove the two digits from the possible values.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Constraint propagation applies Elimination and Only Choice repeatedly until the two processes cannot further reduce the possible solution. 

Elimination: if a box has only one possible value, no other boxes in any unit the box belongs to should have that digit as a possible value. It can be achieved in the following steps:

Step 1: find all boxes which has only one possible values.

Step 2: find all peers of this box, which includes rows, columns, squares and two diagonal regions.

Step 3: for each all peer box, remove that digit from the possible values.

Only Choice: for each unit in a Sudoku, it must have digits from 1 to 9. If a digit in a certain unit is only possible to be in one box, that box must have that digit as a solution. It can be achieved in the following steps:

Step 1: for each unit in the Sudoku, for each digit 1 to 9, check the number of possible places the certain digits can be.

Step 2: if the digits is only possible to be in one box, it means it must be in that box.

Step 3: set the digit as the solved value for that box.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

