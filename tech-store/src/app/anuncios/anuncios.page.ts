import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Anuncio } from './anuncios.model';  // Modelo de Anúncio
import { Usuario } from '../home/usuario.model';  // Modelo de Usuário
import { HttpClient, HttpClientModule, HttpHeaders } from '@angular/common/http';
import { IonicModule, LoadingController, NavController, ToastController } from '@ionic/angular';
import { Storage } from '@ionic/storage-angular';

@Component({
  selector: 'app-anuncios',
  templateUrl: './anuncios.page.html',
  styleUrls: ['./anuncios.page.scss'],
  standalone: true,
  imports: [IonicModule, CommonModule, HttpClientModule],
  providers: [HttpClient, Storage]
})
export class AnunciosPage implements OnInit {

  public usuario: Usuario = new Usuario();
  public lista_anuncios: Anuncio[] = [];  // Lista de Anúncios

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
      this.consultarAnunciosSistemaWeb();
    } else {
      this.controle_navegacao.navigateRoot('/home');
    }
  }

  // Função para consultar anúncios
  async consultarAnunciosSistemaWeb() {
    // Inicializar interface com efeito de carregamento
    const loading = await this.controle_carregamento.create({ message: 'Pesquisando anúncios...', duration: 60000 });
    await loading.present();

    let http_headers: HttpHeaders = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Token ${this.usuario.token}`
    });

    // Requisita a lista de anúncios para a API do sistema
    this.http.get(
      'http://127.0.0.1:8000/anuncios/api/', // Ajuste o endpoint para a API de anúncios
      {
        headers: http_headers
      }
    ).subscribe({
      next: async (resposta: any) => {
        this.lista_anuncios = resposta;

        // Finaliza interface com efeito de carregamento
        loading.dismiss();
      },
      error: async (erro: any) => {
        loading.dismiss();
        const mensagem = await this.controle_toast.create({
          message: `Falha ao consultar anúncios: ${erro.message}`,
          cssClass: 'ion-text-center',
          duration: 2000
        });
        mensagem.present();
      }
    });
  }

  // Função para excluir anúncio
  async excluirAnuncio(id: number) {
    // Inicializa interface com efeito de carregamento
    const loading = await this.controle_carregamento.create({ message: 'Excluindo anúncio...', duration: 30000 });
    await loading.present();

    let http_headers: HttpHeaders = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Token ${this.usuario.token}`
    });

    // Requisição para excluir o anúncio
    this.http.delete(
      `http://127.0.0.1:8000/anuncios/api/${id}/`,  // Ajuste o endpoint para a API de excluir anúncio
      {
        headers: http_headers
      }
    ).subscribe({
      next: async () => {
        // Atualiza a lista de anúncios após a exclusão
        this.consultarAnunciosSistemaWeb();

        // Finaliza interface com efeito de carregamento
        loading.dismiss();
      },
      error: async (erro: any) => {
        loading.dismiss();
        const mensagem = await this.controle_toast.create({
          message: `Falha ao excluir o anúncio: ${erro.message}`,
          cssClass: 'ion-text-center',
          duration: 2000
        });
        mensagem.present();
      }
    });
  }
}
