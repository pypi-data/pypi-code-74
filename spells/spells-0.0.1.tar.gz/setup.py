# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['spells',
 'spells.env.Lib.site-packages',
 'spells.env.Lib.site-packages.PIL',
 'spells.env.Lib.site-packages.aenum',
 'spells.env.Lib.site-packages.click',
 'spells.env.Lib.site-packages.cutesnowflakes',
 'spells.env.Lib.site-packages.numpy',
 'spells.env.Lib.site-packages.numpy.compat',
 'spells.env.Lib.site-packages.numpy.compat.tests',
 'spells.env.Lib.site-packages.numpy.core',
 'spells.env.Lib.site-packages.numpy.core.tests',
 'spells.env.Lib.site-packages.numpy.distutils',
 'spells.env.Lib.site-packages.numpy.distutils.command',
 'spells.env.Lib.site-packages.numpy.distutils.fcompiler',
 'spells.env.Lib.site-packages.numpy.distutils.tests',
 'spells.env.Lib.site-packages.numpy.doc',
 'spells.env.Lib.site-packages.numpy.f2py',
 'spells.env.Lib.site-packages.numpy.f2py.tests',
 'spells.env.Lib.site-packages.numpy.fft',
 'spells.env.Lib.site-packages.numpy.fft.tests',
 'spells.env.Lib.site-packages.numpy.lib',
 'spells.env.Lib.site-packages.numpy.lib.tests',
 'spells.env.Lib.site-packages.numpy.linalg',
 'spells.env.Lib.site-packages.numpy.linalg.tests',
 'spells.env.Lib.site-packages.numpy.ma',
 'spells.env.Lib.site-packages.numpy.ma.tests',
 'spells.env.Lib.site-packages.numpy.matrixlib',
 'spells.env.Lib.site-packages.numpy.matrixlib.tests',
 'spells.env.Lib.site-packages.numpy.polynomial',
 'spells.env.Lib.site-packages.numpy.polynomial.tests',
 'spells.env.Lib.site-packages.numpy.random',
 'spells.env.Lib.site-packages.numpy.random._examples.cffi',
 'spells.env.Lib.site-packages.numpy.random._examples.cython',
 'spells.env.Lib.site-packages.numpy.random._examples.numba',
 'spells.env.Lib.site-packages.numpy.random.tests',
 'spells.env.Lib.site-packages.numpy.random.tests.data',
 'spells.env.Lib.site-packages.numpy.testing',
 'spells.env.Lib.site-packages.numpy.testing._private',
 'spells.env.Lib.site-packages.numpy.testing.tests',
 'spells.env.Lib.site-packages.numpy.tests',
 'spells.env.Lib.site-packages.pip',
 'spells.env.Lib.site-packages.pip._internal',
 'spells.env.Lib.site-packages.pip._internal.cli',
 'spells.env.Lib.site-packages.pip._internal.commands',
 'spells.env.Lib.site-packages.pip._internal.distributions',
 'spells.env.Lib.site-packages.pip._internal.index',
 'spells.env.Lib.site-packages.pip._internal.models',
 'spells.env.Lib.site-packages.pip._internal.network',
 'spells.env.Lib.site-packages.pip._internal.operations',
 'spells.env.Lib.site-packages.pip._internal.operations.build',
 'spells.env.Lib.site-packages.pip._internal.operations.install',
 'spells.env.Lib.site-packages.pip._internal.req',
 'spells.env.Lib.site-packages.pip._internal.resolution',
 'spells.env.Lib.site-packages.pip._internal.resolution.legacy',
 'spells.env.Lib.site-packages.pip._internal.resolution.resolvelib',
 'spells.env.Lib.site-packages.pip._internal.utils',
 'spells.env.Lib.site-packages.pip._internal.vcs',
 'spells.env.Lib.site-packages.pip._vendor',
 'spells.env.Lib.site-packages.pip._vendor.cachecontrol',
 'spells.env.Lib.site-packages.pip._vendor.cachecontrol.caches',
 'spells.env.Lib.site-packages.pip._vendor.certifi',
 'spells.env.Lib.site-packages.pip._vendor.chardet',
 'spells.env.Lib.site-packages.pip._vendor.chardet.cli',
 'spells.env.Lib.site-packages.pip._vendor.colorama',
 'spells.env.Lib.site-packages.pip._vendor.distlib',
 'spells.env.Lib.site-packages.pip._vendor.distlib._backport',
 'spells.env.Lib.site-packages.pip._vendor.html5lib',
 'spells.env.Lib.site-packages.pip._vendor.html5lib._trie',
 'spells.env.Lib.site-packages.pip._vendor.html5lib.filters',
 'spells.env.Lib.site-packages.pip._vendor.html5lib.treeadapters',
 'spells.env.Lib.site-packages.pip._vendor.html5lib.treebuilders',
 'spells.env.Lib.site-packages.pip._vendor.html5lib.treewalkers',
 'spells.env.Lib.site-packages.pip._vendor.idna',
 'spells.env.Lib.site-packages.pip._vendor.msgpack',
 'spells.env.Lib.site-packages.pip._vendor.packaging',
 'spells.env.Lib.site-packages.pip._vendor.pep517',
 'spells.env.Lib.site-packages.pip._vendor.pkg_resources',
 'spells.env.Lib.site-packages.pip._vendor.progress',
 'spells.env.Lib.site-packages.pip._vendor.requests',
 'spells.env.Lib.site-packages.pip._vendor.resolvelib',
 'spells.env.Lib.site-packages.pip._vendor.resolvelib.compat',
 'spells.env.Lib.site-packages.pip._vendor.toml',
 'spells.env.Lib.site-packages.pip._vendor.urllib3',
 'spells.env.Lib.site-packages.pip._vendor.urllib3.contrib',
 'spells.env.Lib.site-packages.pip._vendor.urllib3.contrib._securetransport',
 'spells.env.Lib.site-packages.pip._vendor.urllib3.packages',
 'spells.env.Lib.site-packages.pip._vendor.urllib3.packages.backports',
 'spells.env.Lib.site-packages.pip._vendor.urllib3.packages.ssl_match_hostname',
 'spells.env.Lib.site-packages.pip._vendor.urllib3.util',
 'spells.env.Lib.site-packages.pip._vendor.webencodings',
 'spells.env.Lib.site-packages.pkg_resources',
 'spells.env.Lib.site-packages.pkg_resources._vendor',
 'spells.env.Lib.site-packages.pkg_resources._vendor.packaging',
 'spells.env.Lib.site-packages.pkg_resources.extern',
 'spells.env.Lib.site-packages.setuptools',
 'spells.env.Lib.site-packages.setuptools._distutils',
 'spells.env.Lib.site-packages.setuptools._distutils.command',
 'spells.env.Lib.site-packages.setuptools._vendor',
 'spells.env.Lib.site-packages.setuptools._vendor.packaging',
 'spells.env.Lib.site-packages.setuptools.command',
 'spells.env.Lib.site-packages.setuptools.extern']

