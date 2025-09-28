###########################################################
#                  A rule based hypenator                 #
#                  tanersezerr@gmail.com                  #
#          The function to hyphenate the word              #
#         The code is humble and old-fashioned            #
#     however it is good for high accuracy hyphenation     #
###########################################################
#         Some patterns generate same output              #
#        and could be nested in a single rule             #
#  but it is better to separate and follow each pattern   #
###########################################################

consonant = ["b", "c", "ç", "d", "f", "g", "ğ", "h", "j", "k", "l", "m", "n", "p", "r", "s", "ş", "t", "v", "y", "z",
             "B", "C", "Ç", "D", "F", "G", "Ğ", "H", "J", "K", "L", "M", "N", "P", "R", "S", "Ş", "T", "V", "Y", "Z"]
vowel = ["a", "e", "ı", "i", "o", "ö", "u", "ü", "â", "î", "û",
         "A", "E", "I", "İ", "O", "Ö", "U", "Ü", "Â", "Î", "Û"]

######### A function to create vowel-consonant pattern of the word
def annotate(syllable, join="+"):
    tag = ""
    for letter in syllable.replace("-", ""):
        if letter in consonant:
            tag += 'C'
        elif letter in vowel:
            tag += 'V'
        else:
            tag = 'No_S'
            break
    return "{}".format(tag)

######### Not necessary any more
def char_list(girdi):
    chars = []
    for char in girdi:
        chars.append(char)
    return chars

######### A function to count letters in input word
def create_wl(girdi):
    wl = len(girdi)
    return int(wl)

######### Count vowels in word
def count_vowel(string):
    num_vowels=0
    for char in string.lower():
        if char in "aeıioöuü":
           num_vowels = num_vowels+1
    return num_vowels

######### Count consonants in word
def count_cons(string):
    num_cons=0
    for char in string.lower():
        if char in "bcçdfgğhjklmnprsştvyz":
           num_cons = num_cons+1
    return num_cons

######### Create Output
def ts_hecele(word) -> object:
    return (f"{word}\t{annotate(word)}\t{hecele(word)}\t{create_wl(word)}")
def ts_check(word) -> object:
    return (f"{hecele(word)}")

def ts_t_part(word) -> object:
    return (f"{hecele(word)}")

######### main_function
def hecele(word):
    chars = char_list(word)
    sayi = create_wl(word)



################# 1 ###################
# required rule: 1 #
#1 a - V
    if sayi == 1 and chars[0] in vowel:
        return word

################# 2 ###################
# required rule: 1 #
#1 ve | el - VC | CV
    if sayi == 2 and count_vowel(word) == 1 and count_cons(word) == 1:
        return word

################# 3 ###################
# required rule: 5 #
#1 bir - CVC
    elif sayi == 3 and count_vowel(word) == 1 and chars[0] not in vowel:
        return word
#2 ilk - VCC
    elif sayi == 3 and count_vowel(word) == 1 and chars[0] in vowel:
        return word
#3 iki - VCV
    elif sayi == 3 and count_vowel(word) == 2 and chars[0] in vowel:
        word = "".join(char_list(word[0])) + "-" + "".join(char_list(word[1:3]))
        return word
#4 şii - CVV
    elif sayi == 3 and count_vowel(word) == 2 and chars[-2] in vowel and chars[-1] in vowel:
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3]))
        return word
#5 kro - CCV
    elif sayi == 3 and count_vowel(word) == 1 and chars[0] in consonant and chars[1] in consonant:
        return word

################# 4 ###################
# required rule: 6 #

#1 ayma - VCCV
    elif sayi == 4 and annotate(word) == "VCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4]))
        return word
#2 dört - CVCC
    elif sayi == 4 and count_vowel(word) == 1:
        return word
#3  trio - CCVV
    elif sayi == 4 and count_vowel(word) == 2 and chars[0] in consonant and chars[1] in consonant and chars[2] in vowel and chars[3] in vowel:
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3]))
        return word
#4 kedi - CVCV
    elif sayi == 4 and count_vowel(word) == 2 and chars[0] in consonant:
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:]))
        return word
#5 ilik - VCVC
    elif sayi == 4 and count_vowel(word) == 2 and chars[0] in vowel:
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:]))
        return word
#6 obua - VCVV
    elif sayi == 4 and count_vowel(word) == 3 and chars[-2] in vowel and chars[-1] in vowel:
        word = "".join(char_list(word[0])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3]))
        return word
#7 aile - VVCV
    elif sayi == 4 and count_vowel(word) == 3 and chars[0] in vowel:
        word = "".join(char_list(word[0])) + "-" + "".join(char_list(word[1])) + "-" + "".join(char_list(word[2:4]))
        return word
#8 tren - CCVC
    elif sayi == 4 and count_vowel(word) == 1:
        return word
#9 aort - VVCC
    elif sayi == 4 and count_vowel(word) == 2 and chars[0] in vowel and chars[1] in vowel and chars[2] in consonant and chars[3] in consonant:
        word = "".join(char_list(word[0])) + "-" + "".join(char_list(word[1:3]))
        return word
################# 5 ###################
# required rule: 18 #
#1 prens - CCVCC
    elif sayi == 5 and count_vowel(word) == 1:
        return word
#2 ödünç - VCVVC
    elif sayi == 5 and annotate(word) == "VCVCC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:5]))
        return word
#3 badem - CVCVC
    elif sayi == 5 and annotate(word) == "CVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5]))
        return word
#4 yolcu - CVCCV
    elif sayi == 5 and annotate(word) == "CVCCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:]))
        return word
#5 arttı - VCCCV
    elif sayi == 5 and annotate(word) == "VCCCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5]))
        return word
#6 uzsal - VCCVC
    elif sayi == 5 and annotate(word) == "VCCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5]))
        return word
#7 ileri - VCVCV
    elif sayi == 5 and annotate(word) == "VCVCV":
        word = "".join(char_list(word[0])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5]))
        return word
#8 havai - CVCVV
    elif sayi == 5 and annotate(word) == "CVCVV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[-1]))
        return word
#9 teori - CVVCV
    elif sayi == 5 and annotate(word) == "CVVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2])) + "-" + "".join(char_list(word[3:5]))
        return word
#10 geoit - CVVVC
    elif sayi == 5 and annotate(word) == "CVVVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2])) + "-" + "".join(char_list(word[3:5]))
        return word
#11 prova - CCVCV
    elif sayi == 5 and annotate(word) == "CCVCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5]))
        return word
#12 geldi - CVCCV
    elif sayi == 5 and annotate(word) == "CVCCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5]))
        return word
#13 facia - CVCVV
    elif sayi == 5 and annotate(word) == "CVCVV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[5]))
        return word
#14 aidat - VVCVC
    elif sayi == 5 and annotate(word) == "VVCVC":
        word = "".join(char_list(word[0])) + "-" + "".join(char_list(word[1])) + "-" + "".join(char_list(word[2:5]))
        return word
#15 ideal - VCVVC
    elif sayi == 5 and annotate(word) == "VCVVC":
        word = "".join(char_list(word[0])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5]))
        return word
#16 deist - CVVCC
    elif sayi == 5 and annotate(word) == "CVVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5]))
        return word
#17 emtia - VCCVV
    elif sayi == 5 and annotate(word) == "VCCVV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4]))
        return word
#18 fleol - CCVVC
    elif sayi == 5 and annotate(word) == "CCVVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5]))
        return word

################# 6 ###################
# required rule: 29 #
#1 sfenks
    elif sayi == 6 and count_vowel(word) == 1:
        return word
#2 makine - CVCVCV
    elif sayi == 6 and annotate(word) == "CVCVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6]))
        return word
#3 geldik - CVCCVC
    elif sayi == 6 and annotate(word) == "CVCCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:6]))
        return word
#4 özveri - VCCVCV
    elif sayi == 6 and annotate(word) == "VCCVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6]))
        return word
#5 iletim - VCVCVC
    elif sayi == 6 and annotate(word) == "VCVCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:6]))
        return word
#6 üzümlü - VCVCCV
    elif sayi == 6 and annotate(word) == "VCVCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:6]))
        return word
#7 tostçu - CVCCCV
    elif sayi == 6 and annotate(word) == "CVCCCV":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:6]))
        return word
#8 sporcu - CCVCCV
    elif sayi == 6 and annotate(word) == "CCVCCV":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:6]))
        return word
#9 kriter - CCVCVC
    elif sayi == 6 and annotate(word) == "CCVCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:6]))
        return word
#10 daimdi - CVVCCV
    elif sayi == 6 and annotate(word) == "CVVCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6]))
        return word
#11 üstsel - VCCCVC
    elif sayi == 6 and annotate(word) == "VCCCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:6]))
        return word
#12 zoolog - CVVCVC
    elif sayi == 6 and annotate(word) == "CVVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2])) + "-" + "".join(char_list(word[3:6]))
        return word
#13 züğürt - CVCVCC
    elif sayi == 6 and annotate(word) == "CVCVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:6]))
        return word
#14 ziraat - CVCVVC
    elif sayi == 6 and annotate(word) == "CVCVVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6]))
        return word
#15 artist - VCCVCC
    elif sayi == 6 and annotate(word) == "VCCVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:6]))
        return word
#16 iadesi - VVCVCV
    elif sayi == 6 and annotate(word) == "VVCVCV":
        word = "".join(char_list(word[0])) + "-" + "".join(char_list(word[1])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6]))
        return word
#17 iguana - VCVVCV
    elif sayi == 6 and annotate(word) == "VCVVCV":
        word = "".join(char_list(word[0])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3])) + "-" + "".join(char_list(word[4:6]))
        return word
#18 azrail - VCCVVC
    elif sayi == 6 and annotate(word) == "VCCVVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6]))
        return word
