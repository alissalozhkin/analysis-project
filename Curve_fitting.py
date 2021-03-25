from typing import List, Tuple
import matplotlib.pyplot as plt
import plotting_data_with_pandas as pd_with_pandas
from scipy.optimize import curve_fit


def linear_function(x: float, m: float, b: float) -> float:
    """Return the model linear function that will be used as a parameter in the curve_fit function
    """
    return m * x + b


def quadratic_function(x: float, a: float, b: float, c: float) -> float:
    """Return the model quadratic function that will be used as a parameter in the curve_fit function
    """
    return (a * x) + (b * x ** 2) + c


def cubic_function(x: float, a: float, b: float, c: float, d: float) -> float:
    """Return the model quadratic function that will be used as a parameter in the curve_fit function
    """
    return (a * x) + (b * x ** 2) + (c * x ** 3) + d


def quintic_function(x: float, a: float, b: float, c: float, d: float, e: float, f: float) -> float:
    """Return the model quintic function that will be used as a parameter in the curve_fit function
    """
    return (a * x) + (b * x ** 2) + (c * x ** 3) + (d * x ** 4) + (e * x ** 5) + f


def exponential_function(x: float, a: float, b: float) -> float:
    """Return the model exponential function that will be used as a parameter in the curve_fit function
    """
    return a ** x + b


def linear_curve_fitting_and_plotting(ind_filename: str, dep_filename: str) -> None:
    """Graph a scatter plot and a linear curve of best fit of the independent and dependent
    variables indicated by ind_filename and dep_filename respectively
    Preconditions:
        - ind_filename != ''
        - dep_filename != ''
    """
    independent_name = pd_with_pandas.get_name(ind_filename)  # title for the x-axis
    lists = pd_with_pandas.filenames_to_lists(ind_filename, dep_filename)
    ind_list, dep_list = lists[0], lists[1]

    n = len(ind_list)
    y_values = []
    variables = curve_fit(linear_function, ind_list, dep_list)
    for i in range(n):
        y_value = linear_function(ind_list[i], variables[0][0], variables[0][1])
        y_values.append(y_value)

    variables = (ind_list, dep_list, y_values)

    plotting_data_with_curve(independent_name, variables)


def quadratic_curve_fitting_and_plotting(ind_filename: str, dep_filename: str) -> None:
    """Graph a scatter plot and a quadratic curve of best fit of the independent and dependent
    variables indicated by ind_filename and dep_filename respectively
    Preconditions:
        - ind_filename != ''
        - dep_filename != ''
    """
    independent_name = pd_with_pandas.get_name(ind_filename)  # title for the x-axis
    lists = pd_with_pandas.filenames_to_lists(ind_filename, dep_filename)
    ind_list, dep_list = lists[0], lists[1]

    n = len(ind_list)
    y_values = []
    variables = curve_fit(quadratic_function, ind_list, dep_list)
    for i in range(n):
        y_value = quadratic_function(ind_list[i], variables[0][0], variables[0][1], variables[0][2])
        y_values.append(y_value)

    variables = (ind_list, dep_list, y_values)

    plotting_data_with_curve(independent_name, variables)


def cubic_curve_fitting_and_plotting(ind_filename: str, dep_filename: str) -> None:
    """Graph a scatter plot and a cubic curve of best fit of the independent and dependent
    variables indicated by ind_filename and dep_filename respectively
    Preconditions:
        - ind_filename != ''
        - dep_filename != ''
    """
    independent_name = pd_with_pandas.get_name(ind_filename)  # title for the x-axis
    lists = pd_with_pandas.filenames_to_lists(ind_filename, dep_filename)
    ind_list, dep_list = lists[0], lists[1]

    n = len(ind_list)
    y_values = []
    variables = curve_fit(cubic_function, ind_list, dep_list)
    for i in range(n):
        y_value = cubic_function(ind_list[i], variables[0][0], variables[0][1], variables[0][2],
                                 variables[0][3])
        y_values.append(y_value)

    variables = (ind_list, dep_list, y_values)

    plotting_data_with_curve(independent_name, variables)


def quintic_curve_fitting_and_plotting(ind_filename: str, dep_filename: str) -> None:
    """Graph a scatter plot and a quintic curve of best fit of the independent and dependent
    variables indicated by ind_filename and dep_filename respectively
    Preconditions:
        - ind_filename != ''
        - dep_filename != ''
    """
    independent_name = pd_with_pandas.get_name(ind_filename)  # title for the x-axis
    lists = pd_with_pandas.filenames_to_lists(ind_filename, dep_filename)
    ind_list, dep_list = lists[0], lists[1]

    n = len(ind_list)
    y_values = []
    variables = curve_fit(quintic_function, ind_list, dep_list)
    for i in range(n):
        y_value = quintic_function(ind_list[i], variables[0][0], variables[0][1], variables[0][2],
                                   variables[0][3], variables[0][4], variables[0][5])
        y_values.append(y_value)

    variables = (ind_list, dep_list, y_values)

    plotting_data_with_curve(independent_name, variables)


def exponential_curve_fitting_and_plotting(ind_filename: str, dep_filename: str) -> None:
    """Graph a scatter plot and an exponential curve of best fit of the independent and dependent
    variables indicated by ind_filename and dep_filename respectively
    Preconditions:
        - ind_filename != ''
        - dep_filename != ''
    """
    independent_name = pd_with_pandas.get_name(ind_filename)  # title for the x-axis
    lists = pd_with_pandas.filenames_to_lists(ind_filename, dep_filename)
    ind_list, dep_list = lists[0], lists[1]

    n = len(ind_list)
    y_values = []
    variables = curve_fit(exponential_function, ind_list, dep_list)
    for i in range(n):
        y_value = exponential_function(ind_list[i], variables[0][0], variables[0][1])
        y_values.append(y_value)

    variables = (ind_list, dep_list, y_values)

    plotting_data_with_curve(independent_name, variables)


def plotting_data_with_curve(independent_name: str, variables: Tuple[List, List, List]) -> None:
    """Plot the data in a scatter plot together with the curve of best fit
    Preconditions:
        - independent_name != ''
        - variables != ()
    """
    plt.scatter(variables[0], variables[1])  # line connecting dots with mathplotlib
    plt.plot(variables[0], variables[2], '--', color='red')
    plt.show()
    # creating title and axes titles
    plt.figtext(.5, .9, independent_name + ' Against Global Mean Sea Level Changes from 1993 to 2014',
                fontsize=7.5, ha='center')
    plt.xlabel(independent_name)
    plt.ylabel('Global Mean Sea Level Change (inches)')
