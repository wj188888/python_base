# 有一个500G的文件，需要一行行写入到数据库中去
# 首先for i in data是不行的，这些都是放在内存中

def myreadlines(f, newline):
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            # 这一步是更新buf，让每次截取的内容都是分割符的后面；
            buf = buf[pos + len(newline):]
        chunk = f.read(4096*10)
        if not chunk:
            yield buf
            break
        buf += chunk

with open(r"file_data/wj_input.txt") as f:
    for line in myreadlines(f, "{|}"):
        print(line)