import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { QuoteCategoryHomeComponent } from './home/QuoteCategory-home.component';
import { QuoteCategoryNewComponent } from './new/QuoteCategory-new.component';
import { QuoteCategoryDetailComponent } from './detail/QuoteCategory-detail.component';

const routes: Routes = [
  {path: '', component: QuoteCategoryHomeComponent},
  { path: 'new', component: QuoteCategoryNewComponent },
  { path: ':id', component: QuoteCategoryDetailComponent,
    data: {
      oPermission: {
        permissionId: 'QuoteCategory-detail-permissions'
      }
    }
  }
];

export const QUOTECATEGORY_MODULE_DECLARATIONS = [
    QuoteCategoryHomeComponent,
    QuoteCategoryNewComponent,
    QuoteCategoryDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class QuoteCategoryRoutingModule { }