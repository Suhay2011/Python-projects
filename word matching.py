#function to check wheather
#first and last characters of words match
def mach_words(words):
    ctr = 0
    lst = []
    for word in words:
            if len(word) > 1 and word[0] == word[-1]:
                  ctr += 1
                  lst.append(word)

    print("List of words with first and last words same/n", lst)
    return ctr

count = mach_words(['abd', 'cfc' ,'xyz', 'aba', '1221'])
print("Number of words with first and last character same/n", count)
