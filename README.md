# 🛒 Web Scraping - Análise de Produtos de E-commerce

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scrapy](https://img.shields.io/badge/Scrapy-2.11+-green.svg)
![Power BI](https://img.shields.io/badge/Power_BI-DAX-orange.svg)

Um projeto completo de web scraping e análise de dados para extração e processamento de informações de produtos de um e-commerce.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido para coletar, processar e analisar dados de produtos de uma loja online fictícia (web-scraping.dev). O objetivo era criar um pipeline completo de dados, desde a extração via web scraping até a análise visual no Power BI.

### 🎯 Objetivos
- Extrair dados estruturados de produtos de e-commerce
- Implementar paginação automática para coletar todos os produtos
- Processar e limpar os dados para análise
- Criar métricas e indicadores de negócio
- Visualizar insights através de dashboard

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** - Linguagem principal
- **Scrapy** - Framework para web scraping
- **Power BI** - Visualização e análise de dados
- **DAX** - Linguagem para fórmulas no Power BI
- **Pandas** - Manipulação de dados (opcional)

## 📁 Estrutura do Projeto

```
ecommerce-scraper/
│
├── spiders/
│   └── shop_spider.py          # Spider principal do Scrapy
│
├── output/
│   ├── produtos.json           # Dados extraídos em JSON
│   └── produtos.csv            # Dados extraídos em CSV
│
├── powerbi/
│   ├── dashboard.pbix          # Arquivo do Power BI
│   └── medidas_dax.txt         # Fórmulas DAX utilizadas
│
└── README.md                   # Documentação
```

## 🚀 Como Executar

### 1. Instalação das Dependências
```bash
pip install scrapy pandas
```

### 2. Executar o Spider
```bash
# Extrair dados para JSON
scrapy crawl E_shop_spider -o produtos.json

# Extrair dados para CSV
scrapy crawl E_shop_spider -o produtos.csv
```

### 3. Configuração do Power BI
1. Importar o arquivo `produtos.json` ou `produtos.csv` no Power BI
2. Aplicar as fórmulas DAX da seção abaixo
3. Criar visualizações conforme necessário

## 🔍 O Que Foi Coletado

Para cada produto, foram extraídas as seguintes informações:

| Campo | Descrição | Exemplo |
|-------|-----------|---------|
| `name` | Nome do produto | "Box of Chocolate Candy" |
| `price` | Preço | 24.99 |
| `description` | Descrição curta | "Indulge your sweet tooth..." |
| `image` | URL da imagem | `https://web-scraping.dev/...` |
| `link` | Link para página do produto | `https://web-scraping.dev/product/1` |

## 📊 Métricas e Indicadores (DAX)

### Métricas Principais Implementadas

```dax
// Contagem de produtos por categoria
Total Poções = CALCULATE(COUNTROWS(produtos), CONTAINSSTRING(produtos[Name], "Potion"))
Total Não Poções = CALCULATE(COUNTROWS(produtos), NOT CONTAINSSTRING(produtos[Name], "Potion"))

// Valores médios
Preço Médio Loja = AVERAGE(produtos[price])
Preço Médio Poções = CALCULATE(AVERAGE(produtos[price]), CONTAINSSTRING(produtos[Name], "Potion"))

// Produtos específicos
Quantidade Cat Ear Beanie = CALCULATE(COUNTROWS(produtos), produtos[Name] = "Cat Ear Beanie")
Preço Chocolate Candy = CALCULATE(VALUES(produtos[price]), produtos[Name] = "Box of Chocolate Candy")

// Soma total
Soma Total Loja = SUM(produtos[price])
```

### Filtros por Categoria
- **Poções**: Produtos que contêm "Potion" no nome
- **Calçados**: Produtos que contêm "Shoe", "Sneaker", "Boot"
- **Doces**: Produtos específicos como "Box of Chocolate Candy"

## 🎯 Insights Obtidos

### Descobertas Principais
1. **Distribuição de Produtos**: Identificação da proporção entre poções e outros produtos
2. **Faixa de Preços**: Análise da variação de preços na loja
3. **Produtos Únicos**: Detecção de itens com características especiais
4. **Categorização Automática**: Classificação de produtos por tipo baseado no nome

### Dashboard Recomendado
- **Cards**: Total de produtos, valor total da loja, preço médio
- **Gráfico de Pizza**: Distribuição poções vs não-poções
- **Tabela**: Lista completa de produtos com preços
- **Filtros**: Por categoria, faixa de preço, tipo de produto

## 🧠 Desafios e Aprendizados

### 🎯 Desafios Enfrentados

1. **Paginação Dinâmica**
   - Problema: O spider coletava apenas a primeira página
   - Solução: Implementação de lógica para seguir links de paginação automaticamente
   - Código: Detecção do botão ">" usando `:contains(">")`

2. **Tratamento de Dados**
   - Problema: Preços sendo interpretados como texto no Power BI
   - Solução: Conversão para `float` no Scrapy e uso de `VALUE()` no DAX
   - Aprendizado: Importância da tipagem correta desde a extração

3. **Seletores CSS**
   - Problema: Classes com nomes similares (`product` vs `products`)
   - Solução: Uso do Scrapy Shell para testar seletores
   - Aprendizado: `div.row.product` vs `div.row.products`

4. **Fórmulas DAX**
   - Problema: Confusão entre `COUNTROWS` e `DISTINCTCOUNT`
   - Solução: Estudo da documentação e testes práticos
   - Aprendizado: `COUNTROWS` conta linhas, `DISTINCTCOUNT` conta valores únicos

### 💡 Lições Aprendidas

1. **Validação Contínua**
   - Testar seletores no Scrapy Shell antes de implementar
   - Verificar dados intermediários durante o processamento

2. **Documentação é Fundamental**
   - Manter registro das fórmulas DAX utilizadas
   - Comentar o código para futuras manutenções

3. **Pensamento em Pipeline**
   - Considerar desde a extração até a visualização
   - Estruturar dados pensando na análise final

4. **Resiliência com Erros**
   - Erros de sintaxe são comuns (ex: `callbck` vs `callback`)
   - Paciência para depuração passo a passo

## 🔄 Fluxo de Trabalho Desenvolvido

```
Coleta (Scrapy) → Limpeza (Python) → Armazenamento (JSON/CSV) → 
Análise (Power BI) → Visualização (Dashboard) → Insights
```

## 📈 Próximos Passos

### Melhorias Potenciais
1. **Automação Completa**
   - Script para executar scraping periodicamente
   - Integração com banco de dados

2. **Análises Avançadas**
   - Segmentação por faixa de preço
   - Análise de sentimentos nas descrições
   - Recomendação de preços

3. **Dashboard Interativo**
   - Filtros dinâmicos por múltiplas categorias
   - Comparativo temporal (se houver histórico)
   - Exportação de relatórios

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Reportar bugs ou problemas
2. Sugerir novas funcionalidades
3. Enviar pull requests com melhorias



**Desenvolvido com ❤️ para fins educacionais e de aprendizado em web scraping e análise de dados.**

---
*Última atualização: Dezembro 2024*
