import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { HttpHeaders } from '@angular/common/http';
import { Observable, catchError, retry} from 'rxjs';
import { RedirectResponse } from '../model/url';

export interface HeadersObject {
  headers: HttpHeaders;
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http:HttpClient) { 

  }
  apiurl='http://localhost:8620/users';

  RegisterUser(inputdata:any){
    return this.http.post(this.apiurl + '/register',inputdata)
  }
  Login(inputdata:any){
    return this.http.post(this.apiurl + '/login',inputdata)
  }
  isloggedin(){
    return sessionStorage.getItem('token')!=null;
  }
  getAuthenticatedHeaders(httpAccept: string = 'application/json'): HeadersObject {
    const token = sessionStorage.getItem('token')
    return {
        headers: new HttpHeaders({ Authorization: `Bearer ${token}`, accept: httpAccept })
    };
  }
  GetAllUrl(){
    return this.http.get('http://localhost:8650/urls', this.getAuthenticatedHeaders());
  }

  Redirect(key:string): Observable<RedirectResponse>{
    const urlApi = 'http://localhost:8650/urls/redirect/'+key
    return this.http
    .get<RedirectResponse>(urlApi)
    .pipe(
      retry(1)
    )
  }

  CreateUrl(inputdata:any){
    return this.http.post('http://localhost:8650/urls', inputdata,this.getAuthenticatedHeaders());
  }
}