package_data = \
{'': ['*'],
 'spells': ['env/*',
            'env/Lib/site-packages/Pillow-8.0.0.dist-info/*',
            'env/Lib/site-packages/aenum-2.2.6.dist-info/*',
            'env/Lib/site-packages/click-8.0.0a1.dist-info/*',
            'env/Lib/site-packages/cutesnowflakes-1.0.1.dist-info/*',
            'env/Lib/site-packages/numpy-1.19.3.dist-info/*',
            'env/Lib/site-packages/numpy/.libs/*',
            'env/Lib/site-packages/numpy/core/include/numpy/*',
            'env/Lib/site-packages/numpy/core/include/numpy/random/*',
            'env/Lib/site-packages/numpy/core/lib/*',
            'env/Lib/site-packages/numpy/core/lib/npy-pkg-config/*',
            'env/Lib/site-packages/numpy/core/tests/data/*',
            'env/Lib/site-packages/numpy/distutils/mingw/*',
            'env/Lib/site-packages/numpy/f2py/src/*',
            'env/Lib/site-packages/numpy/f2py/tests/src/array_from_pyobj/*',
            'env/Lib/site-packages/numpy/f2py/tests/src/assumed_shape/*',
            'env/Lib/site-packages/numpy/f2py/tests/src/common/*',
            'env/Lib/site-packages/numpy/f2py/tests/src/kind/*',
            'env/Lib/site-packages/numpy/f2py/tests/src/mixed/*',
            'env/Lib/site-packages/numpy/f2py/tests/src/parameter/*',
            'env/Lib/site-packages/numpy/f2py/tests/src/regression/*',
            'env/Lib/site-packages/numpy/f2py/tests/src/size/*',
            'env/Lib/site-packages/numpy/f2py/tests/src/string/*',
            'env/Lib/site-packages/numpy/lib/tests/data/*',
            'env/Lib/site-packages/numpy/random/lib/*',
            'env/Lib/site-packages/pip-20.2.3.dist-info/*',
            'env/Lib/site-packages/setuptools-49.2.1.dist-info/*',
            'env/Scripts/*']}

setup_kwargs = {
    'name': 'spells',
    'version': '0.0.1',
    'description': 'Developer-friendly cross-platform build scripts and project automation.',
    'long_description': None,
    'author': 'CodeBizarre',
    'author_email': 'https://github.com/CodeBizarre/',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
