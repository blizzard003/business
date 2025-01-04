import rclpy
from rclpy.node import Node
from business_msgs.srv import Query

rclpy.init()
node = Node("listener")


def main():
    client = node.create_client(Query, 'query')
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('待機中')

    req = Query.Request()
    req.day in ["月","火","水","木","金"]
    future = client.call_async(req)

    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("{}".format(response.business))

            break

    node.destroy_node()
    rclpy.shutdown()

