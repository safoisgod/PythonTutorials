#words to emoji convertor

message = input(">>>")
words = message.split(" ")
emoji_convertor ={
    "happy": "😂",
    "sad": "😢",
    "crying": "😭"
}
output = ""

for word in words:
#for each item in the command (set of WORDS), we go to the EMOJI_CONVERTOR
#get the KEY(corresponding item in the set of WORDS) and if that is not available we just get words
#(CORRESPONDING KEY, WHAT SHOULD APPEAR IF VALUE DOESNT CORRSPOND
#we add the space to seprate each item
    output += emoji_convertor.get(word, word) + " "
print(output)

