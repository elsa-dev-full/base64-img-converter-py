import base64
from base64 import decodebytes

def convertStringToImage(stringData):
    with open("result.jpg","wb") as f:
        f.write(decodebytes(stringData))
        f.close()

if __name__ == "__main__":
    with open("test.jpg", "rb") as imageFile:
        stringImage = base64.b64encode(imageFile.read())
        print("stringImage", stringImage)
    convertStringToImage(stringImage)