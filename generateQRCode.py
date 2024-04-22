import qrcode

name = input("Enter the name of the project:")
data = input("Enter the link:")

img = qrcode.make(data)

img.save(f"generatedQRCode/{name}.png")