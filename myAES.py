from Crypto.Cipher.AES import MODE_ECB
from Crypto.Cipher.AES import new as newAES
from base64 import encodebytes,decodebytes
class AesCrypt():
    def __init__(self,key,encode_):
        self.encode_ = encode_
        self.key = self.add_16(key)
        self.aes = newAES(self.key,MODE_ECB) #创建一个aes对象
        #这里的密钥长度必须是16、24或32，目前16位的就够用了

    def add_16(self,par):
        par = par.encode(self.encode_)
        while len(par) % 16 != 0:
            par += b'\x05'
        return par

    def aesencrypt(self,text):
        text = self.add_16(text)
        self.encrypt_text = self.aes.encrypt(text)
        return encodebytes(self.encrypt_text).decode().strip()

    def aesdecrypt(self,text):
        text = decodebytes(text.encode(self.encode_))
        self.decrypt_text = self.aes.decrypt(text)
        return self.decrypt_text.decode(self.encode_).strip('\5')

if __name__ == '__main__':
    pr = AesCrypt('0725@pwdorgopenp','utf-8')
    en_text = pr.aesencrypt('lchAK47.423')
    de_text = pr.aesdecrypt('LCzBICBsiIKNn/VByB3wRw==')
    print('密文:',en_text)
    print('明文:',de_text)
