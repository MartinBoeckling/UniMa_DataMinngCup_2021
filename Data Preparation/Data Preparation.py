# import relevant packages
import pandas as pd
import jenkspy

# initialize binning method for transactions
# read data
transaction_data = pd.read_csv(r'Dataset\transactions.csv', sep='|', encoding='utf-8')
print(transaction_data.columns)
# create click bin
click_bins = jenkspy.jenks_breaks(transaction_data['click'], nb_class=5)
click_bins[1] = (click_bins[1] + 0.1)
print(click_bins)
transaction_data['click_bins'] = pd.cut(transaction_data['click'], bins=click_bins, labels=['click_1', 'click_2', 'click_3', 'click_4', 'click_5'], include_lowest=True)
# create basket bin
basket_bins = jenkspy.jenks_breaks(transaction_data['basket'], nb_class=5)
basket_bins[1] = (basket_bins[1] + 0.1)
print(basket_bins)
transaction_data['basket_bins'] = pd.cut(transaction_data['basket'], bins=click_bins, labels=['basket_1', 'basket_2', 'basket_3', 'basket_4', 'basket_5'], include_lowest=True)
# create order bin
order_bins = jenkspy.jenks_breaks(transaction_data['order'], nb_class=5)
order_bins[1] = (order_bins[1] + 0.1)
print(order_bins)
transaction_data['order_bins'] = pd.cut(transaction_data['order'], bins=click_bins, labels=['order_1', 'order_2', 'order_3', 'order_4', 'order_5'], include_lowest=True)
print(transaction_data)
# write result to repo
transaction_data.to_csv(r'Dataset\Prepared Dataset\transaction_bins.csv', index=False)
