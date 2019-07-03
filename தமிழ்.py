from tamil import utf8 as tamilutf8


மெல்லினம் = tamilutf8.mellinam_letters
மெய்யெழுத்து = tamilutf8.mei_letters
உயிரெழுத்து = tamilutf8.uyir_letters

def பிரம்மி(வாக்கியம்):
    pass

def பண்டைய_எழுத்து(வாக்கியம் , வருடம் ):
    pass

def பண்டைய_சொல் (வாக்கியம், வருடம்  ):
    pass

def பண்டைய_வாக்கியம்_ஆக்கு(வாக்கியம், வருடம் ):
    pass

def தனிமொழி_ஆக்கு(வாக்கியம் ):
    pass

# @join_words
# def தொடர்மொழி_ஆக்கு(வாக்கியம்):
#     # return வா
#     s = வாக்கியம்
#     s= வாக்கியம்
#     return s

def testaaa(str):
    a = str

def join_words(words):
    return words, words

def தொடர்மொழி_ஆக்கு(நிலைமொழி, வருமொழி):
    தொடர்மொழி= 'அய்யொ'
    நிலைமொழி_எழுத்துக்கள் = tamilutf8.get_letters(நிலைமொழி)
    வருமொழி_எழுத்துக்கள் = tamilutf8.get_letters(வருமொழி)

    #தனிக்குறில் முன் நின்ற மெய் உயிர்வரின் இரட்டுதல்
    if len(நிலைமொழி_எழுத்துக்கள்) == 2 and \
        கடையெழுத்து(நிலைமொழி) in மெய்யெழுத்து and \
        முதலெழுத்து(வருமொழி) in உயிரெழுத்து:
            தொடர்மொழி = தனிக்குறில்_முன்_நின்ற_மெய்_உயிர்வரின்_இரட்டுதல்(நிலைமொழி, வருமொழி)
    return தொடர்மொழி

def கடையெழுத்து(சொல்):
    return tamilutf8.get_letters(சொல்)[-1]

def முதலெழுத்து(சொல்):
    return tamilutf8.get_letters(சொல்)[0]

def உயிர்மெய்_ஆக்கு(எழுத்து1,எழுத்து2):
    return tamilutf8.joinMeiUyir(எழுத்து1,எழுத்து2)

def தனிக்குறில்_முன்_நின்ற_மெய்_உயிர்வரின்_இரட்டுதல்(நிலைமொழி, வருமொழி):
    நிலைமொழி_எழுத்துக்கள் = tamilutf8.get_letters(நிலைமொழி)
    வருமொழி_எழுத்துக்கள் = tamilutf8.get_letters(வருமொழி)
    தொமொ =   நிலைமொழி_எழுத்துக்கள் + \
                    list(உயிர்மெய்_ஆக்கு(நிலைமொழி_எழுத்துக்கள்[-1],வருமொழி_எழுத்துக்கள்[0])) +\
                    வருமொழி_எழுத்துக்கள்[1:]

    தொடர்மொழி=''

    for எழுத்து in தொமொ :
        தொடர்மொழி = தொடர்மொழி + எழுத்து
    
    return தொடர்மொழி    
