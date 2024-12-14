import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { IProduct } from 'src/app/models/product.model';

@Component({
  selector: 'app-product-card-list',
  templateUrl: './product-card-list.component.html',
  styleUrls: ['./product-card-list.component.scss']
})
export class ProductCardListComponent implements OnInit {
  @Input() products!: IProduct[];
  @Input() isLoading!: boolean;
  @Output() loadMoreEmitter = new EventEmitter();

  constructor() { }

  onLoadMoreProducts() {
    this.loadMoreEmitter.emit();
  }

  ngOnInit(): void {}
}
