#palindrome function

def pal_checker(string):
    clean_str = "".join(c.lower() for c in string if c.isalnum())
    return clean_str == clean_str[::-1]

strings_to_test = [
"rats live on no Evil Star",
"Sit on a potato pan, Otis.",
"Cigar? Toss it in a can. It is so tragic.",
"Go hang a salami, I'm a lasagna hog.",
"A man, a plan, a canal, Panama!"
]

for string in strings_to_test:
    print(pal_checker(string))