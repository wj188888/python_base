# -*- coding: utf-8 -*-
# @Author: jie wang
# @Date: 2023/5/15 22:52
'''
解密流程：
输入文本str
字符串编码utf-8 （bytes）
rsa加密（bytes）
base64编码（bytes）
解码为字符串str

完整代码
'''

import base64
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
from Crypto.PublicKey import RSA

#--------------生成密钥对---------------
def create_rsa_pair(is_save=False):
    f = RSA.generate(2048)
    private_key = f.exportKey("PEM") #生成私钥
    public_key = f.publickey().exportKey() #生成公钥
    if is_save:
        with  open("crypto_private_key.pem", "wb") as f:
            f.write(private_key)
        with open("crypto_public_key.pem", "wb") as f:
            f.write(public_key)
    return public_key, private_key

def read_public_key(file_path="cryptoo_public_key.pem") -> bytes:
    with open(file_path, "rb") as x:
        b = x.read()
        return b

def read_private_key(file_path="crypto_public_key.pem") -> bytes:
    with open(file_path, "rb") as x:
        b = x.read()
        return b

# --------------------加密----------------
def encryption(text: str, public_key: bytes):
    #字符串指定编码（转为bytes）
    text = text.encode('utf-8')
    #构建公钥对象
    cipher_public = PKCS1_v1_5.new(RSA.importKey(public_key))
    #加密(bytes)
    text_encrypted = cipher_public.encrypt(text)
    #base64编码，并转变成字符串
    text_encrypted_base64 = base64.b64encode(text_encrypted).decode()

    return text_encrypted_base64

# ---------------------解密--------------------
def decryption(text_encrypted_base64: str, private_key: bytes):
    #字符串指定编码（转为bytes)
    text_encrypted_base64 = text_encrypted_base64.encode('utf-8')
    #base64解码
    text_encrypted = base64.b64encode(text_encrypted_base64)
    #构建私钥对象
    cipher_private = PKCS1_v1_5.new(RSA.importKey(private_key))
    #解密(bytes)
    text_decrypted = cipher_private.decrypt(text_encrypted, Random.new().read)
    #解码为字符串
    text_decrypted = text_decrypted.decode()

    return text_decrypted

if __name__ == '__main__':
    # create_rsa_pair(is_save=True)
    # public_key = read_public_key()
    # private_key = read_private_key()
    public_key, private_key = create_rsa_pair(is_save=True)

    #加密
    text = '123456'
    text_encrypted_base64 = encryption(text, public_key)
    print("密文:", text_encrypted_base64)

    #解密
    text_decrypted = decryption(text_encrypted_base64, private_key)
    print("明文:", text_decrypted)
