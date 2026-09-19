# password-brute-forse-analysis
Python project demonstrating password brute-force search and analyzing how password length and alphabet size affect the number of required attempts.

## About

The first program generates possible password combinations and checks them one by one until the entered password is found. The program supports English uppercase and lowercase letters, digits, and special characters. The second program calculates the average number of attempts required for passwords of different lengths and for different alphabet sizes, then visualizes the results using Matplotlib.

The project was developed as part of university work during the fourth year of university.

## Key Functions

* password_find() - rerforms the brute-force search for the entered password.
* itertools.product() - generates all possible combinations of characters for a specified password length.
* time.time() - used to measure the time required to find the password.
* plt.plot() - creates the line graph for password length analysis.
* ax2.bar() - creates the bar chart for alphabet size analysis.

## Key Variables

* chars - set of characters used for password generation;
* secret_password - password entered by the user;
* max_length - maximum password length used during the search;
* start_time - starting time of the brute-force process;
* tries - number of password attempts;
* total_combinations - total number of possible combinations;
* guess_i - generated character combination;
* guess - generated password candidate;
* total_time - time spent searching for the password;
* lengths_data - password lengths used for graph construction;
* avg_tries_length_data - average number of attempts for different password lengths;
* password_length - fixed password length used for alphabet comparison;
* alphabets - collection of character sets used in the analysis;
* alphabet_names - names of the character sets;
* alphabet_sizes - sizes of the character sets;
* avg_tries_alphabet_data - average number of attempts for different alphabet sizes.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/dolzhkris/password-brute-force-analysis.git
```

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the program:

```bash
python main.py
```

Enter a password when prompted.
