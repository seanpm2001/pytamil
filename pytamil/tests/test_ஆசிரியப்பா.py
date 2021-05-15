import pytest
from pytamil.தமிழ் import எழுத்து
from pytamil.தமிழ் import ஆசிரியப்பா



@pytest.mark.parametrize("பத்தி", \
    [ 
        #குறுந்தொகை - 3. குறிஞ்சி - தலைவி கூற்று
        ('''
        நிலத்தினும் பெரிதே வானினும் உயர்ந்தன்று
        = கருவிளம் புளிமா கூவிளம் புளிமாங்காய்
        நீரினும் ஆரள வின்றே சாரல்
        = கூவிளம் கூவிளம் தேமா தேமா
        கருங்கோல் குறிஞ்சிப் பூக்கொண்டு
        = புளிமா புளிமா தேமாங்காய்
        பெருந்தேன் இழைக்கும் நாடனொடு நட்பே
        = புளிமா புளிமா கூவிளங்காய் தேமா
        '''),


    ])
def test_நேரிசை_ஆசிரியப்பா(பத்தி):   
    
    # extract செய்யுள் lines only
    பாடல்_அடிகள் =  [ அடி.strip() for i,அடி in enumerate(பத்தி.strip().splitlines()) if not i%2 ]
    பாடல் =  "\n".join(பாடல்_அடிகள்)

    # extract சீர் வாய்பாடு lines only
    சீர்_அடிகள் =  [ அடி.strip() for i,அடி in enumerate(பத்தி.strip().splitlines()) if i%2 ]

    அடிவரிசை = ஆசிரியப்பா.சீர்_வாய்பாடு_கொடு(பாடல்)
    புது_சீர்_அடிகள் = ["= "+" ".join(அடி) for அடி in அடிவரிசை]

    assert சீர்_அடிகள் == புது_சீர்_அடிகள்
    
    
	

