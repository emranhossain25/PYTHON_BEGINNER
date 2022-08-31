def remove_vowels(word):
    vowels=['a','e','i','o','u']
    result=[letter for letter in word if letter.lower() not in vowels]
    result=''.join(result)
    print(result)

word=input("Enter any word: ")
remove_vowels(word)

