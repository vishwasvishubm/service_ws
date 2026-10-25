# ROS 2 Service: Add Two Ints

A ROS 2 service server and client using `example_interfaces/srv/AddTwoInts`. The client sends two integers from the command line and prints the sum returned by the server.

## Packages

- `math_service` (ament_python): `math_server`, `math_client`

## Requirements

- Ubuntu 24.04, ROS 2 Jazzy

## Build

```bash
cd service_ws
source /opt/ros/jazzy/setup.bash
colcon build
source install/setup.bash
```

## Run

Source `install/setup.bash` in every new terminal first.

```bash
# Terminal 1
ros2 run math_service math_server

# Terminal 2
ros2 run math_service math_client 3 5
```

## Concepts practised

services, request/response, async client calls, `wait_for_service`
