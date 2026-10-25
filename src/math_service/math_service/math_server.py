import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class MathServer(Node):

    def __init__(self):
        super().__init__('math_server')

        self.service = self.create_service(
            AddTwoInts,
            'add_two_ints',
            self.add_two_ints_callback
        )

        self.get_logger().info('Math server is ready!')

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b

        self.get_logger().info(
            f'Received: {request.a} + {request.b} = {response.sum}'
        )

        return response


def main(args=None):
    rclpy.init(args=args)

    node = MathServer()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
