import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductsPageComponent } from './products.component';
import { ProductCardListModule } from 'src/app/components/product-card-list/product-card-list.module';
import { ProductCategoriesModule } from '../../components/product-categories/product-categories.module';

@NgModule({
  declarations: [
    ProductsPageComponent,
  ],
  imports: [
    CommonModule,
    ProductCardListModule,
    ProductCategoriesModule
  ],
  exports: [
    ProductsPageComponent,
  ]
})
export class ProductsPageModule { }
