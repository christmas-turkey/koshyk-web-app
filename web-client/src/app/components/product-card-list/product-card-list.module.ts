import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductCardListComponent } from './product-card-list.component';
import { ProductCardModule } from '../product-card/product-card.module';


@NgModule({
  declarations: [ProductCardListComponent],
  imports: [
    CommonModule, 
    ProductCardModule
  ],
  exports: [ProductCardListComponent]
})
export class ProductCardListModule { }