#19 aitlik - VVCCVC
    elif sayi == 6 and annotate(word) == "VVCCVC":
        word = "".join(char_list(word[0])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:6]))
        return word
#20 stoacı - CCVVCV
    elif sayi == 6 and annotate(word) == "CCVVCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3])) + "-" + "".join(char_list(word[4:6]))
        return word
#21 beddua - CVCCVV
    elif sayi == 6 and annotate(word) == "CVCCVV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:6]))
        return word
#22 spreyi - CCCVCV
    elif sayi == 6 and annotate(word) == "CCCVCV":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:6]))
        return word
#23 egoist - VCVVCC
    elif sayi == 6 and annotate(word) == "VCVVCC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:6]))
        return word
#24 ekstra - VCCCCV
    elif sayi == 6 and annotate(word) == "VCCCCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:6]))
        return word
#25 maaile - CVVVCV
    elif sayi == 6 and annotate(word) == "CVVVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2]))+ "-" + "".join(char_list(word[3])) + "-" + "".join(char_list(word[4:6]))
        return word
#26 aortla - VVCCCV
    elif sayi == 6 and annotate(word) == "VVCCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4]))+ "-" + "".join(char_list(word[4:6]))
        return word
#27 oktrua - VCCCVV
    elif sayi == 6 and annotate(word) == "VCCCVV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5]))+ "-" + "".join(char_list(word[5:6]))
        return word
#28 taoizm - CVVVCC
    elif sayi == 6 and annotate(word) == "CVVVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2]))+ "-" + "".join(char_list(word[3:6]))
        return word
#29 stereo - CCVCVV
    elif sayi == 6 and annotate(word) == "CCVCVV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5]))+ "-" + "".join(char_list(word[5:6]))
        return word

################# 7 ###################
# required rule: 46 #
#1 yönetim - CVCVCVC
    elif sayi == 7 and annotate(word) == "CVCVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:7]))
        return word
#2 zatürre - CVCVCCV
    elif sayi == 7 and annotate(word) == "CVCVCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#3 zırvana - CVCCVCV
    elif sayi == 7 and annotate(word) == "CVCCVCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#4 ölçüsel - VCCVCVC
    elif sayi == 7 and annotate(word) == "VCCVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:7]))
        return word
#5 özellik - VCVCCVC
    elif sayi == 7 and annotate(word) == "VCVCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:7]))
        return word
#6 üretici - VCVCVCV
    elif sayi == 7 and annotate(word) == "VCVCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#7 ürküntü - VCCVCCV
    elif sayi == 7 and annotate(word) == "VCCVCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#8 kurtçuk - CVCCCVC
    elif sayi == 7 and annotate(word) == "CVCCCVC":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:7]))
        return word
#9 kruvaze - CCVCVCV
    elif sayi == 7 and annotate(word) == "CCVCVCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#10 krampon - CCVCCVC
    elif sayi == 7 and annotate(word) == "CCVCCVC":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:7]))
        return word
#11 teessüf - CVVCCVC
    elif sayi == 7 and annotate(word) == "CVVCCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:7]))
        return word
#12 zooloji - CVVCVCV
    elif sayi == 7 and annotate(word) == "CVVCVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#13 enstitü - VCCCVCV
    elif sayi == 7 and annotate(word) == "VCCCVCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#14 cezaevi - CVCVVCV
    elif sayi == 7 and annotate(word) == "CVCVVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#15 ağartma - VCVCCCV
    elif sayi == 7 and annotate(word) == "VCVCCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#16 satranç - CVCCVCC
    elif sayi == 7 and annotate(word) == "CVCCVCC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:7]))
        return word
#17 kramplı - CCVCCCV
    elif sayi == 7 and annotate(word) == "CCVCCCV":
        word = "".join(char_list(word[0:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#18 ailesel - VVCVCVC
    elif sayi == 7 and annotate(word) == "VVCVCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:7]))
        return word
#19 orduevi - VCCVVCV
    elif sayi == 7 and annotate(word) == "VCCVVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#20 penguen - CVCCVVC
    elif sayi == 7 and annotate(word) == "CVCCVVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#21 itaatçi - VCVVCCV
    elif sayi == 7 and annotate(word) == "VCVVCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#22 ideolog - VCVVCVC
    elif sayi == 7 and annotate(word) == "VCVVCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:7]))
        return word
#23 ailemle - VVCVCCV
    elif sayi == 7 and annotate(word) == "VVCVCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#24 ekinoks - VCVCVCC
    elif sayi == 7 and annotate(word) == "VCVCVCC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:7]))
        return word
#25 maestro - CVVCCCV
    elif sayi == 7 and annotate(word) == "CVVCCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#26 kreatif - CCVVCVC
    elif sayi == 7 and annotate(word) == "CCVVCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:7]))
        return word
#27 stresli - CCCVCCV
    elif sayi == 7 and annotate(word) == "CCCVCCV":
        word = "".join(char_list(word[0:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#28 aitliğe - VVCCVCV
    elif sayi == 7 and annotate(word) == "VVCCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#29 müdafaa - CVCVCVV
    elif sayi == 7 and annotate(word) == "CVCVCVV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:7]))
        return word
#30 frekans - CCVCVCC
    elif sayi == 7 and annotate(word) == "CCVCVCC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:7]))
        return word
#31 karstlı - CVCCCCV
    elif sayi == 7 and annotate(word) == "CVCCCCV":
        word = "".join(char_list(word[0:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#32 dadaizm - CVCVVCC
    elif sayi == 7 and annotate(word) == "CVCVVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:7]))
        return word
#33 flüorla - CCVVCCV
    elif sayi == 7 and annotate(word) == "CCVVCCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#34 stresin - CCCVCVC
    elif sayi == 7 and annotate(word) == "CCCVCVC":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:7]))
        return word
#35 suikast - CVVCVCC
    elif sayi == 7 and annotate(word) == "CVVCVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:7]))
        return word
#36 ekspres - VCCCCVC
    elif sayi == 7 and annotate(word) == "VCCCCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:7]))
        return word
#37 iptidai - VCCVCVV
    elif sayi == 7 and annotate(word) == "VCCVCVV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:7]))
        return word
#38 aysberg - VCCCVCC
    elif sayi == 7 and annotate(word) == "VCCCVCC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:7]))
        return word
#39 aorttan - VVCCCVC
    elif sayi == 7 and annotate(word) == "VVCCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:7]))
        return word
#40 geoidin - CVVVCVC
    elif sayi == 7 and annotate(word) == "CVVVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:7]))
        return word
#41 protein - CCVCVVC
    elif sayi == 7 and annotate(word) == "CCVCVVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#42 aneroit - VCVCVVC
    elif sayi == 7 and annotate(word) == "VCVCVVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#43 arkaizm - VCCVVCC
    elif sayi == 7 and annotate(word) == "VCCVVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:7]))
        return word
#44 ansambl - VCCVCCC
    elif sayi == 7 and annotate(word) == "VCCVCCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:7]))
        return word
#45 geoitle - CVVVCCV
    elif sayi == 7 and annotate(word) == "CVVVCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7]))
        return word
#46 neozoik - CVVCVVC
    elif sayi == 7 and annotate(word) == "CVVCVVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7]))
        return word

################# 8 ###################
# required rule: 62 #
#1 yıldırım - CVCCVCVC
    elif sayi == 8 and annotate(word) == "CVCCVCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:8]))
        return word
#2 zararsız - CVCVCCVC
    elif sayi == 8 and annotate(word) == "CVCVCCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:8]))
        return word
#3 -4 -5 -6 -7 -8 -9  tarayıcı - CVCVCVCV | özverili - VCCVCVCV | diaspora - CVVCCVCV | pediatri - CVCVVCCV | arkaüstü - VCCVVCCV | müracaat - CVCVCVVC | aksesuar - VCCVCVVC
    elif sayi == 8 and annotate(word) == "CVCVCVCV" or annotate(word) == "VCCVCVCV" or annotate(word) == "CVVCCVCV" or annotate(word) == "CVCVVCCV" or annotate(word) == "VCCVVCCV" or annotate(word) == "CVCVCVVC" or annotate(word) == "VCCVCVVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8]))
        return word
#10 -11 - zindancı - CVCCVCCV | üstlenme - VCCCVCCV
    elif sayi == 8 and annotate(word) == "CVCCVCCV" or annotate(word) == "VCCCVCCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:8]))
        return word
#12 uyarılar - VCVCVCVC
    elif sayi == 8 and annotate(word) == "VCVCVCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:8]))
        return word
#13 - 14 üsteğmen - VCCVCCVC | deistler - CVVCCCVC
    elif sayi == 8 and annotate(word) == "VCCVCCVC" or annotate(word) == "CVVCCCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:8]))
        return word
#15 - 16 - 17 üfürükçü - VCVCVCCV | egoistçe - VCVVCCCV | aitlerdi - VVCCVCCV
    elif sayi == 8 and annotate(word) == "VCVCVCCV" or annotate(word) == "VCVVCCCV" or annotate(word) == "VVCCVCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:8]))
        return word
#18 - 19 -20 özetleme - VCVCCVCV | akordeon - VCVCCVVC | aorttaki - VVCCCVCV
    elif sayi == 8 and annotate(word) == "VCVCCVCV" or annotate(word) == "VCVCCVVC" or annotate(word) == "VVCCCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8]))
        return word
#21 - 22 - 23 -24 - 25 - 26 denklemi - CVCCCVCV | presleme - CCVCCVCV | ekstralı - VCCCCVCV | strateji - CCCVCVCV | pankreas - CVCCCVVC | frambuaz - CCVCCVVC
    elif sayi == 8 and annotate(word) == "CVCCCVCV" or annotate(word) == "CCVCCVCV" or annotate(word) == "VCCCCVCV" or annotate(word) == "CCCVCVCV" or annotate(word) == "CVCCCVVC" or annotate(word) == "CCVCCVVC":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8]))
        return word
#27 kraterli - CCVCVCCV
    elif sayi == 8 and annotate(word) == "CCVCVCCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:8]))
        return word
#28 - 29 - 30 - 31 prosedür - CCVCVCVC | antrikot - VCCCVCVC | triatlon - CCVVCCVC | panteizm - CVCCVVCC
    elif sayi == 8 and annotate(word) == "CCVCVCVC" or annotate(word) == "VCCCVCVC" or annotate(word) == "CCVVCCVC" or annotate(word) == "CVCCVVCC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:8]))
        return word
#32 -33 yanıltma - CVCVCCCV | asbestli - VCCVCCCV
    elif sayi == 8 and annotate(word) == "CVCVCCCV" or annotate(word) == "VCCVCCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:6])) + "-" + "".join(char_list(word[6:8]))
        return word
#34 - 35 kainatın - CVVCVCVC | geoitler - CVVVCCVC
    elif sayi == 8 and annotate(word) == "CVVCVCVC" or annotate(word) == "CVVVCCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:8]))
        return word
#36 fiilimsi - CVVCVCCV
    elif sayi == 8 and annotate(word) == "CVVCVCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:8]))
        return word
#37 elektron - VCVCCCVC
    elif sayi == 8 and annotate(word) == "VCVCCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:5])) + "-" + "".join(char_list(word[5:8]))
        return word
#38 füzeatan - CVCVVCVC
    elif sayi == 8 and annotate(word) == "CVCVVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:5])) + "-" + "".join(char_list(word[5:8]))
        return word
#39 -40 - 41 tramplen - CCVCCCVC | stresten - CCCVCCVC | angström - VCCCCCVC
    elif sayi == 8 and annotate(word) == "CCVCCCVC" or annotate(word) == "CCCVCCVC" or annotate(word) == "VCCCCCVC":
        word = "".join(char_list(word[0:5])) + "-" + "".join(char_list(word[5:8]))
        return word
#42 - 43 dünyaevi - CVCCVVCV | proteini - CCVCVVCV
    elif sayi == 8 and annotate(word) == "CVCCVVCV" or annotate(word) == "CCVCVVCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:6])) + "-" + "".join(char_list(word[6:8]))
        return word
#44 - 45 - 46 piyanist - CVCVCVCC | atletizm - VCCVCVCC | reeskont - CVVCCVCC
    elif sayi == 8 and annotate(word) == "CVCVCVCC" or annotate(word) == "VCCVCVCC" or annotate(word) == "CVVCCVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:8]))
        return word
#47 aeroloji - VVCVCVCV
    elif sayi == 8 and annotate(word) == "VVCVCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8]))
        return word
#48 -49 - 50 itaatsiz - VCVVCCVC | aitçilik - VVCCVCVC | ilanıaşk - VCVCVVCC
    elif sayi == 8 and annotate(word) == "VCVVCCVC" or annotate(word) == "VVCCVCVC" or annotate(word) == "VCVCVVCC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:8]))
        return word
#51 arkeolog - VCCVVCVC
    elif sayi == 8 and annotate(word) == "VCCVVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:5])) + "-" + "".join(char_list(word[5:8]))
        return word
#52 ideoloji - VCVVCVCV
    elif sayi == 8 and annotate(word) == "VCVVCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8]))
        return word
#53 aidatsız - VVCVCCVC
    elif sayi == 8 and annotate(word) == "VVCVCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:8]))
        return word
#54 -55 -56 tungsten - CVCCCCVC | kontrast - CVCCCVCC | greyfurt - CCVCCVCC
    elif sayi == 8 and annotate(word) == "CVCCCCVC" or annotate(word) == "CVCCCVCC" or annotate(word) == "CCVCCVCC":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:8]))
        return word
