# -*- coding: utf-8 -*-

import re

tel1 = "707-827-7019"
res = re.match(r"(\d{3,4}[.-]?)+", tel1, flags=0)
res1 = re.fullmatch(r"(\d{3,4}[.-]?)+", tel1, flags=0)
res2 = re.fullmatch(r"(\d{3}[.-]?){2}\d{4}", tel1, flags=0)
res3 = re.fullmatch(r"^(\(\d{3}\)|^\d{3}[.-]? )? \d{3}[.-]? \d{4}$", tel1, flags=0)
print(res)
print(res1)
print(res2)
print(res3)
