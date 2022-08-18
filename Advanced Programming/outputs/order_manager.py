import json
from dstruct.order import Order
from dstruct.priority_queue import PriorityQueue


class OrderManager:

    def __init__(self):
        self.order_queue = PriorityQueue()

    def read_json(self, filename):

        f = open(filename)
        order_data = json.load(f)

        # Iterating through the json data
        for id in order_data.keys():
            id_keys = order_data[id].keys()

            # Check if order_date, priority, and quantity are keys
            # if "order_date" in id_keys and "priority" in id_keys and "quantity" in id_keys:
            try:
                order = Order(order_data[id]["order_date"].strip(),
                              order_data[id]["priority"].strip(),
                              order_data[id]["quantity"])

                try:
                    self.order_queue.enqueue(order)
                except Exception as e:
                    # THERE ARE 8 INVALID FIELDS
                    print(type(e).__name__, ': ', str(e), "Order ID:", id, ">>", order_data[id], sep=" ")

            except Exception as e:
                # THERE ARE 5 KEY ERRORS
                print(type(e).__name__, ': ', str(e), "Order ID:", id, ">>", order_data[id], sep=" ")

    def print_info(self):
        # Output order data
        print("Order Data:", self.order_queue)

        # There 87 orders in the order queue
        print("Order Queue Size", self.order_queue.size())


def main():
    om = OrderManager()
    om.read_json("orders.json")
    om.print_info()


if __name__ == '__main__':
    main()