# -*- coding:utf8 -*-

class CodeGeneratorBackend():
    """代码生成输出类"""

    def begin(self, tab="\t"):
        self.code = []
        self.tab = tab
        self.level = 0

    def end(self):
        # return string.join(self.code, "")
        return "".join(self.code)

    def write(self, string):
        self.code.append(self.tab * self.level + string)

    def indent(self):
        self.level = self.level + 1

    def dedent(self):
        if self.level == 0:
            raise SyntaxError("internal error in code generator")
        self.level = self.level - 1