import detectlanguage

api_key = 'de848c36995c6df37d61bfdd547584fe'

detectlanguage.configuration.api_key = api_key

def detect():
    word = input('Entrez du texte : ')
    language = detectlanguage.simple_detect(word)
    print(language)
    detect()

detect()