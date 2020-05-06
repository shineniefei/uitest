import os
from io import BytesIO

import qrcode
import requests
from PIL import Image
from pyzbar import pyzbar


class Qrcode:
    def textToQr(data):
        # 实例化二维码生成类
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        if data is None:
            data = "https://www.baidu.com"
        qr.add_data(data=data)

        # 启用二维码颜色设置
        qr.make(fit=True)
        img = qr.make_image(fill_color="green", back_color="white")

        # 显示二维码
        # img.show()
        return img

    def qrToText(img_adds):
        if os.path.isfile(img_adds):
            img = Image.open(img_adds)
        else:
            rq_img = requests.get(img_adds).content
            img = Image.open(BytesIO(rq_img))

        # img.show()

        text_list = pyzbar.decode(img)
        for text in text_list:
            barcode = text.data.decode("utf-8")
            print(barcode)

        return text_list


if __name__ == "__main__":
    Qrcodes = Qrcode()
    Qrcodes.textToQr('aaa')
    Qrcodes.qrToText('https://www.liantu.com/images/2013/liantu.png')
