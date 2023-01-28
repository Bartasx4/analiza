import pathlib
import pickle
import csv


class Analiza:
    ALPHABET = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyżźz'
    REPLACE = {'é': 'e', 'š': 'ą'}

    def __init__(self, book_path=None):
        self.book_path = 'C:\\Users\\Bartek\\Documents\\books_pl' if book_path is None else book_path
        self.unique_list = self._clean_words(self._load_words())

    def char_position(self):
        ...

    def _clean_words(self, word_list: set) -> set:
        delete_char = ',.!?:;—-–()*…«»/„”\'\" \n\r'
        new_list = set()
        for word in word_list:
            add = True
            new_word = word.lower().strip(delete_char)
            for key, value in self.REPLACE.items():
                new_word = new_word.replace(key, value)
            if len(new_word) == 0 or new_word.isdigit() or not new_word.isalpha():
                add = False
                continue
            for char in new_word:
                if char not in self.ALPHABET:
                    add = False
                    continue
            if add:
                new_list.add(new_word)
        return new_list

    def _delete(self, word_list: set):
        new_list = set()
        for word in self.unique_list:
            if len(word) >= 3:
                if word[0] == word[1] and word[0] == word[2]:
                    continue
                new_list.add(word)
        return new_list

    def _load_files(self):
        unique_list = set()
        path = pathlib.Path(self.book_path)
        book_list = list(path.glob('*.txt'))
        for index, book in enumerate(book_list):
            print(f'\rBook: {index}/{len(book_list)}', end='')
            with open(book.absolute(), 'r', encoding='utf8') as file:
                for line in file:
                    clean_list = self._clean_words(set(line.split()))
                    unique_list.update(clean_list)
        print('')
        return unique_list

    def _save_words(self):
        with open('words.pkl', 'wb') as file:
            pickle.dump(self.unique_list, file)

    def count(self):
        return self.__len__()

    def _load_words(self):
        with open('words.pkl', 'rb') as file:
            unique_list = pickle.load(file)
            self.unique_list = unique_list
        return unique_list

    @property
    def max(self):
        length = 0
        word = ''
        for element in self.unique_list:
            if len(element) > length:
                length = len(element)
                word = element
        return length, word

    def to_csv(self, file_name='data.csv'):
        header = ['word', 'length'] + [str(i + 1) for i in range(self.max[0])]

        with open(file_name, 'w', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for i, word in enumerate(self.unique_list):
                print(f'\rWord: {i + 1}/{len(self.unique_list)}', end='')
                line = [word, len(word)]
                for char in word:
                    line.append(char)
                try:
                    writer.writerow(line)
                except UnicodeEncodeError as e:
                    print(word.center(11, '#'))

    def __len__(self):
        return len(self.unique_list)
