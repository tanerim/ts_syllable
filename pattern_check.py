# check_patterns.py

import sys

# Türkçedeki ünlü harfler
VOWELS = "aeıioöuüAEIİOÖUÜ"

def annotate(word: str) -> str:
    """Bir sözcüğün V/C paternini çıkarır."""
    return "".join("V" if ch in VOWELS else "C" for ch in word)

def load_patterns(pattern_file: str) -> set:
    """Dosyadan bilinen paternleri yükler (sadece sağ taraftaki pattern kısmı)."""
    patterns = set()
    with open(pattern_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(" - ")
            if len(parts) == 2:
                patterns.add(parts[1])  # sağ taraf (pattern)
    return patterns


def check_words(wordlist, length: int, known_patterns: set):
    """Belirtilen uzunluktaki sözcüklerin paternlerini kontrol eder."""
    with open(wordlist, encoding="utf-8") as f:
        words = [w.strip() for w in f if w.strip()]

    for word in words:
        if len(word) == length:
            pattern = annotate(word)
            if pattern not in known_patterns:
                print(f"Uyarı: {word} -> {pattern}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Kullanım: python check_patterns.py <wordlist.txt> <patterns.txt> <uzunluk>")
        sys.exit(1)

    wordlist = sys.argv[1]
    pattern_file = sys.argv[2]
    length = int(sys.argv[3])

    known_patterns = load_patterns(pattern_file)
    check_words(wordlist, length, known_patterns)
