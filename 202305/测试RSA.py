# -*- coding: utf-8 -*-
# @Author: jie wang
# @Date: 2023/5/17 9:21

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

# 生成RSA密钥对
key = RSA.generate(2048)

# 获取公钥和私钥
public_key = key.publickey()
private_key = key

# 加密字符串
message = '18428333658'
cipher = PKCS1_v1_5.new(public_key)
ciphertext = cipher.encrypt(message.encode())

# 解密字符串
cipher = PKCS1_v1_5.new(private_key)
plaintext = cipher.decrypt(ciphertext, None).decode()

#截取20位
ciphertext = ciphertext.hex()
ciphertext = ciphertext[0 : 31 : 1]
print('加密后的字符串:', ciphertext)
print('解密后的字符串:', plaintext)
