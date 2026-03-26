class LUT3DGenerator:
    def __init__(self, size=33):
        self.size = size
        self.lut = []

    def generate(self):
        # Generating a blank 3D LUT
        self.lut = [[[0 for _ in range(3)] for _ in range(self.size)] for _ in range(self.size)]
        step = 1.0 / (self.size - 1)
        for r in range(self.size):
            for g in range(self.size):
                for b in range(self.size):
                    self.lut[r][g][b] = [r * step, g * step, b * step]
        return self.lut

    def save(self, filename):
        with open(filename, 'w') as f:
            for r in range(self.size):
                for g in range(self.size):
                    for b in range(self.size):
                        f.write(f'{self.lut[r][g][b][0]}, {self.lut[r][g][b][1]}, {self.lut[r][g][b][2]}\n')

# Example usage:
# generator = LUT3DGenerator(size=33)
# generator.generate()
# generator.save('output.cube')
