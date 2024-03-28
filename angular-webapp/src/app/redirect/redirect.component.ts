import { OnInit, Component, ViewChild, inject } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { DOCUMENT } from '@angular/common';
import { AuthService } from '../service/auth.service';
import { RedirectResponse } from '../model/url';
@Component({
  selector: 'app-redirect',
  templateUrl: './redirect.component.html',
  styleUrls: ['./redirect.component.css']
})
export class RedirectComponent implements OnInit {

  key: string | null;

  constructor(
    private service: AuthService, 
    public activatedRoute: ActivatedRoute,
  ){}


  ngOnInit(): void {
    this.key = this.activatedRoute.snapshot.paramMap.get('key');
    this.redirect();
  }

  redirect() {
    if (this.key != null) {
      this.service.Redirect(this.key).subscribe((redirectResponse: RedirectResponse) => {
        window.location.href = redirectResponse.long_url;
      })
    }
  }
}
