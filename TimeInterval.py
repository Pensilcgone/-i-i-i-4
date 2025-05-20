class TimeInterval:

    def __init__(self, hours: int, minutes: int, seconds: int):
        if not all(isinstance(x, int) for x in [hours, minutes, seconds]):
            raise TypeError("Час має бути цілим числом.")
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Час не може бути від’ємним.")
        if minutes >= 60 or seconds >= 60:
            raise ValueError("Хвилини і секунди мають бути < 60.")
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return f"{self.__hours}h {self.__minutes}m {self.__seconds}s"

    def to_seconds(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds

    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            return NotImplemented
        total = self.to_seconds() + other.to_seconds()
        return TimeInterval.from_seconds(total)

    def __sub__(self, other):
        if not isinstance(other, TimeInterval):
            return NotImplemented
        total = self.to_seconds() - other.to_seconds()
        if total < 0:
            raise ValueError("Результат не може бути від’ємним.")
        return TimeInterval.from_seconds(total)

    def __eq__(self, other):
        if not isinstance(other, TimeInterval):
            return NotImplemented
        return self.to_seconds() == other.to_seconds()

    @classmethod
    def from_seconds(cls, total_seconds: int):
        if total_seconds < 0:
            raise ValueError("Секунди не можуть бути від’ємними.")
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        return cls(h, m, s)


if __name__ == "__main__":
    try:
        t1 = TimeInterval(1, 30, 45)
        t2 = TimeInterval(0, 45, 30)

        print("t1:", t1)
        print("t2:", t2)
        print("Додавання:", t1 + t2)
        print("Віднімання:", t1 - t2)
        print("t1 == t2:", t1 == t2)
        print("t1 в секундах:", t1.to_seconds())

    except (ValueError, TypeError) as e:
        print("Помилка:", e)