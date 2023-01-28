import pandas as pd

from analiza import Analiza


if __name__ == '__main__':
    # analiza = None
    analiza = Analiza()
    if analiza:
        print(f'Words: {analiza.count()}')
        print('')

    data = {}
    for word in analiza.unique_list:
        for char in word:
            if char not in data:
                data[char] = 0
            data[char] += 1

    char_sum = sum(data.values())
    for char in data:
        data[char] = [100 * data[char] / char_sum]

    table = pd.DataFrame(data)
    table.sort_index(axis=1, inplace=True)
    print(table.head())

    # table = pd.read_csv('data.csv', dtype=str)
    # print(table.head())
    # data = table.drop(['word', 'length'], axis=1)
    ...
