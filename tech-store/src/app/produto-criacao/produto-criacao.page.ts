import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { IonicModule, LoadingController, NavController, ToastController } from '@ionic/angular';
import { Storage } from '@ionic/storage-angular';
import { Produtos } from '../produtos/produtos.model';
import { Usuario } from '../home/usuario.model';

@Component({
  selector: 'app-produto-criacao',
  templateUrl: './produto-criacao.page.html',
  styleUrls: ['./produto-criacao.page.scss'],
  standalone: false,
  providers: [HttpClient, Storage]
})
export class ProdutoCriacaoPage implements OnInit {

  public usuario: Usuario = new Usuario();
  public novoProduto: Produtos = this.criarProdutoVazio();

  constructor(
    private http: HttpClient,
    private storage: Storage,
    private controle_toast: ToastController,
    private controle_navegacao: NavController,
    private controle_carregamento: LoadingController
  ) { }

  async ngOnInit() {
    await this.storage.create();
    const registro = await this.storage.get('usuario');

    if (registro) {
      this.usuario = Object.assign(new Usuario(), registro);
    } else {
      this.controle_navegacao.navigateRoot('/home');
    }
  }

  criarProdutoVazio(): Produtos {
    return new Produtos();
  }

  async salvarNovoProduto() {
    const loading = await this.controle_carregamento.create({ message: 'Salvando produto...', duration: 30000 });
    await loading.present();

    const http_headers: HttpHeaders = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Token ${this.usuario.token}`
    });

    this.http.post('http://127.0.0.1:8000/produtos/api/create/', this.novoProduto, { headers: http_headers })
      .subscribe({
        next: async () => {
          loading.dismiss();
          const mensagem = await this.controle_toast.create({
            message: 'Produto criado com sucesso!',
            cssClass: 'ion-text-center',
            duration: 2000
          });
          mensagem.present();
          this.controle_navegacao.navigateRoot('/produtos');
        },
        error: async (erro: any) => {
          loading.dismiss();
          const mensagem = await this.controle_toast.create({
            message: `Falha ao criar produto: ${erro.message || 'Erro desconhecido'}`,
            cssClass: 'ion-text-center',
            duration: 2000
          });
          mensagem.present();
        }
      });
  }
}
