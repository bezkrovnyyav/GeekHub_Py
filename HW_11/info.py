'''Сайт для виконання завдання: https://jsonplaceholder.typicode.com
Написати програму, яка буде робити наступне:
1. Робить запрос на https://jsonplaceholder.typicode.com/users і вертає коротку інформацію про користувачів (ID, ім'я, нікнейм)
2. Запропонувати обрати користувача (ввести ID)
3. Розробити наступну менюшку (із вкладеними пунктами):
   1. Повна інформація про користувача
   2. Пости:
      - перелік постів користувача (ID та заголовок)
      - інформація про конкретний пост (ID, заголовок, текст, кількість коментарів + перелік їхніх ID)
   3. ТУДУшка:
      - список невиконаних задач
      - список виконаних задач
   4. Вивести URL рандомної картинки'''

import random
import requests
import json

url = 'https://jsonplaceholder.typicode.com/'

# information about all users
def info_about_users():
    response = requests.get(url + 'users')
    users_info = json.loads(response.text)
    id_users = []
    for users in users_info:
        print(f'ID: {users["id"]}'.ljust(8) + f'name: {users["name"]}'.ljust(32) + f'username: {users["username"]}')
        id_users.append(str(users['id']))

    return id_users

# all information about user
def info_about_user(id):
    url = 'https://jsonplaceholder.typicode.com/' + f'users/{id}/'
    response = requests.get(url)
    user_info = json.loads(response.text)
    print(f'{user_info["name"]}:'.upper())
    print('email:'.ljust(9) + f'{user_info["email"]}')
    print('phone:'.ljust(9) + f'{user_info["phone"]}')
    print(f'website: {user_info["website"]}')
    print(f'address: {user_info["address"]["city"]}, {user_info["address"]["street"]}, {user_info["address"]["suite"]}')

# information about all posts user
def show_posts(id):
    response = requests.get(url + f'users/{id}/posts')
    posts = json.loads(response.text)
    id_posts = []
    for post in posts:
        print(f'id: {post["id"]}'.ljust(8) + f' - title: {post["title"]}')
        id_posts.append(str(post["id"]))

    return id_posts

# information about post
def info_about_post(id_posts):
    print('Select the id of the post you want to view')
    choice = input('Your choice: ')
    if choice not in id_posts:
        print('No such ID!')
        return
    else:
        response = requests.get(url + f'posts/{choice}')
        post = json.loads(response.text)
        print('ID:'.ljust(8) + f'{post["id"]}')
        print('TITLE:'.ljust(8) + f'{post["title"]}')
        print(f'BODY:\n{post["body"]}')
        print('-' * 5)

        return choice

# information about numbers of comments and ID_comments
def comments(id_post):
    respose = requests.get(url + f'posts/{id_post}/comments')
    comments = json.loads(respose.text)
    print('Number of comments: ' + str(len(comments)))
    id_comments = []
    for comment in comments:
        id_comments.append(comment["id"])
    print(f'Comments ID: {id_comments}')

# information about not-completed/completed tasks
def todos(id):
    response = requests.get(url + f'users/{id}/todos')
    tasks = json.loads(response.text)
    print('-' * 40)
    print('Not completed tasks: '.upper())
    for task in tasks:
        if task["completed"] == False:
            print(f'Task: {task["title"]}')
    print('-' * 40)
    print('Completed tasks: '.upper())
    for task in tasks:
        if task["completed"] == True:
            print(f'Task: {task["title"]}')

# return random id_albums current user
def return_albums(id):
    response = requests.get(url + f'users/{id}/albums')
    albums = json.loads(response.text)
    id_albums = []
    for album in albums:
        id_albums.append(album["id"])

    return random.choice(id_albums)

# shows random picture URL in current album
def show_picture_url(id_albums):
    response = requests.get(url + f'albums/{str(id_albums)}/photos')
    photos = json.loads(response.text)
    photos_urls = []
    for photo in photos:
        photos_urls.append(photo["url"])
    print(random.choice(photos_urls))


def menu():
    id_users = info_about_users()
    id = input('Choose ID for take user information: ')
    if id not in id_users:
        print('No such ID')
    else:
        while True:     
            print('''
What do you want to see about user?
1 - see all information of this user
2 - see all posts this user
3 - see list of completed tasks and not completed
4 - see URL random picture
5 - back to list of users
6 - exit the program''')    
            choise = input('Your choice: ')
            if choise == '1':
                print('-' * 50)
                info_about_user(id)
                print('-' * 50)
            elif choise == '2':
                id_posts = show_posts(id)
                id_post = info_about_post(id_posts)
                if id_post:
                    comments(id_post)
                else:
                    continue
            elif choise == '3':
                todos(id)
            elif choise == '4':
                show_picture_url(return_albums(id))           
            elif choise == '5':
                menu()
            elif choise == '6':
                exit()
            else:
                print('You wrong, there is no such option!!!')
                print('-' * 30)

if __name__ == '__main__':
    menu()