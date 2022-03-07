# -*- coding: utf-8 -*-
'''有时，测试需要调用依赖于全局设置的功能，或者调用无法轻松测试的代码(如网络访问)。monkeypatch fixture可以帮助您安全地设置/删除属性、
字典项或环境变量，或修改sys. patch。导入的路径。
'''

from pathlib import Path

def getssh():
    return Path.home()

def test_getssh(monkeypatch):
    def mockreturn():
        return Path("/abc")

    monkeypatch.setattr(Path, "home", mockreturn)

    x = getssh()
    assert x == Path("/abc/.ssh")

# -------------分割线-----------------
