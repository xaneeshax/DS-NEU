from datetime import datetime


class PriorityQueue:

    def __init__(self):
        # Stores the order
        self.orders = []
        # Assigned rank for each of the priority types
        self.rank = {'L': 0, 'M': 1, 'H': 2}

    def size(self):
        # Get size of the order queue
        return len(self.orders)

    def list_orders(self):
        # Function I used for debugging
        print("Current Order Queue:")
        for order in self.orders:
            print(order)

    def to_list(self):
        # convert the priority queue to a list
        return list(self.orders)

    def __str__(self):
        return f"Orders: {[str(order) for order in list(self.orders)]}"

    @staticmethod
    def date_diff(o1, o2):
        # Find the difference between two dates using the datetime module
        o1_date = datetime.strptime(o1.get_order_date(), "%Y-%m-%d")
        o2_date = datetime.strptime(o2.get_order_date(), "%Y-%m-%d")
        return (o2_date - o1_date).days

    def enqueue(self, o):

        # Raise errors if the value for any of the fields are invalid
        if o.get_priority() not in ["L", "M", "H"]:
            raise ValueError("Invalid Priority Type")
        elif len(o.get_order_date()) != 10:
            raise ValueError("Invalid Order Date")
        elif type(o.get_quantity()) != int:
            raise ValueError("Invalid quantity")
        else:

            # If there are no orders - simply just append to the order queue
            if len(self.orders) == 0:
                self.orders.append(o)
            else:
                # Find the range of indexes that store orders of the same priority
                start = -1
                stop = len(self.orders)

                # Traverse through the current order queue
                for ind, curr_order in enumerate(self.orders):

                    # Maps the values to ranks for comparision purposes
                    # If the rank is higher than that of the new order, then we increment start
                    if self.rank[o.get_priority()] > self.rank[curr_order.get_priority()]:
                        start = ind

                    # When we hit the first value that has a higher priority we break from the loop
                    elif self.rank[o.get_priority()] < self.rank[curr_order.get_priority()]:
                        stop = ind
                        break

                # If start and stop are the same, then there is only one possible index to insert the order
                if start == stop:
                    self.orders.insert(start, o)
                    return
                # If the stop and start are apart by 1 and are of diff priorities the situation is "L" & "H" and
                # "M" needs to be inserted in between
                elif stop - start == 1 and o.get_priority() != self.orders[start].get_priority():
                    self.orders.insert(stop, o)
                    return

                # Now that we have the right priority range - we find the right place to
                # insert by date and quantity
                else:
                    same_dates = []
                    for ind in range(start + 1, stop):

                        # Checks how many days the new order is relative to an order in the queue
                        curr_diff = self.date_diff(o, self.orders[ind])

                        # Append to "Same Dates" if the difference in dates is 0
                        if curr_diff == 0:
                            same_dates.append(ind)

                            # Check for "fencepost case"
                            if ind == stop - 1:
                                for i in same_dates:
                                    # Insert at correct index based on date
                                    if o.get_quantity() < self.orders[i].get_quantity():
                                        self.orders.insert(i, o)
                                        return
                                self.orders.insert(same_dates[-1] + 1, o)
                                return

                        # Check for "fencepost case"
                        elif ind == stop - 1 and curr_diff > 0:
                            self.orders.insert(stop, o)
                            return

                        # Once we reach a date then is sooner than the new order we
                        # insert the order into the queue if there are no other orders
                        # with the same date
                        elif curr_diff < 0:
                            if len(same_dates) == 0:
                                self.orders.insert(ind, o)
                                return
                            # If there are orders with the same date we need to sort by date
                            else:
                                for i in same_dates:
                                    # Inserts the order once it finds an existing order with
                                    # a higher quantity purchased
                                    if o.get_quantity() < self.orders[i].get_quantity():
                                        self.orders.insert(i, o)
                                        return

                                # Fence post case for the dates
                                self.orders.insert(same_dates[-1] + 1, o)
                                return

    def dequeue(self):
        try:
            self.orders.pop(-1)
        except IndexError:
            return None

    def peek(self):
        try:
            return self.orders[-1]
        except IndexError:
            return None

    def is_empty(self):
        return len(self.orders) == 0

    def clear(self):
        self.orders = []