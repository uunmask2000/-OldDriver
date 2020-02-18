import base64
import re 
import string

class CustomEncryption:
    '''
    預設值
    '''

    def __init__(self, key=None):
        if key == None:
            self.key = '1234567'
        self.key = key

    def b16_encode(self, srt_):
        # 貼加密字串
        encoded = base64.b16encode(srt_.encode('utf-8')).decode('ascii')
        return encoded

    def b16_decode(self, encoded):
        # 加密字串取代為空
        # data = base64.b16decode(encoded).decode('utf-8')
        data = base64.b16decode(encoded.encode('ascii')).decode('utf-8')
        return data

    '''
    處理字串
    '''
    def removePunctuation(self, line):
        punctuation = "<>-""|！？｡＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟…‧﹏"""
        re_punctuation = "[{}]+".format(punctuation)
        line = re.sub(re_punctuation, "", line)
        # return line.strip().strip(b'\x00'.decode())
        out = "".join(line.split())
        out = out.replace('/', "").replace('.', "").replace('\\', "").replace(
            '?', "").replace('>', "").replace('<', "").replace(' ', "").replace('-', "")
        return out
