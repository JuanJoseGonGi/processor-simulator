# imports Models
from models import control_unit, alu, record


class Processor:
    def __init__(self):
        self.ALU = alu.ALU()
        self.PC = record.Record()
        self.UC = control_unit.ControlUnit()
        self.MBR = record.Record()
        self.MAR = record.Record()
        self.IR = record.Record()
