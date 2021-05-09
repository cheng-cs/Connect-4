# Connect-4

## Introduction




## System commands (using Pyenv and Pipenv)

Assuming that you will use [Pyenv](https://github.com/pyenv/pyenv) to download and manage your installation of Python, this practical assignment also invites you to use [Pipenv](https://github.com/pypa/pipenv) to create a virtual environment, install and manage development packages, and to run Python commands. Previously, you should have run the following command:

- Install and upgrade the `pipenv` command: `pip install pipenv --user` or `sudo -H pip install -U pipenv` (note, if you have both Python2 and Python3, you may need to use `pip3` command instead of `pip`)

Here is a sample of the Pipenv commands that you will need to run during this assignment. Please note these commands are using the scripts located in your practical directory. If you prefer to run each individual tool separately, please refer to the commands you used in the previous practical.

- Install the new development dependencies with new `pytest` plugins: `pipenv` command: `pipenv install --dev`
- Run the linters and the formatter to check the Python source code: `pipenv run lint --check`

Here is a sample of the Pipenv commands that you will need to run this program.

- use the `cd` command and navigate to your connect4 folder.
- enter `python connect4.py` in your terminal to run the program
- To stop the program enter `control z` for mac.

To run one of these commands, you must be in the main directory for this assignment where the configuration files are located. Then, you can type these commands in the terminal and study the output.

## Output
when you run the code, you should see the following output:
```
[[ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]]
Player 1 Make your move (0-6):
```
When a player wins, they should see the following output:
```
Player 1 Wins
[[ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  2.  0.  0.  0.  0.  0.]
 [ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  2.  2.  0.  0.  0.  0.]
 [ 1.  1.  1.  1.  2.  0.  0.]]
```

Running the test suite with `pytest` should produce output similar to this:

```
Test session starts (platform: darwin, Python 3.9.2, pytest 6.2.2, pytest-sugar 0.9.4)
rootdir: /Users/gary/Documents/203-cs/project/project-2/Connect-4
plugins: clarity-0.3.0a0, sugar-0.9.4
collecting ...
 tests/test_connect4.py ✓✓✓✓           100% ██████████

Results (0.14s):
       4 passed

```
## Using Gradle

## Updates

## GitHub Actions
