import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

rclpy.init()
node = Node("talker")


def cb(request, response):
    if request.day in ["月","火","水","木","金"]:
       response.business = "営業日"

    else:
       response.business = "休業日"

    return response


def main():
    srv = node.create_service(Query, "query", cb)
    rclpy.spin(node)

