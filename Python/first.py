import re
import pandas as pd  # table display



def lexical_diversity(filename):

    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()


    words = re.findall(r'\b\w+\b', text.lower())


    unique_words = set(words)


    return len(unique_words), len(words), len(unique_words) / len(words) if words else 0



filename = 'batman-returns_final.txt'


unique_count, total_count, diversity_score = lexical_diversity(filename)


data = {"Metric": ["Total Words", "Unique Words", "Lexical Diversity"],
        "Value": [total_count, unique_count, diversity_score]}
df = pd.DataFrame(data)


print(df.to_string(index=False))
