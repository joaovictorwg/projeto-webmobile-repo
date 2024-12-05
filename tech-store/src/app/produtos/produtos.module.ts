import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProdutosPage } from './produtos.page';  // Importe a página
import { IonicModule } from '@ionic/angular';   // Importe o módulo Ionic se necessário
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { ProdutoCriacaoPage } from '../produto-criacao/produto-criacao.page';


@NgModule({
  imports: [
    CommonModule,
    IonicModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    RouterModule.forChild([  // Use forChild aqui para as rotas deste módulo
      {
        path: '',
        component: ProdutosPage,
      }
    ]),

  ],
  declarations: [ ProdutosPage, ProdutoCriacaoPage ], 
  exports: [ProdutosPage],  // Exporte a página, se necessário
})
export class ProdutosPageModule {}
