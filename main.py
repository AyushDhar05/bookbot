import sys
from stats import get_num_words, charFrequency, getSortedDict

def get_book_text(filePath):
    res = ""
    with open(filePath) as f:
        res += f.read()
    return res

def main(sys=sys.argv):
    # path = "./books/frankenstein.txt"
    if len(sys) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys[1]
    
    try:
        fullText = get_book_text(f"{path}")
    except:
        raise("File not found!")
    
    length = get_num_words(f"{path}")
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {length} total words")
    print("--------- Character Count -------")
    my_dict = charFrequency(fullText)
    print(my_dict)
    listDict = getSortedDict(my_dict)
    for dict in listDict:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()