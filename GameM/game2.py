import numpy as np

def random_predict(number: int = 1) -> int:
    """[the function of searching for a hidden number by brute force]

    Args:
        number (int, optional): [the hidden number]. Defaults to 1.

    Returns:
        int: [number of guessing attempts]
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)      # estimated number
        if number == predict_number: break              # if desired value is found, break
                                                        
    return count

def speed_predict(number: int = 1) -> int:
    """ The function of a quick search for a hidden number

    Args:
        number (int, optional): [the hidden number]. Defaults to 1.

    Returns:
        int: [number of guessing attempts]
    """
    
    count       = 1                                     # if the number 100 is guessed, count = 1
    min_number  = 1                                     # lower limit of the search range
    max_number  = 100                                   # upper limit of the search range
    
    while number < 100:                                 # We guess the number 100 right away. Instead of True
        if number > (max_number+min_number) // 2:       # if the number is greater than the middle of the range
            min_number = (max_number+min_number) // 2   # move up min_number
        elif number < (max_number+min_number) // 2:     # if the number is less than the middle of the range
            max_number = (max_number+min_number) // 2   # move down max_number
        else: break                                     # desired value is found, break
        count += 1
        
    return count
            

def score_game(counting_func) -> int:
    """For how many attempts on average for 1000 approaches does our algorithm guess

    Args:
        counting_func ([function]): guessing function

    Returns:
        int: average number of attempts
    """

    count_ls = []                                           # list to save the number of attempts
    np.random.seed(1) # Fix LED for
    random_array = np.random.randint(1, 101, size=(1000))   # made a list of numbers

    for number in random_array:
        count_ls.append(counting_func(number))

    score = int(np.mean(count_ls))                           # we find the average number of attempts

    print(f'The algorithm of the function ({counting_func.__name__.capitalize()}) guesses the number on average for: {score} attempts')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)
    score_game(speed_predict)
  
    
    

