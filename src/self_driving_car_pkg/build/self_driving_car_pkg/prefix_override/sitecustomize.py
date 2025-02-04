import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/dervis/similasyon_ws/src/self_driving_car_pkg/install/self_driving_car_pkg'
