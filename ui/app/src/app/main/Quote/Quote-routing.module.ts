import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { QuoteHomeComponent } from './home/Quote-home.component';
import { QuoteNewComponent } from './new/Quote-new.component';
import { QuoteDetailComponent } from './detail/Quote-detail.component';

const routes: Routes = [
  {path: '', component: QuoteHomeComponent},
  { path: 'new', component: QuoteNewComponent },
  { path: ':id', component: QuoteDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Quote-detail-permissions'
      }
    }
  },{
    path: ':quote_id/QuoteCategory', loadChildren: () => import('../QuoteCategory/QuoteCategory.module').then(m => m.QuoteCategoryModule),
    data: {
        oPermission: {
            permissionId: 'QuoteCategory-detail-permissions'
        }
    }
}
];

export const QUOTE_MODULE_DECLARATIONS = [
    QuoteHomeComponent,
    QuoteNewComponent,
    QuoteDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class QuoteRoutingModule { }