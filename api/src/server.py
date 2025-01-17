from fastapi import FastAPI
from src.services.products import (
    get_all_products,
    get_product_by_id,
    search_products,
    get_product_categories,
    get_products_by_category
)


app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    """
    Check if the server is up and running
    """

    return {"description": "Server is up and running"}


@app.get("/api/get_all_products")
def get_all_products_route(
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

    products = get_all_products(limit, sort_by, sort_order)
    return products

@app.get("/api/products/{product_id}")
def get_product_by_id_route(
    product_id: int,
):
    """
    Retrieve a product by its ID from the dummyjson API

    Args:
        product_id (int): The ID of the product to retrieve
    
    Returns:
        JSON: The product retrieved from the dummyjson API
    """

    product = get_product_by_id(product_id)
    return product

@app.get("/api/search_products")
def search_products_route(
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

    products = search_products(query, limit, sort_by, sort_order)
    return products

@app.get("/api/get_product_categories")
def get_product_categories_route():
    """
    Retrieve all product categories from the dummyjson API

    Returns:
        JSON: The product categories retrieved from the dummyjson API
    """

    categories = get_product_categories()
    return categories

@app.get("/api/products/category/{category}")
def get_products_by_category_route(
    category: str,
    limit: int = 0,
    sort_by: str = "title",
    sort_order: str = "asc",
):
    """
    Retrieve all products in a category from the dummyjson API

    Args:
        category (str): The category to retrieve products from
        limit (int): The number of products to retrieve. Default is 0, which retrieves all products
        sort_by (str): The field to sort by. Default is "title"
        sort_order (str): The order to sort by. Default is "asc"
    
    Returns:
        JSON: The products retrieved from the dummyjson API
    """

    products = get_products_by_category(category, limit, sort_by, sort_order)
    return products