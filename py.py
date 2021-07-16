#Списки и переменные.

shop = {
    'молочное': {
        'молоко': 85,
        'кефир': 90
    },
    'мучное': {
        'хлеб': 30,
        'булочка': 25
    },
    'напитки': {
        'кола': 100,
        'квас': 80
    }
}
 
basket = []
book = {}
user_balance=150
product_price=0
#Общие функции
#1 Вывод всех товаров магазина
def print_all(shop = shop):
    for sections, products in shop.items():
        print('Раздел: ' + sections)
        for product, price in products.items():
            print(product + ' - ' + str(price))

#2 Вывод товаров определенного раздела
def print_section(section, shop=shop):
    if section.lower() in shop:
        print('Товары раздела "{}":' .format(section))
        for product, price in shop[section].items():
            print(product + ' - ' + str(price))
    else:
        print('Такого раздела в магазине нет!')

#Функции для администратора
#1 Добавление продукта в магазин
def add_product(user_section, product, price, shop = shop):
    if user_section.lower() in shop:
        shop[user_section].update({product: price})
        print('Продукт "{}" был успешно добавлен в магазин!' .format(product))
        print_all()
    elif user_section.lower() not in shop:
        shop.update({user_section:{}})
        shop[user_section].update({product: price})
        print('Раздел "{}" успешно добавлен в ваш магазин!' .format(user_section))
        print('Так же продукт "{}" был успешно добавлен в магазин!' .format(product))
    else:
        return 'Ошибка!'    

#2 Удаление продукта из магазина
def remove_product(user_section, rem_product, shop = shop):  
    if user_section.lower() in shop:
        shop[user_section].pop(rem_product)
        print('Продукт "{}" был успешно удален из магазина!' .format(rem_product))
        print_all()
    elif user_section.lower() not in shop:
        print('Такого раздела в магазине нет')
    else:
        return 'Ошибка!'

#3 Изменение стоимости товара
def change_price(update_product, new_price, shop = shop):
    for sections, products in shop.items():
        for product, price in products.items():
            if product.lower() == update_product.lower():
                products.update({product: int(new_price)})
                print('Стоимость продукта "{}" была успешно обновлена!' .format(product))
                print_all()

#4 Процентная наценка на  все товары
def percent_margin(percent):
    for sections, products in shop.items():
        print('Раздел: ' + sections)
        for product, price in products.items():
            new_price = price + ((price/100)*percent)
            print(product + ' - ' + str(new_price))

#5 Добавление раздела в магазин
def add_section(new_section):
    if new_section not in shop:
        shop.update({new_section:{}})
        print_all()
    elif new_section in shop:
        print('Такой раздел уже существует!')
    else:
        return 'Ошибка!'

#Функции клиента
#1 Покупка продуктов и добавление в корзину
def buy_product(group, purchased_product, balance, basket = basket, shop=shop):
    basket.append(purchased_product)
    return basket
   
#2 Отзывы о магазине
def book_of_cas(nickname, report, book = book):
    book.update({nickname: report})
    print('Ваш отзыв принят. Спасибо за обратную связь!')
    print(book)

#Программа магазина
while True:

    print('Добро пожаловать в программу магазина!')
    name = input('Здравствуйте! Пожалуйста, представьтесь:\n')
    #Меню админа
    while name.lower() == 'admin' or name.lower() == 'админ':
        
        print('Управление магазином')
        input('Нажмите любую клавишу для продолжения')
        doing_admin = input('Введите 1, чтобы просмотреть список всех товаров.\nВведите 2, чтобы просмотреть товары в определенном разделе.\nВведите 3, чтобы добавить товар.\nВведите 4, чтобы удалить товар.\nВведите 5, чтобы изменить стоимость товара.\nВведите 6, чтобы установить процентную наценку на все.\nВведите 7, чтобы добавить раздел в магазин.\n')

        if doing_admin == '1':
            print('Список всех товаров магазина.')
            print_all()
        elif doing_admin == '2':
            print('Просмотр разделов.')
            print_section(section = input('Введите название раздела:\n'))
        elif doing_admin == '3':
            print('Добавление товаров.') 
            add_product(user_section = input('Введите название раздела:\n'), product = input('Введите название добавляемого товара:\n'), price = input('Введите стоимость товара:\n'))
        elif doing_admin == '4':
            print('Удаление товаров.')
            remove_product(user_section = input('Введите, в каком разделе находится этот продукт:\n'), rem_product = input('Введите название продукта, который нужно удалить:\n'))
        elif doing_admin == '5':
            print('Обновление стоимости товаров.')
            change_price(update_product = input('Введите название продукта, которому следует обновить стоимость:\n'), new_price = input('Введите необходимую стоимость продукта:\n'))
        elif doing_admin == '6':
            print('Процентная наценка')
            percent_margin(percent = int(input('Введите процент наценки:\n')))
        elif doing_admin == '7':
            print('Добавление раздела в магазин.')
            add_section(new_section = input('Введите название добавляемой секции:\n'))
        else:
            print('выход из программы управления магазином.')
            break
    
    #Личный кабинет клиента
    print('Здравствуйте,', name)
    while name.lower() != 'admin' or name.lower() != 'админ':
        print(product_price)
        user_balance-=product_price
        print('Личный кабинет клиента.\nНа вашем счете ', user_balance,' Руб.\nВ вашей корзине находятся:\n')
        print('\n'.join(basket)) 
        input('Нажмите любую клавишу для продолжения')
        doing_client = input('Введите 1, чтобы просмотреть список всех товаров.\nВведите 2, чтобы просмотреть товары в определенном разделе.\nВведите 3, чтобы перейти к покупке товара.\nВведите 4, чтобы оставить отзыв о нашем магазине.\n')

        if doing_client == '1':
            print('Список всех товаров магазина.')
            print_all()
        elif doing_client == '2':
            print('Просмотр разделов.')
            print_section(section = input('Введите название раздела:\n'))
        elif doing_client == '3':
            print_all()
            group = input('Введите название раздела: ')
            if user_balance > min(shop[group].values()):
                purchased_product = input('Введите название товара который хотите купить:\n')
                a = shop[group].pop(purchased_product)
                user_balance -= a
                buy_product(group, purchased_product, user_balance)
        elif doing_client == '4':
            book_of_cas(nickname = input('Введите псевдоним:\n'), report = input('Поле для отзыва:\n'))
        else:
            print('выход из программы магазина.')
            break
            