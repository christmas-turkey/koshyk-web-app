import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-product-rating',
  templateUrl: './product-rating.component.html',
  styleUrls: ['./product-rating.component.scss']
})
export class ProductRatingComponent implements OnInit {
  @Input() rating!: number;

  constructor() {}

  ngOnInit(): void {}
}
