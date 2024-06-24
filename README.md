**Índice**
================

* [Introdução](#introdução)
* [Requisitos](#requisitos)
* [Instalação](#instalação)
* [Gráficos](#gráficos)
* [Contribuições](#contribuições)


**Introdução**
===============

Este projeto tem como objetivo gerar gráficos de abundância total, abundância por trilha, temperatura, umidade e precipitação, bem como um gráfico que junta todas essas informações. O projeto foi desenvolvido em Python na versão 3.12.3. Os requisitos para rodar os códigos, bem como os gráficos que o mesmo gera podem ser encontrados nas seções abaixo.


**Requisitos**
==============

* Lista de requisitos necessários para executar este projeto:
   * Python 3.12 ou versão superior.
   * As seguintes bibliotecas:
       * pandas
       * matplotlib
       * matplotlib.pyplot
       * matplotlib.ticker


**Instalação**
==============

Para instalar os requisitos apresentados anteriormente, será necessário utilizar o gerenciador de pacotes pip.

```python
pip install pandas
pip install matplotlib
pip install matplotlib.pyplot
pip install numpy
```

* Em seguida, faça download de todos os arquivos.
* Adapte o diretório dos arquivos .csv para o código
* Execute o código


**Gráficos**
============

* Com os códigos fornecidos acima, podemos gerar 4 gráficos para a análise dos dados presentes nos arquivos .csv
* O arquivo "TCC - Fig 3 (Abund Total).py" gera um gráfico de abundância total de todas as famílias com uma escala do eixo y em formato logarítmico para facilitar a visualização devido à alta diferença total dos valores analisados.

![TCC - Fig 3 (Abund Total)](https://github.com/Glei19/TCC-DIPTERA-BRACHYCERA/assets/84149863/27e652ba-76c0-48b1-95a4-cdca78051bae)


* O arquivo "TCC - Fig 4 (Abund - Trilha).py gera um gráfico de abundância total de cada família encontrada na respectiva trilha, o mesmo está em escala logarítimica para facilitar a visualização. 

![TCC - Fig 4 (Abund - Trilha)](https://github.com/Glei19/TCC-DIPTERA-BRACHYCERA/assets/84149863/84a1a9cb-4386-4167-a094-187e68e8977d)


* O arquivo "TCC - Fig 5 (Clima + Abund1).py" gera um gráfico de abundância das famílias "Anthomyiidae, Calliphoridae e Fanniidae" coletadas ao longo dos meses em comparação com as variações dos fatores climáticos.


![TCC - Fig 5 (Clima + Abund1)](https://github.com/Glei19/TCC-DIPTERA-BRACHYCERA/assets/84149863/a87fea0f-272c-42a9-9cbb-f7d9ba501b42)


* O arquivo "TCC - Fig 6  (Clima + Abund2 Log).py" gera um gráfico de abundância das famílias "Mesembrinellidae, Muscidae e Sarcophagidae" coletadas ao longo dos meses em comparação com as variações dos fatores climáticos, o gráfico apresenta escala logarítmica para facilitar a visualização devido à alta diferença nos valores de abundância.


![TCC - Fig 6  (Clima + Abund2 Log)](https://github.com/Glei19/TCC-DIPTERA-BRACHYCERA/assets/84149863/c393db97-86c7-4bd9-b3f2-302d4f79fdcd)


**Contribuições**
================

Contribuições para este projeto são bem-vindas. Para contribuir, basta enviar um pull request no repositório deste projeto.
