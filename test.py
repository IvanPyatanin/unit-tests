import pytest
from unittest import TestCase
from main import discriminant
from mentors import min_course
from test2 import boy_girl
from task2 import create_


#test1
@pytest.mark.parametrize(
    "a, b, c", [
        (1, 8, 15),
        (1, -13, 12),
        (-4, 28, -49)
    ]
)

def test_discriminant( a, b, c):
    res = discriminant(a, b, c)
    assert res >= 0

#test2
def test_courses():
    x = 2
    res = min_course([2, 3, 4, 5])
    assert res == x

#test3
def test_bg():
    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    res =   boy_girl(boys, girls)
    assert res != 'Кто-то может остаться без пары.'

#task2
class Test_task2(TestCase):

    def setUp(self) -> None:
        with open('token.txt', 'r') as f:
            self.token = f.read()
        print(self.token)


    def test_upload(self):

        name_pack = 'Hello'
        res = create_(name_pack, self.token)
        self.assertGreaterEqual(res, 200)
        self.assertLessEqual(res, 300)

    def test_upload_error(self):

        name_pack = ''
        res = create_(name_pack)
        self.assertGreaterEqual(res, 200)
        self.assertLessEqual(res, 300)