class PhysicalMemory:
    _instance = None

    # Initalizes the physical memory with 128MB of RAM
    # 0x0000000 - 0x7FFFFFF
    physical_memory = bytearray(1024*1024*128)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance