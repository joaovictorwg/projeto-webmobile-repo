import { Component } from '@angular/core';
import { ModalController } from '@ionic/angular';

// Defina uma interface para o tipo de produto
interface Produto {
  id: number;
  titulo: string;
  categoria: string;
  foto: string;
}

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent {
  usuario = { nome: 'João' }; // Exemplo de usuário, pode vir de um serviço ou API
  lista_produtos: Produto[] = [
    // Exemplo de lista de produtos com uma foto codificada em base64
    { id: 1, titulo: 'Produto 1', categoria: 'Categoria 1', foto: '...' },
    { id: 2, titulo: 'Produto 2', categoria: 'Categoria 2', foto: '' }
  ];

  constructor(private modalController: ModalController) {}



  // Função para excluir um produto da lista (exemplo)
  excluirProdutos(produtoId: number) {
    console.log('Excluir produto com id:', produtoId);
    // Adicione aqui a lógica para excluir o produto da lista ou do banco de dados
  }
}
