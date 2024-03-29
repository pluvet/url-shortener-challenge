import { OnInit, Component, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatDialog } from '@angular/material/dialog';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from '../service/auth.service';
import { AddUrlModalComponent } from '../add-url-modal/add-url-modal.component';


@Component({
  selector: 'app-url',
  templateUrl: './url.component.html',
  styleUrls: ['./url.component.css']
})
export class UrlComponent implements OnInit {

  constructor(private service: AuthService,private toastr:ToastrService,private router: Router, public dialog: MatDialog) {
  }
  urlList: any;
  dataSource: any;
  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  ngOnInit(): void {
    this.LoadUrl();
  }

  LoadUrl() {
    this.service.GetAllUrl().subscribe(res => {
      if (!res) {
        return;
      }
      this.urlList = res;
      this.dataSource = new MatTableDataSource(this.urlList.urls);
      this.dataSource.paginator = this.paginator;
      this.dataSource.sort = this.sort;
    });
  }
  displayedColumns: string[] = ['key', 'long_url', 'short_url', 'visits'];

  addUrl() {
    const dialogRef = this.dialog.open(AddUrlModalComponent, {
      width: '450px'
    });

    dialogRef.afterClosed().subscribe(() => {
      this.LoadUrl();
    });
    
  }


}
