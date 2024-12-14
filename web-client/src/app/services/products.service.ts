import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { IProduct } from '../models/product.model';


@Injectable({
  providedIn: 'root'
})
export class ProductsService {

  constructor(private http: HttpClient) { }

  getAllProducts(skip: number=0, limit: number=20) {
    return this.http.get<IProduct[]>(`${environment.apiUrl}/api/products?skip=${skip}&limit=${limit}`);
  }

  getProductsByCategory(
    category: string,
    skip: number=0,
    limit: number=20
  ) {
    return this.http.get<IProduct[]>(
      `${environment.apiUrl}/api/products/${category}?skip=${skip}&limit=${limit}`
    );
  }

  getProductCategories() {
    return this.http.get<string[]>(`${environment.apiUrl}/api/categories`);
  }
}
