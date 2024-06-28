#the function do not contain the input and output
def emoji_convert(message):
    words = message.split(" ")
    emoji_convertor ={
        "happy": "😂",
        "sad": "😢",
        "crying": "😭"
    }
    output = ""

    for word in words:
        output += emoji_convertor.get(word, word) + " "
    return output

message = input(">>>")
#the return statement is then stored in the definition as RESULT
result = emoji_convert(message)
print(result)
