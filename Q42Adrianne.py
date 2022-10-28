#Adrianne Quiz 4
lines= "I want # to # go # home#"
def count_hashtag(string,target):
    total=0
    index=0
    while index <len(string):
        if string[index: index+len(target)]==target:
            total+=1
            index+=len(target)
        else:
            index+=1
    return total

def hash_spam(string):
        if count_hashtag(string, "#")>=4:
            print("This is considered a spam!")
        else:
            return None

print(hash_spam(lines))
