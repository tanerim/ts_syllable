import os
import sys
from ts_hecele import ts_hecele, hecele
to_input = []
if len(sys.argv) == 1:
    word = (input("Sözcük giriniz: \n"))
    to_input.append(word)
elif len(sys.argv) == 2:
    file = open(sys.argv[1])
    input_words = file.read().splitlines()
    for word in input_words:
        to_input.append(word)


if __name__ == '__main__':
    for word in to_input:
        print(ts_hecele(word))


