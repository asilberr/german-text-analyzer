import pandas as pd
import spacy
from collections import Counter

# Load the Spacy German model
nlp = spacy.load("de_core_news_lg")

# Define additional stopwords
## TODO: Add any additional stopwords that you want to filter out
additional_stopwords = {''}

# Add the additional stopwords to the Spacy stopwords list
for word in additional_stopwords:
    nlp.vocab[word].is_stop = True

# Path to CSV file
## TODO: Change the file path to the location of your CSV file
## TODO: Check for correct delimiter and skiprows
file_path = '/'
df = pd.read_csv(file_path, delimiter=';', skiprows=6)

# Initialize a Counter to store the word frequencies
word_freq = Counter()

# Define a mapping table for word normalization
## TODO: Add any additional mappings that you want to apply
word_mapping = {
    # Add more mappings as needed
}

# Process each column in the DataFrame
for column in df.columns:
    # Remove missing values and concatenate the text in the column
    column_text = ' '.join(df[column].dropna().astype(str).tolist())
    
    # Process the text using Spacy
    doc = nlp(column_text)
    
    # Filter out stopwords and punctuation, and lemmatize the tokens
    filtered_tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    
    # Normalize the tokens using the mapping table
    normalized_tokens = [word_mapping.get(token, token) for token in filtered_tokens]
    
    # Update the Counter with the normalized tokens
    word_freq.update(normalized_tokens)

# Convert the Counter to a DataFrame
word_freq_df = pd.DataFrame(word_freq.items(), columns=['Wort', 'Anzahl'])

# Sort the DataFrame by word frequency in descending order
## TODO: Change the output file path to the desired location
output_file_path = '/'
word_freq_df.to_csv(output_file_path, index=False)

print(f"Worthäufigkeiten wurden in {output_file_path} gespeichert.")