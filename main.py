"""This file contains the code needed to run the final project,
which will display a panel of buttons that the user can interact with
to learn more about the relationship between rising sea levels and other
environmental factors related to climate change."""
from typing import List
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backend_bases import Event

from matplotlib.widgets import Button

import stats_analysis
from curve_equations import cubic_equation_of_best_fit, exponential_equation_of_best_fit, \
    quadratic_equation_of_best_fit
from curve_fitting import cubic_curve_fitting_and_plotting, exponential_curve_fitting_and_plotting, \
    linear_curve_fitting_and_plotting, quadratic_curve_fitting_and_plotting
from plotting_data_with_pandas import create_data_frame


class ButtonHandler:
    """A class that handles events from the buttons in the interactive window."""
    # Private Instance Attributes:
    #   - _df1: a pandas DataFrame containing data to be plotted
    #   - _df2: a pandas DataFrame containing data to be plotted
    #   - _df3: a pandas DataFrame containing data to be plotted
    #   - _ind_filename1: name of the file containing data on one
    #       of the independent variables
    #   - _ind_filename2: name of the file containing data on one
    #       of the independent variables
    #   - _ind_filename3: name of the file containing data on one
    #       of the independent variables
    _df1: pd.DataFrame
    _df2: pd.DataFrame
    _df3: pd.DataFrame
    _ind_filename1: str
    _ind_filename2: str
    _ind_filename3: str
    _dep_filename: str

    def __init__(self, ind_filename1: str, ind_filename2: str,
                 ind_filename3: str, dep_filename: str, df1: pd.DataFrame, df2: pd.DataFrame,
                 df3: pd.DataFrame):
        """Intialize a new ButtonHandler object."""
        self._df1 = df1
        self._df2 = df2
        self._df3 = df3
        self._ind_filename1 = ind_filename1
        self._ind_filename2 = ind_filename2
        self._ind_filename3 = ind_filename3
        self._dep_filename = dep_filename

    def line1(self, _: Event) -> None:
        """Plot the scatter plot and line of best fit for the data in df1."""
        ax = linear_curve_fitting_and_plotting(self._ind_filename1, self._dep_filename)
        plt.subplots_adjust(bottom=0.25)

        x_vals = self._df1[self._df1.columns[0]].values.tolist()
        y_vals = self._df1['Global Mean Sea Levels'].values.tolist()
        line_equation = stats_analysis.best_fit_regression_equation(x_vals, y_vals)
        correlation = str(stats_analysis.correlation(x_vals, y_vals))
        r_squared = str(stats_analysis.r_squared(x_vals, y_vals))

        ax.set_xlabel(self._df1.columns[0] + '\nCorrelation of Data: ' + correlation +
                      '\nEquation of line fit: ' + line_equation +
                      '\nR Squared Value: ' + r_squared)
        plt.draw()

    def line2(self, _: Event) -> None:
        """Plot the scatter plot and line of best fit for the data in df2."""
        ax = linear_curve_fitting_and_plotting(self._ind_filename2, self._dep_filename)
        plt.subplots_adjust(bottom=0.25)

        x_vals = self._df2[self._df2.columns[0]].values.tolist()
        y_vals = self._df2['Global Mean Sea Levels'].values.tolist()

        line_equation = stats_analysis.best_fit_regression_equation(x_vals, y_vals)
        correlation = str(stats_analysis.correlation(x_vals, y_vals))
        r_squared = str(stats_analysis.r_squared(x_vals, y_vals))

        ax.set_xlabel(self._df2.columns[0] + '\nCorrelation of Data: ' + correlation +
                      '\nEquation of line fit: ' + line_equation +
                      '\nR Squared Value: ' + r_squared)
        plt.draw()

    def line3(self, _: Event) -> None:
        """Plot the scatter plot and line of best fit for the data in df3."""
        ax = linear_curve_fitting_and_plotting(self._ind_filename3, self._dep_filename)
        plt.subplots_adjust(bottom=0.25)

        x_vals = self._df3[self._df3.columns[0]].values.tolist()
        y_vals = self._df3['Global Mean Sea Levels'].values.tolist()

        line_equation = stats_analysis.best_fit_regression_equation(x_vals, y_vals)
        correlation = str(stats_analysis.correlation(x_vals, y_vals))
        r_squared = str(stats_analysis.r_squared(x_vals, y_vals))

        ax.set_xlabel(self._df3.columns[0] + '\nCorrelation of Data: ' + correlation +
                      '\nEquation of line fit: ' + line_equation +
                      '\nR Squared Value: ' + r_squared)

        plt.draw()

    def stats(self, _: Event) -> None:
        """Display the results of performing multiple linear regression on the data,
        as well as the root mean squared error for each independent variable in the
        dataframes."""
        _, ax = plt.subplots()
        coef, intercept, r_2 = stats_analysis.multiple_lin_reg(self._df1, self._df2, self._df3)
        coef_new = [round(co, 8) for co in coef]

        ax.set_title('Please full screen this window.')

        # displaying results of performing multiple linear regression
        plt.text(0.0, 0.75, ' Multiple Linear Regression: \n Coefficients: ' +
                 str(coef_new) + '\n Intercept:' + str(intercept) + '\n R^2 Value: ' +
                 str(r_2) + '\n Equation: \n ' + self._df1.columns[0] + ' * ' + str(coef_new[0])
                 + ' + ' + self._df2.columns[0] + ' * ' + str(coef_new[1]) + ' + ' +
                 self._df3.columns[0] + ' * ' + str(coef_new[2]) + ' + ' + str(intercept))

        # calculating and displaying the root mean square error
        x_vals = self._df1[self._df1.columns[0]].values.tolist()
        y_vals = self._df1['Global Mean Sea Levels'].values.tolist()
        plt.text(0.0, 0.575, '\n Root Mean Squared Error (' + self._df1.columns[0] + '): ' +
                 str(stats_analysis.root_mean_squared_error(5, 25, x_vals, y_vals)) +
                 '\n Root Mean Squared Error (' + self._df2.columns[0] + '): ' +
                 str(stats_analysis.root_mean_squared_error(100, 120, x_vals, y_vals)) +
                 '\n Root Mean Squared Error (' + self._df3.columns[0] + '): ' +
                 str(stats_analysis.root_mean_squared_error(-10, -5, x_vals, y_vals)))

        plt.draw()

    def exponential1(self, _: Event) -> None:
        """Plot the scatter plot and the exponential curve of best fit
        for the data in df1."""
        ax = exponential_curve_fitting_and_plotting(self._ind_filename1,
                                                    self._dep_filename)
        plt.subplots_adjust(bottom=0.25)

        ax.set_xlabel(self._df1.columns[0] + '\n\nEquation: \n' +
                      exponential_equation_of_best_fit(self._ind_filename1,
                                                       self._dep_filename))

        plt.draw()

    def exponential2(self, _: Event) -> None:
        """Plot the scatter plot and the exponential curve of best fit
        for the data in df2."""
        ax = exponential_curve_fitting_and_plotting(self._ind_filename2,
                                                    self._dep_filename)
        plt.subplots_adjust(bottom=0.25)

        ax.set_xlabel(self._df2.columns[0] + '\n\nEquation: \n' +
                      exponential_equation_of_best_fit(self._ind_filename2,
                                                       self._dep_filename))

        plt.draw()

    def exponential3(self, _: Event) -> None:
        """Plot the scatter plot and the exponential curve of best fit
        for the data in df3."""
        ax = exponential_curve_fitting_and_plotting(self._ind_filename3,
                                                    self._dep_filename)
        plt.subplots_adjust(bottom=0.25)

        ax.set_xlabel(self._df3.columns[0] + '\n\nEquation: \n' +
                      exponential_equation_of_best_fit(self._ind_filename3,
                                                       self._dep_filename))

        plt.draw()

    def quadratic1(self, _: Event) -> None:
        """Plot the scatter plot and the quadratic curve of best fit
        for the data in df1."""
        ax = quadratic_curve_fitting_and_plotting(self._ind_filename1,
                                                  self._dep_filename)
        plt.subplots_adjust(bottom=0.25)

        ax.set_xlabel(self._df1.columns[0] + '\n\nEquation: \n' +
                      quadratic_equation_of_best_fit(self._ind_filename1,
                                                     self._dep_filename))

        plt.draw()

    def quadratic2(self, _: Event) -> None:
        """Plot the scatter plot and the quadratic curve of best fit
        for the data in df2."""
        ax = quadratic_curve_fitting_and_plotting(self._ind_filename2,
                                                  self._dep_filename)
        plt.subplots_adjust(bottom=0.25)

        ax.set_xlabel(self._df2.columns[0] + '\n\nEquation: \n' +
                      quadratic_equation_of_best_fit(self._ind_filename2,
                                                     self._dep_filename))

        plt.draw()

    def quadratic3(self, _: Event) -> None:
        """Plot the scatter plot and the quadratic curve of best fit
        for the data in df3."""
        ax = quadratic_curve_fitting_and_plotting(self._ind_filename3,
                                                  self._dep_filename)
        plt.subplots_adjust(bottom=0.25)

        ax.set_xlabel(self._df3.columns[0] + '\n\nEquation: \n' +
                      quadratic_equation_of_best_fit(self._ind_filename3,
                                                     self._dep_filename))

        plt.draw()

    def cubic1(self, _: Event) -> None:
        """Plot the scatter plot and the cubic curve of best fit
        for the data in df1."""
        ax = cubic_curve_fitting_and_plotting(self._ind_filename1,
                                              self._dep_filename)
        plt.subplots_adjust(bottom=0.25)

        ax.set_xlabel(self._df1.columns[0] + '\n\nEquation: \n' +
                      cubic_equation_of_best_fit(self._ind_filename1,
                                                 self._dep_filename))

        plt.draw()

    def cubic2(self, _: Event) -> None:
        """Plot the scatter plot and the cubic curve of best fit
        for the data in df2."""
        ax = cubic_curve_fitting_and_plotting(self._ind_filename2,
                                              self._dep_filename)
        plt.subplots_adjust(bottom=0.25)

        ax.set_xlabel(self._df2.columns[0] + '\n\nEquation: \n' +
                      cubic_equation_of_best_fit(self._ind_filename2,
                                                 self._dep_filename))

        plt.draw()

    def cubic3(self, _: Event) -> None:
        """Plot the scatter plot and the cubic curve of best fit
        for the data in df3."""
        ax = cubic_curve_fitting_and_plotting(self._ind_filename3, self._dep_filename)
        plt.subplots_adjust(bottom=0.25)

        ax.set_xlabel(self._df3.columns[0] + '\n\nEquation: ' +
                      cubic_equation_of_best_fit(self._ind_filename3, self._dep_filename))

        plt.draw()


