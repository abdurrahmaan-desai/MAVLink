# MAVLink Test Project

## Prerequisites
- pymavlink

## Usage:
- Start master_drone.py
- Run slave_drones.py

Experiment with commented code

## Note:
If the `receive_heartbeat()` method is enabled on master_drone.py, the program will not continue until a heartbeat is received (It is a blocking method).

Currently, the system will only assume 1 drone is connected. See [source-system-filtering](https://github.com/peterbarker/dronekit-python/tree/source-system-filtering/examples/multivehicle) to set up multi-vehicle networks.

## Resources:

[MAVLink Documentation](https://mavlink.io/en/mavgen_python/)

[Source-system-filtering](https://github.com/peterbarker/dronekit-python/tree/source-system-filtering/examples/multivehicle)

[Pymavlink Examples](https://mavlink.io/en/mavgen_python/examples.html)

[Example Custom Application - Medium](https://medium.com/@tonyjacob_/using-mavlink-for-custom-applications-466e1d632f84)
