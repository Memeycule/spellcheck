class SpacingError(Exception):
    pass
class SpellCheck:
    def __init__(self):
        self.list = None

    def correct(self, string: str):
        if " " in string:
            raise SpacingError("String Contains Spaces. Correction Failed.")
            return
        fix1 = {}
        ee = []
        for word in string:
            ee.append(word)
            for i in self.list:
                a_b = []
                for k in i:
                    a_b.append(k)
                same = list(set(a_b).intersection(ee))
                fix1[i] = len(same)    
        e = max(fix1.items(), key=lambda x: x[1])

        return e[0]
    def set_list(self, lst: list):
        self.list = lst


