import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {QUOTE_MODULE_DECLARATIONS, QuoteRoutingModule} from  './Quote-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    QuoteRoutingModule
  ],
  declarations: QUOTE_MODULE_DECLARATIONS,
  exports: QUOTE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class QuoteModule { }