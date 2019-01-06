print("SARIM ALI KHAN")
print("18B-043-CS(A)")
print("LAB 09")



def duplicate(filename):
    infile = open(filename,'r')
    words = infile.read()
    infile.close()
    text = words.split()
    words2 = ['sarim']
    for word in text:
        if word in words2:
            return True
        else:
            words2.append(word)
    return False

print(duplicate('sarim.txt'))
