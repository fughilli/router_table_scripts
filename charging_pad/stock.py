import fractions
import numpy as np

kMmPerInch = 25.4

stock_size_in = np.array((6, 5 + 9/16))

stock_size_mm = stock_size_in * kMmPerInch

half_stock_size_mm = stock_size_mm / 2

work_offset = np.array((11, 5+9/16)) / 2 * kMmPerInch

print("Stock offset X:", half_stock_size_mm[0], "Stock offset Y: ", half_stock_size_mm[1])
print("G0 X{:.4f} Y{:.4f}".format(*half_stock_size_mm))
print("G0 X{:.4f} Y{:.4f}".format(*work_offset))
