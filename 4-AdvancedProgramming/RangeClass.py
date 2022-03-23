class Range:

    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = 0

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):

        if self.step > 0:
            if self.start > self.stop:
                raise StopIteration
            self.current += 1
            if self.current == 1:
                return self.start
            elif self.current > 1:
                self.start += self.step
                if self.start < self.stop:
                    return self.start
                else:
                    raise StopIteration
        else:
            if self.start < self.stop:
                raise StopIteration
            else:
                self.current -= 1
                if self.current == -1:
                    return self.start
                elif self.current < -1:
                    self.start += self.step
                    # print(f'start: {self.start}')
                    # print(f'stop: {self.stop}')
                    if self.start > self.stop:
                        return self.start
                    else:
                        raise StopIteration


iter = Range(-2, -5, 1)
print(list(iter))
# for i in iter:
#     print(i)
