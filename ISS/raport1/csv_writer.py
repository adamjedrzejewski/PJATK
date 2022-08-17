'''
This is script that showcases use of Pandas library and generates a random
CSV file.
'''

import pandas as pd
import argparse



def main(args):
    a = [1, 4, 6, 12, 11]
    b = ['Apple', 'Tomato', 'Orange', 'Potato', 'Banana']
    c = [534.32, 123.5, 6543.12, 123.54, 123.76]
    data_dict = {'A number':a, 'Something':b, 'Floater':c}
    dataframe = pd.DataFrame(data_dict)
    print(dataframe.info())
    print(dataframe.head())
    print(dataframe.describe())
    dataframe.to_csv(args.output, index=False, sep=';')

def parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-o', '--output', type=str, required=True,
    help='Name of csv file that will be generated.')
    return parser.parse_args()
    

if __name__ == '__main__':
    main(parse_arguments())