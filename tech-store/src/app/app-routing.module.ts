import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProdutoCriacaoPage } from './produto-criacao/produto-criacao.page';

export const routes: Routes = [
  {
    path: 'home',
    loadComponent: () => import('./home/home.page').then((m) => m.HomePage),
  },
  {
    path: '',
    redirectTo: 'produtos',
    pathMatch: 'full',
  },
  {
    path: 'produtos',
    loadChildren: () => import('./produtos/produtos.module').then((m) => m.ProdutosPageModule),
  },
  {
    path: 'anuncios',
    loadComponent: () => import('./anuncios/anuncios.page').then((m) => m.AnunciosPage),
  },
  {
    path: 'criar-produto',
    component: ProdutoCriacaoPage
  },
 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
