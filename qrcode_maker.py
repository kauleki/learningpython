# import qrcode
import segno
# img = qrcode ('gaurav Mainali')
# type(img)  # qrcode.image.pil.PilImage
# img.save("Gaurav.png")
# basic_qrcode.py

import segno

# qrcode = segno.make_qr(("गौरदेव प्रिन्टर्स \n प्रि-प्रिन्ट डिजाइन तथा स्क्रिनप्रिन्ट सम्बन्धी काम ") )
#
# qrcode.save("Gauradev.png")

qrcode = segno.make_qr("https://oicchitwan.bagamati.gov.np/")
qrcode.save("Oicchitwan.png")