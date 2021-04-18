from statistics import mean, median, variance, correlation
import csv


def load_data(path):
    """
    Loads data from given csv
    :param path: path to csv file
    :return: returns data as dict {name_of_feature: list_of_values}
    """
    with open(path, 'r') as f:
        reader = csv.reader(f)
        read_header = None
        data = {}
        index_to_column_name = {}
        for row in reader:
            if not read_header:
                # we are at first row with names of columns
                for i, column_name in enumerate(row):  # enumerate generates index together with value
                    data[column_name] = []  # initializing as empty list
                    index_to_column_name[i] = column_name
                read_header = True
            else:
                # need to append values to data lists. We don't know column name, only index.
                for i, value in enumerate(row):
                    current_column_name = index_to_column_name[i]  # reproducing column name
                    data[current_column_name].append(float(value))
    return data


def run_analysis():
    """
    the function that used to calculate for the main function purpose
           """
    file_path = './winequality.csv'
    data = load_data(file_path)

    # first way of printing. Everything casted to string, and spaces put automatically between passed values.
    print('Number of features:', len(data))
    for feature_name, list_of_values in sorted(data.items()):
        # second way of printing. We print single string after format function.
        # Format function fills {} with values passed as arguments. It has nice applications for better printing,
        # like limiting number of digits for floats or other formatting tools.
        print('"{}". Mean: {:3.2f}, Median: {:.2f}, Std: {:.4f}'.format(
            feature_name, mean(list_of_values), median(list_of_values), variance(list_of_values)**0.5))

    # here you should compute correlations. Be careful, pair should be sorted before printing
    min_1 = 2
    max_1 = -2
    strongest_pair = []
    weakest_pair = []

    for index in range(len(data.items())-1):
        feature_name_1, list_of_values_1 = list(data.items())[index]
        for index_2 in range(index+1, len(data.items())):
            feature_name_2, list_of_values_2 = list(data.items())[index_2]
            cor = correlation(list_of_values_1, list_of_values_2)
            if abs(cor) < abs(min_1):
                min_1 = cor
                weakest_pair = sorted([feature_name_1, feature_name_2])
            if cor > max_1:
                max_1 = cor
                strongest_pair = sorted([feature_name_1, feature_name_2])

    high_correlation = max_1
    print('The strongest linear relationship is between: "{}","{}". '
          'The value is: {:.4f}'.format(strongest_pair[0], strongest_pair[1], high_correlation))

    low_correlation = min_1
    print('The weakest linear relationship is between: "{}","{}". '
          'The value is: {:.4f}'.format(*weakest_pair, low_correlation))  # * converts list to arguments.
    # Line 53 is equivalent to line 48, this is just other way to use list as arguments


if __name__ == '__main__':
    """ Calculates and prints the 2 variables with the highest correlation 
    and the 2 variables with the lowest correlation,all by lexicography order.
    the variables are the features in the data collected in winequality.csv and winequality_2.csv
       """
    run_analysis()
