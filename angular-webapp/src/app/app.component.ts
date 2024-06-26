import { Component,DoCheck } from '@angular/core';
import { ActivatedRoute, Route, Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements DoCheck {
  title = 'authentication';
  isadmin=false;
  isMenuVisible=false;
  constructor(private route:Router){
  }
  ngDoCheck(): void {
    let currentroute = this.route.url;
    if (currentroute == '/home' || currentroute == '/url') {
      this.isMenuVisible = true
    } else {
      this.isMenuVisible = false
    }
  }
}
