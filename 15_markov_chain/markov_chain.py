import markovify 
import pandas as pd 

# Read the CSV file
df = pd.read_csv('airport_reviews.csv')

N = 100

# Process the text
review_subset = df['content'][0:N]
text = " ".join(review_subset)  # Join the reviews with spaces

# Create the model with state_size=2 for better coherence
markov_chain_model = markovify.Text(text, state_size=2)

print("Generated full sentences:")
print("-----------------------")
# Generate sentences
for i in range(5):
    sentence = markov_chain_model.make_sentence()
    if sentence:
        print(f"{i+1}. {sentence}")
    
print("\nGenerated short sentences (max 140 chars):")
print("----------------------------------------")
# generate sentences of no more than 140 characters
for i in range(3):
    sentence = markov_chain_model.make_short_sentence(140)
    if sentence:
        print(f"{i+1}. {sentence}")