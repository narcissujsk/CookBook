import  html
import inspect


def avg(first, *rest):
    return (first+sum(rest))/(1+len(rest))


def make_elemet(name,value,**attrs):
    keyvals=[ ' %s="%s"' % item for item in attrs.items()]
    attr_str=''.join(keyvals)
    element='<{name}{attrs}>{value}</name>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )
    return element


def minnum(*values,clip=None):
    m=min(values)
    if clip is not None:
        m=clip if clip>m else m
    return m

#
add=lambda a,b:a+b



m = add("dd","f")
print(m)
print(add.__annotations__)