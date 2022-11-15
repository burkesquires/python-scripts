import easyocr

gpu = False # if you want to use GPU, set gpu=True
languages = ['en'] # refer https://www.jaided.ai/easyocr/ for supporting languages

reader = easyocr.Reader(languages, gpu=gpu)

IMG_PATH = 'test1.png'
result = reader.readtext(IMG_PATH)

text = ''.join(tup[1] for tup in result)
print(text)