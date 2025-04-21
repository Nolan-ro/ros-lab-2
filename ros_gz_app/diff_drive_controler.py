#Author: Nolan Robbins
#Date: April 21th 2025
#Description:

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from geometry_msgs.msg import Twist

from sensor_msgs.msg import LaserScan


class FallowWall(Node):
    
    def __init__(self):
        super().__init__('fallow_wall')
        self.publisher_ = self.create_publisher(Twist, 'diff_drive/cmd_vel', 10)
        self.subscription = self.create_subscription( #sub
            LaserScan,
            'diff_drvie/scan',
            self.listener_callback,
            10)
        
        self.subscription #sub

    

    def listener_callback(self, msg):
        # self.get_logger().info('Turtle Position: x=%.2f, y=%.2f, angle = %2f' % (position.x, position.y,position.theta))
        msg = LaserScan
        msg.linear.x = 1.0
        msg.angular.z = 0
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: linear.x={msg.linear.x}, angular.z={msg.angular.z}')



def main(args=None):
    rclpy.init(args=args)

    
    wall_follower = FallowWall()

    rclpy.spin(wall_follower)
      
    wall_follower.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
