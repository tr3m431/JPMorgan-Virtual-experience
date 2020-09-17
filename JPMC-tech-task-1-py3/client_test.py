import unittest
from client3 import *
#returns:
    # quote['stock'],
    # float(quote['top_bid']['price']),
    # float(quote['top_ask']['price']),
    # (float(quote['top_bid']['price']) + float(quote['top_ask']['price']))/2

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 121.2, (120.48 + 121.2)/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[1]), ('DEF', 117.87, 121.68, (117.87 + 121.68)/2))


  """ ------------ Add more unit tests ------------ """
  # getRatio with non zero denominator
  def test_getRatio_with_non_zero_denominator(self):
      prices = [15, 15]
      self.assertEqual(getRatio(prices[0], prices[1]), 1)

  # getRatio with zero denominator
  def test_getRatio_with_zero_denominator(self):
      prices = [15, 0]
      self.assertEqual(getRatio(prices[0], prices[1]), None)

if __name__ == '__main__':
    unittest.main()
