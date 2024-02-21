from pathlib import Path
import json
import os

gallery_directory = Path(r"C:\Users\mitro\Downloads\Mitya")  # You have to put it manually
data_file = Path(r"C:\Users\mitro\PycharmProjects\tag-o-matic\.data\data.json")  # Same here


class TagsHandler:
    def __init__(self, filename=data_file):
        self.path = filename
        self.dicti = {}

    def __enter__(self) -> dict:
        with open(self.path, 'r', encoding='utf-8') as file:
            if os.stat(self.path).st_size != 0:  # Exceptions are gay
                self.dicti = json.load(file)
                for image in self.dicti:
                    self.dicti[image]['tags'] = set(self.dicti[image]['tags'])
        return self.dicti

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.path, 'w', encoding='utf-8') as file:
            for image in self.dicti:
                self.dicti[image]['tags'] = list(self.dicti[image]['tags'])
            json.dump(self.dicti, file, indent=2, ensure_ascii=False)


def check_if_path_broken() -> None:
    assert os.path.isdir(gallery_directory)
    assert os.path.exists(gallery_directory)
    print('Files:', [filename for filename in os.listdir(gallery_directory)])


def create_dict(filename: str, index: int, picture_name: str, iterable: list | set, boolean: bool) -> dict:
    to_do = {
        filename: {
            "index": index,
            "name": picture_name,
            "tags": iterable,
            "nsfw": boolean,
        }
    }
    return to_do


def main():
    def help_me():
        print('-' * 128)
        print('СПИСОК КОМАНД:')
        print('help - показать данный список команд.')
        print('show - показать все записи и информацию о них.')
        print('open <индекс> - открыть файл в галерее с выбранным индексом.')
        print('edit <индекс> - редактировать запись с выбранным индексом.')
        print('find <*теги> - выводит на экран записи с соответствующими тегами (через пробел).')
        print('exit - закрыть программу.')
        print('-' * 128)
        print()

    with TagsHandler(data_file) as fm:
        index_list = [fm[filename]["index"] for filename in os.listdir(gallery_directory)]
        max_index = max(index_list)
        for i, filename in enumerate(os.listdir(gallery_directory)):
            if filename not in fm:
                fm.update(create_dict(str(filename), max_index + 1, 'NAME', ['TAGS', 'TAGS', 'TAGS'], False))
                max_index += 1

    print('Tag-o-matic, by Mitya "Mitrotsky"')
    help_me()

    while True:
        command = input('>>> ').lower().split()
        match command:
            case "open", index, *_:
                for filename in os.listdir(gallery_directory):
                    if fm[filename]['index'] == int(index):
                        print(f"Открываем {filename}...")
                        os.system(str(gallery_directory / str(filename)))
                        print()

            case "show", *_:
                for filename in os.listdir(gallery_directory):
                    print(f"[{fm[filename]['index']:^4}] {fm[filename]['name']:<30}| "
                          f"{filename:<40}| {fm[filename]['tags']}")
                print()

            case "edit", index, *_:
                with TagsHandler(data_file) as fm:
                    for filename in os.listdir(gallery_directory):
                        if fm[filename]['index'] == int(index):
                            print(f'Приступаем к редактированию {filename}...')
                            picture_name = input("Введите название изображения: ")
                            tags = input("Введите теги изображения (через пробел): ").split()
                            nsfw = True if input("NSFW (True или False): ").lower() == 'true' else False
                            fm.update(create_dict(str(filename), fm[filename]['index'], picture_name, tags, nsfw))
                            print(f'Редактирование {filename} завершено. Успешно сохранено.\n')

            case "find", *tags:
                for filename in os.listdir(gallery_directory):
                    if set(tags).issubset(set([tag.lower() for tag in fm[filename]['tags']])):
                        print(f"[{fm[filename]['index']:^4}] {fm[filename]['name']:<30}| "
                              f"{filename:<40}| {fm[filename]['tags']}")
                print()

            case "help", *_:
                help_me()

            case "exit", *_:
                break

            case _:
                continue


if __name__ == '__main__':
    main()
