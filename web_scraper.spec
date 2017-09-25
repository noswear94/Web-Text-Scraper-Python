# -*- mode: python -*-

block_cipher = None


a = Analysis(['web_scraper.py'],
             pathex=['C:\\Users\\noswear\\PycharmProjects\\YouTube\\crawler\\Web Scraper'],
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
          name='web_scraper',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='Web_Scraper.ico')
