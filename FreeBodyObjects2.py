from math import atan2, degrees, radians, sin, cos


# Last problem, you created a new class called Force. Copy that
# class below:


class Force:

    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    def get_horizontal(self):
        horizontal = self.magnitude * cos(radians(self.angle))
        return horizontal

    def get_vertical(self):
        vertical = self.magnitude * sin(radians(self.angle))  # in sin
        return vertical

    def get_angle(self, use_degrees=True):
        if use_degrees == False:
            return radians(self.angle)
        else:
            return self.angle


# In this problem, you're going to use that class to calculate
# the net force from a list of forces.
#
# Write a function called find_net_force. find_net_force should
# have one parameter: a list of instances of Force. The
# function should return new instance of Force with the total
# net magnitude and net angle as the values for its magnitude
# and angle attributes.
#
# As a reminder:
#
# - To find the magnitude of the net force, sum all the
#   horizontal components and sum all the vertical components.
#   The net force is the square root of the sum of the squares
#   of the horizontal forces and the vertical foces (i.e.
#   (total_horizontal ** 2 + total_vertical ** 2) ** 0.5)
# - To find the angle of the net force, call atan2 with two
#   arguments: the total vertical and total horizontal
#   forces (in that order).
# - Remember to round both the magnitude and direction to one
#   decimal place. This can be done using round(magnitude, 1)
#   and round(angle, 1).
# - The Force class has three methods: get_horizontal returns
#   a single force's horizontal component. get_vertical
#   returns a single force's vertical component. get_angle
#   returns a single force's angle in degrees (or in radians
#   if you call get_angle(use_degrees = False).
#
# HINT: Don't overcomplicate this. The Force class does a lot
# of your work for you. Use it! You should not need any trig
# functions except atan2, degrees, and radians.


# Add your function here!


def find_net_force(force_instances):
    total_h = 0  # Initialize variable for h
    total_v = 0  # Initialize variable for v
    for instance in force_instances:
        total_h += float(instance.get_horizontal())
        total_v += float(instance.get_vertical())
    net_force = (total_h ** 2 + total_v ** 2) ** 0.5
    net_force = round(net_force,1)
    net_angle = degrees(atan2(total_v, total_h))
    net_angle = round(net_angle,1)
    total_force = Force(net_force, net_angle) #call class
    return total_force


# Below are some lines of code that will test your object.
# You can change these lines to test your code in different
# ways.
#
# If your code works correctly, this will originally run
# error-free and print:
# 103.1
# -14.0

force_1 = Force(50, 90)
force_2 = Force(75, -90)
force_3 = Force(100, 0)
forces = [force_1, force_2, force_3]
net_force = find_net_force(forces)
print(net_force.magnitude)
print(net_force.get_angle())
