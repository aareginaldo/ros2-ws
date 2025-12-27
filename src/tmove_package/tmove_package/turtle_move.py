import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleCircle(Node):
    def __init__(self):
        super().__init__('turtle_circle_publisher')
        # Create a publisher that publishes to the /turtle1/cmd_vel topic
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        # Set a timer to call the move_turtle function at a regular interval (10 Hz)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.move_turtle)
        self.get_logger().info("Turtle moving in a circle!")

    def move_turtle(self):
        # Create a new Twist message to control the velocity of the turtle
        twist = Twist()
        # Set linear velocity in x direction (forward motion)
        twist.linear.x = 1.0  # Move forward with a velocity of 1.0 m/s
        # Set angular velocity in z direction (rotation)
        twist.angular.z = 1.0  # Rotate counterclockwise with a velocity of 1.0 rad/s

        # Publish the velocity command to the turtle
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    # Create a node object
    turtle_circle_publisher = TurtleCircle()
    # Spin the node so that the timer callback is continuously executed
    rclpy.spin(turtle_circle_publisher)

    # Shutdown when finished
    turtle_circle_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
