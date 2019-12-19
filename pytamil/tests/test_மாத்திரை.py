import pytest
from pytamil.தமிழ் import எழுத்து

@pytest.mark.parametrize("தொடர்", "மாத்திரைவரிசை", \
						[ 
                            ('காடு',[[0,1,'நெடில்'],[1,1,'குற்றியலுகரம்']]), 
                            ('மெய்ய்எழுத்து','மெய்யெழுத்து') 

						])
def test_உயிர்மெய்தொகை(விரிபதம், உயிர்மெய்பதம்):
    எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(விரிபதம்)
    பதம் = எழுத்து.உயிர்மெய்தொகை(எழுத்துவரிசை)
    assert பதம் == உயிர்மெய்பதம்
	