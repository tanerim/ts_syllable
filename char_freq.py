import sys

f = open(sys.argv[1])
my_text = f.read()

alphabet = ["a", "e", "ı", "i", "o", "ö", "u", "ü", "f", "g", "ğ", "d", "r", "n", "h", "p", "q", "w", "t", "k", "m", "l", "y", "ş", "j", "v", "c", "ç", "z", "s", "b"]

for char in alphabet:
    char_freq = []
    counts = char, str(my_text.count(char))
    print(f"{char}\t{my_text.count(char)}")

