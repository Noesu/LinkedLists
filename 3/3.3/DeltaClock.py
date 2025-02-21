class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int) ->None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> int:
        return self.hours * 3600 + self.minutes * 60 + self.seconds

class DeltaClock:
    def __init__(self, clock1: Clock, clock2: Clock) -> None:
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self) -> str:
        diff_h, diff_m = divmod(len(self), 3600)
        diff_m, diff_s = divmod(diff_m, 60)
        return f'{diff_h:>02}: {diff_m:>02}: {diff_s:>02}'

    def __len__(self) -> int:
        return max(0, self.clock1.get_time() - self.clock2.get_time())


########################################################################################################################

# Тесты для класса Clock
clock1 = Clock(2, 0, 0)
clock2 = Clock(1, 15, 2)
clock3 = Clock(0, 0, 0)
clock4 = Clock(1, 0, 0)

# Проверяем создание объектов класса Clock
assert clock1.hours == 2
assert clock1.minutes == 0
assert clock1.seconds == 0

assert clock2.hours == 1
assert clock2.minutes == 15
assert clock2.seconds == 2

# Проверяем метод get_time
assert clock1.get_time() == 7200
assert clock2.get_time() == 4502
assert clock3.get_time() == 0
assert clock4.get_time() == 3600

# Тесты для класса DeltaClock
dt1 = DeltaClock(clock1, clock2)
dt2 = DeltaClock(clock2, clock3)
dt3 = DeltaClock(clock1, clock3)
dt4 = DeltaClock(clock3, clock4)
pass

# Проверяем метод __str__
assert str(dt1) == '00: 44: 58', f"Unexpected string representation: {str(dt1)}"
assert str(dt2) == '01: 15: 02', f"Unexpected string representation: {str(dt2)}"
assert str(dt3) == '02: 00: 00', f"Unexpected string representation: {str(dt3)}"
print(len(dt4))
assert str(dt4) == '00: 00: 00', f"Unexpected string representation: {str(dt4)}"  # разница меньше 0, поэтому 0

# Проверяем метод __len__
assert len(dt1) == 2698, f"Unexpected length: {len(dt1)}"
assert len(dt2) == 4502, f"Unexpected length: {len(dt2)}"
assert len(dt3) == 7200, f"Unexpected length: {len(dt3)}"
assert len(dt4) == 0, f"Unexpected length: {len(dt4)}"  # разница меньше 0, поэтому 0

print("Все тесты пройдены успешно!")