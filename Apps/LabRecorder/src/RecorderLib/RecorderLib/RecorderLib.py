# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.3
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_RecorderLib', [dirname(__file__)])
        except ImportError:
            import _RecorderLib
            return _RecorderLib
        if fp is not None:
            try:
                _mod = imp.load_module('_RecorderLib', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _RecorderLib = swig_import_helper()
    del swig_import_helper
else:
    import _RecorderLib
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def cdata(ptr, nelements=1):
    return _RecorderLib.cdata(ptr, nelements)
cdata = _RecorderLib.cdata

def memmove(data, indata):
    return _RecorderLib.memmove(data, indata)
memmove = _RecorderLib.memmove

def rl_start_recording(filename, recordfrom, num_recordfrom, watchfor, collect_offsets):
    return _RecorderLib.rl_start_recording(filename, recordfrom, num_recordfrom, watchfor, collect_offsets)
rl_start_recording = _RecorderLib.rl_start_recording

def rl_end_recording(rec):
    return _RecorderLib.rl_end_recording(rec)
rl_end_recording = _RecorderLib.rl_end_recording

def new_info(nelements):
    return _RecorderLib.new_info(nelements)
new_info = _RecorderLib.new_info

def delete_info(ary):
    return _RecorderLib.delete_info(ary)
delete_info = _RecorderLib.delete_info

def info_getitem(ary, index):
    return _RecorderLib.info_getitem(ary, index)
info_getitem = _RecorderLib.info_getitem

def info_setitem(ary, index, value):
    return _RecorderLib.info_setitem(ary, index, value)
info_setitem = _RecorderLib.info_setitem

def new_str(nelements):
    return _RecorderLib.new_str(nelements)
new_str = _RecorderLib.new_str

def delete_str(ary):
    return _RecorderLib.delete_str(ary)
delete_str = _RecorderLib.delete_str

def str_getitem(ary, index):
    return _RecorderLib.str_getitem(ary, index)
str_getitem = _RecorderLib.str_getitem

def str_setitem(ary, index, value):
    return _RecorderLib.str_setitem(ary, index, value)
str_setitem = _RecorderLib.str_setitem
# This file is compatible with both classic and new-style classes.

