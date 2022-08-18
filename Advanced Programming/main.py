import json
import random
import random as rnd

from dstruct.order import Order
from dstruct.evo import Environment
from dstruct.profiler import Profiler


def setup_time(orders):
    """ Determines whether the prior product and current product are of the same product type """
    return sum([1 for i in range(1, len(orders)) if orders[i].get_product() != orders[i-1].get_product()])


def priority_score(orders):
    """ Determines the priority score by finding all LOW items before the last HIGH item """
    last_high_priority = max([ind for ind, o in enumerate(orders) if o.get_priority() == "HIGH"])
    return sum([orders[i].get_quantity() for i in range(last_high_priority) if orders[i].get_priority() == "LOW"])


def delay(orders):
    """ Determines delay based on the previous order ID """
    return sum([orders[i-1].get_quantity() for i in range(1, len(orders)) if orders[i].get_id() < orders[i-1].get_id()])


@Profiler.profile
def swapper(solutions):
    """ Agent: Swap two random values """
    orders = solutions[0]
    i = rnd.randrange(0, len(orders))
    j = rnd.randrange(0, len(orders))
    orders[i], orders[j] = orders[j], orders[i]
    return orders


@Profiler.profile
def push_low_priority(solutions):
    """ Finds a low priority time in the beginning of the list and pushes it further back """
    orders = solutions[0]

    # Find a low priority item and push it further down the list
    for ind, order in enumerate(orders):
        if order.get_priority() == "LOW":
            curr_order = orders.pop(ind)
            orders.insert(rnd.randrange(ind, len(orders)), curr_order)
            break
    return orders


@Profiler.profile
def swap_priorities(solutions):
    """ Swaps an ID with a lower one """
    # Get a random order
    orders = solutions[0]
    i = rnd.randrange(0, len(orders))
    curr_order_priority = orders[i].get_id()

    # Find the first order that has a lower ID and switch
    for j in range(i, len(orders)):
        if orders[j].get_id() < curr_order_priority:
            orders[j], orders[i] = orders[i], orders[j]
        break
    return orders


@Profiler.profile
def same_product_type(solutions):
    """ Places a random order with one of the same type """
    # Get a random order
    orders = solutions[0]
    rand_ind = rnd.randrange(1, len(orders) - 1)
    curr_product = orders[rand_ind].get_product()

    # Place the product next to one of the same type
    if curr_product != orders[rand_ind - 1].get_product() and curr_product != orders[rand_ind + 1].get_product():
        for ind in (rand_ind + 1, len(orders)):
            if orders[ind].get_product() == curr_product:
                curr_order = orders.pop(rand_ind)
                orders.insert(ind, curr_order)
            break
    return orders


def read_json(filename):
    """ Convert JSON file to list of Orders """

    # open and load file
    f = open(filename)
    order_data = json.load(f)

    #  store the orders
    orders = []

    # Iterating through the json data
    for o_id in order_data.keys():
        curr_order = Order(order_data[o_id]["priority"],
                           order_data[o_id]["product"],
                           order_data[o_id]["quantity"],
                           o_id)
        # add order to the list
        orders.append(curr_order)

    return orders


@Profiler.profile
def main():

    orders = read_json("orders.json")
    random.shuffle(orders)

    # Create population
    E = Environment()

    # Register fitness criteria "High-LastIndex", "Delays", "Setups"
    E.add_fitness_criteria("Setups", setup_time)
    E.add_fitness_criteria("High-LastIndex", priority_score)
    E.add_fitness_criteria("Delays", delay)

    # Register agents
    E.add_agent("swapper", swapper, 1)
    E.add_agent("push_low_priority", push_low_priority, 1)
    E.add_agent("swap_priorities", swap_priorities, 1)
    E.add_agent("same_product_type", same_product_type, 1)

    # Add initial solution
    E.add_solution(orders)
    print(E)

    # Run the evolver
    print("Start Evolution")
    E.evolve(2000000, 500, 50000)


if __name__ == '__main__':
    main()
    Profiler.report()
