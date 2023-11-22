import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePriceAskGreaterThanBid(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # (Edit 2: Added assertion)
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # (Edit 3: Added assertion)
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  """ ------------ Add more unit tests ------------ """
  # (Edit 4: Added Test for Bid = Ask)
  def test_getDataPoint_calculatePriceBidEqualsAsk(self):
    quotes = [
      {'top_ask': {'price': 120.48, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
    ]

    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  # (Edit 5: Added test that combines all above scenarious into 1 test function as alternative)
  def test_getDataPoint_calculatePriceAll(self):
    """ my alternative version of the tests above is to combine all the different scenarios into one table without including any duplicates"""
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 120.48, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',  'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    # (Edit 6: Another way of doing the above test cases, is with the reduced number of lines)
    # quotes = [
    #   {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453','top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
    #   {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453','top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'DEF'},
    #   {'top_ask': {'price': 120.48, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453','top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'GHI'},
    # ]

  # (Edit 1: My different version of the original "test_getDataPoint_calculatePrice")
  def test_getDataPoint_calculatePriceAlternativeApproach(self):
    """
    The first test "test_getDataPoint_calculatePriceAskGreaterThanBid" is poor because it copies the implementation
      of the main code into the test.
      This test is the same scenario as the original test except that it shows a different testing style.
      The different style here is that the new approach here uses precalculated values as the expected values.
      Many developers prefer this approach.
      """
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    """ ------------ Add the assertion below ------------ """
    expected_results = {
     'ABC': ('ABC', 120.48, 121.2, 120.84),
     'DEF': ('DEF', 117.87, 121.68, 119.775)
    }

    for quote in quotes:
      actual = getDataPoint(quote)

      # better test as expected values are independently calculated in advance
      stock_code = quote['stock']
      expected = expected_results[stock_code]

      self.assertEqual(actual, expected)

      # implementation below is the one suggested by JPMC/Forage, you can see that it is just a copy of the main code in client.py .
      # expected = (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price'] + quote['top_ask']['price']) / 2)

      # Full Original:
      # def test_getDataPoint_calculatePriceAskGreaterThanBid(self):
      #   quotes = [
      #     {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      #     {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
      #   ]
      #   """ ------------ Add the assertion below ------------ """
      #   for quote in quotes:
      #     self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],(quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getRatio_whenBisZero(self):
    actual = getRatio(10,0)
    self.assertEqual(actual,None)

  def test_getRatio_whenAisZero(self):
    actual = getRatio(0,1)
    self.assertEqual(actual,0)

  def test_getRatio_whenBandAisZero(self):
    actual = getRatio(0,0)
    self.assertEqual(actual,None)
  def test_getRatio_whenBisNonZero(self):
    actual = getRatio(10,2)
    self.assertEqual(actual,5)



if __name__ == '__main__':
    unittest.main()
