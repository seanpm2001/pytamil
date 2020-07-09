import pytest
from pytamil.தமிழ் import எழுத்து
from pytamil.தமிழ் import மாத்திரை
import yaml
from yaml import Loader, Dumper

@pytest.mark.parametrize("தொடர், மாத்திரைவரிசை", \
						[ 
                            ('ஊக்கம்', 'ஊ:உயிர்நெடில்:2 க்:மெய்:0.5 க:உயிர்மெய்க்குறில்:1 ம்:மெய்:0.5'  ),
                            ('அஃது' , 'அ:உயிர்க்குறில்:1 ஃ:ஆய்தம்:0.5 து:குற்றியலுகரம்:0.5'),
                            ('குழூஉக்குறி', 'கு:உயிர்மெய்க்குறில்:1 ழூஉ:உயிரளபெடை:3 க்:மெய்:0.5 கு:உயிர்மெய்க்குறில்:1 றி:உயிர்மெய்க்குறில்:1'),
                            ('மங்ங்கலம்', 'ம:உயிர்மெய்க்குறில்:1 ங்ங்:ஒற்றளபெடை:1 க:உயிர்மெய்க்குறில்:1 ல:உயிர்மெய்க்குறில்:1 ம்:மெய்:0.5'),
                            ('ஔவையார்', 'ஔ:ஔகாரக்குறுக்கம்:1 வை:ஐகாரக்குறுக்கம்_இடைகடை:1 யா:உயிர்மெய்நெடில்:2 ர்:மெய்:0.5'),
                            ('மௌவல்', 'மௌ:ஔகாரக்குறுக்கம்:1 வ:உயிர்மெய்க்குறில்:1 ல்:மெய்:0.5'),
                            ('நாடு','நா:உயிர்மெய்நெடில்:2 டு:குற்றியலுகரம்:0.5'),
                            ('பந்து', 'ப:உயிர்மெய்க்குறில்:1 ந்:மெய்:0.5 து:குற்றியலுகரம்:0.5'),
                            ('அது', 'அ:உயிர்க்குறில்:1 து:உயிர்மெய்க்குறில்:1'),
                            ('ஐவர்', 'ஐ:ஐகாரக்குறுக்கம்_முதல்:1.5 வ:உயிர்மெய்க்குறில்:1 ர்:மெய்:0.5'),
                            ('நசைஇ', 'ந:உயிர்மெய்க்குறில்:1 சைஇ:உயிரளபெடை:3'),
                            ('ஐ', 'ஐ:உயிர்நெடில்:2'),
                            ('பகைவர்' , 'ப:உயிர்மெய்க்குறில்:1 கை:ஐகாரக்குறுக்கம்_இடைகடை:1 வ:உயிர்மெய்க்குறில்:1 ர்:மெய்:0.5'),
                            ('தவளை','த:உயிர்மெய்க்குறில்:1 வ:உயிர்மெய்க்குறில்:1 ளை:ஐகாரக்குறுக்கம்_இடைகடை:1'),
                            ( 'ஔ' , 'ஔ:உயிர்நெடில்:2' ),
                            ('வௌவால்' , 'வௌ:ஔகாரக்குறுக்கம்:1 வா:உயிர்மெய்நெடில்:2 ல்:மெய்:0.5'),
                            ('சென்ம்','செ:உயிர்மெய்க்குறில்:1 ன்:மெய்:0.5 ம்:மகரக்குறுக்கம்:0.25'),
                            ('முஃடீது','மு:உயிர்மெய்க்குறில்:1 ஃ:ஆய்தக்குறுக்கம்:0.25 டீ:உயிர்மெய்நெடில்:2 து:குற்றியலுகரம்:0.5'),
                            ('தரும்வளவன்','த:உயிர்மெய்க்குறில்:1 ரு:உயிர்மெய்க்குறில்:1 ம்:மகரக்குறுக்கம்:0.25 வ:உயிர்மெய்க்குறில்:1 ள:உயிர்மெய்க்குறில்:1 வ:உயிர்மெய்க்குறில்:1 ன்:மெய்:0.5'),
                            ('கேண்மியா', 'கே:உயிர்மெய்நெடில்:2 ண்:மெய்:0.5 மி:குற்றியலிகரம்:0.5 யா:உயிர்மெய்நெடில்:2'),
                            ('நாடியாது', 'நா:உயிர்மெய்நெடில்:2 டி:குற்றியலிகரம்:0.5 யா:உயிர்மெய்நெடில்:2 து:குற்றியலுகரம்:0.5')


						])
def test_மாத்திரைவரிசை_கொடு(தொடர், மாத்திரைவரிசை):
    வரிசை = மாத்திரை.மாத்திரைவரிசை_கொடு(தொடர்)
    textstr=""
    for எ in வரிசை:
        textstr= textstr +எ[0] + ':' + எ[1] + ':' + str(எ[2]) + ' '

    assert textstr.strip() == மாத்திரைவரிசை
	

##################
filename = "pytamil/தமிழ்/resources/மாத்திரை.yaml" 
fo = open(filename, "r")
entries = list(yaml.load_all(fo,Loader=Loader))[1] #load second document in the file

சான்றுகள் = []
சான்றுகள் = மாத்திரை.getசான்றுகள்(entries,சான்றுகள் )

params = []
for சான்று in சான்றுகள்:
	params.append( (சான்று.பதம், சான்று.மாத்திரைவரிசை))

@pytest.mark.parametrize("பதம், மாத்திரைவரிசை", params)
def test_சான்று_மாத்திரைவரிசை_கொடு(பதம், மாத்திரைவரிசை):
    வரிசை = மாத்திரை.மாத்திரைவரிசை_கொடு(பதம்)
    textstr=""
    for எ in வரிசை:
        textstr= textstr +எ[0] + ':' + எ[1] + ' '

    assert textstr.strip() == மாத்திரைவரிசை