import autocomplete


input_text = '동해물과 백두산이 마르고 닳도록, 하느님이 보우하사 우리나라 만세~'

print(autocomplete.find_keywords(input_text, 'ㅁ'))
print(autocomplete.find_keywords(input_text, '우린'))
print(autocomplete.find_keywords(input_text, '록한'))