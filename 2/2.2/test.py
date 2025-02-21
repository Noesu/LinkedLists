from time import monotonic

digits = [99 ** 2 * n for n in range(1, 1000000000000000000000, 1000002345670000)]

a1 = monotonic()
for digit in digits:
    _ = digit * digit
print((monotonic()-a1)*1000)

a1 = monotonic()
for digit in digits:
    _ = digit ** 2
print((monotonic()-a1)*1000)

a1 = monotonic()
for digit in digits:
    _ = pow(digit, 2)
print((monotonic()-a1)*1000)
