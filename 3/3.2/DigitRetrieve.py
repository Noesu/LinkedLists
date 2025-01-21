class DigitRetrieve:
    def __call__(self, value: str, *args, **kwargs):
        try:
            return int(value)
        except ValueError:
            return None


########################################################################################################################

dg = DigitRetrieve()

d1 = dg("123")   # 123 (целое число)
d2 = dg("45.54")   # None (не целое число)
d3 = dg("-56")   # -56 (целое число)
d4 = dg("12fg")  # None (не целое число)
d5 = dg("abc")   # None (не целое число)

st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
