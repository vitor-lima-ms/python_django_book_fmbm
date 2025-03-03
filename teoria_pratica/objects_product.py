from class_product import Product

first_product = Product(1, 'Smartphone', 1000.00, 10)
first_product.stock_in(10)
first_product.stock_out(5)
# first_product.view_qtd_in_stock()

# print(first_product._Product__price) Notacao para acessar atributos privados

# first_product.description = 'iPhone' Setter
# print(first_product.description) Getter