export class Anuncio {
  public id: number;
  public data: string; // Data de criação do anúncio
  public titulo: string;
  public descricao: string; // Descrição do anúncio
  public preco: number; // Preço do produto anunciado
  public usuario: number; // ID do usuário responsável pelo anúncio
  public produtoId: number; // ID do produto relacionado ao anúncio
  public produtoTitulo?: string; // Título do produto (pode ser opcional)
  public produtoDescricao?: string; // Descrição do produto (pode ser opcional)
  public foto?: string; // URL ou caminho da foto do produto (opcional)

  constructor() {
    this.id = 0;
    this.data = '';
    this.descricao = '';
    this.preco = 0;
    this.usuario = 0;
    this.produtoId = 0;
    this.produtoTitulo = '';
    this.produtoDescricao = '';
    this.foto = undefined;
    this.titulo = '';
  }
}
