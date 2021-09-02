"""Module containing functions for statistical analysis."""

from typing import List, Tuple, Any
from math import ceil, sqrt
from pandas import DataFrame
from sklearn.linear_model import LinearRegression


class EmptyDatasetError(Exception):
    """Exception raised when calling statistical function on an empty data set."""

    def __str__(self) -> str:
        """Return a string representation of this error."""
        return 'function cannot be called on an empty dataset'


def median(values: List[float]) -> float:
    """Returns the mean of the data
    Preconditions:
        - len(values) != 0
    >>> median([5.0, 7.0, 9.0, 11.0, 9.0])
    9.0
    >>> median([2.0, 2.0, 7.0, 4.0, 5.0, 1.0])
    3.0
    """
    global position
    length = len(values)
    sorted_list = sorted(values)
    if length % 2 == 1:
        position = ceil(length / 2)
        return sorted_list[int(position) - 1]
    elif length % 2 == 0 and length != 0:
        position = length / 2
        right_median = sorted_list[int(position)]
        left_median = sorted_list[int(position) - 1]
        return (right_median + left_median) / 2
    elif length == 0:
        raise EmptyDatasetError


def mode(values: List[float]) -> float:
    """Returns the mode of the data
     Preconditions:
        - len(values) != 0
    >>> mode([2.0, 3.0, 6.0, 3.0, 7.0, 5.0, 1.0, 2.0, 3.0, 9.0])
    3.0
    >>> mode([13.0, 17.0, 20.0, 21.0, 23.0, 23.0, 26.0, 29.0, 30.0])
    23.0
    """

    empty_list = []
    for num in values:
        temp_list = [number for number in values if number == num]
        list.append(empty_list, temp_list)

    length = [len(numb) for numb in empty_list]
    maximum = max(length)
    index = length.index(maximum)
    if len(values) != 0:
        return empty_list[index][0]
    else:
        raise EmptyDatasetError


def mean(values: List[float]) -> float:
    """Returns the mean of the data
     Preconditions:
        - len(values) != 0
    >>> mean([3.0, 4.0, 6.0, 6.0, 8.0, 9.0, 11.0])
    6.714285714285714
    """
    if len(values) != 0:
        return sum(values) / len(values)
    else:
        raise EmptyDatasetError


def sample_standard_deviation(values: List[float]) -> float:
    """returns the measure of variability in the data
     Preconditions:
        - len(values) != 0"""
    average = mean(values)
    numerator1 = [num - average for num in values]
    numerator2 = [number ** 2 for number in numerator1]
    numerator3 = sum(numerator2)
    denominator = len(values) - 1
    final_value = sqrt(numerator3 / denominator)
    if len(values) != 0:
        return final_value
    else:
        raise EmptyDatasetError


def correlation(x_values: List[float], y_values: List[float]) -> float:
    """Returns the correlation between variables x and y
    correlation: the measure of strength and direction between two quantitative variables
    Preconditions:
        - len(x_values) == len(y_values)
        - len(x_values) != 0
        - len(y_values) != 0
    """
    average_of_x = mean(x_values)
    average_of_y = mean(y_values)
    standard_deviation_x = sample_standard_deviation(x_values)
    standard_deviation_y = sample_standard_deviation(y_values)
    x_difference = [num - average_of_x for num in x_values]
    y_difference = [num - average_of_y for num in y_values]
    empty_list = []
    for i in range(0, len(x_difference)):
        product = x_difference[i] * y_difference[i]
        list.append(empty_list, product)

    summation = sum(empty_list)
    result = summation / (standard_deviation_x * standard_deviation_y)
    return result / (len(x_difference) - 1)


def slope_of_best_fit(x_values: List[float], y_values: List[float]) -> float:
    """Return the slope of the line of best fit
    Preconditions:
        - len(x_values) == len(y_values)
        - len(x_values) != 0
        - len(y_values) != 0"""
    deviation_of_x = sample_standard_deviation(x_values)
    deviation_of_y = sample_standard_deviation(y_values)
    r = correlation(x_values, y_values)
    m = r * (deviation_of_y / deviation_of_x)
    return m


