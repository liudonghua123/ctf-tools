# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
IDA Plugin SDK API wrapper: funcs
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ida_funcs', [dirname(__file__)])
        except ImportError:
            import _ida_funcs
            return _ida_funcs
        if fp is not None:
            try:
                _mod = imp.load_module('_ida_funcs', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ida_funcs = swig_import_helper()
    del swig_import_helper
else:
    import _ida_funcs
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


import ida_idaapi

import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        func.func_dict["bc695redef"] = True
        return func

import ida_range
class regarg_t(object):
    """
    Proxy of C++ regarg_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    reg = _swig_property(_ida_funcs.regarg_t_reg_get, _ida_funcs.regarg_t_reg_set)
    type = _swig_property(_ida_funcs.regarg_t_type_get, _ida_funcs.regarg_t_type_set)
    name = _swig_property(_ida_funcs.regarg_t_name_get, _ida_funcs.regarg_t_name_set)
    def __init__(self, *args):
        """
        __init__(self) -> regarg_t
        """
        this = _ida_funcs.new_regarg_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_funcs.delete_regarg_t
    __del__ = lambda self : None;
regarg_t_swigregister = _ida_funcs.regarg_t_swigregister
regarg_t_swigregister(regarg_t)

class func_t(ida_range.range_t):
    """
    Proxy of C++ func_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    flags = _swig_property(_ida_funcs.func_t_flags_get, _ida_funcs.func_t_flags_set)
    def is_far(self, *args):
        """
        is_far(self) -> bool
        """
        return _ida_funcs.func_t_is_far(self, *args)

    def does_return(self, *args):
        """
        does_return(self) -> bool
        """
        return _ida_funcs.func_t_does_return(self, *args)

    def analyzed_sp(self, *args):
        """
        analyzed_sp(self) -> bool
        """
        return _ida_funcs.func_t_analyzed_sp(self, *args)

    frame = _swig_property(_ida_funcs.func_t_frame_get, _ida_funcs.func_t_frame_set)
    frsize = _swig_property(_ida_funcs.func_t_frsize_get, _ida_funcs.func_t_frsize_set)
    frregs = _swig_property(_ida_funcs.func_t_frregs_get, _ida_funcs.func_t_frregs_set)
    argsize = _swig_property(_ida_funcs.func_t_argsize_get, _ida_funcs.func_t_argsize_set)
    fpd = _swig_property(_ida_funcs.func_t_fpd_get, _ida_funcs.func_t_fpd_set)
    color = _swig_property(_ida_funcs.func_t_color_get, _ida_funcs.func_t_color_set)
    pntqty = _swig_property(_ida_funcs.func_t_pntqty_get, _ida_funcs.func_t_pntqty_set)
    points = _swig_property(_ida_funcs.func_t_points_get, _ida_funcs.func_t_points_set)
    regvarqty = _swig_property(_ida_funcs.func_t_regvarqty_get, _ida_funcs.func_t_regvarqty_set)
    regvars = _swig_property(_ida_funcs.func_t_regvars_get, _ida_funcs.func_t_regvars_set)
    llabelqty = _swig_property(_ida_funcs.func_t_llabelqty_get, _ida_funcs.func_t_llabelqty_set)
    llabels = _swig_property(_ida_funcs.func_t_llabels_get, _ida_funcs.func_t_llabels_set)
    regargqty = _swig_property(_ida_funcs.func_t_regargqty_get, _ida_funcs.func_t_regargqty_set)
    regargs = _swig_property(_ida_funcs.func_t_regargs_get, _ida_funcs.func_t_regargs_set)
    tailqty = _swig_property(_ida_funcs.func_t_tailqty_get, _ida_funcs.func_t_tailqty_set)
    tails = _swig_property(_ida_funcs.func_t_tails_get, _ida_funcs.func_t_tails_set)
    owner = _swig_property(_ida_funcs.func_t_owner_get, _ida_funcs.func_t_owner_set)
    refqty = _swig_property(_ida_funcs.func_t_refqty_get, _ida_funcs.func_t_refqty_set)
    referers = _swig_property(_ida_funcs.func_t_referers_get, _ida_funcs.func_t_referers_set)
    def __init__(self, *args):
        """
        __init__(self, start=0, end=0, f=0) -> func_t
        """
        this = _ida_funcs.new_func_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_funcs.delete_func_t
    __del__ = lambda self : None;
func_t_swigregister = _ida_funcs.func_t_swigregister
func_t_swigregister(func_t)
FUNC_NORET = _ida_funcs.FUNC_NORET
FUNC_FAR = _ida_funcs.FUNC_FAR
FUNC_LIB = _ida_funcs.FUNC_LIB
FUNC_STATICDEF = _ida_funcs.FUNC_STATICDEF
FUNC_FRAME = _ida_funcs.FUNC_FRAME
FUNC_USERFAR = _ida_funcs.FUNC_USERFAR
FUNC_HIDDEN = _ida_funcs.FUNC_HIDDEN
FUNC_THUNK = _ida_funcs.FUNC_THUNK
FUNC_BOTTOMBP = _ida_funcs.FUNC_BOTTOMBP
FUNC_NORET_PENDING = _ida_funcs.FUNC_NORET_PENDING
FUNC_SP_READY = _ida_funcs.FUNC_SP_READY
FUNC_PURGED_OK = _ida_funcs.FUNC_PURGED_OK
FUNC_TAIL = _ida_funcs.FUNC_TAIL


def is_func_entry(*args):
  """
  is_func_entry(pfn) -> bool
  """
  return _ida_funcs.is_func_entry(*args)

def is_func_tail(*args):
  """
  is_func_tail(pfn) -> bool
  """
  return _ida_funcs.is_func_tail(*args)

def lock_func_range(*args):
  """
  lock_func_range(pfn, lock)
  """
  return _ida_funcs.lock_func_range(*args)
class lock_func(object):
    """
    Proxy of C++ lock_func class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args):
        """
        __init__(self, _pfn) -> lock_func
        """
        this = _ida_funcs.new_lock_func(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_funcs.delete_lock_func
    __del__ = lambda self : None;
lock_func_swigregister = _ida_funcs.lock_func_swigregister
lock_func_swigregister(lock_func)


def is_func_locked(*args):
  """
  is_func_locked(pfn) -> bool
  """
  return _ida_funcs.is_func_locked(*args)

def get_func(*args):
  """
  get_func(ea) -> func_t
  """
  return _ida_funcs.get_func(*args)

def get_func_chunknum(*args):
  """
  get_func_chunknum(pfn, ea) -> int
  """
  return _ida_funcs.get_func_chunknum(*args)

def func_contains(*args):
  """
  func_contains(pfn, ea) -> bool
  """
  return _ida_funcs.func_contains(*args)

def is_same_func(*args):
  """
  is_same_func(ea1, ea2) -> bool
  """
  return _ida_funcs.is_same_func(*args)

def getn_func(*args):
  """
  getn_func(n) -> func_t
  """
  return _ida_funcs.getn_func(*args)

def get_func_qty(*args):
  """
  get_func_qty() -> size_t
  """
  return _ida_funcs.get_func_qty(*args)

def get_func_num(*args):
  """
  get_func_num(ea) -> int
  """
  return _ida_funcs.get_func_num(*args)

def get_prev_func(*args):
  """
  get_prev_func(ea) -> func_t
  """
  return _ida_funcs.get_prev_func(*args)

def get_next_func(*args):
  """
  get_next_func(ea) -> func_t
  """
  return _ida_funcs.get_next_func(*args)

def get_func_ranges(*args):
  """
  get_func_ranges(ranges, pfn) -> ea_t
  """
  return _ida_funcs.get_func_ranges(*args)

def get_func_cmt(*args):
  """
  get_func_cmt(pfn, repeatable) -> ssize_t
  """
  return _ida_funcs.get_func_cmt(*args)

def set_func_cmt(*args):
  """
  set_func_cmt(pfn, cmt, repeatable) -> bool
  """
  return _ida_funcs.set_func_cmt(*args)

def update_func(*args):
  """
  update_func(pfn) -> bool
  """
  return _ida_funcs.update_func(*args)

def add_func_ex(*args):
  """
  add_func_ex(pfn) -> bool
  """
  return _ida_funcs.add_func_ex(*args)

def add_func(*args):
  """
  add_func(ea1, ea2=BADADDR) -> bool
  """
  return _ida_funcs.add_func(*args)

def del_func(*args):
  """
  del_func(ea) -> bool
  """
  return _ida_funcs.del_func(*args)

def set_func_start(*args):
  """
  set_func_start(ea, newstart) -> int
  """
  return _ida_funcs.set_func_start(*args)
MOVE_FUNC_OK = _ida_funcs.MOVE_FUNC_OK
MOVE_FUNC_NOCODE = _ida_funcs.MOVE_FUNC_NOCODE
MOVE_FUNC_BADSTART = _ida_funcs.MOVE_FUNC_BADSTART
MOVE_FUNC_NOFUNC = _ida_funcs.MOVE_FUNC_NOFUNC
MOVE_FUNC_REFUSED = _ida_funcs.MOVE_FUNC_REFUSED

def set_func_end(*args):
  """
  set_func_end(ea, newend) -> bool
  """
  return _ida_funcs.set_func_end(*args)

def reanalyze_function(*args):
  """
  reanalyze_function(pfn, ea1=0, ea2=BADADDR, analyze_parents=False)
  """
  return _ida_funcs.reanalyze_function(*args)

def find_func_bounds(*args):
  """
  find_func_bounds(nfn, flags) -> int
  """
  return _ida_funcs.find_func_bounds(*args)
FIND_FUNC_NORMAL = _ida_funcs.FIND_FUNC_NORMAL
FIND_FUNC_DEFINE = _ida_funcs.FIND_FUNC_DEFINE
FIND_FUNC_IGNOREFN = _ida_funcs.FIND_FUNC_IGNOREFN
FIND_FUNC_KEEPBD = _ida_funcs.FIND_FUNC_KEEPBD
FIND_FUNC_UNDEF = _ida_funcs.FIND_FUNC_UNDEF
FIND_FUNC_OK = _ida_funcs.FIND_FUNC_OK
FIND_FUNC_EXIST = _ida_funcs.FIND_FUNC_EXIST

def get_func_name(*args):
  """
  get_func_name(ea) -> ssize_t
  """
  return _ida_funcs.get_func_name(*args)

def get_func_bitness(*args):
  """
  get_func_bitness(pfn) -> int
  """
  return _ida_funcs.get_func_bitness(*args)

def get_func_bits(*args):
  """
  get_func_bits(pfn) -> int
  """
  return _ida_funcs.get_func_bits(*args)

def get_func_bytes(*args):
  """
  get_func_bytes(pfn) -> int
  """
  return _ida_funcs.get_func_bytes(*args)

def is_visible_func(*args):
  """
  is_visible_func(pfn) -> bool
  """
  return _ida_funcs.is_visible_func(*args)

def is_finally_visible_func(*args):
  """
  is_finally_visible_func(pfn) -> bool
  """
  return _ida_funcs.is_finally_visible_func(*args)

def set_visible_func(*args):
  """
  set_visible_func(pfn, visible)
  """
  return _ida_funcs.set_visible_func(*args)

def set_func_name_if_jumpfunc(*args):
  """
  set_func_name_if_jumpfunc(pfn, oldname) -> int
  """
  return _ida_funcs.set_func_name_if_jumpfunc(*args)

def calc_thunk_func_target(*args):
  """
  calc_thunk_func_target(pfn, fptr) -> ea_t
  """
  return _ida_funcs.calc_thunk_func_target(*args)

def func_does_return(*args):
  """
  func_does_return(callee) -> bool
  """
  return _ida_funcs.func_does_return(*args)

def reanalyze_noret_flag(*args):
  """
  reanalyze_noret_flag(ea) -> bool
  """
  return _ida_funcs.reanalyze_noret_flag(*args)

def set_noret_insn(*args):
  """
  set_noret_insn(insn_ea, noret) -> bool
  """
  return _ida_funcs.set_noret_insn(*args)

def get_fchunk(*args):
  """
  get_fchunk(ea) -> func_t
  """
  return _ida_funcs.get_fchunk(*args)

def getn_fchunk(*args):
  """
  getn_fchunk(n) -> func_t
  """
  return _ida_funcs.getn_fchunk(*args)

def get_fchunk_qty(*args):
  """
  get_fchunk_qty() -> size_t
  """
  return _ida_funcs.get_fchunk_qty(*args)

def get_fchunk_num(*args):
  """
  get_fchunk_num(ea) -> int
  """
  return _ida_funcs.get_fchunk_num(*args)

def get_prev_fchunk(*args):
  """
  get_prev_fchunk(ea) -> func_t
  """
  return _ida_funcs.get_prev_fchunk(*args)

def get_next_fchunk(*args):
  """
  get_next_fchunk(ea) -> func_t
  """
  return _ida_funcs.get_next_fchunk(*args)

def append_func_tail(*args):
  """
  append_func_tail(pfn, ea1, ea2) -> bool
  """
  return _ida_funcs.append_func_tail(*args)

def remove_func_tail(*args):
  """
  remove_func_tail(pfn, tail_ea) -> bool
  """
  return _ida_funcs.remove_func_tail(*args)

def set_tail_owner(*args):
  """
  set_tail_owner(fnt, func_start) -> bool
  """
  return _ida_funcs.set_tail_owner(*args)

def func_tail_iterator_set(*args):
  """
  func_tail_iterator_set(fti, pfn, ea) -> bool
  """
  return _ida_funcs.func_tail_iterator_set(*args)

def func_tail_iterator_set_ea(*args):
  """
  func_tail_iterator_set_ea(fti, ea) -> bool
  """
  return _ida_funcs.func_tail_iterator_set_ea(*args)

def func_parent_iterator_set(*args):
  """
  func_parent_iterator_set(fpi, pfn) -> bool
  """
  return _ida_funcs.func_parent_iterator_set(*args)

def func_item_iterator_next(*args):
  """
  func_item_iterator_next(fii, testf, ud) -> bool
  """
  return _ida_funcs.func_item_iterator_next(*args)

def func_item_iterator_prev(*args):
  """
  func_item_iterator_prev(fii, testf, ud) -> bool
  """
  return _ida_funcs.func_item_iterator_prev(*args)

def func_item_iterator_decode_prev_insn(*args):
  """
  func_item_iterator_decode_prev_insn(fii, out) -> bool
  """
  return _ida_funcs.func_item_iterator_decode_prev_insn(*args)

def func_item_iterator_decode_preceding_insn(*args):
  """
  func_item_iterator_decode_preceding_insn(fii, visited, p_farref, out) -> bool
  """
  return _ida_funcs.func_item_iterator_decode_preceding_insn(*args)

def f_any(*args):
  """
  f_any(arg1, arg2) -> bool
  """
  return _ida_funcs.f_any(*args)
class func_tail_iterator_t(object):
    """
    Proxy of C++ func_tail_iterator_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args):
        """
        __init__(self) -> func_tail_iterator_t
        __init__(self, _pfn, ea=BADADDR) -> func_tail_iterator_t
        """
        this = _ida_funcs.new_func_tail_iterator_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_funcs.delete_func_tail_iterator_t
    __del__ = lambda self : None;
    def set(self, *args):
        """
        set(self, _pfn, ea=BADADDR) -> bool
        """
        return _ida_funcs.func_tail_iterator_t_set(self, *args)

    def set_ea(self, *args):
        """
        set_ea(self, ea) -> bool
        """
        return _ida_funcs.func_tail_iterator_t_set_ea(self, *args)

    def set_range(self, *args):
        """
        set_range(self, ea1, ea2) -> bool
        """
        return _ida_funcs.func_tail_iterator_t_set_range(self, *args)

    def chunk(self, *args):
        """
        chunk(self) -> range_t
        """
        return _ida_funcs.func_tail_iterator_t_chunk(self, *args)

    def first(self, *args):
        """
        first(self) -> bool
        """
        return _ida_funcs.func_tail_iterator_t_first(self, *args)

    def last(self, *args):
        """
        last(self) -> bool
        """
        return _ida_funcs.func_tail_iterator_t_last(self, *args)

    def next(self, *args):
        """
        next(self) -> bool
        """
        return _ida_funcs.func_tail_iterator_t_next(self, *args)

    def prev(self, *args):
        """
        prev(self) -> bool
        """
        return _ida_funcs.func_tail_iterator_t_prev(self, *args)

    def main(self, *args):
        """
        main(self) -> bool
        """
        return _ida_funcs.func_tail_iterator_t_main(self, *args)

