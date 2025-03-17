
import qrcode

data = "https://github.com/RohitAlam080"


game3 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)
game3.add_data(data)
game3.make(fit=True)

gamer =game3.make_image(fill_color="black", back_color="LightYellow")
gamer.save("github.png")

print("congratulation!")

data = "https://in.linkedin.com/in/rohit-alam-14828b338"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)
qr.add_data(data)
qr.make(fit=True)

img =qr.make_image(fill_color="Black", back_color="White")
img.save("linkedin.png")

print("congratulation!")