#57 kreozotu - CCVVCVCV
    elif sayi == 8 and annotate(word) == "CCVVCVCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8]))
        return word
#58 anarşist - VCVCCVCC
    elif sayi == 8 and annotate(word) == "VCVCCVCC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:8]))
        return word
#59 maailece - CVVVCVCV
    elif sayi == 8 and annotate(word) == "CVVVCVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8]))
        return word
#60 idealist - VCVVCVCC
    elif sayi == 8 and annotate(word) == "VCVVCVCC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:8]))
        return word
#61 istisnai - VCCVCCVV
    elif sayi == 8 and annotate(word) == "VCCVCCVV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:8]))
        return word
#62 kontekst - CVCCVCCC
    elif sayi == 8 and annotate(word) == "CVCCVCCC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:8]))
        return word

################# 9 ###################
# required rule: 97 #
    elif sayi == 9 and word[-4:] == "spor" and annotate(word) == "CVCCVCCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:9]))
        return word
# 1 - 2 - 3 - 4 - 5 - 6 -7 - 8 - 9
# psikoloji - CCVCVCVCV | astronomi - VCCCVCVCV | kubbealtı - CVCCVVCCV | proteinli - CCVCVVCCV | devridaim - CVCCVCVVC | espritüel - VCCCVCVVC | kreasyonu - CCVVCCVCV | enflüanza - VCCCVVCCV | spiritüel - CCVCVCVVC
    elif sayi == 9 and annotate(word) == "CCVCVCVCV" or annotate(word) == "VCCCVCVCV" or annotate(word) == "CVCCVVCCV" or annotate(word) == "CCVCVVCCV" or annotate(word) == "CVCCVCVVC" or annotate(word) == "VCCCVCVVC" or annotate(word) == "CCVVCCVCV"  or annotate(word) == "VCCCVVCCV" or annotate(word) == "CCVCVCVVC" :
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 10 - 11 - 12 - 13 - 14 - 15 - 16
# yaşanacak - CVCVCVCVC | özverisiz - VCCVCVCVC | teokratik - CVVCCVCVC | vukuatsız - CVCVVCCVC | politeist - CVCVCVVCC | amfiteatr - VCCVCVVCC | ivmeölçer - VCCVVCCVC
    elif sayi == 9 and annotate(word) == "CVCVCVCVC" or annotate(word) == "VCCVCVCVC" or annotate(word) == "CVVCCVCVC" or annotate(word) == "CVCVVCCVC" or annotate(word) == "CVCVCVVCC" or annotate(word) == "VCCVCVVCC" or annotate(word) == "VCCVVCCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:9]))
        return word
# 17 - 18 - 19 - 20 - 21
# vedalaşma - CVCVCVCCV | uydurukçu - VCCVCVCCV | taahhütlü - CVVCCVCCV | poliandri - CVCVVCCCV | arkaizmle - VCCVVCCCV
    elif sayi == 9 and annotate(word) == "CVCVCVCCV" or annotate(word) == "VCCVCVCCV" or annotate(word) == "CVVCCVCCV" or annotate(word) == "CVCVVCCCV" or annotate(word) == "VCCVVCCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 22 - 23 - 24 - 25
# cıvıltılı - CVCVCCVCV | ısmarlama - VCCVCCVCV | seansları - CVVCCCVCV | rezervuar - CVCVCCVVC |
    elif sayi == 9 and annotate(word) == "CVCVCCVCV" or annotate(word) == "VCCVCCVCV" or annotate(word) == "CVVCCCVCV" or annotate(word) == "CVCVCCVVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 26 - 27 - 28
# kamuoyuna - CVCVVCVCV | arkeoloji - VCCVVCVCV | paleozoik - CVCVVCVVC
    elif sayi == 9 and annotate(word) == "CVCVVCVCV"  or annotate(word) == "VCCVVCVCV" or annotate(word) == "CVCVVCVVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 29 - 30 - 31 - 32
# rastlaşıp - CVCCCVCVC | gladyatör - CCVCCVCVC | enstrüman - VCCCCVCVC | stratejik - CCCVCVCVC |
    elif sayi == 9 and annotate(word) == "CVCCCVCVC" or annotate(word) == "CCVCCVCVC" or annotate(word) == "VCCCCVCVC" or annotate(word) == "CCCVCVCVC":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:9]))
        return word
# 33 - 34 - 35
# gerdirtme - CVCCVCCCV | ekspresti - VCCCCVCCV | arttırttı - VCCCVCCCV |
    elif sayi == 9 and annotate(word) == "CVCCVCCCV" or annotate(word) == "VCCCCVCCV" or annotate(word) == "VCCCVCCCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 36 - 37 - 38
# muadilini - CVVCVCVCV | geoitleri - CVVVCCVCV | neozoikte - CVVCVVCCV |
    elif sayi == 9 and annotate(word) == "CVVCVCVCV" or annotate(word) == "CVVVCCVCV" or annotate(word) == "CVVCVVCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 39 - 40 - 41 - 42 - 43