def run_program(ind_filename1: str, ind_filename2: str, ind_filename3: str, dep_filename: str) -> \
        List[Button]:
    """Displays a panel of buttons for the user to interact with. The buttons display scatter plots
    with various mathematical models and statistics. Returns a list of Buttons so that the Buttons
    can be interacted with.

    Preconditions:
        - 'CO2' in ind_filename1 or 'CO2' in ind_filename2 or 'CO2' in ind_filename3
        - ind_filename1 != ''
        - ind_filename2 != ''
        - ind_filename3 != ''
        - dep_filename != ''
    """
    # creating the dataframes from the given data
    df1 = create_data_frame(ind_filename1, dep_filename)
    df2 = create_data_frame(ind_filename2, dep_filename)
    df3 = create_data_frame(ind_filename3, dep_filename)

    callback = ButtonHandler(ind_filename1, ind_filename2, ind_filename3,
                             dep_filename, df1, df2, df3)

    # buttons and axes for statistics
    axstats = plt.axes([0.0, 0.85, 0.5, 0.10])
    bstats = Button(axstats, 'General Statistical Analysis')
    bstats.on_clicked(callback.stats)

    # axes for line buttons
    axline1 = plt.axes([0.0, 0.55, 0.5, 0.1])
    axline2 = plt.axes([0.0, 0.65, 0.5, 0.10])
    axline3 = plt.axes([0.0, 0.75, 0.5, 0.10])

    # buttons for lines
    bfirst = Button(axline1, 'Line - Factor: ' + df1.columns[0])
    bfirst.on_clicked(callback.line1)
    bsecond = Button(axline2, 'Line - Factor: ' + df2.columns[0])
    bsecond.on_clicked(callback.line2)
    bthree = Button(axline3, 'Line - Factor: ' + df3.columns[0])
    bthree.on_clicked(callback.line3)

    # axes for exponentials
    ax_exp_first = plt.axes([0.0, 0.45, 0.5, 0.1])
    ax_exp_second = plt.axes([0.0, 0.35, 0.5, 0.10])
    ax_exp_third = plt.axes([0.0, 0.25, 0.5, 0.10])

    # buttons for exponentials
    bexp_first = Button(ax_exp_first, 'Exponential - Factor: ' + df1.columns[0])
    bexp_first.on_clicked(callback.exponential1)
    bexp_second = Button(ax_exp_second, 'Exponential - Factor: ' + df2.columns[0])
    bexp_second.on_clicked(callback.exponential2)
    bexp_third = Button(ax_exp_third, 'Exponential - Factor: ' + df3.columns[0])
    bexp_third.on_clicked(callback.exponential3)

    # axes for quadratics
    ax_quad_first = plt.axes([0.5, 0.55, 0.5, 0.1])
    ax_quad_second = plt.axes([0.5, 0.65, 0.5, 0.10])
    ax_quad_third = plt.axes([0.5, 0.75, 0.5, 0.10])

    # buttons for quadratics
    bquad_first = Button(ax_quad_first, 'Quadratic - Factor: ' + df1.columns[0])
    bquad_first.on_clicked(callback.quadratic1)
    bquad_second = Button(ax_quad_second, 'Quadratic - Factor: ' + df2.columns[0])
    bquad_second.on_clicked(callback.quadratic2)
    bquad_third = Button(ax_quad_third, 'Quadratic - Factor: ' + df3.columns[0])
    bquad_third.on_clicked(callback.quadratic3)

    # axes for cubics
    ax_cubic_first = plt.axes([0.5, 0.45, 0.5, 0.1])
    ax_cubic_second = plt.axes([0.5, 0.35, 0.5, 0.10])
    ax_cubic_third = plt.axes([0.5, 0.25, 0.5, 0.10])

    # buttons for cubics
    bcub_first = Button(ax_cubic_first, 'Cubic - Factor: ' + df1.columns[0])
    bcub_first.on_clicked(callback.cubic1)
    bcub_second = Button(ax_cubic_second, 'Cubic - Factor: ' + df2.columns[0])
    bcub_second.on_clicked(callback.cubic2)
    bcub_third = Button(ax_cubic_third, 'Cubic - Factor: ' + df3.columns[0])
    bcub_third.on_clicked(callback.cubic3)

    plt.show()

    return [bfirst, bsecond, bthree, bstats,
            bexp_first, bexp_second, bexp_third,
            bquad_first, bquad_second, bquad_third,
            bcub_first, bcub_third, bcub_second]
