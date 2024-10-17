import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {PHILOSOPHER_MODULE_DECLARATIONS, PhilosopherRoutingModule} from  './Philosopher-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    PhilosopherRoutingModule
  ],
  declarations: PHILOSOPHER_MODULE_DECLARATIONS,
  exports: PHILOSOPHER_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class PhilosopherModule { }