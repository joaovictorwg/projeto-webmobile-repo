import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Produtos } from './produtos.model';
import { Usuario } from '../home/usuario.model';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { IonicModule, LoadingController, NavController, ToastController } from '@ionic/angular';
import { Storage } from '@ionic/storage-angular';

@Component({
  selector: 'app-produtos',
  templateUrl: './produtos.page.html',
  styleUrls: ['./produtos.page.scss'],
  standalone: false,
  providers: [HttpClient, Storage]
})
export class ProdutosPage implements OnInit {

  public usuario: Usuario = new Usuario();
  public lista_produtos: Produtos[] = [];
  public produtoEdicao: Produtos = this.criarProdutoVazio();

  constructor(
    public http: HttpClient,
    public storage: Storage,
    public controle_toast: ToastController,
    public controle_navegacao: NavController,
    public controle_carregamento: LoadingController
  ) { }

  async ngOnInit() {
    // Verifica se existe registro de configuração para o usuário
    await this.storage.create();
    const registro = await this.storage.get('usuario');

    if (registro) {
      this.usuario = Object.assign(new Usuario(), registro);
      this.consultarProdutosSistemaWeb();
    } else {
      this.controle_navegacao.navigateRoot('/home');
    }
  }

  criarProdutoVazio(): Produtos {
    return new Produtos(); // Cria um objeto de produto vazio
  }

  async consultarProdutosSistemaWeb() {
    const loading = await this.controle_carregamento.create({ message: 'Pesquisando...', duration: 60000 });
    await loading.present();

    const http_headers: HttpHeaders = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Token ${this.usuario.token}`
    });

    this.http.get('http://127.0.0.1:8000/produtos/api/', { headers: http_headers })
      .subscribe({
        next: async (resposta: any) => {
          this.lista_produtos = resposta;
          loading.dismiss();
        },
        error: async (erro: any) => {
          loading.dismiss();
          const mensagem = await this.controle_toast.create({
            message: `Falha ao consultar produtos: ${erro.message}`,
            cssClass: 'ion-text-center',
            duration: 2000
          });
          mensagem.present();
        }
      });
  }

  async excluirProdutos(id: number) {
    const loading = await this.controle_carregamento.create({ message: 'Excluindo...', duration: 30000 });
    await loading.present();

    const http_headers: HttpHeaders = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Token ${this.usuario.token}`
    });

    this.http.delete(`http://127.0.0.1:8000/produtos/api/delete/${id}/`, { headers: http_headers })
      .subscribe({
        next: async () => {
          this.consultarProdutosSistemaWeb();
          loading.dismiss();
          const mensagem = await this.controle_toast.create({
            message: 'Produto excluído com sucesso!',
            cssClass: 'ion-text-center',
            duration: 2000
          });
          mensagem.present();
        },
        error: async (erro: any) => {
          loading.dismiss();
          const mensagem = await this.controle_toast.create({
            message: `Falha ao excluir o produto: ${erro.message || 'Erro desconhecido'}`,
            cssClass: 'ion-text-center',
            duration: 2000
          });
          mensagem.present();
        }
      });
  }

  // Função para navegar para a página de descrição
  abrirPaginaDescricao(produto: Produtos) {
    this.controle_navegacao.navigateForward('/produto-descricao', {
      queryParams: { produto: JSON.stringify(produto) }
    });
  }

  // Função para navegar para a página de edição

  navegarParaEdicao(produto: Produtos) {
    this.controle_navegacao.navigateForward('/produto-edicao', {
      queryParams: { produto: JSON.stringify(produto) }
    });
  }
  
}
