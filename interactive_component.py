"""Interactive components."""
from matplotlib.widgets import Button
from typing import List, Tuple
import pandas as pd
import matplotlib.pyplot as plt
import math

from matplotlib.backend_bases import Event
from matplotlib.figure import Figure
from matplotlib.widgets import Button, Slider
from pandas import DataFrame

import stats_analysis
from curve_fitting import cubic_curve_fitting_and_plotting, exponential_curve_fitting_and_plotting, \
    linear_curve_fitting_and_plotting, quadratic_curve_fitting_and_plotting
from plotting_data_with_pandas import create_scatter_plot


def plot_graphs(df1: DataFrame, df2: DataFrame, df3: DataFrame) -> None:
    """Plotting the graphs using Plotly."""

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2, right=0.8)

    ax.set_title(df1.columns[0] + '\nClick on legend line to toggle line on/off')
    line1, = ax.plot(df1[df1.columns[0]], df1['Global Mean Sea Levels'],
                     lw=2, color='blue', label=df1.columns[0])

    ######
    # stats analysis
    ######
    y_vals = df1[df1.columns[0]].values.tolist()
    x_vals = df1['Global Mean Sea Levels'].values.tolist()
    line_equation = stats_analysis.best_fit_regression_equation(x_vals, y_vals)
    correlation = str(stats_analysis.correlation(x_vals, y_vals))
    r_squared = str(stats_analysis.r_squared(x_vals, y_vals))
    ax.set_xlabel('Correlation of Data: ' + correlation + '\nEquation of line fit: ' + line_equation +
                  '\nR Squared Value: ' + r_squared)

    # equation = stats_analysis.best_fit_regression_equation(x_vals, y_vals)[3:]
    # y_int = stats_analysis.y_intercept_of_best_fit(x_vals, y_vals)
    # slope = stats_analysis.slope_of_best_fit(x_vals, y_vals)
    # y_vals_act = [slope * x + y_int for x in x_vals]

    # line_reg = ax.plot(df1[df1.columns[0]], y_vals_act, lw=2, color='red')

    # line2, = ax.plot(df2[df2.columns[0]], df2['Global Mean Sea Levels'],
    #                  lw=2, color='red', label=df2.columns[0])
    # line3, = ax.plot(df3[df3.columns[0]], df3['Global Mean Sea Levels'],
    #                  lw=2, color='green', label=df3.columns[0])

    # positioning the legend
    leg = ax.legend(loc='lower right', fancybox=True, shadow=True, title='Legend')
    leg.get_frame().set_alpha(0.5)  # sets opacity of the legend -- todo: could perhaps make
    # it so that it goes transparent when you're not hovering over it?
    # higher value in the brackets means less transparent

    # TODO: there's a better way to do this
    line1.set_marker('8')
    line1.set_linestyle('None')
    leg_line = leg.get_lines()[0]
    leg_line.set_picker(True)
    leg_line.set_pickradius(5)
    leg_line = line1

    def onpick(event) -> None:  # TODO: move this outside the function
        """
        It's getting mad at me for not having a docstring but i honestly don't understand
        why the tutorials are saying to have this function in here
        """
        # on the pick event, find the orig line corresponding to the
        # legend proxy line, and toggle the visibility
        legend_line = event.artist
        # original_line = lined[legend_line]
        original_line = line1
        vis = not original_line.get_visible()
        original_line.set_visible(vis)

        # Change the alpha on the line in the legend so we can see what lines
        # have been toggled
        if vis:
            legend_line.set_alpha(1.0)
        else:
            legend_line.set_alpha(0.2)

        fig.canvas.draw()

    fig.canvas.mpl_connect('pick_event', onpick)

    plt.draw()

    # return bback

    ################################################################
    # BUTTONS
    # >>> df3 = create_scatter_plot('co2_levels.xlsx', 'global_sea_levels.csv')
    # >>> df1 = create_scatter_plot('global_temperature.csv', 'global_sea_levels.csv')
    # >>> df2 = create_scatter_plot('glacier_mass_balance.csv', 'global_sea_levels.csv')
    # >>> plot_graphs(df1, df2, df3)
    ################################################################


