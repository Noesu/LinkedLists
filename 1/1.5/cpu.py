class CPU:
    def __init__(self, name: str, fr: int):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name: str, volume: int):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name: str, cpu: CPU, memory: list[Memory], total_mem_slots: int = 4):
        if len(memory) > total_mem_slots:
            raise ValueError("Excess amount of memory chips")
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = total_mem_slots
        self.mem_slots = memory

    def get_config(self) -> list:
        return [f"Материнская плата: {self.name}",
                f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
                f"Слотов памяти: {self.total_mem_slots}",
                f"Память: {'; '.join([f'{i.name} - {i.volume}' for i in self.mem_slots])}"]


mb = MotherBoard("Asus", CPU("AMD", 2400), [Memory("Hynix", 4), Memory("Hynix", 4)])
print(mb.get_config())
