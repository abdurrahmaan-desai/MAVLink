from pymavlink import mavutil
import time

def receive_heartbeat():
    """
    Method to receive a heartbeat from another drone.

    Note: this is a blocking method. Until a heartbeat is received,
    nothing will happen.

    Args:
        None

    Returns:
        None
    """

    print("Waiting for heartbeat")

    # Wait for a heartbeat from another drone and print out information
    drone_1.wait_heartbeat()
    print("Heartbeat from system (system %u component %u)" % (
            drone_1.target_system, drone_1.target_component))


def receive_messages():
    """
    Method to receive a message from another drone

    Infinite loop with exception printing for demonstration purposes.
    Will sleep for 3 seconds to make incoming messages clear

    Args:
        None

    Returns:
        None
    """
    while True:
        try:
            print(drone_1.recv_match().to_dict())
            time.sleep(3)
        except:
            print('Nothing')


if __name__ == '__main__':
    # Set up listening connection
    drone_1 = mavutil.mavlink_connection('udpin:localhost:14540')

    # receive_heartbeat()
    receive_messages()
