"""
use pytesseract need install  Pillow，Tesseract-OCR，chi_tra.traineddata（中文识别包）
"""
from PIL import Image
import  pytesseract 
import jieba
def qcr_image(url_path):
    image = Image.open(r'{}'.format(url_path)) 
    text = pytesseract.image_to_string(image,lang='chi_sim') # 中文识别包
    # print(result)#
    # text="今天吃饭了吗"

    long_str=jieba.cut(text,cut_all=True)
    print('分词个数===>{ %d}' % len(list(long_str)))

    str_list=list(jieba.cut(text,cut_all=False))
    # print(str_list)
    ss = "-".join(str_list)
    ss = ss.replace("\n","")
    ss = ss.replace(" ","")
    ss = ss.replace("--","-")
    str_list = ss.split("-")
    dic = {}
    dic["content"] = str_list
    return dic

if __name__ == '__main__':
    res = qcr_image('test.png')
    print("qcr result===>",res)
