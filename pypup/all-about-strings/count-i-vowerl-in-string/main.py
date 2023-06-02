def vowel_counter(s):
    return len([i for i in s.lower() if i == 'i'])


print(vowel_counter("I love competitive programming."))
