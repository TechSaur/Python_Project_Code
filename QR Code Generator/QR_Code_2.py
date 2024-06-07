# Importing Library
import qrcode as qr

#data to encode
data = "Sp"

# Creating an instance of Qr Code Class
qrc = qr.QRCode(version=1,
                box_size=10,
                border=5)       # Default border size is 4

# Adding data to the instance 'qrc'
qrc.add_data(''' 
            Hello Guddu.
            How are you ?
            What are you doing ?          
''')

qrc.make(fit=True)          #  This method with (fit=True) ensures that the entire dimension of the QR Code is
                            # utilized, even if our input data could fit into less number of boxes.

img = qrc.make_image(fill_color = "red",
                     back_color = "white")

img.save("techy.png")