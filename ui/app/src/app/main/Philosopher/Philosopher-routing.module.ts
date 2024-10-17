import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PhilosopherHomeComponent } from './home/Philosopher-home.component';
import { PhilosopherNewComponent } from './new/Philosopher-new.component';
import { PhilosopherDetailComponent } from './detail/Philosopher-detail.component';

const routes: Routes = [
  {path: '', component: PhilosopherHomeComponent},
  { path: 'new', component: PhilosopherNewComponent },
  { path: ':id', component: PhilosopherDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Philosopher-detail-permissions'
      }
    }
  },{
    path: ':philosopher_id/Quote', loadChildren: () => import('../Quote/Quote.module').then(m => m.QuoteModule),
    data: {
        oPermission: {
            permissionId: 'Quote-detail-permissions'
        }
    }
}
];

export const PHILOSOPHER_MODULE_DECLARATIONS = [
    PhilosopherHomeComponent,
    PhilosopherNewComponent,
    PhilosopherDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PhilosopherRoutingModule { }