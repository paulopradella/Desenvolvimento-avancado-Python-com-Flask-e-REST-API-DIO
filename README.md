# Desenvolvimento-avançado-Python-com-Flask-e-REST-API
Introdução ao REST API com Flask:

Requisitos Básicos:
Windows, Linux ou OSX
Lógica de programação
Possuir fundamentos em Python

Agenda:
O que é uma API:
É um conjunto de rotinas para acesso a um aplicativo/ software/ plataforma baseado na Web
Acrônimo de Application Programming Interface - Interface e programação de aplicativos
APIs são importantes quando se tem a intenção de realizar integrações com outros serviços
Com as APIs são importantes quando se tem intenção de realizar integrações com outros serviços
Com as APIs a comunidade de software fica transparente ao usuário
APIs podem ser locais, baseada e web e baseada em programas

O que é REST:
É um modelo a ser utilizado para projetar arquiteturas de software baseado em comunicação via rede
Acrônimo de Representational State Transfer - Transferencia de Estado Representacional
Foi definido por Roy Fielding em sua tese de doutorado (PhD) na UC Irvine no ano 2000
REST projeta a ideia de que todo recurso deveria responder aos mesma métodos.

O que é REST API:
É uma API desenvolvida utilizando os princípios da arquitetura REST
Um REST API e utilizado na comunicação/ integração entre software através de serviços web
Um REST AP é consumido através e requisição TTP
REST API são geralmente representados em seus formatos por JSON e XML. Também são usados paginas HTML, PDF e arquivos de imagens
Ao implementar um REST PI cada método deve ser responsável por um tipo diferente de ano. Exemplo: Consulta, Alteração, Inclusão e Exclusão.

Métodos do protocolo HTTP:
GET - Método que solicita algum recurso ou objeto do servidor por meio da URI.
POST - Método usado para envio de arquivo/dados ou formulário HTML para o servidor
PUT - Aceitar criar ou modificar um objeto do servidor
DELETE - Informa por meio da URI o objeto a ser deletado
Existem outros…

URL, URN e URI:
URL: Uniform Resource Locator - Localizador de Recurso Universal
Host que será acessado. Exemplo: globallabs.academy
URN: Uniform Rosource Name - Nome do Recurso Universal
É o recurso que será identificado. Exemplo: /category/blog/
URI: Unform Resource Identifier - Identificador de Recurso Universal
É o identificador do recurso, podendo ser uma imagem, um arquivo ou uma página. Exemplo: https://globallabs.academy/categoryblog/
URI une Protocolo (https://), URL(globallabs.academy) e a URN (/category/blog)

XML e JSON:
XML - Extensible Markup Language:
É uma linguagem de marcação
Utilizada para compatilhamentode informações através de requisições HTTP

JSON - JavaScript Object Notation (Será a usada no curso)
É um formato de troca de dados entre sistemas independente da linguagem utilizada derivado do JavaScript
Muitas linguagens possuem suporte nativo a JSON 


Framework Flask:
É um microframework para Python utilizado para desenvolvimento de aplicações WEB
É chamado de microframework porque ontem um núcleo simples, mas é estendível
Flask não possui camada de abstração para banco de dados, validação de formulários entre outros, mas é possível estender com outras bibliotecas
Por ser leve e simples de usar, Flask é um dos frameworks Python mais utilizados para desenvolvimento de APIs
