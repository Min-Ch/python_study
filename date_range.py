import time

from datetime import date, timedelta


class Sequence:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date

        while current_day <= self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days

    def __getitem__(self, day_no):
        return self._range[day_no]

    def __len__(self):
        return len(self._range)


class Iter:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day > self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


class ContainerIter:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current = self.start_date
        while current <= self.end_date:
            yield current
            current += timedelta(days=1)

    def __len__(self):
        return (self.end_date - self.start_date).days + 1


def converter(lst):
    return (f"{cls} ({'{:.4f}'.format(time)}/ms)" for cls, time in sorted(lst, key=lambda x: x[1]))


def main(start_date, end_date):
    total_elapse = []
    cls_elapse = []
    iter_elapse = []

    for cls in [Sequence, Iter, ContainerIter]:
        start_time = time.time()
        print(f"========= START {cls.__name__} =========")

        start = date(year=start_date[0], month=start_date[1], day=start_date[2])
        end = date(year=end_date[0], month=end_date[1], day=end_date[2])

        date_range = cls(start_date=start, end_date=end)
        cls_time = time.time() - start_time

        count = 0
        for d in date_range:
            count += 1
            # print(d)

        # for d in date_range:
        #     print(d)

        end_time = time.time() - start_time

        total_elapse.append((cls.__name__, end_time*1000))
        cls_elapse.append((cls.__name__, cls_time*1000 ))
        iter_elapse.append((cls.__name__, (end_time-cls_time)*1000))
        print(f"========== END {cls.__name__} ==========")

    print('총 시간 :', ' < '.join(converter(total_elapse)))
    print('객체 생성 시간 :', ' < '.join(converter(cls_elapse)))
    print('반복문 시간 :', ' < '.join(converter(iter_elapse)))


if __name__ == '__main__':
    main(start_date=[1000, 1, 1], end_date=[9999, 12, 30])
