import sys
class ro:
    def __init__(self, **kwargs):
        try:
            for k in kwargs:
                sys.argv[k] = self.kwargs[k]
        except:    
            pass
    def __init_subclass__(self):
        try:
            pass
        except:
            pass
class he(ro):
    def __init__(self, **kwargs):
        super(he, self).__init__(**kwargs)

