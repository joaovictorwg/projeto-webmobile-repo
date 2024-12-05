export class Produtos {
    public id: number; 
    public titulo: string; 
    public descricao: string; 
    public estado: number; 
    public estado_display?: string; 
    public categoria: number; 
    public categoria_display?: string; 
    public foto?: string; 
  
    constructor() {
      this.id = 0;
      this.titulo = '';
      this.descricao = '';
      this.estado = 0;
      this.estado_display = '';
      this.categoria = 0;
      this.categoria_display = '';
      this.foto = undefined;
    }
  }
  