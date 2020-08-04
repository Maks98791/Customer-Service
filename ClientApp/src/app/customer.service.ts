import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Customer } from './customer';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class CustomerService {

  private baseUrl = 'http://localhost:8000/api/customers/';

  constructor(private http: HttpClient) { }

  getCutomer(id: number): Observable<object> {
    var url = this.baseUrl + id;
    return this.http.get(url);
  }

  getCustomerByAge(age: number): Observable<any> {
    var url = this.baseUrl + 'age/' + age;
    return this.http.get(url);
  }

  getAllCustomers(): Observable<any> {
    return this.http.get(this.baseUrl);
  }

  createCustomer(customer: Object): Observable<object> {
    return this.http.post(this.baseUrl, customer);
  } 

  updateCustomer(id: number, value: any): Observable<object> {
    var url = this.baseUrl + id;
    return this.http.put(url, value);
  }

  deleteCustomer(id: number): Observable<any> {
    var url = this.baseUrl + id;
    return this.http.delete(url);
  }

  deleteAllCustomers(): Observable<any> {
    return this.http.delete(this.baseUrl);
  }
}
