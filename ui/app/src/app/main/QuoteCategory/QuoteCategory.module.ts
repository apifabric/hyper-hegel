import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {QUOTECATEGORY_MODULE_DECLARATIONS, QuoteCategoryRoutingModule} from  './QuoteCategory-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    QuoteCategoryRoutingModule
  ],
  declarations: QUOTECATEGORY_MODULE_DECLARATIONS,
  exports: QUOTECATEGORY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class QuoteCategoryModule { }