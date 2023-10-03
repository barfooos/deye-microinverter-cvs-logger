#!python
import locale
from pysolarmanv5 import PySolarmanV5
from datetime import datetime



INVERTER_PORT = 8899 # standardport
INVERTER_HOST = "10.0.0.1"
INVERTER_SERIALNUMBER = 08150815
CSV_FILE = "deye.csv"


def main():
    modbus = PySolarmanV5(
        INVERTER_HOST,
        INVERTER_SERIALNUMBER,
        port=INVERTER_PORT,
        mb_slave_id=1,
        verbose=True,
        auto_reconnect=True)

    total_yield  = (modbus.read_holding_registers(register_addr=63, quantity=1))[0]/10
    ac_power  = (modbus.read_holding_registers(register_addr=86, quantity=1))[0]/10
    ac_current  = (modbus.read_holding_registers(register_addr=76, quantity=1))[0]/10
    ac_voltage  = (modbus.read_holding_registers(register_addr=73, quantity=1))[0]/10
    dc_voltage_1  = (modbus.read_holding_registers(register_addr=109, quantity=1))[0]/10
    dc_voltage_2  = (modbus.read_holding_registers(register_addr=111, quantity=1))[0]/10

    current_date = datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime('%H:%M:%S')

    locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

    with open(CSV_FILE, "a") as myfile:
        myfile.write((f"{current_date};{current_time};{total_yield};{ac_voltage};{dc_voltage_1};{dc_voltage_2};{ac_current};{ac_power}\n").replace(".",","))

if __name__ == "__main__":
   main()
