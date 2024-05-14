from pymavlink import mavutil


def send_heartbeat(drone):
    """
    Method to send a heartbeat to the master drone

    Args:
        drone: the drone to enact the action on

    Returns:
        None
    """
    drone.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
                             mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)


def send_message(drone: mavutil.mavserial, message: str):
    """
    Method to send a message to the master drone

    Args:
        drone: the drone to enact the action on
        message: the message to sense

    Returns:
        None
    """
    drone.mav.statustext_send(mavutil.mavlink.MAV_SEVERITY_NOTICE,
                              message.encode())


if __name__ == '__main__':
    drone_2 = mavutil.mavlink_connection('udpout:localhost:14540')
    drone_3 = mavutil.mavlink_connection('udpout:localhost:14540')

    # send_heartbeat(drone_2)
    # send_heartbeat(drone_3)

    send_message(drone_2, "This is a message from drone 2")
    send_message(drone_3, "This is a message from drone 3")