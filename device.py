class DeviceResource:
    def __init__(self):
        self.CPU_total = 0.0
        self.CPU_used = 0.0
        self.GPU_total = 0.0
        self.GPU_used = 0.0
        self.Memery_total = 0.0
        self.Memery_used = 0.0
        self.disk_total = 0.0
        self.disk_used = 0.0

class Device:
    def __init__(self):
        self.MAC = "MAC addr"
        self.alias = "alias"
        self.resources = DeviceResource()
        self.information = "info"
    