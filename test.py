import unittest
from main import calculate_volume, Cube, Cylinder, Cone

class TestMyProgram(unittest.TestCase):
    def test_cube_volume(self):
        cube = Cube(10, 10, 10)
        self.assertEquals(cube.volume(), 1000)

    def test_cylinder_volume(self):
        cylinder = Cylinder(10, 5)
        self.assertEquals(cylinder.volume(), 1570.7963267948967)    

    def test_cone_volume(self):
        cone = Cone(10, 5)
        self.assertEquals(cone.volume(), 523.5987755982989)

    def test_cube_with_cone_drill(self):
        cube = Cube(10, 10, 10)
        cone = Cone(10, 5)
        cube.subtract.append(cone)
        self.assertEquals(cube.childrenVolume(), cone.volume())
        self.assertEquals(cube.volume(), 1000 - cone.volume())

if __name__ == '__main__':
    unittest.main()
