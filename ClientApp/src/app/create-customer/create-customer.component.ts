import { Component, OnInit } from '@angular/core';
import { Customer } from '../customer';
import { CustomerService } from '../customer.service';

@Component({
  selector: 'create-customer',
  templateUrl: './create-customer.component.html',
  styleUrls: ['./create-customer.component.css']
})
export class CreateCustomerComponent implements OnInit {

  customer: Customer = new Customer();
  submitted = false;

  constructor(private customerService: CustomerService) { }

  ngOnInit(): void {
  }

  createNewCustomer() {
    this.submitted = false;
    this.customer = new Customer();
  }

  saveNewCustomer() {
    this.customerService.createCustomer(this.customer)
      .subscribe(data => {
        console.log(data);
        this.submitted = true;
      },
      error => console.log(error));
    
      this.customer = new Customer();
  }

  onSubmit() {
    this.saveNewCustomer();
  }

}
