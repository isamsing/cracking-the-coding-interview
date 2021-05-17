"""
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps,
or 3 steps at a time. Implement a method to count how many possible ways the child can run up
the stairs.
"""


def getWaysToClimb(steps: int, memo={}) -> int:
    if steps in memo:
        return memo[steps]
    elif steps < 0:
        return 0
    elif steps == 0:
        return 1
    else:
        memo[steps] = getWaysToClimb(steps - 1) + getWaysToClimb(steps - 2) + getWaysToClimb(steps - 3)
        return memo[steps]


if __name__ == '__main__':
    print(getWaysToClimb(100))
