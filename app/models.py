from django.db import models

class UF(models.Model):
    nome = models.CharField(max_length=2)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    

class Bairro(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    

class tipoLogradouro(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Logradouro(models.Model):
    tipo = models.ForeignKey(tipoLogradouro, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    

class tipoPessoas(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Pessoas(models.Model):
    tipo = models.ForeignKey(tipoPessoas, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=10)
    dataNascimento = models.DateField()
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    logradouro = models.ForeignKey(Logradouro, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    

class Locador(models.Model):
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    creci = models.CharField(max_length=10)

    def __str__(self):
        return self.pessoa.nome
    

class Locatario(models.Model):
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome
    
class Usuario(models.Model):
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    login = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.pessoa.nome
    

class Avalista(models.Model):
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome
    

class tipoImovel(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Imovel(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey(tipoImovel, on_delete=models.CASCADE)
    logradouro = models.ForeignKey(Logradouro, on_delete=models.CASCADE)
    descricao = models.TextField()
    valorAluguel = models.DecimalField(max_digits=10, decimal_places=2)
    valorVenda = models.DecimalField(max_digits=10, decimal_places=2)
    situacao = models.BooleanField()

    def __str__(self):
        return self.descricao
    

class ContratoAluguel(models.Model):
    locador = models.ForeignKey(Locador, on_delete=models.CASCADE)
    locatario = models.ForeignKey(Locatario, on_delete=models.CASCADE)
    avalista = models.ForeignKey(Avalista, on_delete=models.CASCADE)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    dataInicio = models.DateField()
    dataFim = models.DateField()
    valorAluguel = models.DecimalField(max_digits=10, decimal_places=2)
    situacao = models.BooleanField()

    def __str__(self):
        return self.imovel.descricao
    

class ContratoVenda(models.Model):
    vendedor = models.ForeignKey(Locador, on_delete=models.CASCADE)
    comprador = models.ForeignKey(Locatario, on_delete=models.CASCADE)
    avalista = models.ForeignKey(Avalista, on_delete=models.CASCADE)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    dataVenda = models.DateField()
    valorVenda = models.DecimalField(max_digits=10, decimal_places=2),
    parcelado = models.BooleanField()
    qtdParcelas = models.IntegerField()
    situacao = models.BooleanField()

    def __str__(self):
        return self.imovel.descricao


class Pagamento(models.Model):
    contrato = models.ForeignKey(ContratoAluguel, on_delete=models.CASCADE)
    dataPagamento = models.DateField()
    valorPago = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.contrato.imovel.descricao