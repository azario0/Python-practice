import random
import pandas as pd

def generate_lotto_numbers():
    numbers = []
    for _ in range(6):
        number = random.randint(1, 45)
        while number in numbers:
            number = random.randint(1, 45)
        numbers.append(number)
    return numbers

def make_prediction():
    numbers = generate_lotto_numbers()
    prediction = pd.DataFrame({
        "Number": numbers,
        "Probability": 1/45 ** 6
    })
    return prediction

if __name__ == "__main__":
    prediction = make_prediction()
    print(prediction)