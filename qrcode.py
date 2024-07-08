import qrcode
qr=qrcode.QRCode(
    version=5,
    box_size=5,
    border=2
)
name=input("enter you name:")
age=int(input("enter your age:"))
mobile=int(input("enter your mobile:"))
data={"name":name,"age":age,"mobile":mobile}
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image()
img.save("docp.png")
img.show()