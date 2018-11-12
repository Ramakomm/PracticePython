def reverseWords(str):
    return ' '.join(str.split()[::-1])


sentence = input("please the setence yoou wanna reverse  :")
print(reverseWords(sentence))
