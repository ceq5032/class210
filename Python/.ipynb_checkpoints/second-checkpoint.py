import re
from collections import Counter
import pandas as pd  # table display



def lexical_diversity(filename):

    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()


    words = re.findall(r'\b\w+\b', text.lower())


    unique_words = set(words)


    word_counts = Counter(words)


    top_5_words = word_counts.most_common(5)

    return len(unique_words), len(words), len(unique_words) / len(words) if words else 0, top_5_words



filename = 'batman-returns_final.txt'


unique_count, total_count, diversity_score, top_5_words = lexical_diversity(filename)

# table
data = {
    "Metric": ["Total Words", "Unique Words", "Lexical Diversity"],
    "Value": [total_count, unique_count, diversity_score]
}
df = pd.DataFrame(data)

# Print the table
print(df.to_string(index=False))

# Display top 5 words
print("\nTop 5 Words:")
for word, count in top_5_words:
    print(f"{word}: {count}")
