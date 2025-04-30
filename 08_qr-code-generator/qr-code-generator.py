import qrcode 

data = "Don't love me like you do "

qr = qrcode.QRCode(version = 1 , box_size =10 , border = 5)

qr.add_data(data)
qr.make(fit = True)
img= qr.make_image(fill_color = 'red'  , back_color = 'white'  )

img.save('E:/Python/04_assignment/assignment_01/online_class_projects/qr-code-generator/myqr1.png')