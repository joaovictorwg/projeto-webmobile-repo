import { Usuario } from './usuario.model';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Storage } from '@ionic/storage-angular';
import { AlertController, IonicModule, NavController, ToastController, LoadingController } from '@ionic/angular';
import { HttpHeaders, HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
  standalone: true,
  imports: [IonicModule, CommonModule, FormsModule, HttpClientModule],
  providers: [HttpClient, Storage]
})
export class HomePage implements OnInit {
  constructor(
    public controle_carregamento: LoadingController,
    public controle_navegacao: NavController,
    public controle_alerta: AlertController,
    public controle_toast: ToastController,
    public http: HttpClient, 
    public storage: Storage,
  ) {}

  async ngOnInit(){
    await this.storage.create()
  }

  public instancia: { username: string, password: string } = {
    username: '',
    password: ''
  };

  async autenticarUsuario() {

    // Inicializa interface com efeito de carregamento
 
    const loading = await this.controle_carregamento.create({message: 'Autenticando...', duration: 15000});
    await loading.present();

    let http_headers: HttpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    // Autentica usuário junto ca API do sistema web
    this.http.post(
      'http://127.0.0.1:8000/autenticacao-api/',
      this.instancia,
      {
        headers: http_headers
      }
    ).subscribe({
      next: async (resposta: any) =>{
        let usuario: Usuario = Object.assign(new Usuario(), resposta)
        await this.storage.set('usuario', usuario)

        loading.dismiss()
        this.controle_navegacao.navigateRoot('/produtos')

      },
      error: async (erro: any) => {
         loading.dismiss();
         const mensagem = await this.controle_toast.create({
          message: `Falha ao autenticar usuário: ${erro.message}`,
          cssClass: 'ion-text-center',
          duration: 2000
         });
         mensagem.present();
      }
    });
    
  }

}