import plotting_data_with_pandas as pd_with_pandas
from Curve_fitting import linear_function, quadratic_function, cubic_function, exponential_function
from scipy.optimize import curve_fit


def linear_equation_of_best_fit(ind_filename: str, dep_filename: str) -> str:
    """Returns the linear equation of best fit as a string for the dependent and independent
    variables indicated by dep_filename and ind_filename respectively
    Preconditions:
        - independent_name != ''
        - variables != ()
    """
    lists = pd_with_pandas.filenames_to_lists(ind_filename, dep_filename)
    ind_list, dep_list = lists[0], lists[1]

    optimal_values, covariance = curve_fit(linear_function, ind_list, dep_list)

    return 'y = ' + str(optimal_values[0]) + ' * x ' + '+ ' + str(optimal_values[1])


def quadratic_equation_of_best_fit(ind_filename: str, dep_filename: str) -> str:
    """Returns the quadratic equation of best fit as a string for the dependent and independent
    variables indicated by dep_filename and ind_filename respectively
    Preconditions:
        - independent_name != ''
        - variables != ()
    """
    lists = pd_with_pandas.filenames_to_lists(ind_filename, dep_filename)
    ind_list, dep_list = lists[0], lists[1]

    optimal_values, covariance = curve_fit(quadratic_function, ind_list, dep_list)

    return 'y = ' + str(optimal_values[1]) + ' * x ^ 2 ' + '+ ' + str(optimal_values[0]) + ' * x ' + \
           '+ ' + str(optimal_values[2])


def cubic_equation_of_best_fit(ind_filename: str, dep_filename: str) -> str:
    """Returns the cubic equation of best fit as a string for the dependent and independent
    variables indicated by dep_filename and ind_filename respectively
    Preconditions:
        - independent_name != ''
        - variables != ()
    """
    lists = pd_with_pandas.filenames_to_lists(ind_filename, dep_filename)
    ind_list, dep_list = lists[0], lists[1]

    optimal_values, covariance = curve_fit(cubic_function, ind_list, dep_list)

    return 'y = ' + str(optimal_values[2]) + ' * x^3 ' + ' + ' + str(optimal_values[1]) + ' * x ^ 2' + \
           ' + ' + str(optimal_values[0]) + ' * x ' + ' + ' + str(optimal_values[3])


def exponential_equation_of_best_fit(ind_filename: str, dep_filename: str) -> str:
    """Returns the exponential equation of best fit as a string for the dependent and independent
    variables indicated by dep_filename and ind_filename respectively
    Preconditions:
        - independent_name != ''
        - variables != ()
    """
    lists = pd_with_pandas.filenames_to_lists(ind_filename, dep_filename)
    ind_list, dep_list = lists[0], lists[1]

    optimal_values, covariance = curve_fit(exponential_function, ind_list, dep_list)

    return 'y = ' + str(optimal_values[0]) + ' ^ x ' + ' + ' + str(optimal_values[1])
