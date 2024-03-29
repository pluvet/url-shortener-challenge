import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UrlComponent } from './url/url.component';
import { AuthGuard } from './guard/auth.guard';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { RedirectComponent } from './redirect/redirect.component';

const routes: Routes = [
  {path: '',redirectTo: 'home',pathMatch: 'full'},
  {component:LoginComponent,path:'login'},
  {component:RegisterComponent,path:'register'},
  {component:HomeComponent,path:'home',canActivate:[AuthGuard]},
  {component:UrlComponent,path:'url',canActivate:[AuthGuard]},
  {component:RedirectComponent,path:':key'},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
