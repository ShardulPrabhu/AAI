from fuzzywuzzy import fuzz
from fuzzywuzzy import process
#Ratio
print("Ratio")
Str_A = 'FuzzyWuzzy is a lifesaver!'
Str_B = 'fuzzy wuzzy is = LIFE SAVER.'
ratio = fuzz.ratio (Str_A.lower (), Str_B.lower())
print('Similarity score: {}'.format (ratio))
print("=================================================================")
#Partial Ratio
print("Partial Ratio")
Str_A = 'Chicago, Illinois'
Str_B = 'Chicago'
ratio = fuzz.partial_ratio (Str_A.lower(), Str_B.lower())
print('partial_ratio: {}'.format (ratio))
print("=================================================================")
#Token Sort Ratio
print("Token Sort Ratio")
Str_A = 'Gunner William Kline'
Str_B = 'Kline,Gunner William'
ratio = fuzz.token_sort_ratio (Str_A, Str_B)
print ('token_sort_ratio: {}' .format (ratio))
print("=================================================================")#Token Set Ratio
print("Token Set Ratio")
Str_A = 'The 3000 meter steeplechase winner, Soufiane and El Bakkali'
Str_B = 'Soufian E1 Bakkli'
ratio = fuzz.token_set_ratio(Str_A, Str_B)
print('token_set_ratio: {}'.format(ratio))
print("Done")
print("Name Shardul Prabhu")
