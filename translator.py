from transformers import MarianMTModel, MarianTokenizer
from transformers import AutoTokenizer, AutoModelForCausalLM
import random

"""
Tokenizer converts raw text into tokens that the model can process.
Model processes the tokens and generates an output (e.g., translation, text generation).

"""

def load_french_sentences():
    """Loads french statements"""
    tokenizer = AutoTokenizer.from_pretrained("dbddv01/gpt2-french-small")
    model = AutoModelForCausalLM.from_pretrained("dbddv01/gpt2-french-small")
    return(tokenizer,model)

def load_spanish_sentences():
    """Loads spanish statements"""
    tokenizer = AutoTokenizer.from_pretrained("DeepESP/gpt2-spanish")
    model = AutoModelForCausalLM.from_pretrained("DeepESP/gpt2-spanish")
    return(tokenizer,model)

def load_japanese_sentences():
    """Loads japanese statements"""
    tokenizer = AutoTokenizer.from_pretrained("abeja/gpt2-large-japanese")
    model = AutoModelForCausalLM.from_pretrained("abeja/gpt2-large-japanese")
    return(tokenizer,model)

def load_mandarin_sentences():
    """Loads chinese statements"""
    tokenizer = AutoTokenizer.from_pretrained("uer/gpt2-chinese-cluecorpussmall")
    model = AutoModelForCausalLM.from_pretrained("uer/gpt2-chinese-cluecorpussmall")
    return(tokenizer,model)

def load_german_sentences():
    """Loads german statements"""
    tokenizer = AutoTokenizer.from_pretrained("stefan-it/german-gpt2-larger")
    model = AutoModelForCausalLM.from_pretrained("stefan-it/german-gpt2-larger")
    return(tokenizer,model)

    
def load_translation_model():

    model_name = "Helsinki-NLP/opus-mt-mul-en"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

# Function to translate text to English
def translate_to_english(text, tokenizer, model):
    try:
        # Tokenize the input text
        inputs = tokenizer(text, return_tensors="pt", padding=True)
        # Translate the input text
        translated = model.generate(**inputs)
        # Decode the translated text
        output = tokenizer.decode(translated[0], skip_special_tokens=True)
        return output
    except Exception as e:
        return f"Error in translation: {str(e)}"

def generate_sentences(language):
    """
    condition = True
    while condition:
        if language.lower()not in ['french','spanish','japanese','mandarin','german']:
            language = input("Please enter a valid language: ")
        else:
            condition = False
    """
    
    if language == 'french':
        tokenizer, model = load_french_sentences()

    elif language == 'spanish':
        tokenizer, model = load_spanish_sentences()
    
    elif language == 'japanese':
        tokenizer, model = load_japanese_sentences()
    
    elif language == 'mandarin':

        tokenizer,model = load_mandarin_sentences()
    
    else:
        tokenizer,model = load_german_sentences()

    input_prompt = f"Please generate a sentence in {language}: "
    inputs = tokenizer(input_prompt, return_tensors="pt")
    output = model.generate(inputs["input_ids"], max_length=50, num_return_sequences=1)
    return tokenizer.decode(output[0], skip_special_tokens=True)


generate_sentences('french')
"""    
# Chatbot function
def chatbot():
    # print("Welcome to the Translator Chatbot!")
    # print("Type 'exit' to end the chat.")
    # print("You can send messages in any language, and I will translate them to English.")

    # Load the translation model
    tokenizer, model = load_translation_model()

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        # Translate the user's message to English
        translated_message = translate_to_english(user_input, tokenizer, model)
        print(f"Chatbot (Translated to English): {translated_message}")

    # file_name = 'french_text'
    # with open(file_name, 'r') as f:
    #     content = f.read()
    
    # translated_message = translate_to_english(content, tokenizer, model) 
    # print(f"Translation into English: {translated_message}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()

"""