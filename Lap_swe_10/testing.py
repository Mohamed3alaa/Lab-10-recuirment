import unittest


class TestToDoListApp(unittest.TestCase):

    def test_add_task(self):
        app.testing = True
        client = app.test_client()
        client.post('/add-task', data={'task': 'cook'})
        response = client.get('/')
        self.assertIn('cook', response.data)

    def test_get_tasks(self):
        app.testing = True
        client = app.test_client()
        client.post('/add-task', data={'task': 'Clean the house'})
        response = client.get('/')
        self.assertIn('Clean the house', response.data)

if __name__ == '__main__':
    unittest.main()
