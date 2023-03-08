import qrcode

data = "https://www.aarhusbraetspilscafe.dk/"

img = qrcode.make(data)

img.save('AABraetspilQR.png')