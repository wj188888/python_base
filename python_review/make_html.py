# -*- coding: utf-8 -*-

def tag(name, *content, cls=None, **attrs):
    '''生成一个或多个HTML标签'''
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attrs_str = ''.join('%s="%s"'%(attr,value) for attr,value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s<%s>'%(name,attr_str,c,name) for c in content)
    else:
        return '<%s%s />'%(name, attr_str)


if __name__ == '__main__':
    x=tag("html",'<body>','<content>','<div>','</div>')
    print(x)