import pandas as pd
import matplotlib.pyplot as plt
import pickle

from analiza import Analiza


def save_temp(obj, file_name='temp.pkl'):
    with open(file_name, 'wb') as file:
        pickle.dump(obj, file)


def load_temp(file_name='temp.pkl'):
    with open(file_name, 'rb') as file:
        obj = pickle.load(file)
    return obj


def char_percentage(word_list=None):
    unique_list = word_list
    if unique_list is None:
        analiza = Analiza()
        unique_list = analiza.unique_list
    data = {}
    for word in unique_list:
        for char in word:
            if char not in data:
                data[char] = 0
            data[char] += 1

    char_sum = sum(data.values())
    for char in data:
        data[char] = [100 * data[char] / char_sum]
    return data


if __name__ == '__main__':
    data_set = load_temp()

    table = pd.DataFrame(data_set)
    table.sort_index(axis=1, inplace=True)
    table.plot(kind='bar', figsize=(30, 20))
    plt.show()

    # table = pd.read_csv('data.csv', dtype=str)
    # print(table.head())
    # data = table.drop(['word', 'length'], axis=1)
    ...
