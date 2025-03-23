
def word_count(contents):
    words = contents.split()
    return len(words)

def char_counts(string):
    #words = "these are words"
    chars = list(string)
    #print(chars)
    char_counts = {}

    for i in range(0, len(chars)):
        char = chars[i].lower()
        
        if char not in char_counts:
            #print(f"char not found. adding {char}")
            char_counts[char] = 1
        else:
            char_counts[char] += 1
            #print(f"char found. count of char is {char_counts[char]}")
    return char_counts

def sort_by_count(dictionary):
    sorted_list = sorted(dictionary.items(), key=lambda item: item[1], reverse=True )
    #print(sorted_list)
    sorted_dict = {key: value for key, value in sorted_list}
    return sorted_dict

