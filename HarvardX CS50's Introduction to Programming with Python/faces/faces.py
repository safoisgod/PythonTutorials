def main():
    making_faces = input()
    convert(making_faces)


def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    print(text)

main()