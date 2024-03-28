import { Component, Inject, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms'
import { ToastrService } from 'ngx-toastr';
import { AuthService } from '../service/auth.service';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { Url } from '../model/url';

interface DialogData {
}
@Component({
  selector: 'app-add-url-modal',
  templateUrl: './add-url-modal.component.html',
  styleUrls: ['./add-url-modal.component.scss']
})
export class AddUrlModalComponent implements OnInit {

  constructor(private builder: FormBuilder, private service: AuthService, private toastr: ToastrService,
    private dialogRef: MatDialogRef<AddUrlModalComponent>, @Inject(MAT_DIALOG_DATA) public data: DialogData) {
  }
  ngOnInit(): void {
  }

  urlform = this.builder.group({
    key: this.builder.control(''),
    long_url: this.builder.control(''),
    short_url: this.builder.control(''),
    visits: this.builder.control(''),
  });

  OnSave() {
    const url = this.urlform.getRawValue();
    this.service.CreateUrl(url).subscribe(res => {
      this.toastr.success('Created successfully.');
      this.dialogRef.close();
    });
  }

}
