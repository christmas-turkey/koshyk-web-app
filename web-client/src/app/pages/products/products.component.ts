import { Component, OnInit } from '@angular/core';
import { ProductsService } from '../../services/products.service'
import { IProduct } from 'src/app/models/product.model';

@Component({
  selector: 'app-products-page',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss']
})
export class ProductsPageComponent implements OnInit {
  skip = 0;
  limit = 10;
  products: IProduct[] = [];

  isLoading = true;
  errorMessage: string | null = null;

  categories: string[] = [];  
  selectedCategory: string | null = null;

  constructor( private productsService: ProductsService )  {}

  loadCategories(): void {
    this.productsService.getProductCategories().subscribe({
      next: (data) => {
        this.categories = data;
      },
      error: (error) => {
        this.errorMessage = 'Failed to load categories';
      }
    })
  }

  loadProducts(category: string | null, skip: number = 0, limit: number = 20): void {
    this.isLoading = true;
    
    // If category is provided, get products by category, otherwise get all products
    const controller = category ? this.productsService.getProductsByCategory(category, skip, limit) : this.productsService.getAllProducts(skip, limit);

    controller.subscribe({
      next: (data) => {
        this.products = this.products.concat(data);
        this.isLoading = false;
      },
      error: (error) => {
        this.errorMessage = 'Failed to load products';
        this.isLoading = false;
      }
    })
  }

  loadMoreProducts(): void {
    this.skip += this.limit;
    this.loadProducts(this.selectedCategory, this.skip, this.limit);
  }

  onSelectCategory(category: string | null): void {
    this.selectedCategory = category;
    this.products = [];
    this.skip = 0;
    this.loadProducts(this.selectedCategory, this.skip, this.limit);
  }

  ngOnInit(): void {
    this.loadProducts(this.selectedCategory, this.skip, this.limit);
    this.loadCategories();
  }
}