def button_panel(ind_filename1: str, ind_filename2: str, ind_filename3: str, dep_filename: str) -> \
        List[Button]:
    """Buttons!"""

    df1 = create_scatter_plot(ind_filename1, dep_filename)
    df2 = create_scatter_plot(ind_filename2, dep_filename)
    df3 = create_scatter_plot(ind_filename3, dep_filename)

    class Index:

        def next(self, event):
            ax = linear_curve_fitting_and_plotting(ind_filename1, dep_filename)
            plt.subplots_adjust(bottom=0.25)

            x_vals = df1[df1.columns[0]].values.tolist()
            y_vals = df1['Global Mean Sea Levels'].values.tolist()
            line_equation = stats_analysis.best_fit_regression_equation(x_vals, y_vals)
            correlation = str(stats_analysis.correlation(x_vals, y_vals))
            r_squared = str(stats_analysis.r_squared(x_vals, y_vals))
            # rt_mn_sq_er = str(stats_analysis.root_mean_squared_error())

            ax.set_xlabel(df1.columns[0] + '\nCorrelation of Data: ' + correlation +
                              '\nEquation of line fit: ' + line_equation +
                          '\nR Squared Value: ' + r_squared)
            plt.draw()

        def prev(self, event):
            ax = linear_curve_fitting_and_plotting(ind_filename2, dep_filename)
            plt.subplots_adjust(bottom=0.25)

            x_vals = df2[df2.columns[0]].values.tolist()
            y_vals = df2['Global Mean Sea Levels'].values.tolist()

            line_equation = stats_analysis.best_fit_regression_equation(x_vals, y_vals)
            correlation = str(stats_analysis.correlation(x_vals, y_vals))
            r_squared = str(stats_analysis.r_squared(x_vals, y_vals))

            ax.set_xlabel(df2.columns[0] + '\nCorrelation of Data: ' + correlation +
                          '\nEquation of line fit: ' + line_equation +
                          '\nR Squared Value: ' + r_squared)
            plt.draw()

        def mid(self, event):
            ax = linear_curve_fitting_and_plotting(ind_filename3, dep_filename)
            plt.subplots_adjust(bottom=0.25)

            x_vals = df3[df3.columns[0]].values.tolist()
            y_vals = df3['Global Mean Sea Levels'].values.tolist()

            line_equation = stats_analysis.best_fit_regression_equation(x_vals, y_vals)
            correlation = str(stats_analysis.correlation(x_vals, y_vals))
            r_squared = str(stats_analysis.r_squared(x_vals, y_vals))

            ax.set_xlabel(df3.columns[0] + '\nCorrelation of Data: ' + correlation +
                          '\nEquation of line fit: ' + line_equation +
                          '\nR Squared Value: ' + r_squared)

            plt.draw()

        def stats(self, event):
            fig, ax = plt.subplots()
            coef, intercept, r_2 = stats_analysis.multiple_lin_reg(df1, df2, df3)
            coef_new = [round(co, 8) for co in coef]
            ax.set_title('Please full screen this window.')
            plt.text(0.0, 0.75, ' Multiple Linear Regression: \n Coefficients: ' +
                     str(coef_new) + '\n Intercept:' + str(intercept) + '\n R^2 Value: ' +
                     str(r_2) + '\n Equation: \n ' + df1.columns[0] + ' * ' + str(coef_new[0]) +
                     ' + ' + df2.columns[0] + ' * ' + str(coef_new[1]) + ' + ' +
                     df3.columns[0] + ' * ' + str(coef_new[2]) + ' + ' + str(intercept))

            x_vals = df1[df1.columns[0]].values.tolist()
            y_vals = df1['Global Mean Sea Levels'].values.tolist()
            plt.text(0.0, 0.4, '\n Root Mean Squared Error (' + df1.columns[0] + '): ' +
                     str(stats_analysis.root_mean_squared_error(5, 25, x_vals, y_vals)) +
                     '\n Root Mean Squared Error (' + df2.columns[0] + '): ' +
                     str(stats_analysis.root_mean_squared_error(100, 120, x_vals, y_vals)) +
                     '\n Root Mean Squared Error (' + df3.columns[0] + '): ' +
                     str(stats_analysis.root_mean_squared_error(-10, -5, x_vals, y_vals)))

            plt.draw()

        def exponential1(self, event):
            exponential_curve_fitting_and_plotting(ind_filename1, dep_filename)

        def exponential2(self, event):
            exponential_curve_fitting_and_plotting(ind_filename2, dep_filename)

        def exponential3(self, event):
            exponential_curve_fitting_and_plotting(ind_filename3, dep_filename)

        def quadratic1(self, event):
            quadratic_curve_fitting_and_plotting(ind_filename1, dep_filename)

        def quadratic2(self, event):
            quadratic_curve_fitting_and_plotting(ind_filename2, dep_filename)

        def quadratic3(self, event):
            quadratic_curve_fitting_and_plotting(ind_filename3, dep_filename)

        def cubic1(self, event):
            cubic_curve_fitting_and_plotting(ind_filename1, dep_filename)

        def cubic2(self, event):
            cubic_curve_fitting_and_plotting(ind_filename2, dep_filename)

        def cubic3(self, event):
            cubic_curve_fitting_and_plotting(ind_filename3, dep_filename)

    callback = Index()

    axprev = plt.axes([0.0, 0.55, 0.5, 0.1])
    axnext = plt.axes([0.0, 0.65, 0.5, 0.10])
    axmid = plt.axes([0.0, 0.75, 0.5, 0.10])
    axstats = plt.axes([0.0, 0.85, 0.5, 0.10])

    # buttons for scatters and lines ?
    bfirst = Button(axprev, 'Line - Factor: ' + df1.columns[0])
    bfirst.on_clicked(callback.next)
    bsecond = Button(axnext, 'Line - Factor: ' + df2.columns[0])
    bsecond.on_clicked(callback.prev)
    bthree = Button(axmid, 'Line - Factor: ' + df3.columns[0])
    bthree.on_clicked(callback.mid)
    bstats = Button(axstats, 'General Statistical Analysis')
    bstats.on_clicked(callback.stats)

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

    # for quadratics
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

    # for cubics
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
