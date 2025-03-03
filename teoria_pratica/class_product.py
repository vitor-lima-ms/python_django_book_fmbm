class Product:
    """Class that represents a general product"""
    
    def __init__(
            self,
            id: int,
            description: str,
            price: float,
            stock_qtd: float=0.0,
    ) -> None:
        self.__id = id
        self.__description = description
        self.__price = price
        self.__stock_qtd = stock_qtd
    
    """Method for inserting products into stock"""
    def stock_in(self, qtd: float) -> None:
        self.__stock_qtd += qtd

    """Method for removing products into stock"""
    def stock_out(self, qtd: float) -> None:
        self.__stock_qtd -= qtd
    
    """Method to see how many products are in stock"""
    def view_qtd_in_stock(self) -> None:
        print(f'A quantidade do produto {self.__description} é {self.__stock_qtd}')
    
    """getter for __id. This property does not be changed"""
    @property
    def id(self) -> int:
        return self.__id
    
    """getter and setter for __description"""
    @property
    def description(self) -> str:
        return self.__description
    @description.setter
    def description(self, new_value: str) -> None:
        self.__description = new_value
    
    """getter and setter for __price"""
    @property
    def price(self) -> float:
        return self.__price
    @price.setter
    def price(self, new_value: float) -> None:
        if new_value <= 0:
            print('Error: Price must be a positive number.')
        else:
            self.__price = new_value

    """getter for __stock_qtd. There is no point in changing this property directly. This should be done with the stock_in and stock_out methods."""
    @property
    def stock_qtd(self) -> float:
        return self.__stock_qtd