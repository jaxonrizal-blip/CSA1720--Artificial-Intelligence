import nltk
import random
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLP resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Chatbot knowledge base
questions = [
    "hello hi hey",
    "what is your name",
    "how are you",
    "what is artificial intelligence",
    "what is machine learning",
    "what is python",
    "what is NLP",
    "what can you do",
    "who created you",
    "goodbye bye"
]

answers = [
    "Hello! Welcome to our chatbot.",
    "I am a simple NLP-based chatbot.",
    "I am doing great! How can I help you?",
    "Artificial Intelligence enables machines to perform tasks that require human intelligence.",
    "Machine Learning allows computers to learn from data.",
    "Python is a popular programming language.",
    "NLP stands for Natural Language Processing. It helps computers understand human language.",
    "I can answer basic questions using NLP techniques.",
    "I was created using Python programming.",
    "Goodbye! Have a nice day!"
]

# Text preprocessing
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)

    tokens = [
        word for word in tokens
        if word not in stop_words
        and word not in string.punctuation
    ]

    return " ".join(tokens)

# Preprocess questions
processed_questions = [
    preprocess(q) for q in questions
]

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(
    processed_questions
)

# Generate chatbot response
def chatbot_response(user_input):

    if user_input.lower().strip() in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day!"

    processed_input = preprocess(user_input)

    if not processed_input:
        return "Please enter a meaningful message."

    input_vector = vectorizer.transform(
        [processed_input]
    )

    similarity = cosine_similarity(
        input_vector,
        question_vectors
    )

    best_match = similarity.argmax()
    confidence = similarity[0][best_match]

    if confidence < 0.20:
        return "Sorry, I don't understand. Can you ask another question?"

    return answers[best_match]


# Main chatbot
print("================================")
print("     NLP CHATBOT")
print("================================")
print("Type 'exit' to stop chatting.")

while True:

    user_input = input("\nYou: ")

    if user_input.lower().strip() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    response = chatbot_response(user_input)

    print("Bot:", response)
