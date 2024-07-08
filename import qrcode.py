import qrcode 
qr=qrcode.make("follow ravs edits")
data="https://www.instagram.com/ravs_edits_/?hl=en"
qr=qrcode.make(data)
qr.save("docp.png")
qr.show()