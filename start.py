from shop import *


def main():
    while True:
        choice = input(
        'Выберите действие: 1-показать список продуктов\n\
        2-показать продукт по id\n\
        3-добавить продукт\n\
        4-обновить продукт\n\
        5-удалить продукт\n\
        exit чтобы выйти\n\
        Ваш выбор: '
        )
        if choice == '1':
            print('Если какая-то фильтрация вам не нужна, нажмите Enter')
            print(*get_data(
                ge_price=input('Отфильтруйте выше определенной price: '),
                le_price=input('Отфильтруйте ниже определенной price: '),
                page=input('Выберите страницу: '),
                date=input('Отфильтруйте по дате (2022-10-4 xx:xx:xx): ')), sep='\n'
            )
        elif choice == '2':
            print(new_id())
        elif choice == '3':
            print(new_product())
        elif choice == '4':
            print(reduct_product())
        elif choice == '5':
            print(delete_product())
        elif choice.lower() == 'exit':
            break
        else:
            print('нет такого варианта!')


if __name__ == '__main__':
    main()
