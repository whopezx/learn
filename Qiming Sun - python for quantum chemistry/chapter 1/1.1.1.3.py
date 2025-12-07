import sys
import importlib
from pipreqs import pipreqs


imports = pipreqs.get_all_imports('./')
for name in imports:
    mod = importlib.import_module(name)
    print(mod)
# 下面是7-9行代码输出的结果，可以看出截至至当前，'./'路径下依赖三个库，分别为pipreqs，pyscf和numpy
# importlib等模块应该都是内置模块，安装python的时候就安装了，所以这里没有统计
'''
<module 'pipreqs' from '/home/whope/miniconda3/envs/pfqc/lib/python3.10/site-packages/pipreqs/__init__.py'>
<module 'pyscf' from '/home/whope/miniconda3/envs/pfqc/lib/python3.10/site-packages/pyscf/__init__.py'>
<module 'numpy' from '/home/whope/miniconda3/envs/pfqc/lib/python3.10/site-packages/numpy/__init__.py'>
'''
# 在网上搜了以下pipreqs这个模块，发现一般使用这个模块来生成requirement文件，在当前环境下输入`pipreqs 。/`即可


# 使用sys，查看site-packages的路径，发现这个路径中没有'.cpython-...'之类的文件，应该是目前安装的模块中没有依赖C或者C++的
# print(sys.path)
# 以下是当前环境pfqc中，site-packages中的文件
'''
IPython                             idna                                          packaging-25.0.dist-info               rpds_py-0.30.0.dist-info
README.txt                          idna-3.11.dist-info                           pandocfilters-1.5.1.dist-info          scipy
__pycache__                         ipython-8.12.3.dist-info                      pandocfilters.py                       scipy-1.15.3.dist-info
_distutils_hack                     jedi                                          parso                                  scipy.libs
asttokens                           jedi-0.19.2.dist-info                         parso-0.8.5.dist-info                  setuptools
asttokens-3.0.1.dist-info           jinja2                                        pexpect                                setuptools-80.9.0-py3.10.egg-info
attr                                jinja2-3.1.6.dist-info                        pexpect-4.9.0.dist-info                six-1.17.0.dist-info
attrs                               jsonschema                                    pickleshare-0.7.5.dist-info            six.py
attrs-25.4.0.dist-info              jsonschema-4.25.1.dist-info                   pickleshare.py                         soupsieve
backcall                            jsonschema_specifications                     pip                                    soupsieve-2.8.dist-info
backcall-0.2.0.dist-info            jsonschema_specifications-2025.9.1.dist-info  pip-25.3.dist-info                     stack_data
beautifulsoup4-4.14.3.dist-info     jupyter.py                                    pipreqs                                stack_data-0.6.3.dist-info
bleach                              jupyter_client                                pipreqs-0.5.0.dist-info                tests
bleach-6.3.0.dist-info              jupyter_client-8.6.3.dist-info                pkg_resources                          tinycss2
bs4                                 jupyter_core                                  platformdirs                           tinycss2-1.4.0.dist-info
certifi                             jupyter_core-5.9.1.dist-info                  platformdirs-4.5.1.dist-info           tornado
certifi-2025.11.12.dist-info        jupyterlab_pygments                           prompt_toolkit                         tornado-6.5.2.dist-info
charset_normalizer                  jupyterlab_pygments-0.3.0.dist-info           prompt_toolkit-3.0.52.dist-info        traitlets
charset_normalizer-3.4.4.dist-info  markupsafe                                    ptyprocess                             traitlets-5.14.3.dist-info
dateutil                            markupsafe-3.0.3.dist-info                    ptyprocess-0.7.0.dist-info             typing_extensions-4.15.0.dist-info
decorator-5.2.1.dist-info           matplotlib_inline                             pure_eval                              typing_extensions.py
decorator.py                        matplotlib_inline-0.2.1.dist-info             pure_eval-0.2.3.dist-info              urllib3
defusedxml                          mistune                                       pygments                               urllib3-2.6.0.dist-info
defusedxml-0.7.1.dist-info          mistune-3.1.4.dist-info                       pygments-2.19.2.dist-info              wcwidth
distutils-precedence.pth            nbclient                                      pyscf                                  wcwidth-0.2.14.dist-info
docopt-0.6.2.dist-info              nbclient-0.10.2.dist-info                     pyscf-2.11.0.dist-info                 webencodings
docopt.py                           nbconvert                                     python_dateutil-2.9.0.post0.dist-info  webencodings-0.5.1.dist-info
executing                           nbconvert-7.16.6.dist-info                    pyzmq-27.1.0.dist-info                 wheel
executing-2.2.1.dist-info           nbformat                                      pyzmq.libs                             wheel-0.45.1.dist-info
fastjsonschema                      nbformat-5.10.4.dist-info                     referencing                            yarg
fastjsonschema-2.21.2.dist-info     numpy                                         referencing-0.37.0.dist-info           yarg-0.1.9.dist-info
h5py                                numpy-2.2.6.dist-info                         requests                               zmq
h5py-3.15.1.dist-info               numpy.libs                                    requests-2.32.5.dist-info
h5py.libs                           packaging                                     rpds
'''
