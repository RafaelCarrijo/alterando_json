

#parte operacional do cálculo de vogais.
def change_json(string):
    vowels = 'AaEeIiOoUu'
    new_json = {}
    vowels_in = [vw for vw in string if vw in vowels]
    number_vowels = len(vowels_in)
    new_json[string] = number_vowels
    return new_json




