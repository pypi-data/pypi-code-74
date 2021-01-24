# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_phrasedml')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_phrasedml')
    _phrasedml = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_phrasedml', [dirname(__file__)])
        except ImportError:
            import _phrasedml
            return _phrasedml
        try:
            _mod = imp.load_module('_phrasedml', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _phrasedml = swig_import_helper()
    del swig_import_helper
else:
    import _phrasedml
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

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
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


class SwigPyIterator(_object):
    """Proxy of C++ swig::SwigPyIterator class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _phrasedml.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        """value(SwigPyIterator self) -> PyObject *"""
        return _phrasedml.SwigPyIterator_value(self)


    def incr(self, n=1):
        """
        incr(SwigPyIterator self, size_t n=1) -> SwigPyIterator
        incr(SwigPyIterator self) -> SwigPyIterator
        """
        return _phrasedml.SwigPyIterator_incr(self, n)


    def decr(self, n=1):
        """
        decr(SwigPyIterator self, size_t n=1) -> SwigPyIterator
        decr(SwigPyIterator self) -> SwigPyIterator
        """
        return _phrasedml.SwigPyIterator_decr(self, n)


    def distance(self, x):
        """distance(SwigPyIterator self, SwigPyIterator x) -> ptrdiff_t"""
        return _phrasedml.SwigPyIterator_distance(self, x)


    def equal(self, x):
        """equal(SwigPyIterator self, SwigPyIterator x) -> bool"""
        return _phrasedml.SwigPyIterator_equal(self, x)


    def copy(self):
        """copy(SwigPyIterator self) -> SwigPyIterator"""
        return _phrasedml.SwigPyIterator_copy(self)


    def next(self):
        """next(SwigPyIterator self) -> PyObject *"""
        return _phrasedml.SwigPyIterator_next(self)


    def __next__(self):
        """__next__(SwigPyIterator self) -> PyObject *"""
        return _phrasedml.SwigPyIterator___next__(self)


    def previous(self):
        """previous(SwigPyIterator self) -> PyObject *"""
        return _phrasedml.SwigPyIterator_previous(self)


    def advance(self, n):
        """advance(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator"""
        return _phrasedml.SwigPyIterator_advance(self, n)


    def __eq__(self, x):
        """__eq__(SwigPyIterator self, SwigPyIterator x) -> bool"""
        return _phrasedml.SwigPyIterator___eq__(self, x)


    def __ne__(self, x):
        """__ne__(SwigPyIterator self, SwigPyIterator x) -> bool"""
        return _phrasedml.SwigPyIterator___ne__(self, x)


    def __iadd__(self, n):
        """__iadd__(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator"""
        return _phrasedml.SwigPyIterator___iadd__(self, n)


    def __isub__(self, n):
        """__isub__(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator"""
        return _phrasedml.SwigPyIterator___isub__(self, n)


    def __add__(self, n):
        """__add__(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator"""
        return _phrasedml.SwigPyIterator___add__(self, n)


    def __sub__(self, *args):
        """
        __sub__(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator
        __sub__(SwigPyIterator self, SwigPyIterator x) -> ptrdiff_t
        """
        return _phrasedml.SwigPyIterator___sub__(self, *args)

    def __iter__(self):
        return self
SwigPyIterator_swigregister = _phrasedml.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

LIBPHRASEDML_VERSION_STRING = _phrasedml.LIBPHRASEDML_VERSION_STRING
PHRASEDML_NAMESPACE_H = _phrasedml.PHRASEDML_NAMESPACE_H

def convertFile(filename):
    """
    convertFile(char const * filename) -> char *


    Convert a file from phraSEDML to SEDML, or visa versa.  If None is
    returned, an error occurred, which can be retrieved with
    getLastError()'.

    Returns The converted file, as a string.

    Parameter 'filename' is the filename as a character string.  May be
    either absolute or relative to the directory the executable is being
    run from.

    See also getLastError().

    """
    return _phrasedml.convertFile(filename)

def convertString(model):
    """
    convertString(char const * model) -> char *


    Convert a model string from phraSEDML to SEDML, or visa versa.  If
    None is returned, an error occurred, which can be retrieved with
    getLastError().

    Returns The converted model, as a string.

    Parameter 'model' is the model as a character string.  May be either
    SED-ML or phraSED-ML.

    See also getLastError().

    """
    return _phrasedml.convertString(model)

def getLastError():
    """
    getLastError() -> char *


    When any function returns an error condition, a longer description of
    the problem is stored in memory, and is obtainable with this function.
    In most cases, this means that a call that returns a pointer returned
    'None' (or 0).

    """
    return _phrasedml.getLastError()

def getLastErrorLine():
    """
    getLastErrorLine() -> int


    Returns the line number of the file where the last error was obtained,
    if the last error was obtained when parsing a phraSED-ML file.
    Otherwise, returns 0.

    """
    return _phrasedml.getLastErrorLine()

def getWarnings():
    """
    getWarnings() -> char *


    When translating some other format to phraSEDML, elements that are
    unable to be translated are saved as warnings, retrievable with this
    function (returns None if no warnings present).

    """
    return _phrasedml.getWarnings()

def getLastSEDML():
    """
    getLastSEDML() -> char *


    If a previous 'convert' call was successful, the library retains an
    internal representation of the SEDML and the PhraSEDML.  This call
    converts that representation to SEDML and returns the value, returning
    an empty string if no such model exists.

    """
    return _phrasedml.getLastSEDML()

def getLastPhraSEDML():
    """
    getLastPhraSEDML() -> char *


    If a previous 'convert' call was successful, the library retains an
    internal representation of the SEDML and the PhraSEDML.  This call
    converts that representation to PhraSEDML and returns the value,
    returning an empty string if no such model exists.

    """
    return _phrasedml.getLastPhraSEDML()

def setWorkingDirectory(directory):
    """
    setWorkingDirectory(char const * directory)


    Sets the working directory for phraSED-ML to look for referenced
    files.

    Parameter 'directory' is the directory as a character string.  May be
    either absolute or relative to the directory the executable is being
    run from.

    """
    return _phrasedml.setWorkingDirectory(directory)

def setReferencedSBML(URI, sbmlstring):
    """
    setReferencedSBML(char const * URI, char const * sbmlstring) -> bool


    Allows phrasedml to use the given SBML document as the filename,
    instead of looking for the file on disk.  If the document is invalid
    SBML, 'false' is returned, but the document is still saved.

    Parameter 'URI' is the string that, when used in phrasedml, should
    reference the 'sbmlstring'. Parameter 'sbmlstring' is the SBML
    document string to use when the 'URI' is encountered.

    Returns a boolean indicating whether the document is valid SBML or
    not.  Either way, the document is saved as the reference document for
    the given filename string.

    """
    return _phrasedml.setReferencedSBML(URI, sbmlstring)

def clearReferencedSBML():
    """
    clearReferencedSBML()


    Clears and removes all referenced SBML documents.

    """
    return _phrasedml.clearReferencedSBML()

def addDotXMLToModelSources(force=False):
    """
    addDotXMLToModelSources(bool force=False)
    addDotXMLToModelSources()


    Sometimes, a user may wish to input phrasedml with the name of a
    model, instead of an actual filename.  This is particularly true in
    Tellurium, where one model is defined by Antimony, and has no
    immediate filename.  When creating SED-ML, however, an actual file
    needs to be referenced.  As such, [modelname].xml is a more realistic
    filename to use than simply [modelname]--this function converts all
    such filenames in the model, and assumes that you are making similar
    changes to the files themselves.  If any filename already ends in
    '.xml' or in '.sbml', that filename will not be changed.  To retrieve
    the modified version, use getLastPhraSEDML() or getLastSEDML().

    """
    return _phrasedml.addDotXMLToModelSources(force)

def setWriteSEDMLTimestamp(writeTimestamp):
    """
    setWriteSEDMLTimestamp(bool writeTimestamp)


    Sets whether, when writing a SED-ML file, the timestamp is included.

    """
    return _phrasedml.setWriteSEDMLTimestamp(writeTimestamp)
# This file is compatible with both classic and new-style classes.


