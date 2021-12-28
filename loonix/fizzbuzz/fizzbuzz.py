# Fizz/Buzz.
Z, D = (int(3.28 * 10 ** 80), {3: 0xa, 5: 0x20})
for i in range(Z):
    _ = "".join([chr(42) * _ + chr(D[_]) for _ in [_ for _ in D if not i % _]])
    _ and print(_) or None
