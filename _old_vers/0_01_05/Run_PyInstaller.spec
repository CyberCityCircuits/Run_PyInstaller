# -*- mode: python -*-

block_cipher = None


a = Analysis(['Run_PyInstaller.py'],
             pathex=['C:\\Users\\DREAM\\Desktop\\David Ray - Python Programming\\Git Repos\\Run_PyInstaller\\_old_vers\\0_01_05'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Run_PyInstaller',
          debug=False,
          strip=False,
          upx=True,
          console=True )
