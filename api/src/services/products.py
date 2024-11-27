import requests


def get_all_products(
    limit: int = 0,
    sort_by: str = "title",
    sort_order: str = "asc",
):
    """
    Retrieve all products from the dummyjson API

    Args:
        limit (int): The number of products to retrieve. Default is 0, which retrieves all products
        sort_by (str): The field to sort by. Default is "title"
        sort_order (str): The order to sort by. Default is "asc"
    
    Returns:
        JSON: The products retrieved from the dummyjson API
    """

    response = requests.get(f"https://dummyjson.com/products?limit={limit}&sortBy={sort_by}&order={sort_order}")
    return response.json()

def get_product_by_id(
    product_id: int,
):
    """
    Retrieve a product by its ID from the dummyjson API

    Args:
        product_id (int): The ID of the product to retrieve
    
    Returns:
        JSON: The product retrieved from the dummyjson API
    """

    response = requests.get(f"https://dummyjson.com/products/{product_id}")
    return response.json()

def search_products(
    query: str,
    limit: int = 0,
    sort_by: str = "title",
    sort_order: str = "asc",
):
    """
    Search for products by a query from the dummyjson API

    Args:
        query (str): The query to search for
        limit (int): The number of products to retrieve. Default is 0, which retrieves all products
        sort_by (str): The field to sort by. Default is "title"
        sort_order (str): The order to sort by. Default is "asc"
    
    Returns:
        JSON: The products retrieved from the dummyjson API
    """

    response = requests.get(f"https://dummyjson.com/products/search?q={query}&limit={limit}&sortBy={sort_by}&order={sort_order}")
    return response.json()

def get_product_categories():
    """
    Retrieve all product category names from the dummyjson API

    Returns:
        JSON: The product categories retrieved from the dummyjson API
    """

    response = requests.get("https://dummyjson.com/products/categories")
    return response.json()

def get_products_by_category(
    category_name: str,
    limit: int = 0,
    sort_by: str = "title",
    sort_order: str = "asc",
):
    """
    Retrieve all products by category name from the dummyjson API

    Args:
        category_name (str): The name of the category to retrieve products from
        limit (int): The number of products to retrieve. Default is 0, which retrieves all products
        sort_by (str): The field to sort by. Default is "title"
        sort_order (str): The order to sort by. Default is "asc"
    
    Returns:
        JSON: The products retrieved from the dummyjson API
    """

    response = requests.get(f"https://dummyjson.com/products/category/{category_name}?limit={limit}&sortBy={sort_by}&order={sort_order}")
    return response.json()