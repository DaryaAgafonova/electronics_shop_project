from src.item import Item
from src.instantiatecsverror import InstantiateCSVError

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    try:
        Item.instantiate_from_csv()
    except FileNotFoundError:
        print("FileNotFoundError: Отсутствует файл item.csv")

    # В файле items.csv удалена последняя колонка.
    try:
        Item.instantiate_from_csv()
    except InstantiateCSVError:
        print("InstantiateCSVError: Файл item.csv поврежден")
    # InstantiateCSVError: Файл item.csv поврежден
