type = input("File name: ").lower().strip()

if type.endswith(".jpeg") or type.endswith(".jpg"):
    print("image/jpeg")
elif type.endswith(".gif"):
    print("image/gif")
elif type.endswith(".png"):
    print("image/png")
elif type.endswith(".txt"):
    print("text/plain")
elif type.endswith(".pdf"):
    print("application/pdf")
elif type.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
