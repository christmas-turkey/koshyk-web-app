import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-product-categories',
  templateUrl: './product-categories.component.html',
  styleUrls: ['./product-categories.component.scss']
})
export class ProductCategoriesComponent implements OnInit {
  @Input() categories: string[] = [];
  @Output() categoryEmitter = new EventEmitter<string | null>();

  selectedCategory: string | null = null;

  constructor() { }

  ngOnInit(): void {}

  onSelectCategory(category: string) {
    if (this.selectedCategory === category) {
      this.selectedCategory = null;
    } else {
      this.selectedCategory = category
    }
    this.categoryEmitter.emit(this.selectedCategory);
  }
}
