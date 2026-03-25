try: 
    with open("maharashtra.txt", r+) as File:
        text= File.read("Bombay")
        newText = text.replace("Bombay","Mumbai")
        File.write(newText)
        File.close()
        File.truncate()
except: 
    print('File I/O Error!')