# branşları - CCVCCCVCV | spreyleme - CCCVCCVCV | kontrpiye - CVCCCCVCV | angströme - VCCCCCVCV | kontrpuan - CVCCCCVVC |
    elif sayi == 9 and annotate(word) == "CCVCCCVCV" or annotate(word) == "CCCVCCVCV" or annotate(word) == "CVCCCCVCV" or annotate(word) == "VCCCCCVCV" or annotate(word) == "CVCCCCVVC":
        word = "".join(char_list(word[0:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 44 - 45 - 46
# yırtmaçlı - CVCCCVCCV | programlı - CCVCCVCCV | stresimle - CCCVCVCCV |
    elif sayi == 9 and annotate(word) == "CVCCCVCCV" or annotate(word) == "CCVCCVCCV" or annotate(word) == "CCCVCVCCV":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 47 - 48 - 49
# etimoloji - VCVCVCVCV | aitliğimi - VVCCVCVCV | uruguaylı - VCVCVVCCV |
    elif sayi == 9 and annotate(word) == "VCVCVCVCV" or annotate(word) == "VVCCVCVCV" or annotate(word) == "VCVCVVCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 50 - 51 - 52
# reformist - CVCVCCVCC | eklektizm - VCCVCCVCC | reeksport - CVVCCCVCC |
    elif sayi == 9 and annotate(word) == "CVCVCCVCC" or annotate(word) == "VCCVCCVCC" or annotate(word) == "CVVCCCVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:9]))
        return word
# 53 - 54
# ideografi - VCVVCCVCV | areometre - VCVVCVCCV |
    elif sayi == 9 and annotate(word) == "VCVVCCVCV" or annotate(word) == "VCVVCVCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 55 - 56
# mumaileyh - CVCVVCVCC | aktüalizm - VCCVVCVCC |
    elif sayi == 9 and annotate(word) == "CVCVVCVCC" or annotate(word) == "VCCVVCVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:5])) + "-" + "".join(char_list(word[5:9]))
        return word
# 57 - 58
# pankreası - CVCCCVVCV | frambuazı - CCVCCVVCV |
    elif sayi == 9 and annotate(word) == "CVCCCVVCV" or annotate(word) == "CCVCCVVCV":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 59 - 60 - 61
# zorlaşmak - CVCCVCCVC | traverten - CCVCVCCVC | enflasyon - VCCCVCCVC |
    elif sayi == 9 and annotate(word) == "CVCCVCCVC" or annotate(word) == "CCVCVCCVC" or annotate(word) == "VCCCVCCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:9]))
        return word
# 62 - 63
# böğürtlen - CVCVCCCVC | eksiltmek - VCCVCCCVC |
    elif sayi == 9 and annotate(word) == "CVCVCCCVC" or annotate(word) == "VCCVCCCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:6])) + "-" + "".join(char_list(word[6:9]))
        return word
# 64 - 65
# vandalizm - CVCCVCVCC | kloroform - CCVCVCVCC |
    elif sayi == 9 and annotate(word) == "CVCCVCVCC" or annotate(word) == "CCVCVCVCC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:9]))
        return word
# 66 - 67
# meşruiyet - CVCCVVCVC | stereotip - CCVCVVCVC |
    elif sayi == 9 and annotate(word) == "CVCCVVCVC" or annotate(word) == "CCVCVVCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:6])) + "-" + "".join(char_list(word[6:9]))
        return word
# 68 - 69
# otobüsler - VCVCVCCVC | aitsizlik - VVCCVCCVC |
    elif sayi == 9 and annotate(word) == "VCVCVCCVC" or annotate(word) == "VVCCVCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:9]))
        return word
# 70 - 71
# araştırma - VCVCCVCCV | aortlarda - VVCCCVCCV |
    elif sayi == 9 and annotate(word) == "VCVCCVCCV" or annotate(word) == "VVCCCVCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 72 - 73
# iadeleşme - VVCVCVCCV | ailelerin - VVCVCVCVC |
    elif sayi == 9 and annotate(word) == "VVCVCVCCV" or annotate(word) == "VVCVCVCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:7]))  + "-" + "".join(char_list(word[7:9]))
        return word
# 74 - 75
# mütalaası - CVCVCVVCV | aksesuarı - VCCVCVVCV |
    elif sayi == 9 and annotate(word) == "CVCVCVVCV" or annotate(word) == "VCCVCVVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:7]))  + "-" + "".join(char_list(word[7:9]))
        return word
# 76
# jeotermal - CVVCVCCVC |
    elif sayi == 9 and annotate(word) == "CVVCVCCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:9]))
        return word
# 77
# abartmama - VCVCCCVCV |
    elif sayi == 9 and annotate(word) == "VCVCCCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 78
# atatürkçü - VCVCVCCCV |
    elif sayi == 9 and annotate(word) == "VCVCVCCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 79
# ideolojik - VCVVCVCVC |
    elif sayi == 9 and annotate(word) == "VCVVCVCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:6]))  + "-" + "".join(char_list(word[6:9]))
        return word
# 80
# bahriyeci - CVCCVCVCV |
    elif sayi == 9 and annotate(word) == "CVCCVCVCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 81
# uzaylılar - VCVCCVCVC |
    elif sayi == 9 and annotate(word) == "VCVCCVCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:9]))
        return word
# 82
# ailemdeki - VVCVCCVCV |
    elif sayi == 9 and annotate(word) == "VVCVCCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 83
# egoistlik - VCVVCCCVC |
    elif sayi == 9 and annotate(word) == "VCVVCCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:9]))
        return word
# 84
# traversli - CCVCVCCCV |
    elif sayi == 9 and annotate(word) == "CCVCVCCCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 85
# suikastçı - CVVCVCCCV |
    elif sayi == 9 and annotate(word) == "CVVCVCCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 86
# stoacılık - CCVVCVCVC |
    elif sayi == 9 and annotate(word) == "CCVVCVCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:9]))
        return word
# 87
# kreozotla - CCVVCVCCV |
    elif sayi == 9 and annotate(word) == "CCVVCVCCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 88
# ekonomist - VCVCVCVCC |
    elif sayi == 9 and annotate(word) == "VCVCVCVCC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:9]))
        return word
# 89
# feodalizm - CVVCVCVCC |
    elif sayi == 9 and annotate(word) == "CVVCVCVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:9]))
        return word
# 90
# aminoasit - VCVCVVCVC |
    elif sayi == 9 and annotate(word) == "VCVCVVCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:6])) + "-" + "".join(char_list(word[6:9]))
        return word
# 91
# akordeonu - VCVCCVVCV |
    elif sayi == 9 and annotate(word) == "VCVCCVVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:7])) + "-" + "".join(char_list(word[7:9]))
        return word
# 92
# geoidinin - CVVVCVCVC |
    elif sayi == 9 and annotate(word) == "CVVVCVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:9]))
        return word
# 93
# maaileydi - CVVVCVCCV |
    elif sayi == 9 and annotate(word) == "CVVVCVCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:9]))
        return word
# 94
# megahertz - CVCVCVCCC |
    elif sayi == 9 and annotate(word) == "CVCVCVCCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:9]))
        return word
# 95
# hornblent - CVCCCCVCC |
    elif sayi == 9 and annotate(word) == "CVCCCCVCC":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:9]))
        return word
# 96
# kontrplak - CVCCCCCVC | transport - CCVCCCVCC |
    elif sayi == 9 and annotate(word) == "CVCCCCCVC" or annotate(word) == "CCVCCCVCC":
        word = "".join(char_list(word[0:5])) + "-" + "".join(char_list(word[5:9]))
        return word
# 97
# sfenksler - CCVCCCCVC |
    elif sayi == 9 and annotate(word) == "CCVCCCCVC":
        word = "".join(char_list(word[0:6])) + "-" + "".join(char_list(word[6:9]))
        return word

################# 10 ###################
# required rule: 125 #
# 1 - 2 - 3 - 4 - 5 - 6 -7 - 8 - 9
#  rölativite - CVCVCVCVCV | aykırılama - VCCVCVCVCV | zaaflarını - CVVCCVCVCV | mozaiklere - CVCVVCCVCV | anneanneme - VCCVVCCVCV | paraguaylı - CVCVCVVCCV | aksesuarcı - VCCVCVVCCV | paraboloit - CVCVCVCVVC | odyovizüel - VCCVCVCVVC
    elif sayi == 10 and annotate(word) == "CVCVCVCVCV" or annotate(word) == "VCCVCVCVCV" or annotate(word) == "CVVCCVCVCV"\
            or annotate(word) == "CVCVVCCVCV"\
            or annotate(word) == "VCCVVCCVCV"\
            or annotate(word) == "CVCVCVVCCV"\
            or annotate(word) == "VCCVCVVCCV"\
            or annotate(word) == "CVCVCVCVVC"\
            or annotate(word) == "VCCVCVCVVC" :
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 10 - 11 - 12 - 13 - 14 - 15 - 16
#  çiftçimize - CVCCCVCVCV | enstrümanı - VCCCCVCVCV | stokçuluğa - CCVCCVCVCV | stratejisi - CCCVCVCVCV | pankreasçı - CVCCCVVCCV | frambuazlı - CCVCCVVCCV | kristaloit - CCVCCVCVVC
    elif sayi == 10 and annotate(word) == "CVCCCVCVCV" or annotate(word) == "VCCCCVCVCV" or annotate(word) == "CCVCCVCVCV"\
            or annotate(word) == "CCCVCVCVCV"\
            or annotate(word) == "CVCCCVVCCV"\
            or annotate(word) == "CCVCCVVCCV"\
            or annotate(word) == "CCVCCVCVVC":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 10 - 11 - 12 - 13 - 14 - 15
#  zırdelilik - CVCCVCVCVC | grekoromen - CCVCVCVCVC | altyapısal - VCCCVCVCVC | penguenler - CVCCVVCCVC | stereoskop - CCVCVVCCVC | pleistosen - CCVVCCVCVC
    elif sayi == 10 and annotate(word) == "CVCCVCVCVC" or annotate(word) == "CCVCVCVCVC" or annotate(word) == "VCCCVCVCVC"\
            or annotate(word) == "CVCCVVCCVC"\
            or annotate(word) == "CCVCVVCCVC"\
            or annotate(word) == "CCVVCCVCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 16 - 17 - 18 - 19 - 20
