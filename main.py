# main.py

from user import User
from privileged_user import PrivilegedUser
from admin import Admin


def save_users_to_file(users, filename):
    with open(filename, 'w') as file:
        for user in users:
            file.write(f"ID={user.user_id}, Name={user.name}, Email={user.email}, Access Level={user.access_level}\n")


def print_file_content(filename):
    with open(filename, 'r') as file:
        content = file.read()
    print(content)


def main():
    # Создание обычного пользователя
    user1 = User(1, "John Doe", "john.doe@example.com")
    print(f"User: ID={user1.user_id}, Name={user1.name}, Email={user1.email}, Access Level={user1.access_level}")

    # Создание еще одного обычного пользователя
    user2 = User(4, "Emily Clark", "emily.clark@example.com")
    print(f"User: ID={user2.user_id}, Name={user2.name}, Email={user2.email}, Access Level={user2.access_level}")

    # Создание привилегированного пользователя
    priv_user = PrivilegedUser(2, "Jane Smith", "jane.smith@example.com")
    print(
        f"Privileged User: ID={priv_user.user_id}, Name={priv_user.name}, Email={priv_user.email}, Access Level={priv_user.access_level}")

    # Проверка методов привилегированного пользователя
    print(f"Метод доступа к данным пользователей: {priv_user.access_user_data()}")
    print(f"Метод доступа к статистике: {priv_user.access_statistics()}")

    # Создание администратора
    admin = Admin(3, "Admin User", "admin@example.com")
    print(f"Admin: ID={admin.user_id}, Name={admin.name}, Email={admin.email}, Access Level={admin.access_level}")

    # Администратор добавляет пользователей
    admin.add_user(user1)
    admin.add_user(priv_user)
    admin.add_user(admin)  # Добавляем администратора в список пользователей
    admin.add_user(user2)  # Добавляем нового обычного пользователя

    # Администратор изменяет уровень доступа пользователя
    admin.set_user_access_level(user1, 'privileged')
    print(
        f"Updated User: ID={user1.user_id}, Name={user1.name}, Email={user1.email}, Access Level={user1.access_level}")

    # Сохранение пользователей в файл users.txt
    save_users_to_file(admin._users, 'users.txt')

    # Вывод содержимого файла users.txt на консоль
    print("Current Users in System:")
    print_file_content('users.txt')

    # Администратор удаляет пользователя
    admin.remove_user(user1)
    print("User removed. Current Users in System:")

    # Сохранение обновленного списка пользователей в файл users.txt
    save_users_to_file(admin._users, 'users.txt')

    # Вывод обновленного содержимого файла users.txt на консоль
    print_file_content('users.txt')


if __name__ == "__main__":
    main()
