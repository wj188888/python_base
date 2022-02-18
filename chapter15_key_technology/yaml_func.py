# -- coding:utf-8 --
'''
    在yaml文件中, 通过{{函数名称（） }}来引用函数

'''
import os
import jinja2
import yaml
import random


def render(tpl_path, **kwargs):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(**kwargs)


# yaml 文件调用以下函数
def rand_str():
    return str(random.randint(1000000, 2000000))


if __name__ == '__main__':
    r = render("aa.yml", **{"rand_str": rand_str})
    print(r)
    print(yaml.safe_load(r))