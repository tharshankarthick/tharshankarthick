import qrcode  # importing qrcode module in python

url = input("Enter the URL: ").strip()  # getting input of a url from the user & strip removes extra space
file_path = "qrcode.png"  # creating a file path to store the created qr

qr = qrcode.QRCode()  # creating a qrcode object
qr.add_data(url)  # adds entered URL/txt into QRcode

img = qr.make_image()  # creating a QR image (Here the QR data converts to image)
img.save(file_path)  # Storing the QR image image in certain fil_path
