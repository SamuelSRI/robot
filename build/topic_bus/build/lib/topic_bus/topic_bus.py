#!/usr/bin/env python 3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class TopicBridge(Node):

    def __init__(self):
        super().__init__('topic_bridge')
        self.subscription = self.create_subscription(
            Odometry,
            '/odom_rf2o',  # Remplacez 'topic_source' par le nom de votre premier topic de type Odometry
            self.source_callback,
            10)
        self.publisher = self.create_publisher(
            Odometry,
            '/odom',  # Remplacez 'topic_destination' par le nom de votre deuxième topic de type Odometry
            10)

    def source_callback(self, msg):
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    topic_bridge = TopicBridge()
    rclpy.spin(topic_bridge)
    topic_bridge.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()