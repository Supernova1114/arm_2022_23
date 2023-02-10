# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Ros2 imports
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

# General imports
import arm_controller


class MinimalSubscriber(Node):

    def __init__(self):

        # Give the node a name.
        super().__init__('minimal_subscriber')

        # Subscribe to the topic 'topic'. Callback gets called when a message is received.
        self.subscription = self.create_subscription(
            Float32MultiArray,
            '/Arm_Controls_Sim',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning


    # This callback definition simply prints an info message to the console, along with the data it received. 
    def listener_callback(self, msg):
        # print(msg.data[0], " ", msg.data[1], " ", msg.data[2])
        arm_controller.set_arm_position(msg.data[0], msg.data[1], msg.data[2])
        


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
