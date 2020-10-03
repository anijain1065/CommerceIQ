class ProductInformation:
    def __init__(self, product_name,
                 currentWarehouseStock,
                 unitsThatCouldBeSoldFromWarehouseInComingEachWeek,
                 unitsThatWillComeInWarehouseStockInComingEachWeek):
        # Product name
        self.product_name = product_name

        # Current product units in stock at warehouse
        self.currentUnitsInStockAtWarehouse = currentWarehouseStock

        # Forecasted product units that will be sold from warehouse in future weeks
        # Eg: if this week 10 units, next week 20 units and week after 30 units
        # [10,20,30]
        self.forecastedUnitsToBeSoldFromWarehouseInEachComingWeek = unitsThatCouldBeSoldFromWarehouseInComingEachWeek

        # Product units that will come in warehouse
        # Eg: if this week 15 units, next week 25 units and week after 35 units
        # [15,25,35]
        self.unitsThatWillComeInWarehouseStockInComingEachWeek = unitsThatWillComeInWarehouseStockInComingEachWeek


def canProductGoOutOfStockInComingNWeeks(productInformation, weeksToCheckForOutOfStock):
    """
    Check if product can go out of stock within N weeks
    :param productInformation:
    :param weeksToCheckForOutOfStock:
    :return True if product will go out of stock in N weeks:
    """
    forecastedUnitsToBeSoldWithinWeeksToCheckForOutOfStock = sum(
        productInformation.forecastedUnitsToBeSoldFromWarehouseInEachComingWeek[:weeksToCheckForOutOfStock])
    unitsThatWillComeInWarehouseWithinWeeksToCheckForOutOfStock = sum(
        productInformation.unitsThatWillComeInWarehouseStockInComingEachWeek[:weeksToCheckForOutOfStock])

    return True if (forecastedUnitsToBeSoldWithinWeeksToCheckForOutOfStock >= (
            productInformation.currentUnitsInStockAtWarehouse + unitsThatWillComeInWarehouseWithinWeeksToCheckForOutOfStock)) else False

'''
if __name__ == "__main__":
    pi = ProductInformation("Mobile", 0, [100,200,300], [0,600,0])
    print(canProductGoOutOfStockInComingNWeeks(pi, 1))
    '''