def y_intercept_of_best_fit(x_values: List[float], y_values: List[float]) -> float:
    """returns the y-intercept of line of best fit
    Preconditions:
        - len(x_values) == len(y_values)
        - len(x_values) != 0
        - len(y_values) != 0
    """
    m = slope_of_best_fit(x_values, y_values)
    average_of_x = mean(x_values)
    average_of_y = mean(y_values)
    b = average_of_y - (m * average_of_x)
    return b


def best_fit_regression_equation(x_values: List[float], y_values: List[float]) -> str:
    """Return equation of line of best fit
    Preconditions:
        - len(x_values) == len(y_values)
        - len(x_values) != 0
        - len(y_values) != 0
    """
    slope = slope_of_best_fit(x_values, y_values)
    y_intercept = y_intercept_of_best_fit(x_values, y_values)
    return 'y = ' + str(slope) + 'x + ' + str(y_intercept)


def interpolation(x_value: float, x_values: List[float], y_values: List[float]) -> float:
    """Return value of y using line of best fit
    Preconditions:
        - x_value in range(round(int(sorted(x_values)[0])), round(int(sorted(x_values)[-1])))
        - len(x_values) == len(y_values)
        - len(x_values) != 0
        - len(y_values) != 0
    >>> x = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    >>> y = [5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0 , 19.0, 21.0, 23.0, 25.0]
    >>> interpolation(1.5, x, y)
    8.0
    """
    m = slope_of_best_fit(x_values, y_values)
    b = y_intercept_of_best_fit(x_values, y_values)
    y_value = m * x_value + b
    return y_value


def extrapolation(start_point: int, end_point: int, x_values: List[float], y_values: List[float]) -> List[float]:
    """Predict the value of the dependent variable for the independent variable that is outside
    the range of our data
    Preconditions:
        - x_value not in range(round(int(sorted(x_values)[0])), round(int(sorted(x_values)[-1])))
        - start_point < end_point
        - len(x_values) == len(y_values)
        - len(x_values) != 0
        - len(y_values) != 0
    >>> x_list = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    >>> y_list = [5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0 , 19.0, 21.0, 23.0, 25.0]
    >>> extrapolation(15, 20, x_list, y_list)
    [35.0, 37.0, 39.0, 41.0, 43.0, 45.0]
    """
    m = slope_of_best_fit(x_values, y_values)
    b = y_intercept_of_best_fit(x_values, y_values)
    empty_list = []
    for x in range(start_point, end_point + 1):
        y_value = m * x + b
        list.append(empty_list, y_value)
    return empty_list


def r_squared(x_values: List[float], y_values: List[float]) -> float:
    """Calculates the coefficient of determination
    Preconditions:
        - len(x_values) == len(y_values)
        - len(x_values) != 0
        - len(y_values) != 0
    """
    r_r = correlation(x_values, y_values)
    r_r_2 = r_r ** 2
    return r_r_2


def variance(values: List[float]) -> float:
    """Calculate the variance of the data. A way to measure the spread of a distribution of
    numerical data
    Preconditions:
        - len(values) != 0
    """
    s = sample_standard_deviation(values)
    return s ** 2


def root_mean_squared_error(start_point: int, end_point: int, x_values: List[float],
                            y_values: List[float]) -> float:
    """Calculates the RMSE. Measures the prediction error for predictions from a linear
     regression model
     Precondition:
        - start_point < end_point
        - len(x_values) == len(y_values)
        - len(x_values) != 0
        - len(y_values) != 0
     """
    predicted_values = extrapolation(start_point, end_point, x_values, y_values)
    empty_list = []
    for value in predicted_values:
        for y in y_values:
            difference = (y - value) ** 2
            list.append(empty_list, difference)

    summation = sum(empty_list)
    denominator = len(x_values) - 1
    root = sqrt(summation / denominator)
    return root


def multiple_lin_reg(df1: DataFrame, df2: DataFrame, df3: DataFrame) -> Tuple[Any, Any, Any]:
    """ Perform multiple linear regression on the given data
    and return coefficients, intercept, and summary of results.
    """
    data = df1.merge(df2).merge(df3)

    # separating features and target
    y = data[df1.columns[1]]
    x = data[[df1.columns[0], df2.columns[0], df3.columns[0]]]

    # defining the multiple linear regression model
    lin_reg = LinearRegression()

    # 'training' the model
    model = lin_reg.fit(x, y)

    return (model.coef_, model.intercept_, model.score(x, y))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
