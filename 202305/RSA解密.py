# -*- coding: utf-8 -*-
# @Author: jie wang
# @Date: 2023/5/15 22:51

import base64
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
from Crypto.PublicKey import RSA
from RSA生成密钥对 import read_public_key, read_private_key
from RSA加密 import encryption

def decryption(text_encrypted_base64: str, private_key: bytes):
    #字符串指定编码（转为bytes）
    text_encrypted_base64 = text_encrypted_base64.encode('utf-8')
    #base64解码
    text_encrypted = base64.b64encode(text_encrypted_base64)
    #构建私钥对象
    cipher_private = PKCS1_v1_5.new(RSA.importKey(private_key))
    #解密（bytes）
    text_decrypted = cipher_private.decrypt(text_encrypted, Random.new().read)
    #解码为字符串
    text_decrypted = text_decrypted.decode()

    return text_decrypted

if __name__ == '__main__':
    #生成密文
    public_key = read_public_key()
    text = '123456'
    text_encrypted_base64 = encryption(text, public_key)
    print("密文：", text_encrypted_base64)

    #解密
    private_key = read_private_key()
    text_decrypted = decryption(text_encrypted_base64, private_key)
    print("明文：", text_decrypted)

'''
报错日志如下：
Traceback (most recent call last):
  File "E:/3_code/python/python_base/202305/RSA解密.py", line 35, in <module>
    text_decrypted = decryption(text_encrypted_base64, private_key)
  File "E:/3_code/python/python_base/202305/RSA解密.py", line 20, in decryption
    text_decrypted = cipher_private.decrypt(text_encrypted, Random.new().read)
  File "E:\3_code\python\python_base\venv\lib\site-packages\Crypto\Cipher\PKCS1_v1_5.py", line 174, in decrypt
    raise ValueError("Ciphertext with incorrect length (not %d bytes)" % k)
ValueError: Ciphertext with incorrect length (not 256 bytes)
'''