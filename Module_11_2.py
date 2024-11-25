import inspect

def introspection_info(obj):
    res,_name,_class = '','',''
    _listinfo = dir(obj)
    _type =f'type: {type(obj)}, '
    _methods = f'methods: {[x for x in _listinfo if '__' in x]}, '
    _attrs = f'attrs: {[x for x in _listinfo if '__' not in x]}, '
    _module = f'module:  {inspect.getmodule(obj) if not None else ''}, '
    if hasattr(obj, '__name__'):
       _name = f'name {obj.__name__}, '
    if hasattr(obj, '__class__'):
        _class = f'class: {obj.__class__.__name__}, '
    _id = f'id: {id(obj)}, '
    _iscallable = f'callable: {True if callable(obj) else False}'

    _res = _type + _methods + _attrs + _module + _name + _class+ _id+_iscallable
    return _res


new_intr = introspection_info(10)
print(new_intr)
new_intr = introspection_info('Hello')
print(new_intr)
new_intr = introspection_info(introspection_info)
print(new_intr)


