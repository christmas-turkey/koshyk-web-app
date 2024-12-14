from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.services.products import (
    get_all_products,
    get_products_by_category,
    get_categories,
)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthcheck")
def healthcheck():
    """
    Check if the server is up and running
    """

    return {"description": "Server is up and running"}


@app.get("/api/products")
def get_all_products_route(
    limit: int = 20,
    skip: int = 0,
    sort_by: str = "title",
    sort_order: str = "asc",
):
    """
    Retrieve products from the Database.

    Query params:
        limit (int, optional): The number of products to retrieve.
        skip (int, optional): The number of products to skip.
        sort_by (str, optional): The field to sort the products by.
        sort_order (str, optional): The order to sort the products by.
    
    Returns:
        JSON: The products retrieved from the Database.
    """

    response = get_all_products(limit, skip, sort_by, sort_order)
    return response

@app.get("/api/products/{category}")
def get_products_by_category_route(
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

    response = get_products_by_category(category, limit, skip, sort_by, sort_order)
    return response

@app.get("/api/categories")
def get_categories_route():
    """
    Retrieve all the categories from the Database.

    Returns:
        JSON: The categories retrieved from the Database.
    """

    response = get_categories()
    return response