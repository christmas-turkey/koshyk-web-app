from src.config.db import get_db


database = get_db()
products_collection = database["products"]


def get_all_products(
    limit: int = 20,
    skip: int = 0,
    sort_by: str = "title",
    sort_order: str = "asc",
):
    """
    Retrieve products from the Database.

    Args:
        limit (int, optional): The number of products to retrieve.
        skip (int, optional): The number of products to skip.
        sort_by (str, optional): The field to sort the products by.
        sort_order (str, optional): The order to sort the products by.
    
    Returns:
        JSON: The products retrieved from the Database.
    """

    products = products_collection \
        .find({}, {"_id": 0}) \
        .limit(limit) \
        .skip(skip) \
        .sort(sort_by, 1 if sort_order == "asc" else -1)
    
    return list(products)


def get_products_by_category(
    category: str,
    limit: int = 20,
    skip: int = 0,
    sort_by: str = "title",
    sort_order: str = "asc",
):
    """
    Retrieve products by category from the Database.

    Args:
        category (str): The category to filter the products by.
        limit (int, optional): The number of products to retrieve.
        skip (int, optional): The number of products to skip.
        sort_by (str, optional): The field to sort the products by.
        sort_order (str, optional): The order to sort the products by.
    
    Returns:
        JSON: The products retrieved from the Database.
    """

    products = products_collection \
        .find({"category": category}, {"_id": 0}) \
        .limit(limit) \
        .skip(skip) \
        .sort(sort_by, 1 if sort_order == "asc" else -1)
    
    return list(products)


def get_categories():
    """
    Retrieve categories from the Database.

    Returns:
        JSON: The categories retrieved from the Database.
    """

    categories = products_collection.distinct("category")
    return list(categories)