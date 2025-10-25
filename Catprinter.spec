# -*- mode: python -*-

block_cipher = None

def get_winrt_path():
    import bleak_winrt
    winrt_path = bleak_winrt.__path__[0]
    return winrt_path

def get_bleak_path():
    import bleak
    bleak_path = bleak.__path__[0]
    return bleak_path

a = Analysis(['print.py'],
         pathex=['C:\\Users\\pedro_gr5e3lw\\Desktop\\GIT\\catprinter_win\\print.py',],
         binaries=None,
         datas=None,
         hiddenimports=['opencv-python', 'pillow', 'numpy', 'httpx'],
         hookspath=None,
         runtime_hooks=None,
         excludes=None,
         win_no_prefer_redirects=None,
         win_private_assemblies=None,
         cipher=block_cipher)

dict_tree_winrt = Tree(get_winrt_path(), prefix='bleak_winrt', excludes=["*.pyc"])
a.datas += dict_tree_winrt
a.binaries = filter(lambda x: 'bleak_winrt' not in x[0], a.binaries)

dict_tree = Tree(get_bleak_path(), prefix='bleak', excludes=["*.pyc"])
a.datas += dict_tree
a.binaries = filter(lambda x: 'bleak' not in x[0], a.binaries)

pyz = PYZ(a.pure, a.zipped_data,
         cipher=block_cipher)
exe = EXE(pyz,
      a.scripts,
      exclude_binaries=True,
      name='Catprinter',
      debug=False,
      strip=None,
      upx=True,
      console=True )
scoll = COLLECT(exe,
           a.binaries,
           a.zipfiles,
           a.datas,
           strip=None,
           upx=True,
           name='Catprinter')