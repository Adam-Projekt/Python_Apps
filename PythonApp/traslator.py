from deep_translator import GoogleTranslator


jazyky = [
    "auto", "en", "fr", "de", "es", "it", "pt", "nl", "pl", "sv",
    "fi", "no", "da", "is", "tr", "el", "ru", "uk", "bg", "ro",
    "hu", "sk", "sl", "hr", "sr", "ar", "fa", "fa", "hi", "bn",
    "ta", "th", "id", "ms", "vi", "ja", "ko",
    "am", "sw", "af", "et", "lt", "lv", "ga", "mt", "sq", "mk",
    "cs"  
]

text = ""
puvodni = text

for i in range(len(jazyky) - 1):
    zdroj = jazyky[i]
    cil = jazyky[i + 1]

    prelozeno = GoogleTranslator(source=zdroj, target=cil).translate(text)

    
    print(f'("{prelozeno}")')
    print() 

    text = prelozeno

print("====================================")
print("Result:")
print(text)
print("====================================")

input("Press Enter")
