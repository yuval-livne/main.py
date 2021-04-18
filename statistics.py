import math


def median(list_of_values):
    """Return the median of a list."""

    sorted_list = sorted(list_of_values)
    center_index = int(len(list_of_values)/2)  # round to int required because division always produces float

    # Median value depends on length on list
    if len(list_of_values) % 2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index-1])/2
    else:
        # Now we need only 1 index for exact value
        result = sorted_list[center_index]
    return result


def mean(list_of_values):
    """Return the mean of a list."""

    return sum(list_of_values)/len(list_of_values)


def variance(list_of_values):
    """Return the variance of a list."""

    average = mean(list_of_values)
    squared_sum = sum([(x - average)**2 for x in list_of_values])
    return squared_sum/(len(list_of_values)-1)


def covariance(first_list_of_values, second_list_of_values):
    """Return the covariance between 2 lists."""

    mean_first = mean(first_list_of_values)
    mean_second = mean(second_list_of_values)
    length = len(first_list_of_values)
    indexes = range(length)
    sum_diff = 0

    for index in indexes:
        sum_diff += ((first_list_of_values[index]-mean_first)*(second_list_of_values[index]-mean_second))

    result = sum_diff/(length-1)
    # Place your code here
    return result


def correlation(first_list_of_values, second_list_of_values):
    """Return the result of the correlation between 2 lists."""

    standard_first = math.sqrt(variance(first_list_of_values))
    standard_second = math.sqrt(variance(second_list_of_values))
    cov = covariance(first_list_of_values, second_list_of_values)

    result = (cov/(standard_first*standard_second))
    # Place your code here
    return result
