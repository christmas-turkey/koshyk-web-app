import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductCardComponent } from './product-card.component';
import { ProductRatingModule } from '../product-rating/product-rating.module';

@NgModule({
  declarations: [ProductCardComponent],
  imports: [
    CommonModule,
    ProductRatingModule
  ],
  exports: [ProductCardComponent]
})
export class ProductCardModule { }
