file_name = "Story"

def read_file_content(file_name):
    s = open('story.txt').read()

def word_count(str):   
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
s = open('story.txt').read()
print(word_count(s))