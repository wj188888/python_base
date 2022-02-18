# -*- coding:utf-8 -*-
import os
import jinja2
import yaml
import importlib
import inspect

def render(tpl_path, **kwargs):
    """渲染yml文件"""
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(**kwargs)


def all_functions():
    """加载debug.模块"""
    debug_module = importlib.import_module("debug");
    all_function = inspect.getmembers(debug_module,inspect.isfunction)

    return dict(all_function)

if __name__ == '__main__':
    r = render("aa.yml", **all_functions())
    print(r)
    print(yaml.safe_load(r))