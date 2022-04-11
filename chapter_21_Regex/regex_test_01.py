# -*- coding: utf-8 -*-

import re

tel1 = "707-827-7019"
res = re.match(r"(\d{3,4}[.-]?)+", tel1, flags=0)
res1 = re.fullmatch(r"(\d{3,4}[.-]?)+", tel1, flags=0)
res2 = re.fullmatch(r"(\d{3}[.-]?){2}\d{4}", tel1, flags=0)
res3 = re.fullmatch(r"^(\(\d{3}\)|^\d{3}[.-]? )? \d{3}[.-]? \d{4}$", tel1, flags=0)
# print(res)
# print(res1)
# print(res2)
# print(res3)


# 熟悉列表操作：
strings = [1,23,45,56,78,55,12,32]
# strings = reversed(strings) # 翻转，倒序排列
# strings.sort()
# strings.sort(reverse=True)
# strings.insert(0,199)
# strings.append(1232)
# strings.insert(int(len(strings)/2), 299)
# strings.pop(2)
# enumerate_str = enumerate(strings, 1)
# for index, value in enumerate_str:
#     print(index, value)

import base64
import rsa

__all__ = ['rsa_encrypt']

def _str2key(s):
    # 对字符串解码
    b_str = base64.b64decode(s)

    if len(b_str) < 162:
        return False

    hex_str = ''

    # 按位转换成16进制
    for x in b_str:
        h = hex(x)[2:]
        h = h.rjust(2, '0')
        hex_str += h

    # 找到模数和指数的开头结束位置
    m_start = 29 * 2
    e_start = 159 * 2
    m_len = 128 * 2
    e_len = 3 * 2

    modulus = hex_str[m_start:m_start + m_len]
    exponent = hex_str[e_start:e_start + e_len]
    print(modulus)
    print(exponent)

    return modulus, exponent

def rsa_encrypt(s, pubkey_str):
    '''
    rsa加密
    :param s:
    :param pubkey_str:公钥
    :return:
    '''
    key = _str2key(s)
    # print(key)
    # modulus = int(key[0], 16)
    # exponent = int(key[1], 16)
    # pubkey = rsa.PublicKey(modulus, exponent)
    # return base64.b64encode(rsa.encrypt(s.encode(), pubkey)).decode()

if __name__ == '__main__':
    public_rsa = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCq3McKAu99WkOq-QTV6v8x0zGDj5ShjiCi1TSwx_bSl-a" \
                 "n0grmunNbpqssUiMkCmaA8RlTwavgnsXFtylnWWPd-_-VFZR7cUt5c7Zd3jpPNbjDOkMr50Y64W4-eO0x8EvSrNsWwpsUieHZ1g" \
                 "lmOMlH6KGHE0h3_yhHOhWe3EYnKwIDAQAB"
    value = rsa_encrypt("12345678", public_rsa)
    print(value)
    ss = _str2key(public_rsa)
    print(ss)