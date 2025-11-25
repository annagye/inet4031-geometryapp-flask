# sphere.py
import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def surfaceArea(self):
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

# Optional: keep this part at the bottom only for testing the script manually
if __name__ == '__main__':
    radius = float(input("Enter radius: "))
    s = Sphere(radius)
    print("Surface Area:", s.surfaceArea())
    print("Volume:", s.volume())
