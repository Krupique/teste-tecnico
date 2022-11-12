### Esse problema tem algumas constraints:

a) Eu preciso conseguir rodar seu código em um Mac OS X OU no Ubuntu;

b) Devemos ser capazes de executar o seu código em uma VM ou máquina limpa com
   os seguintes comandos, ou algo similar:

    git clone seu-repositorio
    cd seu-repositorio
    ./configure (ou algo similar)
    make run (ou algo similar)

c) Devemos também conseguir rodar o seu código no nosso ambiente local;

Esses comandos devem ser o suficiente para configurar uma nova VM e rodar o
seu programa. Considere que o meu usuário não é root, porém tem permissão de
sudo.

**Registre tudo**: testes que forem executados, ideias que gostaria de
implementar se tivesse tempo (explique como você as resolveria, se houvesse
tempo), decisões que forem tomadas e seus porquês, arquiteturas que forem
testadas, os motivos de terem sido modificadas ou abandonadas, instruções de
deploy e instalação, etc. Crie um único arquivo COMMENTS.md ou HISTORY.md no
repositório para isso.

=====================
#### O Problema

O desafio que você deve resolver é o problema da aplicação de Comentários em
versão WEB com HTML/CSS/Javascript + backend usando a linguagem de programação
e ferramentas open source da sua preferência.

A aplicação pode ser incluída em páginas de matérias dos portal da ScaleNews. 
Através dela, os internautas enviam comentários em texto e acompanham o que 
outras pessoas estão falando sobre o assunto em destaque.

Nesse repositório você encontra algumas imagens necessárias para implementação
da parte web que você talvez deseje usar.

============================
#### Regras de negócio

1. O usuário digita o seu email e o texto do comentário e clica em enviar. Seu 
   comentário fica então listado em destaque abaixo da matéria, junto com os 
   20 últimos que foram feitos. Deve ser possível o usuário paginar pelos 
   demais, sem limitação de quantidade.

2. O sistema utiliza o email do usuário para buscar a sua imagem de perfil 
   cadastrada no [Gravatar](http://en.gravatar.com/) e a exibe ao lado do seu
   comentário, uma vez que o mesmo tenha sido enviado com sucesso.

3. Os usuários podem comentar quantas vezes quiserem. Entretanto, o sistema 
   deve impedir que comentários oriundos de ataques maliciosos ou de robôs 
   sejam armazenados. Para não sobrecarregar o usuário com muitas validações, 
   esses casos precisam ser prevenidos com algum mecanismo inteligente que não 
   interfira muito no fluxo de escrita e submissão de um comentário.

4. Como os comentários ficam nas páginas de matérias, é esperada grande 
   quantidade de acessos às mesmas e um volume alto de submissões de 
   comentários concentrados em um curto espaço de tempo, principalmente em 
   eventos como Eleições, Copa do Mundo, etc. Esperamos ter um teste que cubra 
   esse cenário e, por razões práticas, podemos considerar 1000 comentários/seg
   e 200 usuários simultâneos acessando a matéria como baseline de performance.

5. Devemos permitir que os usuários acessem uma página com a listagem das 
   matérias e o número de comentários que cada uma tem. A partir da lista é 
   possível abrir a matéria. Fique atento para que a listagem não fique muito 
   extensa. Esta URL precisa estar documentada em algum lugar do seu projeto.

6. Além disso, os editores e usuários dos nossos portais são exigentes. 
   Portanto a interface do produto é algo bem importante. Organize seu tempo 
   para que esse item também tenha a atenção mínima esperada.

===============================================
#### O que será avaliado na sua solução?

1. Seu código será observado por uma equipe de desenvolvedores que avaliarão a
   implementação do código, simplicidade e clareza da solução, a arquitetura,
   estilo de código, testes unitários, testes funcionais, nível de automação
   dos testes, o design da interface e a documentação.

2. Sua solução será submetida a uma bateria de testes de performance para
   garantir que atende a demanda de uma chamada no Youtube, Instagram, Facebook ou picos de acessos 
   provenientes de acontecimentos de amplo alcance. Fique atento à performance 
   e escalabilidade.

3. A automação da infra-estrutura também é importante. Imagine que você
   precisará fazer deploy do seu código em múltiplos servidores, então não é
   interessante ter que ficar entrando máquina por máquina para fazer o deploy
   da aplicação.

=============
#### Dicas & Recursos

- Use ferramentas e bibliotecas open source, mas documente as decisões e
  porquês;

- Automatize o máximo possível;

- Em caso de dúvidas, pergunte.

- Design do Site (https://www.figma.com/file/g9tVOyvImbBd1wr2lLnKA3/Desafio?node-id=0%3A1)
- [Arquivos](layout.zip)