#  sığışırdık - CVCVCVCCVC | ampütasyon - VCCVCVCCVC | muallimlik - CVVCCVCCVC | veliahtlık - CVCVVCCCVC | arkaizmdir - VCCVVCCCVC
    elif sayi == 10 and annotate(word) == "CVCVCVCCVC" or annotate(word) == "VCCVCVCCVC" or annotate(word) == "CVVCCVCCVC"\
            or annotate(word) == "CVCVVCCCVC"\
            or annotate(word) == "VCCVVCCCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 21 - 22 - 23 - 24 - 25
#  tutkuluydu - CVCCVCVCCV | grafometre - CCVCVCVCCV | örtmedikçe - VCCCVCVCCV | panteistçe - CVCCVVCCCV | kreasyonda - CCVVCCVCCV
    elif sayi == 10 and annotate(word) == "CVCCVCVCCV" or annotate(word) == "CCVCVCVCCV" or annotate(word) == "VCCCVCVCCV"\
            or annotate(word) == "CVCCVVCCCV"\
            or annotate(word) == "CCVVCCVCCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 26 - 27 - 28 - 29
#  yüzüklerin - CVCVCCVCVC | eklentisel - VCCVCCVCVC | deistlerin - CVVCCCVCVC | empermeabl - VCCVCCVVCC
    elif sayi == 10 and annotate(word) == "CVCVCCVCVC" or annotate(word) == "VCCVCCVCVC" or annotate(word) == "CVVCCCVCVC"\
            or annotate(word) == "VCCVCCVVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 30 - 31 - 32 - 33
#  hangardaki - CVCCVCCVCV | gravürleri - CCVCVCCVCV | antlaşmada - VCCCVCCVCV | semtürreis - CVCCVCCVVC
    elif sayi == 10 and annotate(word) == "CVCCVCCVCV" or annotate(word) == "CCVCVCCVCV" or annotate(word) == "VCCCVCCVCV"\
            or annotate(word) == "CVCCVCCVVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 34 - 35 - 36 - 37
#  etimolojik - VCVCVCVCVC | idealleşen - VCVVCCVCVC | aitliğimin - VVCCVCVCVC | izazuikram - VCVCVVCCVC
    elif sayi == 10 and annotate(word) == "VCVCVCVCVC" or annotate(word) == "VCVVCCVCVC" or annotate(word) == "VVCCVCVCVC"\
            or annotate(word) == "VCVCVVCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 38 - 39 - 40 - 41
#  kırlentler - CVCCVCCCVC | frekanslar - CCVCVCCCVC | eksprestir - VCCCCVCCVC | ölçtürtmek - VCCCVCCCVC
    elif sayi == 10 and annotate(word) == "CVCCVCCCVC" or annotate(word) == "CCVCVCCCVC" or annotate(word) == "VCCCCVCCVC" \
             or annotate(word) == "VCCCVCCCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 42 - 43 - 44
#  uyuşturucu - VCVCCVCVCV | akordeoncu - VCVCCVVCCV | aortlarına - VVCCCVCVCV
    elif sayi == 10 and annotate(word) == "VCVCCVCVCV" or annotate(word) == "VCVCCVVCCV" or annotate(word) == "VVCCCVCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 45 - 46 - 47
#  garipleşme - CVCVCCVCCV | uzmanlarca - VCCVCCVCCV | nüanslarda - CVVCCCVCCV
    elif sayi == 10 and annotate(word) == "CVCVCCVCCV" or annotate(word) == "VCCVCCVCCV" or annotate(word) == "CVVCCCVCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 48 - 49 - 50
#  ifadesizce - VCVCVCVCCV | ısıölçerle - VCVVCCVCCV | aitliğiyle - VVCCVCVCCV
    elif sayi == 10 and annotate(word) == "VCVCVCVCCV" or annotate(word) == "VCVVCCVCCV" or annotate(word) == "VVCCVCVCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 51 - 52 - 53
#  imalathane - VCVCVCCVCV | egoistleri - VCVVCCCVCV | aitsizliği - VVCCVCCVCV
    elif sayi == 10 and annotate(word) == "VCVCVCCVCV" or annotate(word) == "VCVVCCCVCV" or annotate(word) == "VVCCVCCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 54 - 55 - 56
#  popülistçe - CVCVCVCCCV | aspidistra - VCCVCVCCCV | reeskontlu - CVVCCVCCCV
    elif sayi == 10 and annotate(word) == "CVCVCVCCCV" or annotate(word) == "VCCVCVCCCV" or annotate(word) == "CVVCCVCCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 57 - 58 - 59
#  spektrumun - CCVCCCVCVC | streptokok - CCCVCCVCVC | karstlaşan - CVCCCCVCVC
    elif sayi == 10 and annotate(word) == "CCVCCCVCVC" or annotate(word) == "CCCVCCVCVC" or annotate(word) == "CVCCCCVCVC":
        word = "".join(char_list(word[0:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 60 - 61 - 62
#  feldspatlı - CVCCCCVCCV | platformda - CCVCCVCCCV | kompleksli - CVCCCVCCCV
    elif sayi == 10 and annotate(word) == "CVCCCCVCCV" or annotate(word) == "CCVCCVCCCV" or annotate(word) == "CVCCCVCCCV":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 63 - 64 - 65
#  yurttaşlık - CVCCCVCCVC | plastikler - CCVCCVCCVC | stratosfer - CCCVCVCCVC
    elif sayi == 10 and annotate(word) == "CVCCCVCCVC" or annotate(word) == "CCVCCVCCVC" or annotate(word) == "CCCVCVCCVC":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 66 - 67
#  şaşırtsana - CVCVCCCVCV | açtırtmama - VCCVCCCVCV
    elif sayi == 10 and annotate(word) == "CVCVCCCVCV" or annotate(word) == "VCCVCCCVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 68 - 69
#  meteorolog - CVCVVCVCVC | osteolojik - VCCVVCVCVC
    elif sayi == 10 and annotate(word) == "CVCVVCVCVC" or annotate(word) == "VCCVVCVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 70 - 71
#  biyoenerji - CVCVVCVCCV | arkeometri - VCCVVCVCCV
    elif sayi == 10 and annotate(word) == "CVCVVCVCCV" or annotate(word) == "VCCVVCVCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:5])) + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 72 - 73
#  sürrealite - CVCCVVCVCV | stereofoni - CCVCVVCVCV
    elif sayi == 10 and annotate(word) == "CVCCVVCVCV" or annotate(word) == "CCVCVVCVCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 74 - 75
#  tramplenci - CCVCCCVCCV | kontrplağı - CVCCCCCVCV
    elif sayi == 10 and annotate(word) == "CCVCCCVCCV" or annotate(word) == "CVCCCCCVCV":
        word = "".join(char_list(word[0:5])) + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 76 - 77
#  müracaatım - CVCVCVVCVC | aksesuarım - VCCVCVVCVC
    elif sayi == 10 and annotate(word) == "CVCVCVVCVC" or annotate(word) == "VCCVCVVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 78 - 79
#  pozitivist - CVCVCVCVCC | ortopedist - VCCVCVCVCC
    elif sayi == 10 and annotate(word) == "CVCVCVCVCC" or annotate(word) == "VCCVCVCVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:10]))
        return word
# 80 - 81
#  konformist - CVCCVCCVCC | kloroplast - CCVCVCCVCC
    elif sayi == 10 and annotate(word) == "CVCCVCCVCC" or annotate(word) == "CCVCVCCVCC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:10]))
        return word
# 82 - 83
#  fortepiano - CVCCVCVVCV | spiritüeli - CCVCVCVVCV
    elif sayi == 10 and annotate(word) == "CVCCVCVVCV" or annotate(word) == "CCVCVCVVCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 84 - 85
#  teferruata - CVCVCCVVCV | incirliova - VCCVCCVVCV
    elif sayi == 10 and annotate(word) == "CVCVCCVVCV" or annotate(word) == "VCCVCCVVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 86
#  elektronik - VCVCCCVCVC
    elif sayi == 10 and annotate(word) == "VCVCCCVCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 87
#  elektronik - CVVCVCVCCV
    elif sayi == 10 and annotate(word) == "CVVCVCVCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 88
#  elektrikli - VCVCCCVCCV
    elif sayi == 10 and annotate(word) == "VCVCCCVCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:5])) + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 89
#  kaotikliği - CVVCVCCVCV
    elif sayi == 10 and annotate(word) == "CVVCVCCVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 90
#  alüvyonsuz - VCVCCVCCVC
    elif sayi == 10 and annotate(word) == "VCVCCVCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 91
#  ebeveynlik - VCVCVCCCVC
    elif sayi == 10 and annotate(word) == "VCVCVCCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 92
#  aidiyetlik - VVCVCVCCVC
    elif sayi == 10 and annotate(word) == "VVCVCVCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 93
#  anaokuluna - VCVVCVCVCV
    elif sayi == 10 and annotate(word) == "VCVVCVCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 94
#  aidatınızı - VVCVCVCVCV
    elif sayi == 10 and annotate(word) == "VVCVCVCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 98
#  striptizci - CCCVCCVCCV
    elif sayi == 10 and annotate(word) == "CCCVCCVCCV":
        word = "".join(char_list(word[0:5])) + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 99
#  ideologlar - VCVVCVCCVC
    elif sayi == 10 and annotate(word) == "VCVVCVCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 100
#  anarşistçe - VCVCCVCCCV
    elif sayi == 10 and annotate(word) == "VCVCCVCCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 101
#  jeosantrik - CVVCVCCCVC
    elif sayi == 10 and annotate(word) == "CVVCVCCCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:7])) + "-" + "".join(char_list(word[7:10]))
        return word

# 102
#  kreatörler - CCVVCVCCVC
    elif sayi == 10 and annotate(word) == "CCVVCVCCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 103
#  ailendendi - VVCVCCVCCV
    elif sayi == 10 and annotate(word) == "VVCVCCVCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 104
#  aidatların - VVCVCCVCVC
    elif sayi == 10 and annotate(word) == "VVCVCCVCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 105
#  idealizmle - VCVVCVCCCV
    elif sayi == 10 and annotate(word) == "VCVVCVCCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 106
#  stoacılara - CCVVCVCVCV
    elif sayi == 10 and annotate(word) == "CCVVCVCVCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 107
#  aminoaside - VCVCVVCVCV
    elif sayi == 10 and annotate(word) == "VCVCVVCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 108
#  elipsoidal - VCVCCVVCVC
    elif sayi == 10 and annotate(word) == "VCVCCVVCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 109
#  oportünist - VCVCCVCVCC
    elif sayi == 10 and annotate(word) == "VCVCCVCVCC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:10]))
        return word
# 110
#  sürrealizm - CVCCVVCVCC
    elif sayi == 10 and annotate(word) == "CVCCVVCVCC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:6])) + "-" + "".join(char_list(word[6:10]))
        return word
# 111
#  postmodern - CVCCCVCVCC | pragmatizm - CCVCCVCVCC
    elif sayi == 10 and annotate(word) == "CVCCCVCVCC" or annotate(word) == "CCVCCVCVCC":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:10]))
        return word
