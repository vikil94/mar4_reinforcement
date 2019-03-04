digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']


new_dictionary = {}
num = len(digits)

for num in range(len(digits)):
    new_dictionary[digits[num]] = { 'french': fr[num], 'english': en[num]}
print(new_dictionary)



# should print this
# {
#   '1': {'french': 'un', 'english': 'one'},
#   '2': {'french': 'deux', 'english': 'two'},
#   '3': {'french': 'trois', 'english': 'three'},
#   ...
#   '9': {'french': 'neuf', 'english': 'nine'}
# }
