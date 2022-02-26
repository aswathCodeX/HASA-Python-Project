from discharge_data import *
from gumbel_reduce import gumbel_reduce_data
from plot_discharge import PlotDischarge
from log import *

time_list = [50, 100, 150, 200, 500, 1000]


def verify_gumbel(func):
    """
    A wrapper function, Wrapper decorator @ should be placed right on
    top of function that is to be wrapped

    :param func: function to be wrapped
    :return: the wrapped function's return value
    """
    def wrapper(args):
        try:
            result = func(args)
            return result
        except KeyError:
            logging.error('ERROR: To extract reduce value numeric value is '
                          'to be passed')
            return np.nan

    return wrapper


@verify_gumbel
def get_reduce_mean(index_):
    """
    Indexing the Gumbel reduce data and determining reduce mean

    :param index_: no. of discharge data in the DataFrame
    :return: indexed reduced mean value
    """
    if index_ in range(100, 150):
        index_ = 150
    elif index_ in range(150, 200):
        index_ = 200
    value = gumbel_reduce_data(csv_file=gumbel_reduce_path)
    return value['Reduced mean'][index_]


@verify_gumbel
def get_reduce_std(index_):
    """
    Indexing the Gumbel reduce data and determining reduce std

    :param index_: no. of discharge data in the DataFrame
    :return: indexed reduced standard deviation value
    """
    if index_ in range(100, 150):
        index_ = 150
    elif index_ in range(150, 200):
        index_ = 200
    value = gumbel_reduce_data(csv_file=gumbel_reduce_path)
    return value['Reduced std'][index_]


def gumbel_distribution(discharge_data):
    """
    Function determines the Gumbel Distribution statistical parameters
    by calling 2 functions and performs mathematical operations to
    return the Extrapolated discharges
    :param discharge_data: pandas DataFrame of Annual maxima
    :return: a list of extrapolated discharges
    """
    number_of_years = discharge_data.shape[0]
    logging.info(
        'Annual Max is calculated for {} years'.format(number_of_years))
    mean_discharge = discharge_data['Discharge [CMS]'].mean()
    std_dev = discharge_data['Discharge [CMS]'].std()
    reduce_mean = get_reduce_mean(number_of_years)
    reduce_std = get_reduce_std(number_of_years)
    main_discharge = []
    for year in time_list:
        reduced_variate = -math.log(math.log(year / (year - 1)))
        try:
            frequency_factor = (reduced_variate - reduce_mean) / reduce_std
        except ZeroDivisionError:
            logging.error("ERROR: Could not  divide  by zero")
        discharge_value = mean_discharge + frequency_factor * std_dev
        main_discharge.append(discharge_value)
    return main_discharge


def main():
    # instantiation of the DischargeDataHandler Class
    raw_discharge_data = DischargeDataHandler(
        data_csv_file=discharge_data_path)

    # calling method to get discharge data
    data = raw_discharge_data.get_discharge_data()
    logging.info("\nThe Annual Maximum Discharge Data is: \n{}".format(data))

    # function call to estimate extrapolated discharges
    output_list = gumbel_distribution(data)

    # instantiation of the PlotDischarge Class
    plotter = PlotDischarge()

    # Flexibilizing the Scatter size using Magic Methods
    plotter * 10
    plotter > 150
    plotter < 5

    # Plotting the Hydrograph
    plotter.plot_discharge(data['Year'], data['Discharge [CMS]'],
                           title='Hydrograph', color='grey')

    # changing the extrapolated discharge plotting arguments to numpy
    t_series = np.array(time_list)
    q_series = np.array(output_list)
    # plotting the extrapolated discharge
    plotter.gumbel_plotting(t_series, q_series, title='Gumbel Extrapolation',
                            color='black')
    # appending extrapolated discharges to a dict
    flood_discharge_dict = {}
    for index, time in enumerate(time_list):
        flood_discharge_dict[time] = output_list[index]
    logging.info(flood_discharge_dict)


if __name__ == '__main__':
    main()


# # instantiation of the DischargeDataHandler Class
# raw_discharge_data = DischargeDataHandler(
#     data_csv_file=discharge_data_path)
#
# # calling method to get discharge data
# data = raw_discharge_data.get_discharge_data()
# logging.info("\nThe Annual Maximum Discharge Data is: \n{}".format(data))
#
# # function call to estimate extrapolated discharges
# output_list = gumbel_distribution(data)
#
# # instantiation of the PlotDischarge Class
# plotter = PlotDischarge()
#
# # Flexibilizing the Scatter size using Magic Methods
# plotter * 100
# plotter > 150
# plotter < 5
#
# # Plotting the Hydrograph
# plotter.plot_discharge(data['Year'], data['Discharge [CMS]'],
#                        title='Hydrograph', color='grey')
#
# # changing the extrapolated discharge plotting arguments to numpy
# t_series = np.array(time_list)
# q_series = np.array(output_list)
# # plotting the extrapolated discharge
# plotter.gumbel_plotting(t_series, q_series, title='Gumbel Extrapolation',
#                         color='black')
# # appending extrapolated discharges to a dict
# flood_discharge_dict = {}
# for index, time in enumerate(time_list):
#     flood_discharge_dict[time] = output_list[index]
# logging.info(flood_discharge_dict)
