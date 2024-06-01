
import segno    
def make_qr(link,file_name):
    qrcode=segno.make_qr(link)
    qrcode.save(
        file_name+".png",
        scale=5,
        border=1
    )
    
def generate_qr(number):
    for i in range(number):
        yield make_qr(str(i), str(i))
        
for i in generate_qr(1):
    ...