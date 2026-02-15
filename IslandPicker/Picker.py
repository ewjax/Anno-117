import math

import numpy



class SimulatedAnnealingSolver:
    """
    Base class for Simulated Annealing Solver derived classes
    child classes should
        - define the array to be solved
        - specify the score() virtual function for a particular sequence of list members
        - the solver optimizer logic finds high scores, i.e. maximums
    """

    def __init__(self):
        # the list of items to be sorted
        self.the_list = []

    def score(self, candidate_list: []) -> float:
        raise NotImplementedError()
        # rv = candidate_list[0] + 0.8 * candidate_list[1] + 0.6 * candidate_list[2]
        # return rv

    def solve(self) -> []:
        """
        Simulated Annealing basic algorithm
            - start with initial random solution, and a high initial temperature T
            -   outer loop
            -       inner loop
            -           determine a neighboring, perturbed solution
            -           determine difference in "cost", DeltaE
            -           if new solution is better, accept it
            -           if new solution is worse, accept it based on probability P = exp(-DeltaE/T)
            -       cool the temperature according to a schedule, T_new = cooling_rate * T_old
        :return:
        """
        outerloop_limit = 100
        innerloop_limit = 1000
        temperature = 100.0
        cooling_rate = 0.95
        current_score = self.score(self.the_list)

        for outer in range(outerloop_limit):

            # print(f"Outer loop: [{outer}] Temperature: [{temperature}]------------------------------------")
            for inner in range(innerloop_limit):
                perturbed_list = self.perturb_list(self.the_list.copy())
                perturbed_score = self.score(perturbed_list)

                accept = False
                # if perturbed_score is better, accept the change
                if perturbed_score > current_score:
                    accept = True

                # if perturbed_score is worse, maybe accept the change
                elif perturbed_score < current_score:
                    # this will be a negative delta
                    delta_score = perturbed_score - current_score
                    prob_acceptance = math.exp(delta_score / temperature)
                    # print(f"prob: [{prob_acceptance}]")
                    if numpy.random.rand() < prob_acceptance:
                        accept = True

                # if perturbed_score is unchanged, do not accept the change

                if accept:
                    self.the_list = perturbed_list
                    current_score = perturbed_score
                    # print(f"New score: [{current_score}]")

            # cool off the annealing
            temperature *= cooling_rate

        return self.the_list

    def perturb_list(self, the_list: []) -> []:
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
        new_segment_start = numpy.random.randint(0, len(the_list) + 1)

        # insert segment back into list in the new position
        the_list = the_list[:new_segment_start] + segment + the_list[new_segment_start:]

        # print("---")
        # print(f"New Seg start   : {new_segment_start}")
        # print(f"Modified List   : {the_list}")
        # print(f"Length          : {len(the_list)}")

        return the_list

class SimpleArray_SimulatedAnnealingSolver(SimulatedAnnealingSolver):
    def __init__(self):
        # call parent ctor
        super().__init__()

        # set up a basic array of numbers
        for i in range(25):
            self.the_list.append(10 * i)

    # define the virtual score() function
    # this one simply defines the score as a weighted sum of the first 3 list values
    def score(self, candidate_list: []) -> float:
        rv = candidate_list[0] + 0.8 * candidate_list[1] + 0.6 * candidate_list[2]
        return rv



def main():

    simple_solver = SimpleArray_SimulatedAnnealingSolver()
    my_list = simple_solver.the_list
    print(f"Initial List   [{len(my_list)}]    : {my_list}")

    my_list = simple_solver.solve()
    print(f"Final List     [{len(my_list)}]    : {my_list}")


if __name__ == '__main__':
    main()