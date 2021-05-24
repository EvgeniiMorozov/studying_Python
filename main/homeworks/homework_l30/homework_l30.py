"""
Известно, что по этому адресу можно получить сериализированные данные:

https://drive.google.com/file/d/1eaHq6eQTafI3TwxO5fWjbFT2ejSh6_L4/view?usp=sharing

Эти данные представляют собой список со словарями. Каждый словарь имеет вид:

{
    "id": id,
    "login": логин,
    "password": пароль,
    "token": токен
}

Десериализовать полученный pickle и прикрепить в комментарии личного кабинета
пароль пользователя с логином "it_shag".
"""
import pickle
import xml.etree.cElementTree as ET


def unpack_pickle(filename: str) -> list[dict]:
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data


def build_xml_schema(data: list[dict], filename: str):
    users = ET.Element('Users')

    for chunk in data:
        user = ET.SubElement(users, 'User')

        user_id = ET.SubElement(user, 'id')
        user_id.text = chunk['id']

        user_login = ET.SubElement(user, 'login')
        user_login.text = chunk['login']

        user_password = ET.SubElement(user, 'password')
        user_password.text = chunk['password']

        user_token = ET.SubElement(user, 'token')
        user_token.text = chunk['token']

    # ET.dump(users)
    tree = ET.ElementTree(users)
    tree.write(filename)


def main():
    pickle_file = 'data.pkl'
    xml_file = 'data.xml'
    # build_xml_schema(unpack_pickle(pickle_file), xml_file)
    for chunk in unpack_pickle(pickle_file):
        if chunk['login'] == 'it_shag':
            print(chunk['password'])


if __name__ == '__main__':
    main()
