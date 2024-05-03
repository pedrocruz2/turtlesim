import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn, Kill, SetPen
import time

class TurtleArt(Node):
    def __init__(self):
        super().__init__('turtle_art')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.spawn_client = self.create_client(Spawn, '/spawn')
        self.kill_client = self.create_client(Kill, '/kill')
        self.pen_client = self.create_client(SetPen, '/turtle1/set_pen')
        time.sleep(2)  # Espera por conexões de serviço

    def draw_shape(self):
        # Fazendo o spawn de uma nova tartaruga
        spawn_future = self.spawn_client.call_async(Spawn.Request(x=5.5, y=5.5, theta=0.0, name='new_turtle'))
        rclpy.spin_until_future_complete(self, spawn_future)
        new_turtle_name = spawn_future.result().name

        # Configurando a caneta
        set_pen = SetPen.Request(r=255, g=0, b=0, width=2, off=0)
        self.pen_client.call_async(set_pen)

        # Desenho
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        for _ in range(10):
            self.publisher_.publish(msg)
            time.sleep(1)

        # Matando a tartaruga criada
        kill_future = self.kill_client.call_async(Kill.Request(name=new_turtle_name))
        rclpy.spin_until_future_complete(self, kill_future)

def main(args=None):
    rclpy.init(args=args)
    turtle_art = TurtleArt()
    turtle_art.draw_shape()
    turtle_art.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
