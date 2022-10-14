from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield average
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)


def grouper(results, key):
    while True:
        results[key] = yield from averager()


def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)

    report(results)


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print(f'{result.count:2} {group:5}', f'averaging {result.average:.2f} {unit}')


data = {
    'girls;kg': [40.1, 50.2, 30.1],
    'boys;kg': [55.1, 60.2, 70.1]
}


if __name__ == '__main__':
    main(data)