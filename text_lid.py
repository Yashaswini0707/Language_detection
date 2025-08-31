import fasttext

# Path to your model
MODEL_PATH = r"C:\Users\Yashu\Desktop\Project_new\lid.176.bin"

# Load model
print("Loading FastText model... (this may take a few seconds)")
model = fasttext.load_model(MODEL_PATH)
print("Model loaded ✅")

# Mapping ISO codes to Indian language names (you can extend this dictionary)
lang_map = {
    "en": "English",
    "kn": "Kannada",
    "te": "Telugu",
    "hi": "Hindi",
    "ta": "Tamil",
    "ml": "Malayalam",
    "mr": "Marathi",
    "bn": "Bengali",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "ur": "Urdu",
    "as": "Assamese",
    "or": "Odia",
    "sa": "Sanskrit",
    "ne": "Nepali",
    "bh": "Bihari",
    "mai": "Maithili",
    "gom": "Goan Konkani",
    "bpy": "Bishnupriya Manipuri",
    "sd": "Sindhi"
}

def detect_language(text):
    lang, prob = model.predict(text)
    code = lang[0].replace("__label__","")  # Fixed: double underscores
    name = lang_map.get(code, f"Unknown ({code})")
    return name, prob[0]

# Test words
samples = [
    "నిఘంటుశోధన",  # Telugu
    "ನಮಸ್ಕಾರ",     # Kannada
    "hello",        # English
    "घर",          # Hindi
    "வணக்கம்",      # Tamil
]

for word in samples:
    lang_name, confidence = detect_language(word)
    print(f"Input: {word} → {lang_name} (confidence={confidence:.2f})")

# Optional: interactive mode
while True:
    text = input("\nEnter a word (or 'exit' to quit): ")
    if text.lower() == "exit":
        break
    lang_name, confidence = detect_language(word)
    print(f"Detected Language: {lang_name} (confidence={confidence:.2f})")
