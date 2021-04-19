class ForExample(object):
    def test(self, list):

        for index, num in enumerate(list):
            print("Index", index)
            print("Value", num)


example = ForExample()

example.test([2, 5, 7, 4])
