import pandas as pd
import random

def create_math_question():
     num1, num2 = random.randint(1, 1000), random.randint(1, 1000)
     answer = num1 + num2
     return f"What is {num1} + {num2}?", str(answer)

dataset = [create_math_question() for _ in range(10000)]
df = pd.DataFrame(dataset, columns=["prompt", "target"])
