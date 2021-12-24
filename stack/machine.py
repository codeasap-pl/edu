class Stack:
    def __init__(self, maxsize=8):
        self.maxsize = maxsize
        self._stack = []

    def push(self, instr):
        assert len(self._stack) < self.maxsize, "Stack overflow"
        self._stack.append(instr)

    def pop(self):
        return self._stack.pop()

    def __bool__(self):
        return bool(self._stack)


class Interpreter:
    def __init__(self, stack_maxsize=8):
        self.accu = None
        self.stack = Stack(stack_maxsize)
        self.stack_maxsize = stack_maxsize

    def reset(self):
        self.accu = None
        self.stack = Stack(self.stack_maxsize)

    def _execute(self, instr):
        op, *arguments = instr.split()
        op = op.upper()
        arguments = list(map(float, arguments))

        if op in ["RESET", "RST", "CLEAR", "CL"]:
            self.reset()
            return

        if op == "PUSH":
            self.stack.push(arguments[0])
        elif op == "POP":
            return self.stack.pop(arguments[0])
        elif op == "INSPECT":
            return list(self.stack._stack)
        elif op in ["+", "ADD"]:
            self.accu = (0 if self.accu is None else self.accu)
            if not self.stack:
                self.accu += self.accu
            else:
                while self.stack:
                    self.accu += self.stack.pop()
            return self.accu
        elif op in ["-", "SUB"]:
            self.accu = (0 if self.accu is None else self.accu)
            if not self.stack:
                self.accu -= self.accu
            else:
                while self.stack:
                    self.accu -= self.stack.pop()
            return self.accu
        elif op in ["*", "MUL"]:
            self.accu = (1 if self.accu is None else self.accu)
            if not self.stack:
                self.accu *= self.accu
            else:
                while self.stack:
                    self.accu *= self.stack.pop()
            return self.accu
        elif op in ["/", "DIV"]:
            self.accu = (0 if self.accu is None else self.accu)
            if not self.stack:
                self.accu /= self.accu
            else:
                while self.stack:
                    self.accu /= self.stack.pop()
            return self.accu
        else:
            try:
                self.stack.push(float(op))
            except ValueError:
                raise Exception("Unsupported operation: %s" % op)

    def run(self):
        print(self.__class__.__name__)
        print("Ctrl-C to exit.")
        while True:
            try:
                instruction = input("> ")
                if not instruction:
                    continue
                result = self._execute(instruction)
                if result is not None:
                    print(result)
            except KeyboardInterrupt:
                return
            except Exception as e:
                print("ERROR", e)


if __name__ == "__main__":
    interpreter = Interpreter(8)
    interpreter.run()
