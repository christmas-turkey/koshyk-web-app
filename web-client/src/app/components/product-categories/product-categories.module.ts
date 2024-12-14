import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductCategoriesComponent } from './product-categories.component'


@NgModule({
  declarations: [ProductCategoriesComponent],
  imports: [
    CommonModule
  ],
  exports: [ProductCategoriesComponent]
})
export class ProductCategoriesModule { }
