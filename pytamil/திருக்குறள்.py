# -*- coding: utf-8 -*-

import sys
import pytamil
from pytamil import தமிழ்
from pytamil.தமிழ்  import மாத்திரை
import csv
import os
import re


குறள் = ['''அகர முதல எழுத்தெல்லாம் ஆதி
           பகவன் முதற்றே உலகு.''',
        '''கற்றதனால் ஆய பயனென்கொல் வாலறிவன்
           நற்றாள் தொழாஅர் எனின்.''',
        '''துப்பார்க்குத் துப்பாய துப்பாக்கித் துப்பார்க்குத்
           துப்பாய தூஉம் மழை.''',
        '''அறத்தாற்றின் இல்வாழ்க்கை ஆற்றின் புறத்தாற்றில்
           போஒய்ப் பெறுவ தெவன்''',
        '''அந்தணர் என்போர் அறவோர்மற் றெவ்வுயிர் க்கும்
           செந்தண்மை பூண்டொழுக லான்.?''',
        '''திறனல்ல தற்பிறர் செய்யினும் நோநொந்து
           அறனல்ல செய்யாமை நன்று.''',
        '''ஓஒதல் வேண்டும் ஒளிமாழ்கும் செய்வினை
           ஆஅதும் என்னு மவர்.''',
        '''ஓஒ இனிதே எமக்கிந்நோய் செய்தகண்
           தாஅம் இதற்பட் டது.''',
        '''நலத்தகை நல்லவர்க்கு ஏஎர் புலத்தகை
           பூஅன்ன கண்ணார் அகத்து.'''
        ]

def குறள்_மாத்திரைவரிசைகள்_கொடு(குறள்_அடி):
    அடிகள் = குறள்_அடி.splitlines()
    
    பதங்கள் =[]
    மாத்திரைவரிசைகள் =[]
    for அடி in  அடிகள்:
        அ = அடி.strip()
        அ = re.sub('[.?]', '', அ) # remove any characters like . ? etc

        பதங்கள்.extend(அ.split())

    for பதம் in  பதங்கள்:

        மாத்திரைவரிசை = மாத்திரை.மாத்திரைவரிசை_கொடு(பதம்)
        # print(மாத்திரை.format(மாத்திரைவரிசை))
        மாத்திரைவரிசைகள்.append(மாத்திரைவரிசை)
    
    return மாத்திரைவரிசைகள்


def குறள்_மாத்திரைஎண்கள்_கொடு(மாத்திரைவரிசைகள், மாத்திரைவகைகள்):
    மாத்திரைஎண்கள்=''
    for மாத்திரைவரிசை in மாத்திரைவரிசைகள்:
        for மாத்திரைவிவரம் in மாத்திரைவரிசை:
            மாத்திரைஎண்கள் = மாத்திரைஎண்கள் + str(மாத்திரைவிவரம்.மாத்திரைஎண்) 
            if மாத்திரைவிவரம்.புணர்மொழி == True: 
                மாத்திரைஎண்கள் = மாத்திரைஎண்கள் + '* '
            else:
                மாத்திரைஎண்கள் = மாத்திரைஎண்கள் + ' '

            வகை = மாத்திரைவிவரம்.மாத்திரைவகை
            மாத்திரைவகைகள்[வகை] = மாத்திரைவகைகள்[வகை] +1
        மாத்திரைஎண்கள் = மாத்திரைஎண்கள்.rstrip() + "    "

    return மாத்திரைஎண்கள், மாத்திரைவகைகள்

# def print_மாத்திரைவரிசைகள்(மாத்திரைவரிசைகள்):

def convert_திருக்குறள்(filepath):
    inpath = filepath
    outpath = os.path.join(os.path.dirname(filepath),"திருக்குறள்-output")
    with open(inpath, "r") as infile, open(outpath, "w") as outfile:
        reader = csv.reader(infile, delimiter=',')
        next(reader, None)  # skip the headers

        # keep in mind that dictionaries are ordered in python 3.7+
        மாத்திரைவகைகள் = {"உயிர்க்குறில்": 0, "உயிர்நெடில்":0, "ஆய்தம்":0, "மெய்":0,
                            "உயிர்மெய்க்குறில்":0, "உயிர்மெய்நெடில்":0, "உயிரளபெடை":0, "ஒற்றளபெடை":0,
                            "ஐகாரக்குறுக்கம்_முதல்":0, "ஐகாரக்குறுக்கம்_இடைகடை":0, "ஒளகாரக்குறுக்கம்":0,
                            "குற்றியலுகரம்":0, "குற்றியலிகரம்":0, "மகரக்குறுக்கம்":0, "ஆய்தக்குறுக்கம்":0}
        
        header = ["குறள்", "எண்", "மாத்திரை" ]
        header.extend(மாத்திரைவகைகள்.keys())

        writer = csv.writer(outfile)
        writer.writerow(header)

        for row in reader:
            குறள்_அடி = row[4]
            குறள்_எண் = row[0]
            மாத்திரைவரிசைகள் = குறள்_மாத்திரைவரிசைகள்_கொடு(குறள்_அடி)
            மாத்திரைவகைகள் = {"உயிர்க்குறில்": 0, "உயிர்நெடில்":0, "ஆய்தம்":0, "மெய்":0,
                            "உயிர்மெய்க்குறில்":0, "உயிர்மெய்நெடில்":0, "உயிரளபெடை":0, "ஒற்றளபெடை":0,
                            "ஐகாரக்குறுக்கம்_முதல்":0, "ஐகாரக்குறுக்கம்_இடைகடை":0, "ஒளகாரக்குறுக்கம்":0,
                            "குற்றியலுகரம்":0, "குற்றியலிகரம்":0, "மகரக்குறுக்கம்":0, "ஆய்தக்குறுக்கம்":0}
            மாத்திரைஎண்கள் , மாத்திரைவகைகள் = குறள்_மாத்திரைஎண்கள்_கொடு(மாத்திரைவரிசைகள், மாத்திரைவகைகள்)
            values = [ *[குறள்_அடி, குறள்_எண், மாத்திரைஎண்கள்] , * மாத்திரைவகைகள்.values()] 
            writer.writerow(values)
            print (குறள்_எண், மாத்திரைஎண்கள்)
            print()



# மாத்திரைவரிசைகள் = குறள்_மாத்திரைவரிசைகள்_கொடு(குறள்[8])
# # # print(குறள்_மாத்திரைஎண்கள்_கொடு(மாத்திரைவரிசைகள்))
# for மாத்திரைவரிசை in மாத்திரைவரிசைகள்:
#     print(மாத்திரை.format(மாத்திரைவரிசை))


convert_திருக்குறள்("pytamil/தமிழ்/resources/திருக்குறள்-input.csv")

