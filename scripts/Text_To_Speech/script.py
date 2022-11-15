from gtts import gTTS
from playsound import playsound
import os

mytext = input("Enter text: ")

print("MENU\n1. English (Australia)\n2. English (United Kingdom)\n3. English (United States)\n4. English (Canada)\n5. English (India)\n6. English (Ireland)\n7. English (South Africa)\n8. French (Canada)\n9. French (France)\n10. Mandarin (China Mainland)\n11. Mandarin (Taiwan)\n12. Portuguese (Brazil)\n13. Portuguese (Portugal)\n14. Spanish (Mexico)\n15. Spanish (Spain)\n16. Spanish (United States)")
option = int(input("Select option: "))
if option == 1:
    language = 'en'
    tld1 = 'com.au'
elif option == 10:
    language = 'zh-CN'
    tld1 = 'com'
elif option == 11:
    language = 'zh-TW'
    tld1 = 'com'
elif option == 12:
    language = 'pt'
    tld1 = 'com.br'
elif option == 13:
    language = 'pt'
    tld1 = 'pt'
elif option == 14:
    language = 'es'
    tld1 = 'com.mx'
elif option == 15:
    language = 'es'
    tld1 = 'es'
elif option == 16:
    language = 'es'
    tld1 = 'com'

elif option == 2:
    language = 'en'
    tld1 = 'co.uk'
elif option == 3:
    language = 'en'
    tld1 = 'com'
elif option == 4:
    language = 'en'
    tld1 = 'ca'
elif option == 5:
    language = 'en'
    tld1 = 'co.in'
elif option == 6:
    language = 'en'
    tld1 = 'ie'
elif option == 7:
    language = 'en'
    tld1 = 'co.za'
elif option == 8:
    language = 'fr'
    tld1 = 'ca'
elif option == 9:
    language = 'fr'
    tld1 = 'fr'
tts = gTTS(text=mytext, tld=tld1, lang=language, slow=False)
audio_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tts.mp3")
tts.save(audio_file)
playsound(audio_file)