# 112
#  gayritabii - CVCCVCVCVV
    elif sayi == 10 and annotate(word) == "CVCCVCVCVV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:10]))
        return word
# 113
#  sfenkslere - CCVCCCCVCV
    elif sayi == 10 and annotate(word) == "CCVCCCCVCV":
        word = "".join(char_list(word[0:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 114
#  paleozoiğe - CVCVVCVVCV
    elif sayi == 10 and annotate(word) == "CVCVVCVVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 115
#  kontekstle - CVCCVCCCCV
    elif sayi == 10 and annotate(word) == "CVCCVCCCCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 116
#  pankreasım - CVCCCVVCVC
    elif sayi == 10 and annotate(word) == "CVCCCVVCVC":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 117
#  kontrpuana - CVCCCCVVCV
    elif sayi == 10 and annotate(word) == "CVCCCCVVCV":
        word = "".join(char_list(word[0:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 118
#  otoerotizm - VCVVCVCVCC
    elif sayi == 10 and annotate(word) == "VCVVCVCVCC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:10]))
        return word
# 119
#  izomorfizm - VCVCVCCVCC
    elif sayi == 10 and annotate(word) == "VCVCVCCVCC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:10]))
        return word
# 120
#  maailenize - CVVVCVCVCV
    elif sayi == 10 and annotate(word) == "CVVVCVCVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 121
#  maaileydik - CVVVCVCCVC
    elif sayi == 10 and annotate(word) == "CVVVCVCCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:10]))
        return word
# 122
#  geoitlerin - CVVVCCVCVC
    elif sayi == 10 and annotate(word) == "CVVVCCVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:10]))
        return word
# 123
#  latifundia - CVCVCVCCVV
    elif sayi == 10 and annotate(word) == "CVCVCVCCVV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:10]))
        return word
# 124
#  getirttirt - CVCVCCCVCC
    elif sayi == 10 and annotate(word) == "CVCVCCCVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:6])) + "-" + "".join(char_list(word[6:10]))
        return word

# 125
#  amalierbaa - VCVCVVCCVV
    elif sayi == 10 and annotate(word) == "VCVCVVCCVV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:10]))
        return word


################# 11 ###################
# required rule: XXX #
# exception for spor

# 1 - 2 - 3
#  meteoroloji - CVCVVCVCVCV | iddianamede - VCCVVCVCVCV  | paleozoikte - CVCVVCVVCCV
    elif sayi == 11 and annotate(word) == "CVCVVCVCVCV" or annotate(word) == "VCCVVCVCVCV" or annotate(word) == "CVCVVCVVCCV" :
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 4 - 5
#  müdafaasına - CVCVCVVCVCV | aksesuarını - VCCVCVVCVCV
    elif sayi == 11 and annotate(word) == "CVCVCVVCVCV" or annotate(word) == "VCCVCVVCVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 6 - 7 - 8 - 9
#  otomobilini - VCVCVCVCVCV | ateizminizi - VCVVCCVCVCV  | aitliğimizi - VVCCVCVCVCV | onomatopeik - VCVCVCVCVVC
    elif sayi == 11 and annotate(word) == "VCVCVCVCVCV" or annotate(word) == "VCVVCCVCVCV" or annotate(word) == "VVCCVCVCVCV" or annotate(word) == "VCVCVCVCVVC" :
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 10 - 11 - 12 - 13 - 14 - 15 - 16
#  sıralamakta - CVCVCVCVCCV | ültimatomla - VCCVCVCVCCV  | müessesemde - CVVCCVCVCCV | masaüstünde - CVCVVCCVCCV | inşaatlaşma	- VCCVVCCVCCV | monoteizmde	- CVCVCVVCCCV | amfiteatrda - VCCVCVVCCCV
    elif sayi == 11 and annotate(word) == "CVCVCVCVCCV" or annotate(word) == "VCCVCVCVCCV" or annotate(word) == "CVVCCVCVCCV" or annotate(word) == "CVCVVCCVCCV"\
            or annotate(word) == "VCCVVCCVCCV" or annotate(word) == "CVCVCVVCCCV" or annotate(word) == "VCCVCVVCCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:9])) + "-" + "".join(char_list(word[9:11]))
        return word

# 17 - 18 - 19 - 20 - 21 - 22 - 23 - 24
# yüzyılımızı  - CVCCVCVCVCV | blokelediği - CCVCVCVCVCV  | antropoloji - VCCCVCVCVCV | penguenlere - CVCCVVCCVCV | kreasyonunu - CCVVCCVCVCV | zümrüdüanka - CVCCVCVVCCV | enflüanzaya - VCCCVVCCVCV | şeytanılain - CVCCVCVCVVC
    elif sayi == 11 and annotate(word) == "CVCCVCVCVCV" or annotate(word) == "CCVCVCVCVCV" or annotate(word) == "VCCCVCVCVCV" or annotate(word) == "CVCCVVCCVCV"\
            or annotate(word) == "CCVVCCVCVCV" or annotate(word) == "CVCCVCVVCCV" or annotate(word) == "VCCCVVCCVCV" or annotate(word) == "CVCCVCVCVVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 25 - 26 - 27 - 28 - 29 - 30
# aksesuarlar - VCCVCVVCCVC | hurafecilik - CVCVCVCVCVC | vukuatların - CVCVVCCVCVC | reaktörünün - CVVCCVCVCVC | ortaöğretim - VCCVVCCVCVC | devalüasyon - CVCVCVVCCVC
    elif sayi == 11 and annotate(word) == "VCCVCVVCCVC" or annotate(word) == "CVCVCVCVCVC" or annotate(word) == "CVCVVCCVCVC"\
            or annotate(word) == "CVVCCVCVCVC" or annotate(word) == "VCCVVCCVCVC" or annotate(word) == "CVCVCVVCCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 31 - 32 - 33 - 34 - 35
# rakiplerini - CVCVCCVCVCV | uzmanlığına - VCCVCCVCVCV | seanslarıma - CVVCCCVCVCV | herifçioğlu - CVCVCCVVCCV | hiperboloit - CVCVCCVCVVC
    elif sayi == 11 and annotate(word) == "CVCVCCVCVCV" or annotate(word) == "VCCVCCVCVCV" or annotate(word) == "CVVCCCVCVCV"\
            or annotate(word) == "CVCVCCVVCCV" or annotate(word) == "CVCVCCVCVVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 36 - 37 - 38 - 39 - 40
# yürüyenlere - CVCVCVCCVCV | muallaklığı - CVVCCVCCVCV | öldürülmesi - VCCVCVCCVCV | veliahtlığı - CVCVVCCCVCV | homoseksüel - CVCVCVCCVVC
    elif sayi == 11 and annotate(word) == "CVCVCVCCVCV" or annotate(word) == "CVVCCVCCVCV" or annotate(word) == "VCCVCVCCVCV"\
            or annotate(word) == "CVCVVCCCVCV" or annotate(word) == "CVCVCVCCVVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 41 - 42 - 43
# proteinimsi - CCVCVVCVCCV | beddualarla - CVCCVVCVCCV | stereografi - CCVCVVCCVCV
    elif sayi == 11 and annotate(word) == "CCVCVVCVCCV" or annotate(word) == "CVCCVVCVCCV" or annotate(word) == "CCVCVVCCVCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:6])) + "-" + "".join(char_list(word[6:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 44 - 45 - 46
# oluvermekte - VCVCVCCVCCV | egoistleşme - VCVVCCCVCCV | aitleştirme - VVCCVCCVCCV
    elif sayi == 11 and annotate(word) == "VCVCVCCVCCV" or annotate(word) == "VCVVCCCVCCV" or annotate(word) == "VVCCVCCVCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 47 - 48 - 49
# üreteçlerin - VCVCVCCVCVC | egoistliğin - VCVVCCCVCVC | aitleştiren - VVCCVCCVCVC
    elif sayi == 11 and annotate(word) == "VCVCVCCVCVC" or annotate(word) == "VCVVCCCVCVC" or annotate(word) == "VVCCVCCVCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 50 - 51 - 52
# ajitatörlük - VCVCVCVCCVC | itaatkarlık - VCVVCCVCCVC | aitsinizdir - VVCCVCVCCVC
    elif sayi == 11 and annotate(word) == "VCVCVCVCCVC" or annotate(word) == "VCVVCCVCCVC" or annotate(word) == "VVCCVCVCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 53 - 54
# meteoritler - CVCVVCVCCVC | antialerjik - VCCVVCVCCVC
    elif sayi == 11 and annotate(word) == "CVCVVCVCCVC" or annotate(word) == "VCCVVCVCCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:5])) + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 55 - 56
# proteininin - CCVCVVCVCVC | virtüözüdür - CVCCVVCVCVC
    elif sayi == 11 and annotate(word) == "CCVCVVCVCVC" or annotate(word) == "CVCCVVCVCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 57 - 58
# istisnaidir - VCCVCCVVCVC | rezervuarın - CVCVCCVVCVC
    elif sayi == 11 and annotate(word) == "VCCVCCVVCVC" or annotate(word) == "CVCVCCVVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 59 - 60
# aortlarının - VVCCCVCVCVC | açıkladılar - VCVCCVCVCVC | akordeonlar - VCVCCVVCCVC
    elif sayi == 11 and annotate(word) == "VVCCCVCVCVC" or annotate(word) == "VCVCCVCVCVC" or annotate(word) == "VCVCCVVCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 61 - 62
# aortlarında - VVCCCVCVCCV | üzüldüğümle - VCVCCVCVCCV
    elif sayi == 11 and annotate(word) == "VVCCCVCVCCV" or annotate(word) == "VCVCCVCVCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 62 - 63
# aortlarında - VVCCCVCVCCV | üzüldüğümle - VCVCCVCVCCV
    elif sayi == 11 and annotate(word) == "VVCCCVCVCCV" or annotate(word) == "VCVCCVCVCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 64 - 65 - 66 - 67 - 68
# kraliyettir - CCVCVCVCCVC | astrologlar - VCCCVCVCCVC | düzgüsellik - CVCCVCVCCVC | panteistlik - CVCCVVCCCVC | kreasyonlar - CCVVCCVCCVC
    elif sayi == 11 and annotate(word) == "CCVCVCVCCVC" or annotate(word) == "VCCCVCVCCVC" or annotate(word) == "CVCCVCVCCVC" or annotate(word) == "CVCCVVCCCVC" or annotate(word) == "CCVVCCVCCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 69 - 70 - 71
# yoksullukla - CVCCVCCVCCV | sloganlarla - CCVCVCCVCCV | enflasyonla - VCCCVCCVCCV
    elif sayi == 11 and annotate(word) == "CVCCVCCVCCV" or annotate(word) == "CCVCVCCVCCV" or annotate(word) == "VCCCVCCVCCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 72 - 73 - 74
# piknikçiler - CVCCVCCVCVC | ilkselcilik - VCCCVCCVCVC | primatların - CCVCVCCVCVC
    elif sayi == 11 and annotate(word) == "CVCCVCCVCVC" or annotate(word) == "VCCCVCCVCVC" or annotate(word) == "CCVCVCCVCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 75 - 76 - 77
# filizlenmek - CVCVCCVCCVC | üstünleşmek - VCCVCCVCCVC | deistlerden - CVVCCCVCCVC
    elif sayi == 11 and annotate(word) == "CVCVCCVCCVC" or annotate(word) == "VCCVCCVCCVC" or annotate(word) == "CVVCCCVCCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 78 - 79 - 80 - 81 - 82 - 83
# şartnameler - CVCCCVCVCVC | prangalamak - CCVCCVCVCVC | enstrümanım - VCCCCVCVCVC | stratejimiz - CCCVCVCVCVC | pankreastan - CVCCCVVCCVC | frambuazdan - CCVCCVVCCVC
    elif sayi == 11 and annotate(word) == "CVCCCVCVCVC" or annotate(word) == "CCVCCVCVCVC" or annotate(word) == "VCCCCVCVCVC" or annotate(word) == "CCCVCVCVCVC" or annotate(word) == "CVCCCVVCCVC" or annotate(word) == "CCVCCVVCCVC":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 84 - 85 - 86 - 87
# rastladıkça - CVCCCVCVCCV | planlamakta - CCVCCVCVCCV | ekstralarla - VCCCCVCVCCV | stratejikti - CCCVCVCVCCV
    elif sayi == 11 and annotate(word) == "CVCCCVCVCCV" or annotate(word) == "CCVCCVCVCCV" or annotate(word) == "VCCCCVCVCCV" or annotate(word) == "CCCVCVCVCCV":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 88 - 89 - 90 - 91
# kentleşmeye - CVCCCVCCVCV | klikleşmesi - CCVCCVCCVCV | stratosferi - CCCVCVCCVCV | ekstremliğe - VCCCCVCCVCV
    elif sayi == 11 and annotate(word) == "CVCCCVCCVCV" or annotate(word) == "CCVCCVCCVCV" or annotate(word) == "CCCVCVCCVCV" or annotate(word) == "VCCCCVCCVCV":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 92 - 93 - 94 - 95
# dikdörtgene - CVCCVCCCVCV | büktürttüğü - CVCCVCCCVCV | stilistliğe - CCVCVCCCVCV | ölçtürtmedi - VCCCVCCCVCV
    elif sayi == 11 and annotate(word) == "CVCCVCCCVCV" or annotate(word) == "CVCCVCCCVCV" or annotate(word) == "CCVCVCCCVCV" or annotate(word) == "VCCCVCCCVCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 96 - 97 - 98 - 99
# trençkotumu - CCVCCCVCVCV | streptokoka - CCCVCCVCVCV | kontrpiyede - CVCCCCVCVCV | kontrpuanlı - CVCCCCVVCCV
    elif sayi == 11 and annotate(word) == "CCVCCCVCVCV" or annotate(word) == "CCCVCCVCVCV" or annotate(word) == "CVCCCCVCVCV" or annotate(word) == "CVCCCCVVCCV":
        word = "".join(char_list(word[0:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 100 - 101 - 102
# popülistlik - CVCVCVCCCVC | ehlibeytten - VCCVCVCCCVC | reeskontlar - CVVCCVCCCVC
    elif sayi == 11 and annotate(word) == "CVCVCVCCCVC" or annotate(word) == "VCCVCVCCCVC" or annotate(word) == "CVVCCVCCCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 103 - 104 - 105
# primitivizm - CCVCVCVCVCC | nasyonalizm - CVCCVCVCVCC | anglikanizm - VCCCVCVCVCC
    elif sayi == 11 and annotate(word) == "CCVCVCVCVCC" or annotate(word) == "CVCCVCVCVCC" or annotate(word) == "VCCCVCVCVCC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:11]))
        return word
# 106 - 107
# reformculuk - CVCVCCCVCVC | asbestlidir - VCCVCCCVCVC
    elif sayi == 11 and annotate(word) == "CVCVCCCVCVC" or annotate(word) == "VCCVCCCVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 108 - 109
# dürüstleşme - CVCVCCCVCCV | ilginçleşti - VCCVCCCVCCV
    elif sayi == 11 and annotate(word) == "CVCVCCCVCCV" or annotate(word) == "VCCVCCCVCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:6])) + "-" + "".join(char_list(word[6:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 110 - 111
# emperyalizm - VCCVCCVCVCC | determinizm - CVCVCCVCVCC
    elif sayi == 11 and annotate(word) == "VCCVCCVCVCC" or annotate(word) == "CVCVCCVCVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:11]))
        return word
# 112 - 113
# putperestçe - CVCCVCVCCCV | kloroformlu - CCVCVCVCCCV
    elif sayi == 11 and annotate(word) == "CVCCVCVCCCV" or annotate(word) == "CCVCVCVCCCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 114 - 115
# metamorfizm - CVCVCVCCVCC | irredantizm - VCCVCVCCVCC
    elif sayi == 11 and annotate(word) == "CVCVCVCCVCC" or annotate(word) == "VCCVCVCCVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:11]))
        return word
# 116 - 117
# ayrıştırtma - VCCVCCVCCCV | monarşizmle - CVCVCCVCCCV
    elif sayi == 11 and annotate(word) == "VCCVCCVCCCV" or annotate(word) == "CVCVCCVCCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:5])) + "-" + "".join(char_list(word[5:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 118 - 119
# greyfurtlar - CCVCCVCCCVC | komplekstir - CVCCCVCCCVC
    elif sayi == 11 and annotate(word) == "CCVCCVCCCVC" or annotate(word) == "CVCCCVCCCVC":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 120 - 121 - 122 - 123
# branşlaşmak - CCVCCCVCCVC | stresliydim - CCCVCCVCCVC | karstlaşmış - CVCCCCVCCVC | kontrplağın - CVCCCCCVCVC
    elif sayi == 11 and annotate(word) == "CCVCCCVCCVC" or annotate(word) == "CCCVCCVCCVC" or annotate(word) == "CVCCCCVCCVC"  or annotate(word) == "CVCCCCCVCVC":
        word = "".join(char_list(word[0:5])) + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 124
# aposteriori - VCVCCVCVVCV
    elif sayi == 11 and annotate(word) == "VCVCCVCVVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:6])) + "-"\
               + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 125
# paleozoiğin - CVCVVCVVCVC
    elif sayi == 11 and annotate(word) == "CVCVVCVVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:5]))\
               + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 126
# geoidimizin - CVVVCVCVCVC
    elif sayi == 11 and annotate(word) == "CVVVCVCVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:4]))\
               + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 127
# aminoasidin - VCVCVVCVCVC
    elif sayi == 11 and annotate(word) == "VCVCVVCVCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5]))\
               + "-" + "".join(char_list(word[5:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 128
# paraboloide - CVCVCVCVVCV
    elif sayi == 11 and annotate(word) == "CVCVCVCVVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6]))\
               + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 129
# aidatlarımı - VVCVCCVCVCV
    elif sayi == 11 and annotate(word) == "VVCVCCVCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:2])) + "-" + "".join(char_list(word[2:5]))\
               + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 130
# aminoasitle - VCVCVVCVCCV
    elif sayi == 11 and annotate(word) == "VCVCVVCVCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5]))\
               + "-" + "".join(char_list(word[5:6])) + "-" + "".join(char_list(word[6:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 131
# akordeonunu - VCVCCVVCVCV
    elif sayi == 11 and annotate(word) == "VCVCCVVCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:6]))\
               + "-" + "".join(char_list(word[6:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 132
# faaliyetini - CVVCVCVCVCV
    elif sayi == 11 and annotate(word) == "CVVCVCVCVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:5]))\
               + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 133
# ideologları - VCVVCVCCVCV
    elif sayi == 11 and annotate(word) == "VCVVCVCCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:4]))\
               + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 134
# iaşelerinde - VVCVCVCVCCV
    elif sayi == 11 and annotate(word) == "VVCVCVCVCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:2])) + "-" + "".join(char_list(word[2:4]))\
               + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 135
# ideolojidir - VCVVCVCVCVC
    elif sayi == 11 and annotate(word) == "VCVVCVCVCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:4]))\
               + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 136
# ideolojimle - VCVVCVCVCCV
    elif sayi == 11 and annotate(word) == "VCVVCVCVCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:4]))\
               + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 137
# ailedekiler - VVCVCVCVCVC
    elif sayi == 11 and annotate(word) == "VVCVCVCVCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:2])) + "-" + "".join(char_list(word[2:4]))\
               + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 138
# aidiyetliği - VVCVCVCCVCV
    elif sayi == 11 and annotate(word) == "VVCVCVCCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:2])) + "-" + "".join(char_list(word[2:4]))\
               + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 139
# müddeiumumi - CVCCVVVCVCV
    elif sayi == 11 and annotate(word) == "CVCCVVVCVCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:6]))\
               + "-" + "".join(char_list(word[6:7])) + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 140
# hisseişayia - CVCCVVCVCVV
    elif sayi == 11 and annotate(word) == "CVCCVVCVCVV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:6]))\
               + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:10])) + "-" + "".join(char_list(word[10:11]))
        return word
# 141
# espritüeldi - VCCCVCVVCCV
    elif sayi == 11 and annotate(word) == "VCCCVCVVCCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:7]))\
               + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 142
# binaenaleyh - CVCVVCVCVCC
    elif sayi == 11 and annotate(word) == "CVCVVCVCVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:5]))\
               + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:11]))
        return word
# 143
# kristaloide - CCVCCVCVVCV
    elif sayi == 11 and annotate(word) == "CCVCCVCVVCV":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8]))\
               + "-" + "".join(char_list(word[8:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 144
# amerikanizm - VCVCVCVCVCC
    elif sayi == 11 and annotate(word) == "VCVCVCVCVCC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5]))\
               + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:11]))
        return word
# 145
# videobantta - CVCVVCVCCCV
    elif sayi == 11 and annotate(word) == "CVCVVCVCCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:5]))\
               + "-" + "".join(char_list(word[5:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 146
# feodalizmle - CVVCVCVCCCV
    elif sayi == 11 and annotate(word) == "CVVCVCVCCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:5])) \
               + "-" + "".join(char_list(word[5:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 147
# pankreasını - CVCCCVVCVCV
    elif sayi == 11 and annotate(word) == "CVCCCVVCVCV":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:7]))\
               + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 148
# stoacıların - CCVVCVCVCVC
    elif sayi == 11 and annotate(word) == "CCVVCVCVCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:6]))\
               + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 149
# kreatörlere - CCVVCVCCVCV
    elif sayi == 11 and annotate(word) == "CCVVCVCCVCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:7]))\
               + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 150
# stoacılarda - CCVVCVCVCCV
    elif sayi == 11 and annotate(word) == "CCVVCVCVCCV":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:4])) + "-" + "".join(char_list(word[4:6]))\
               + "-" + "".join(char_list(word[6:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 151
# uyuşmazlığa - VCVCCVCCVCV
    elif sayi == 11 and annotate(word) == "VCVCCVCCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:7]))\
               + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 152
# bienalinden - CVVCVCVCCVC
    elif sayi == 11 and annotate(word) == "CVVCVCVCCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:5]))\
               + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 153
# akortlamaya - VCVCCCVCVCV
    elif sayi == 11 and annotate(word) == "VCVCCCVCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:5])) + "-" + "".join(char_list(word[5:7]))\
               + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 154
# teamüllerin - CVVCVCCVCVC
    elif sayi == 11 and annotate(word) == "CVVCVCCVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:6]))\
               + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 155
# teoremlerle - CVVCVCCVCCV
    elif sayi == 11 and annotate(word) == "CVVCVCCVCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:6]))\
               + "-" + "".join(char_list(word[6:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 156
# elementleri - VCVCVCCCVCV
    elif sayi == 11 and annotate(word) == "VCVCVCCCVCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:7]))\
               + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 157
# aidatlardan - VVCVCCVCCVC
    elif sayi == 11 and annotate(word) == "VVCVCCVCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:2])) + "-" + "".join(char_list(word[2:5]))\
               + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 158
# suikastları - CVVCVCCCVCV
    elif sayi == 11 and annotate(word) == "CVVCVCCCVCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:7]))\
               + "-" + "".join(char_list(word[7:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 159
# idealisttir - VCVVCVCCCVC
    elif sayi == 11 and annotate(word) == "VCVVCVCCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:4]))\
               + "-" + "".join(char_list(word[4:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 160
# ekonomistle - VCVCVCVCCCV
    elif sayi == 11 and annotate(word) == "VCVCVCVCCCV":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:5]))\
               + "-" + "".join(char_list(word[5:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 161
# müddeialeyh - CVCCVVVCVCC
    elif sayi == 11 and annotate(word) == "CVCCVVVCVCC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:5])) + "-" + "".join(char_list(word[5:6]))\
               + "-" + "".join(char_list(word[6:7])) + "-" + "".join(char_list(word[7:11]))
        return word
# 162
# kontrpuanın - CVCCCCVVCVC
    elif sayi == 11 and annotate(word) == "CVCCCCVVCVC":
        word = "".join(char_list(word[0:5])) + "-" + "".join(char_list(word[5:7])) + "-" + "".join(char_list(word[7:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 163
# jeosantrizm - CVVCVCCCVCC
    elif sayi == 11 and annotate(word) == "CVVCVCCCVCC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:3])) + "-" + "".join(char_list(word[3:7])) + "-" + "".join(char_list(word[7:11]))
        return word
# 164
# uzaklaştırt - VCVCCVCCVCC
    elif sayi == 11 and annotate(word) == "VCVCCVCCVCC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:7])) + "-" + "".join(char_list(word[7:11]))
        return word
# 165
# egosantrizm - VCVCVCCCVCC
    elif sayi == 11 and annotate(word) == "VCVCVCCCVCC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:3])) + "-" + "".join(char_list(word[3:7])) + "-" + "".join(char_list(word[7:11]))
        return word
# 166
# megahertzle - CVCVCVCCCCV
    elif sayi == 11 and annotate(word) == "CVCVCVCCCCV":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 167
# anarşistler - VCVCCVCCCVC
    elif sayi == 11 and annotate(word) == "VCVCCVCCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:4])) + "-" + "".join(char_list(word[4:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 168
# amorflaşmış - VCVCCCVCCVC
    elif sayi == 11 and annotate(word) == "VCVCCCVCCVC":
        word = "".join(char_list(word[0:1])) + "-" + "".join(char_list(word[1:5])) + "-" + "".join(char_list(word[5:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 169
# sfenkslerde - CCVCCCCVCCV
    elif sayi == 11 and annotate(word) == "CCVCCCCVCCV":
        word = "".join(char_list(word[0:6])) + "-" + "".join(char_list(word[6:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 170
# kontrplakla - CVCCCCCVCCV
    elif sayi == 11 and annotate(word) == "CVCCCCCVCCV":
        word = "".join(char_list(word[0:5])) + "-" + "".join(char_list(word[5:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 171
# kontekstten - CVCCVCCCCVC
    elif sayi == 11 and annotate(word) == "CVCCVCCCCVC":
        word = "".join(char_list(word[0:3])) + "-" + "".join(char_list(word[3:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 172
# sfenkslerin - CCVCCCCVCVC
    elif sayi == 11 and annotate(word) == "CCVCCCCVCVC":
        word = "".join(char_list(word[0:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:11]))
        return word
# 173
# hornblentli - CVCCCCVCCCV
    elif sayi == 11 and annotate(word) == "CVCCCCVCCCV":
        word = "".join(char_list(word[0:4])) + "-" + "".join(char_list(word[4:9])) + "-" + "".join(char_list(word[9:11]))
        return word
# 173
# affedebilen - VCCVCVCVCVC
    elif sayi == 11 and annotate(word) == "VCCVCVCVCVC":
        word = "".join(char_list(word[0:2])) + "-" + "".join(char_list(word[2:4])) + "-" + "".join(char_list(word[4:6])) + "-" + "".join(char_list(word[6:8])) + "-" + "".join(char_list(word[8:11]))
        return word



#####################################################################
# Return output
#for word in words:
#    print(ts_hecele(word), v_sayisi)
#####################################################################
# Total number of rules:
# 1 ==> 1
# 2 ==> 2
# 3 ==> 5
# 4 ==> 6
# 5 ==> 18
# 6 ==> 29
# 7 ==> 46
# 8 ==> 62
# 9 ==> 97
# 10 ==> 125
# 11 ==> 173

#Sub_Total = 1 + 2 + 5 + 6 + 18 + 29 + 46 + 62 + 97 + 125 + 173
#print ("# of Rules: ", Sub_Total)