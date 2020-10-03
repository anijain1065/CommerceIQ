import pytest
from PredictOutOfStock import ProductInformation, canProductGoOutOfStockInComingNWeeks

'''
To test the output when product is not sailing and seller wants to shut that particular product.
i.e. Demand=Supply=0
'''
def test_01_ProductShut():
    pi = ProductInformation("Product_Name", 0, [0,0,0], [0,0,0])
    n = canProductGoOutOfStockInComingNWeeks(pi, 3)
    print(n)
    assert n == True

'''
To test the output when 1st week supply is 0 and consequtive demand is fulfilled.
'''
def test_02_ConsequtiveDemandFulfillment():
    pi = ProductInformation("Product_Name", 0, [100,200,300], [0,600,0])
    n = canProductGoOutOfStockInComingNWeeks(pi, 1)
    print(n)
    assert n == True

'''
To test the output when 1st week supply is stored and consequtive demand is fulfilled.
'''
def test_03_DemandFulfillment():
    pi = ProductInformation("Product_Name", 100, [100,200,300], [500])
    n = canProductGoOutOfStockInComingNWeeks(pi, 3)
    print(n)
    assert n == False

'''
To test the output when 1st week demand is 0 and consequtive demand is fulfilled by the supply
coming in 1st week.
'''
def test_04_FirstWeekDemandNull():
    pi = ProductInformation("Product_Name", 0, [0,200,300], [600,0,0])
    n = canProductGoOutOfStockInComingNWeeks(pi, 1)
    print(n)
    assert n == True

if __name__ == "__main__":
    test_01_ProductShut()
    test_02_ConsequtiveDemandFulfillment()
    test_03_DemandFulfillment()
    test_04_FirstWeekDemandNull()
