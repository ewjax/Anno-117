import numpy


def perturb_list(the_list: []) -> []:
    """
    Take an existing list, and perturb it by
        - taking a segment of list members beginning at a random list position,
        - of random length,
        - and inserting the segment back into the list at a new random position
    :param the_list: the original list
    :return: the perturbed list
    """

    # print("---")
    # print(f"Initial List    : {the_list}")
    # print(f"Length          : {len(the_list)}")

    # pick a random segment to remove from current list, in range [0, my_list_len)
    segment_start = numpy.random.randint(0, len(the_list))
    segment_length = numpy.random.randint(1, len(the_list) - segment_start + 1)

    # get the segment using slice syntax, and then remove it from original list
    segment = the_list[segment_start:segment_start+segment_length]
    del the_list[segment_start:segment_start+segment_length]

    # print("---")
    # print(f"Segment start   : {segment_start}")
    # print(f"Segment length  : {segment_length}")
    # print(f"Segment         : {segment}")
    # print(f"Segment length  : {len(segment)}")
    # print(f"Modified List   : {the_list}")
    # print(f"Length          : {len(the_list)}")

    # ensure new segment start isn't the old one, which would just put the segment back where it came from
    new_segment_start = segment_start
    while new_segment_start == segment_start:
        new_segment_start = numpy.random.randint(0, len(the_list) + 1)

    # insert segment back into list in the new position
    the_list = the_list[:new_segment_start] + segment + the_list[new_segment_start:]

    # print("---")
    # print(f"New Seg start   : {new_segment_start}")
    # print(f"Modified List   : {the_list}")
    # print(f"Length          : {len(the_list)}")

    return the_list


def simulated_annealing_optimizer():
    """
    Simulated Annealing basic algorithm
        - start with initial random solution, and a high initial temperature T
        - determine a neighboring, perturbed solution
        - determine difference in cost, DeltaE
        - if new solution is better, accept it
        - if new solution is worse, accept it based on probability P = exp(-DeltaE/T)
        - cool the temperature according to a schedule, T_new = r*T_old
    :return:
    """


    pass




def main():

    # construct a list for testing
    my_list = []
    for i in range(25):
        my_list.append(10*i)

    perturbed_list = perturb_list(my_list.copy())
    print(f"Initial List   [{len(my_list)}]    : {my_list}")
    print(f"Perturbed List [{len(perturbed_list)}]    : {perturbed_list}")



if __name__ == '__main__':
    main()