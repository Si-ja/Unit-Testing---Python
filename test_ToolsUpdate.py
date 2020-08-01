import unittest
from Checker.ToolsUpdate import Functions

class TestFunctions(unittest.TestCase):

    def test_binaryEqualSizeAllTrue2D(self):
        self.assertEqual(Functions.binary(a=[1, 2, 3],
                                          b=[1, 2, 3]),
                         [True, True, True])
        self.assertEqual(Functions.binary(a=[-1, 0, 1],
                                          b=[-1, 0, 1]),
                         [True, True, True])
        self.assertEqual(Functions.binary(a=[0, 0, 0, 0, -999, 999],
                                          b=[0, 0, 0, 0, -999, 999]),
                         [True, True, True, True, True, True])
        self.assertEqual(Functions.binary(a=[None, None],
                                          b=[None, None]),
                         [True, True])
        self.assertEqual(Functions.binary(a=[],
                                          b=[]),
                         [True])

    def test_binaryEqualSizeAllTrue2DNumpy(self):
        import numpy as np
        self.assertEqual(Functions.binary(a=np.array((1, 2, 3)),
                                          b=np.array((1, 2, 3))),
                         [True, True, True])
        self.assertEqual(Functions.binary(a=np.array((-1, 0, 1)),
                                          b=np.array((-1, 0, 1))),
                         [True, True, True])
        self.assertEqual(Functions.binary(a=np.array((0, 0, 0, 0, -999, 999)),
                                          b=np.array((0, 0, 0, 0, -999, 999))),
                         [True, True, True, True, True, True])
        self.assertEqual(Functions.binary(a=np.array((None, None)),
                                          b=np.array((None, None))),
                         [True, True])
        self.assertEqual(Functions.binary(a=np.array(()),
                                          b=np.array(())),
                         [True])

    def test_binaryEqualSizeAllFalse2D(self):
        self.assertEqual(Functions.binary(a=[1, 2, 3],
                                          b=[4, 5, 6]),
                         [False, False, False])
        self.assertEqual(Functions.binary(a=[-1, 1],
                                          b=[1, -1]),
                         [False, False])
        self.assertEqual(Functions.binary(a=[None],
                                          b=[0]),
                         [False])
        self.assertEqual(Functions.binary(a=[None],
                                          b=[]),
                         [False])

    def test_binaryEqualSizeAllFalse2DNumpy(self):
        import numpy as np
        self.assertEqual(Functions.binary(a=np.array((1, 2, 3)),
                                          b=np.array((4, 5, 6))),
                         [False, False, False])
        self.assertEqual(Functions.binary(a=np.array((-1, 1)),
                                          b=np.array((1, -1))),
                         [False, False])

    def test_binaryDifferentSize2D(self):
        self.assertEqual(Functions.binary(a=[-1, 0, 1, 2, 3],
                                          b=[-1, 0, 1, 2]),
                         [True, True, True, True, False])
        self.assertEqual(Functions.binary(a=[None, 0, 999, -200],
                                          b=[None, 0]),
                         [True, True, False, False])
        self.assertEqual(Functions.binary(a=[100, 50, None],
                                          b=[800, 999, None, -420, 666]),
                         [False, False, True, False, False])
        self.assertEqual(Functions.binary(a=[],
                                          b=[None]),
                         [False])
        self.assertEqual(Functions.binary(a=[None, 55],
                                          b=[]),
                         [False, False])

    def test_binaryDifferentSize2DNumpy(self):
        import numpy as np
        self.assertEqual(Functions.binary(a=np.array((-1, 0, 1, 2, 3)),
                                          b=np.array((-1, 0, 1, 2))),
                         [True, True, True, True, False])
        self.assertEqual(Functions.binary(a=np.array((None, 0, 999, -200)),
                                          b=np.array((None, 0))),
                         [True, True, False, False])
        self.assertEqual(Functions.binary(a=np.array((100, 50, None)),
                                          b=np.array((800, 999, None, -420, 666))),
                         [False, False, True, False, False])
        self.assertEqual(Functions.binary(a=np.array((None, 55)),
                                          b=np.array(())),
                         [False, False])

    def test_binaryErrors(self):
        self.assertRaises(ValueError, Functions.binary, [1], [[1], [1, 2]])
        self.assertRaises(ValueError, Functions.binary, [[1], [1, 2]], [1])
        self.assertRaises(ValueError, Functions.binary, [[1], [1, 2]], [[1], [1, 2]])
        self.assertRaises(ValueError, Functions.binary, [[[1], [1, 2], [None, 42]]], [[1], [1, 2]])

    def test_binaryErrorsNumpy(self):
        import numpy as np
        self.assertRaises(ValueError, Functions.binary, np.array((1)), np.array([[1, 3], [1, 2]]))
        self.assertRaises(ValueError, Functions.binary, np.array([[1, -1], [1, 2]]), np.array([1]))
        self.assertRaises(ValueError, Functions.binary, np.array([[1, 2], [1, 2]]), np.array([[1, 999], [1, 2]]))
        self.assertRaises(ValueError, Functions.binary, np.array([[[1, None], [1, 2], [None, 42]]]), np.array([[0, 0], [1, 2]]))

if __name__ == "__main__":
    unittest.main()