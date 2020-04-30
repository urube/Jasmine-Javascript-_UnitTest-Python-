import pytest
from box_toy import Box, Toy


class TestEmptyBox:
    # def setup(self):
    #     self.box = Box()

    def test_a_empty_Box_toy_count(self):
        box = Box()
        assert hasattr(box, 'toy_count')
        assert type(box.toy_count) == int

    def test_b_empty_Box_all_my_toys(self):
        box = Box()
        assert hasattr(box, 'all_toys')
        assert type(box.all_toys) == list
        assert len(box.all_toys) == 0

    def test_c_empty_Box_add_toy_exists(self):
        box = Box()
        assert hasattr(box, 'add_toy')
        assert callable(getattr(box, 'add_toy', None))

    def test_d_empty_Box__str__(self):
        box = Box()
        assert hasattr(box, '__str__')
        assert callable(getattr(box, '__str__', None))
        assert str(box) == 'This box has 0 toys\n'


class TestToy:

    @pytest.fixture(scope='session')
    def database(self):
        data = [('Aardvark', 'Brown', 11.11)]
        return data

    # @pytest.mark.parametrize('d0, d1, d2', data())
    def test_a_Toy_name(self, database):
        # toy = Toy(d0, d1, d2)
        for data in database:
            var1 = data[0]
            var2 = data[1]
            var3 = data[2]
            toy = Toy(var1, var2, var3)
            assert hasattr(toy, 'name')
            assert toy.name == 'Aardvark'

    def test_b_Toy_color(self, database):
        for data in database:
            var1 = data[0]
            var2 = data[1]
            var3 = data[2]
            toy = Toy(var1, var2, var3)
            assert hasattr(toy, 'color')
            assert toy.color == 'Brown'

    def test_c_Toy_cost(self, database):
        for data in database:
            var1 = data[0]
            var2 = data[1]
            var3 = data[2]
            toy = Toy(var1, var2, var3)
            assert hasattr(toy, 'cost')
            assert toy.cost == 11.11

    def test_d_Toy__str__(self, database):
        for data in database:
            var1 = data[0]
            var2 = data[1]
            var3 = data[2]
            toy = Toy(var1, var2, var3)
            assert hasattr(toy, '__str__')
            assert callable(getattr(toy, '__str__', None))
            assert str(toy) == 'Aardvark (Brown) @ $11.11'


class TestToyOfToys:

    @pytest.fixture(scope='session')
    def database(self):
        data = [('Duck', 'Wooden', 33.33),
                ('Aardvark', 'Brown', 11.11),
                ('Doll', 'Pink', 22.22)]
        return data

    # @pytest.mark.parametrize('var1, var2, var3', database())
    # def setup_class(self, var1, var2, var3):
    #     # for data in database:
    #     #     var1 = data[0]
    #     #     var2 = data[1]
    #     #     var3 = data[2]
    #     self.box = Box()
    #     self.box.add_toy(var1, var2, var3)

    def test_a_full_Box_toy_count(self, database):
        for data in database:
            var1 = data[0]
            var2 = data[1]
            var3 = data[2]
            box = Box()
            box.add_toy(var1, var2, var3)
            box.add_toy(var1, var2, var3)
            box.add_toy(var1, var2, var3)
            assert box.toy_count == 3

    def test_b_full_Box_all_toys(self, database):
        for data in database:
            var1 = data[0]
            var2 = data[1]
            var3 = data[2]
            box = Box()
            box.add_toy(var1, var2, var3)
            box.add_toy(var1, var2, var3)
            box.add_toy(var1, var2, var3)
            assert box.toy_count == 3
            assert len(box.all_toys) == 3

    def test_c_full_Box___str__(self, database):
        for data in database:
            var1 = data[0]
            var2 = data[1]
            var3 = data[2]
            box = Box()
            box.add_toy(var1, var2, var3)
            assert str(box) == 'This box has 3 toys\n' \
                   + '\tAardvark (Brown) @ $11.11\n' \
                   + '\tDoll (Pink) @ $22.22\n' \
                   + '\tDuck (Wooden) @ $33.33\n'


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'pytest_best_practice.py'])