func_tail_iterator_t_swigregister = _ida_funcs.func_tail_iterator_t_swigregister
func_tail_iterator_t_swigregister(func_tail_iterator_t)

class func_item_iterator_t(object):
    """
    Proxy of C++ func_item_iterator_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args):
        """
        __init__(self) -> func_item_iterator_t
        __init__(self, pfn, _ea=BADADDR) -> func_item_iterator_t
        """
        this = _ida_funcs.new_func_item_iterator_t(*args)
        try: self.this.append(this)
        except: self.this = this
    def set(self, *args):
        """
        set(self, pfn, _ea=BADADDR) -> bool
        """
        return _ida_funcs.func_item_iterator_t_set(self, *args)

    def set_range(self, *args):
        """
        set_range(self, ea1, ea2) -> bool
        """
        return _ida_funcs.func_item_iterator_t_set_range(self, *args)

    def first(self, *args):
        """
        first(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_first(self, *args)

    def last(self, *args):
        """
        last(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_last(self, *args)

    def current(self, *args):
        """
        current(self) -> ea_t
        """
        return _ida_funcs.func_item_iterator_t_current(self, *args)

    def chunk(self, *args):
        """
        chunk(self) -> range_t
        """
        return _ida_funcs.func_item_iterator_t_chunk(self, *args)

    def next(self, *args):
        """
        next(self, func, ud) -> bool
        """
        return _ida_funcs.func_item_iterator_t_next(self, *args)

    def prev(self, *args):
        """
        prev(self, func, ud) -> bool
        """
        return _ida_funcs.func_item_iterator_t_prev(self, *args)

    def next_addr(self, *args):
        """
        next_addr(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_next_addr(self, *args)

    def next_head(self, *args):
        """
        next_head(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_next_head(self, *args)

    def next_code(self, *args):
        """
        next_code(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_next_code(self, *args)

    def next_data(self, *args):
        """
        next_data(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_next_data(self, *args)

    def next_not_tail(self, *args):
        """
        next_not_tail(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_next_not_tail(self, *args)

    def prev_addr(self, *args):
        """
        prev_addr(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_prev_addr(self, *args)

    def prev_head(self, *args):
        """
        prev_head(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_prev_head(self, *args)

    def prev_code(self, *args):
        """
        prev_code(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_prev_code(self, *args)

    def prev_data(self, *args):
        """
        prev_data(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_prev_data(self, *args)

    def prev_not_tail(self, *args):
        """
        prev_not_tail(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_prev_not_tail(self, *args)

    def decode_prev_insn(self, *args):
        """
        decode_prev_insn(self, out) -> bool
        """
        return _ida_funcs.func_item_iterator_t_decode_prev_insn(self, *args)

    def decode_preceding_insn(self, *args):
        """
        decode_preceding_insn(self, visited, p_farref, out) -> bool
        """
        return _ida_funcs.func_item_iterator_t_decode_preceding_insn(self, *args)

    __swig_destroy__ = _ida_funcs.delete_func_item_iterator_t
    __del__ = lambda self : None;
func_item_iterator_t_swigregister = _ida_funcs.func_item_iterator_t_swigregister
func_item_iterator_t_swigregister(func_item_iterator_t)

class func_parent_iterator_t(object):
    """
    Proxy of C++ func_parent_iterator_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args):
        """
        __init__(self) -> func_parent_iterator_t
        __init__(self, _fnt) -> func_parent_iterator_t
        """
        this = _ida_funcs.new_func_parent_iterator_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_funcs.delete_func_parent_iterator_t
    __del__ = lambda self : None;
    def set(self, *args):
        """
        set(self, _fnt) -> bool
        """
        return _ida_funcs.func_parent_iterator_t_set(self, *args)

    def parent(self, *args):
        """
        parent(self) -> ea_t
        """
        return _ida_funcs.func_parent_iterator_t_parent(self, *args)

    def first(self, *args):
        """
        first(self) -> bool
        """
        return _ida_funcs.func_parent_iterator_t_first(self, *args)

    def last(self, *args):
        """
        last(self) -> bool
        """
        return _ida_funcs.func_parent_iterator_t_last(self, *args)

    def next(self, *args):
        """
        next(self) -> bool
        """
        return _ida_funcs.func_parent_iterator_t_next(self, *args)

    def prev(self, *args):
        """
        prev(self) -> bool
        """
        return _ida_funcs.func_parent_iterator_t_prev(self, *args)

    def reset_fnt(self, *args):
        """
        reset_fnt(self, _fnt)
        """
        return _ida_funcs.func_parent_iterator_t_reset_fnt(self, *args)

func_parent_iterator_t_swigregister = _ida_funcs.func_parent_iterator_t_swigregister
func_parent_iterator_t_swigregister(func_parent_iterator_t)


def get_prev_func_addr(*args):
  """
  get_prev_func_addr(pfn, ea) -> ea_t
  """
  return _ida_funcs.get_prev_func_addr(*args)

def get_next_func_addr(*args):
  """
  get_next_func_addr(pfn, ea) -> ea_t
  """
  return _ida_funcs.get_next_func_addr(*args)

def read_regargs(*args):
  """
  read_regargs(pfn)
  """
  return _ida_funcs.read_regargs(*args)

def add_regarg(*args):
  """
  add_regarg(pfn, reg, tif, name)
  """
  return _ida_funcs.add_regarg(*args)
IDASGN_OK = _ida_funcs.IDASGN_OK
IDASGN_BADARG = _ida_funcs.IDASGN_BADARG
IDASGN_APPLIED = _ida_funcs.IDASGN_APPLIED
IDASGN_CURRENT = _ida_funcs.IDASGN_CURRENT
IDASGN_PLANNED = _ida_funcs.IDASGN_PLANNED

def plan_to_apply_idasgn(*args):
  """
  plan_to_apply_idasgn(fname) -> int
  """
  return _ida_funcs.plan_to_apply_idasgn(*args)

def apply_idasgn_to(*args):
  """
  apply_idasgn_to(signame, ea, is_startup) -> int
  """
  return _ida_funcs.apply_idasgn_to(*args)

def get_idasgn_qty(*args):
  """
  get_idasgn_qty() -> int
  """
  return _ida_funcs.get_idasgn_qty(*args)

def get_current_idasgn(*args):
  """
  get_current_idasgn() -> int
  """
  return _ida_funcs.get_current_idasgn(*args)

def calc_idasgn_state(*args):
  """
  calc_idasgn_state(n) -> int
  """
  return _ida_funcs.calc_idasgn_state(*args)

def del_idasgn(*args):
  """
  del_idasgn(n) -> int
  """
  return _ida_funcs.del_idasgn(*args)

def get_idasgn_title(*args):
  """
  get_idasgn_title(name) -> ssize_t
  """
  return _ida_funcs.get_idasgn_title(*args)

def apply_startup_sig(*args):
  """
  apply_startup_sig(ea, startup) -> bool
  """
  return _ida_funcs.apply_startup_sig(*args)

def try_to_add_libfunc(*args):
  """
  try_to_add_libfunc(ea) -> int
  """
  return _ida_funcs.try_to_add_libfunc(*args)
LIBFUNC_FOUND = _ida_funcs.LIBFUNC_FOUND
LIBFUNC_NONE = _ida_funcs.LIBFUNC_NONE
LIBFUNC_DELAY = _ida_funcs.LIBFUNC_DELAY

def get_fchunk_referer(*args):
  """
  get_fchunk_referer(ea, idx) -> ea_t


  """
  return _ida_funcs.get_fchunk_referer(*args)

def get_idasgn_desc(*args):
  """
  get_idasgn_desc(n) -> PyObject *


  Get information about a signature in the list.
  It returns: (name of signature, names of optional libraries)
  
  See also: get_idasgn_desc_with_matches
  
  @param n: number of signature in the list (0..get_idasgn_qty()-1)
  @return: None on failure or tuple(signame, optlibs)
  """
  return _ida_funcs.get_idasgn_desc(*args)

def get_idasgn_desc_with_matches(*args):
  """
  get_idasgn_desc_with_matches(n) -> PyObject *


  Get information about a signature in the list.
  It returns: (name of signature, names of optional libraries, number of matches)
  
  @param n: number of signature in the list (0..get_idasgn_qty()-1)
  @return: None on failure or tuple(signame, optlibs, nmatches)
  """
  return _ida_funcs.get_idasgn_desc_with_matches(*args)
#<pycode(py_funcs)>
#</pycode(py_funcs)>

if _BC695:
    FUNC_STATIC=FUNC_STATICDEF
    add_regarg2=add_regarg
    clear_func_struct=lambda *args: True
    @bc695redef
    def del_func_cmt(pfn, rpt):
        set_func_cmt(pfn, "", rpt)
    func_parent_iterator_set2=func_parent_iterator_set
    func_setend=set_func_end
    func_setstart=set_func_start
    func_tail_iterator_set2=func_tail_iterator_set
    @bc695redef
    def get_func_limits(pfn, limits):
        import ida_range
        rs = ida_range.rangeset_t()
        if get_func_ranges(rs, pfn) == ida_idaapi.BADADDR:
            return False
        limits.start_ea = rs.begin().start_ea
        limits.end_ea = rs.begin().end_ea
        return True
    get_func_name2=get_func_name




