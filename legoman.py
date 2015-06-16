#@+leo-ver=5-thin
#@+node:.20150531133858.1: * @file man2.py
#@@language python

import cherrypy

# 這是 MAN 類別的定義
'''
# 在 application 中導入子模組
import programs.cdag30.man as cdag30_man
# 加入 cdag30 模組下的 man.py 且以子模組 man 對應其 MAN() 類別
root.cdag30.man = cdag30_man.MAN()

# 完成設定後, 可以利用
/cdag30/man/assembly
# 呼叫 man.py 中 MAN 類別的 assembly 方法
'''
class MAN(object):
    # 各組利用 index 引導隨後的程式執行
    @cherrypy.expose
    def index(self, *args, **kwargs):
        outstring = '''
    40223149

    '''
        return outstring

#@-leo
