# -*- coding: utf-8 -*-
# @Author: jie wang
# @Date: 2023/5/15 22:51

#加密

import base64
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from RSA生成密钥对 import read_public_key, read_private_key

def encryption(text: str, public_key: bytes):
    #字符串指定编码（转为bytes）
    text = text.encode('utf-8')
    #构建公钥对象
    cipher_public = PKCS1_v1_5.new(RSA.import_key(public_key))
    #加密(bytes)
    text_encryted = cipher_public.encrypt(text)
    #base64编码，并转为字符串
    text_encryted_base64 = base64.b64encode(text_encryted).decode()

    return text_encryted_base64

if __name__ == '__main__':
    public_key = read_public_key()
    text = '123456'
    text_encryted_base64 = encryption(text, public_key)
    print("密文：", text_encryted_base64)