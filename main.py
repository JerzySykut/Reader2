from sys import argv
from Reader2 import Reader

if __name__ == '__main__':
    # sprawdzamy czy mamy conajmniej 1 argument (plik wejsciowy)
    if len(argv) < 2:
        print("za mało argumentów")
        exit()
    reader = Reader()
    if reader.loadFromFile(argv[1]):
        # sprawdzamy czy mamy drugi argument (plik wyjsciowy)
        if len(argv) > 2:
            # analizujemy argumenty zmian
            for i in range(3, len(argv)):
                para = argv[i]
                p = para.split(',')
                x = int(p[0])
                y = int(p[1])
                reader.setValue(x, y, p[2])
            reader.printData()
            reader.saveToFile(argv[2])
        else:
            reader.printData()

