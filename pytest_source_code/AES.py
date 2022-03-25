# -*- coding:utf-8 -*-

import base64


from Cryptodome.Cipher import AES
from Cryptodome import Random

def AES_liil():
    """对称加密AES，1.多段加密， 2.多个参数 vi （偏移量）"""
    text = 'zhangxiong'
    Key = b'dasdasds'
    iv = Random.new().read(AES, block_size)
    aes = AES.new(key, AES.MODE_CFB, iv)

    # 加密
    encrypt_text = aes.encrypt(text.encode())
    decrypt_aes = AES.new(key, AES.MODE_CFB, iv)
    print(decrypt_aes)

    # 解密
    print(decrypt_aes.decrypt(encrypt_text))

if __name__ == '__main__':
    # 实验失败
    AES_liil()
