from matplotlib import pyplot
from numpy import sin, pi, ceil


def plot_lissajous():

    # TODO should theta be period?
    def point_generator(a, b, x_amplitude, y_amplitude,
                        theta, phase_angle):
        x = x_amplitude * sin(a * theta + phase_angle)
        y = y_amplitude * sin(b * theta)

        return x, y

    X_AMPLITUDE = 100
    Y_AMPLITUDE = 100
    A = 3
    B = 5
    # phase angle in pi radians
    PHASE_ANGLE = 1.04

    period = pi * 2
    number_of_points = ceil(period * 100)
    angle_step = period / number_of_points

    x_point_array = []
    y_point_array = []

    for point in range(int(number_of_points)):
        x, y = \
            point_generator(A, B, X_AMPLITUDE, Y_AMPLITUDE,
                            point * angle_step, PHASE_ANGLE)

        x_point_array.append(x)
        y_point_array.append(y)

    pyplot.plot(x_point_array, y_point_array)
    pyplot.ylabel('Some Numbers')
    pyplot.show()

plot_lissajous()
