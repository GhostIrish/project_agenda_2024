'''
nao ta com todas as configs no .vscode
'''

'''
OBS: SEMPRE SALVE AS ALTERAÇÕES QUE VOCE FOR FAZENDO COM CTRL + S
POIS AS VEZES O SERVER DA ERRO POR ESSE SIMPLES ATO DE NAO SALVAR
'''

'''
26.02.2024: Criei a pasta project, a .vscode para configurar meu vscode
            configurei todo o ambiente, criei o venv, instalei o django,
            tudo certo, a pasta project foi criada com uma linha de código que cria automaticamente.
            python -m venv venv
            venv/Scripts/Activate
            pip install django
            django-admin startproject project . (cria a pasta projeto na raiz)

            Configurar o git no repositório
            '''
            git config --global user.name 'Hariel'
            git config --global user.email 'harielpimenta@hotmail.com'
            git config --global init.defaultBranch main
            git init
            git add
            git commit -m 'Mensagem do commit'
            git remote add origin URL_DO_GIT, cria o repositorio noo github
'''

'''
27.02.2024: python manage.py startapp contact(criei o app main na 
            pasta  do projeto)
            -fui no arquivo settings do project e adicionei na lista de INSTALLED_APPS a linha 'contact', que faz com que o django reconheça o app que eu acabei de criar, evitando erros!

            -criei as pastas base_template e base_static no meu código, dentro da base templates, criei uma pasta global e dentro dela criei um base.html com um h1 no body escrito 'QUALQUER', so para acrescentar algo.
            -fiz o mesmo no static, mas dessa vez criei um arquivo style.css, agora vou la no settings configurar igual feito anteriormente com o startapp, mas na parte de TEMPLATES.

            -logo apos isso, fui embaixo do STATIC_URL e acrescentei um novo para salvar os statics file e acrescentar no meu site(fazer ele aplicar o css)
            ficou STATICFILES_DIRS = (BASE_DIR / 'base_templates')
            -fui no contact, criei a pasta templates dentro dele, adicionei outra pasta dentro escrito templates e um arquivo 'index.html', tudo feito anteriormente foi para padronizar meu django para reconhecer os templates e o css
            -fui no index e usei o extends que faz um link com o base_html, fazendo com que não seja necessário eu escrever diretamente no index
            pois basicamente o index é a homepage do nosso site e tudo que eu trabalhar com ela será feito no base_html
            -criei na raiz da pasta contact um arquivo de urls.py com aquelas informações
            -entrei no views do contact e criei uma view que é linkada com o index.html
            -voltei no urls e importei da pasta de views do contact, a view que acabei de criar
            -adicionei ela ao urlpatterns e nomeei ela como 'index' para toda vez que me referir a ela ao longo do codigo
            -fui no url do projeto, importei o include e adicionei a linha de codigo 'path('', include('contact.urls'))'
            fazendo com que o projeto busque as informações do url de contacts ao inves de procurar somente direto no projeto
            basicamente a raiz do site foi para o url do contact e não do projeto.
            - fui no base.html e adicionei um link com static no comeco, linkando com o css do projeto
            ai embaixo do titulo para testar eu adicionei o link direto com o arquivo style.css do projeto
            e la nele adicionei um background color red, pra deixar o fundo vermelho e testar para ver se o codigo estava funcionando, e fucinou ate aqui.

            Comecando na area administrativa do django
            -Migrando a base de dados do django:
            python manage.ooy makemigrations
            python manage.py migrate
            -Criando e modificando a senha de um super usuario django:
            python manage.py createsuperuser
            python manage.py changepassword USERNAME
            -Usei o comando python manage.py migration, essa parte trata mais do banco de dados
            vou ter que dar uma olhada no modulo de mysql para saber mais afundo, ai entrando na url do site e dando um /admin na url
            entra em uma tela de login de django administration com login e senha, essa parte
            eu ainda vou criar esse login e senha.
            -usei o python manage.py createsuperuser e criei um usuario admin e senha para aquela parte administrativa
            - loguei e vi toda a parte administrativa do seervidor queo django proporciona, muito maneiro
            caso esqueça a senha, so usar o codigo de alterar password la de cima
            

29.02.2024: criar o primeiro model do django
            -criei uma classe nos models de contact que herda de models.model
            -La criei a classe Contact, a linha de comando com 'max_length'
            diz quantos caracteres pode ter o primeiro nome e outras informações
            o 'blank=True' é para deixar claro que essas partes especificas são facultativas
            -importei do django.utils o timezone, que faz com que na hora que o usuario
            registre as informações, seja registrado a data e momento em que fez isso
            created_date = models.DateTimeField(default=timezone.now) 
            essa linha de codigo acima faz isso.
            -usei os comandos: 
            python manage.ooy makemigrations
            python manage.py migrate
            o primeiro para adicionar a base de dados essas especificações do contact que fiz
            com esse comando um arquivo é criado automaticamente na raiz do codigo
            e  usando esse comando migrate, jogamos as informações do arquivo, que é um resumo
            do que colocamos em model, para dentro da base de dados 
            apos isso se você for olhar la, na base de dados foi adicionado a tabela
            contact com todas as descrições que passamos em models
            - fui em admin do contact, para meio que registrar o contact na area admin do django
            criei a classe Contact admin que usa o decorator @admin.register()
            - depois de fazer isso, indo na parte de admin, pode reparar
            que foi criado uma aba de 'contact', onde faz todas as informações
            que dissemos, ped as informações e salva elas no site, porém salva com o nome do id dela na base de dados.
            aplicando o comando:
            def __str__(self) -> str:
                return f'{self.first_name} {self.last_name}'
            ele altera com exito para o nome e o sobrenome que registramos na base de dados.
            
            - agora irei configurar o admin
            configurando o admin apenas passando o 'list_display'
            e passando oque dos models eu desejo que apareça, salvando
            e atualizando o site, os contacts aparecem mostrando oque eu desejar
            no caso até agora eu pedi para mostrar o first_name, last_Name e o phone
            e realmente é mostrado com essa simples configuração
            - passei uma ordenação tambem, para mostrar o id e ordenar por ele
            coloquei o menos na frente e isso faz com que o id ordene de forma decrescente
            - acrescentei um list_filter, que configura uma aba que mostra um filtros
            e coloquei um filtro por data criada, mas comentei essa parte
            pois não tem tantos contacts ainda registrados pra necessitar do filtro
            -Adicionei embaixo mais algumas buscas e features que o django tem
            vou deixar o codigo que fiz qui la, para não ficar muito poluido visualmente no código em si
            os codigos:
            search_fields = ('first_name', 'last_name') # adiciona filtros de busca
            list_per_page = 5 # quantos contacts serão exibidos por pagina
            list_max_show_all = 200 # limite de quantos contatos o 'show all' mostrará
            - Coloquei esses codigos aqui:
            list_editable = ('first_name', 'last_name')
            list_display_links = ('first_name',)
            o list_editaable faz com que os campos que você passar
            possam ser facilmente alterados diretamente, sem precisar
            clicar no contato, por isso ate comentei essa parte
            pois não achei tao boa esteticamente
            e o list display links é para denominar oque você deseja que seja
            um link direto para o contato, passei o nome, mas qualquer um dos campos poderiam ser  passados

01.03.2024: 
            Trabalhando com o model do django
            
            '''python
            # importe o módulo
            from contact.models import Contact
            # Cria um contato (Lazy)
            # retorna o contato
            contact = Contact(**fields)
            contact.save()
            # Seleciona um contato com o id 10
            # Retorna o contato
            contact = Contact.objects.get(pk=10)
            # Edita um contato
            # Retorna o contato
            contact.field_name1 = 'Novo valor 1'
            contact.field_name2 = 'Novo valor 2'
            contact.save()
            # Apaga um contato
            # Depende da base de dados, geralmente retorna o número
            # de valores manipulados na base de dados
            contact.delete()
            # Seleciona todos os contatos ordenando por id DESC
            # Retorna QuerySet[]
            contacts = Contact.objects.filter(**filters).orders_by('-id')
            '''
            - criei a linha show no models que deixa a gente decidir
            se quer ou não ver o contato quando criar, por padrão
            coloquei sim 'True'
            - Agora fui no settings e criei umas configuações pro site
            receber imagens.
            STATIC_ROOT = BASE_DIR / 'static' # collectstatic
            escrevi isso acima, não tem haver com a parte de receber
            imagens mas o professor disse que futuramene iriamos usar

            esses são os comandos usados para acrescentar imagens do usuario
            MEDIA_URL = 'media/'
            MEDIA_ROOT = BASE_DIR / 'media '
            - usei no cmd o commando python manage.py collectstatic
            para ele coletar os dados estáticos do meu código antes
            de commitar, foi criado a pasta static na raiz do código
            com aquele static_root
            - fiz a pasta static e media ser ignorada pelo git ja que ela só sera alterada
            pelo próprio, então não há necessidade de mandar para o github
            
            picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
            - Resumo do resumo, esse comando aacima faz com que possa ser colocada
            uma imagem no contato, onde vai ser criado uma pasta 'pictures',
            dentro dela vai ser criada outra com o ano '%Y' e dentro dela outra
            xom o mês '%m' para armazendar a foto.
            %SEMPRE que alterar algo na base de dados, tem que ser feito o makemigrations%
            para as mudanças serem aplicadas.
            - a partir dai a imagem salva bonitinho na pasta media que é criada
            na raiz do projeto, mas ela não pode ser carregada no site
            pra isso temos que configurar la nas urls do projeto

            urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
            - esse comando acima configurado nas urls faz com que a imagem que antes não carregava
            quando aberta em outra guia agora carregue
            
04.03.2024: vou criar a categoria, uma foreign key para identificar 
            melhor os contatos na base de dados.
            - isso cria a cateoria do contato no admin la
            - depois fui em admin de contact, fiz esse trecho esse trecho:
            @admin.register(models.Category)
            class CategoryAdmin(admin.ModelAdmin):
                # configuração do seu model no admin do django
                list_display = ('name', )
                ordering = ('-id',) # menos faz com que fique id de forma decrescente
            
            para poder registrar uma categoria para selecionar

            - o category no site aparece em plural, mas um plural errado
            'cateorys' é como aparece la, vou corrigir essa parte
            fiz a classe Meta dentro das categorias, defini o verbose_name
            que seria o nome no singular e o verbose_name_plural, que seria
            o nome da categoria no plural
            
            - Pus no terminal do projeto igual nos codigos abaixo
            criando um usuario do admin novo usando o prompt  de comando
            (venv) PS C:\Users\harie\agenda_project_django_2024> python manage.py shell
            Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
            Type "help", "copyright", "credits" or "license" for more information.       
            (InteractiveConsole)
            >>> from django.contrib.auth.models import User
            >>> user = User.objects.create_user(username='teste1', password='123')
            >>> 
            Mas o usuario vem sem o 'staff' habilitado, ou seja, ele sendo criado assim
            por padrão não vem marcado como um dev, então não tem
            acesso a area admnistrativa do Django, na hora de usar esse login
            no comeco da parte admin, ele não funciona la mesmo colocando as cred-
            enciais certas
            - Agora vou fazer o processo de criar o owner dentro do Contact
            para os contatos poderem ser criados sem as permissões de dev.

            - Agora vamos usar um script que utiliza faker para gerar contatos
            aleatorios para desenvolver melhor o front do site, as views
            Criei uma pasta utils e dentro dela ta o arquivo do script, em caso de duvida
            de como ele funciona criando contatos, ve o video 460 do curso.

05.03.2024: criei um arquivo local com o nome de 'local_settings',
            para armazenar as informações de configurações que uso 
            no código, ja que elas podem entrar em conflito com o site
            ao longo do desenvolvimento, ai criamos esse arquivo para 
            armazenar as settings e não deixamos ele ser upado para O
            github jogando eles nas configurações do gitignore
            try:
                from project.local_settings import *
            except ImportError:
                ...
            colocando essa linha de codigo no settings.py, fazemos com que
            tudo que for feito no local_settings vai ser considerado no 
            settings, mas na hora de upar o servidor, não irão, evitando
            gerar erros e derrubar o servidor.
            isso contorna o problema de ter varios ambientes com varios
            settings diferentes.
            ele so sobescreve a settings do django em si

            - criei no contact uma pasta 'views' e dentro dela um arquivo
            '__init_.py' para o python entender que essa pasta é um pacote
            que importaremos depois, isso faz com que caso você precise
            criar varios arquivos para cada processo do site, voce pode fazer
            nessa pasta, esse processo de criar a pasta pode ser feito em
            qualquer situação ali, pros models e etc.
            - deletei o arquivo views da raiz de contact justamente pq a
            pasta views ja tem um arquivo dentro dela que faz exatamente O
            mesmo.
            ai o codigo da erro, mas indo no init da pasta views e importando
            tudo de contact_views, fazemos o site voltar a funcionar, colocamos
            o flake8 e o ignore para não grifar erros na parte do init onde vai
            ser feita as importações.
            sempre que alterar algo, importe direitinho alterando no init la
            para não gerar erros, é uma forma de se organizar.

            peguei o css ja feito de outro projeto do professor e colei no style.css
            para poupar tempo, qualquer duvida é so ver a aula 463 ou pesquisar
            sobre a classe no css.

            - no base.html voce coloca essa linha de codigo por exemplo:
            {% block content %}{% endblock content %}
            e vai poder trabalhar com essa parte dentro do template que for utilizar
            no caso do base ali, vamos trabalhar no index de contact.
            - agora fiz com que a gente possa acrescentar apenas os blocos
            o h1 você poe direto como no exemplo
            - adicionei a linha  main class="content"> que liga o html
            com a classe content {% block content %}{% endblock content %}
            e essa classe content é trabalhada no index.html para não ser
            tudo feito em um arquivo só e ficado muito grande e dentro do
            index, dentro do bloco content, é fitoo um for para mostrar 
            os nomes de contatos que estão na base de dados, essa parte:
            {% block content %}
                {% for contact in contacts %}
                    {{contact.first_name}}
                {% endfor %}
            {% endblock content %}
            e o contact_views puxa todos os dados do bd retornando eles
            para voce fazer uso no base e no index,
            essa linha de codigo 'contacts = Contact.objects.all()'
            puxa todos nomes do bd.

            - tiramos esse for que fiz anteriormente para poder configurar
            a tabela e não ficar embolado os nomes.
            ####################################################
            - cara, mexi MUITO com html no index nessa aula 465, depois
            da uma passada la no index do contact que eu vou explicando
            linha por linha, mas é basicamente html, não tem muito erro
            *pegar o print dessa parte e colocar no word antes de imprimir
            ####################################################
            
06.03.2024: troquei a linha do contacts de Contact.objects.all().order_by('-id')
            para o código a seguir, fazendo com que ele ordene da Mensagem
            forma, mas so os contatos que tem 'show=True' apareçam
            é uma opção implementada no menu do contato.
            contacts = Contact.objects\
            .filter(show=True)\
            .order_by('-id')
            esses comandos acima fazem oque eu disse anteriormente.
            - fui no list_display no admin do contacts, adicionei o 'show'
            que faz com que no admin mostre quais contatos estão sendo,
            mostrados ou não.

            - fui no template de contact e criei um arquivo contact.html
            pois resumindo, a view renderizaa o template, faz aparecer
            ele, depois você cria a view pq a URL depende dela.
            no contact eu escrevi o código, essa parte é para quando clicar
            em alguma das informações que eu escolher, vai te redirecionar
            pro contato em uma página separada
            - fui no contact_views e fiz a conexão entre ele e o contact.html,
            depois fui na URL do contact e liguei ele com a view para abrir em 
            outra parte do site.
            
            def contact(request, contact_id):
                single_contact = Contact.objects\
                .get(pk=contact_id) # pk == primary key
    
                context = {
                    'contact': single_contact,
                        }
                return render(
                    request,
                    'contact/contact.html',
                    context
                    )
            esse codigo faz oque disse anteriormente, ai depois fui la
            no urlpatterns dentro da url do projeto e codei para que ele
            troque para essa guia.
            - adicionei no contact.html as informações que queria
            na parte de categoria, coloquei pra procurar contact.category.name
            pois buscaria direto o nome e não dependeria do model todo
            se ficasse so com o category, caso alterasse o model, poderiam
            dar ruim.
            - troquei o get do contact no arquivo contact_views, pois
            ele  buscando pelo id e voce alterando algum valor na url
            dispara o erro do django, então alteramos para filter,
            mesmo ele retornando uma lista de valores, colocamos o 
            .first() depois para pegar so o primeiro valor, diminuindo
            o erro e posssibilitando agora levantarmos uma excessão
            caso isso ocorra.
            - importando do django.http http404 e escrevendo assim:
            def contact(request, contact_id):
                single_contact = Contact.objects\
                    .filter(pk=contact_id).first() # pk == primary key

                if single_contact is None:
                    raise Http404()
            pois sem isso, quando ele não encontra nada dessa forma
            ele retornava aquela pagina com o 'email','phone' e etc.
            mas tudo vazio, pois não encontrou nenhuma info com aquele
            ID, mas usando esse if, ao inves disso ou do erro do django
            ele dispara um erro de http404.
            isso é tão comum, que o proprio django tem um atalho no
            django.shortcuts chamado get_object_or_404, que faz exatamente
            oque acabei de fazer manualmente, eai ficou assim.
            single_contact = get_object_or_404(Contact.objects, pk=contact_id, show=True)
            e isso é exatamente oque fiz anteriormente., e ali dentro 
            é possivel passar um filter e etc, especificando mais
            todo esse conteudo ta na aula 467 em caso de duvida.

            - nessa aula 468 foi basicamente so html, ensinando a criar
            o agenda de cima, linkar ele com o menu, criar o link 1, link 2
            e a barra de navegar, so dar uma olhada no base.html
            foi tudo trabalhado por la.

07.03.2024: basicamente a aula começa ensinando a mover algumas partes
            do html  para que o código fique mais limpo, vou fazer com 
            o base.html para exemplificar.
            - fiz isso e coloquei os nomes nas abas do navegador
            <title>{{site_title}} - Agenda</title> assim, ai fui no
            contact_view e adicionei a view relacionada a isso no index
            que é relacionado a pagina principal e ao contact que é rela-
            cionado a parte da pagina do contato separado.
            
            - Essa parte é relacionado com fazer o filtro, a busca fun-
            cionar, criamos uma view search no contact_views.
            - crie uma url para poder renomear o site quando entrar
            na parte de pesquisa, adiciona na _header, no form
            para fazer a ligação com o search do contact_views.
            - criei um 'search_value' para pegar a informação da Query do usuario
            provavelmente ate o final, vai ser usado isso para fazer a busca 
            baseado no que foi dito pelo usuário.
            if search_value == '':
            redirect('contact:index')
            essa linha de codigo verifica se o usuario colocou um valor
            vazio, caso ocorra, você é redirecionado pro index, ou seja
            pro menu principal do site
            - depois modifiquei aqui:
            contacts = Contact.objects\
            .filter(show=True)\
            .filter(first_name__icontains=search_value)\
            .order_by('-id')
            onde coloquei mais um filtro que você poe de primeira oque
            quer buscar, no meu cao foi o first_name, em seguida, poe
            dois __ e o método de busca, no caso foi o icontains,
            mais detalhes sobre isso, ve um poucoo antes dos 10 minutos
            do video 470.
            
11.03.2024: Adicionei mais uma parte no:
            contacts = Contact.objects\
                        .filter(show=True)\
                        .filter(
                        Q(first_name__icontains=search_value) |
                        Q(last_name__icontains=search_value)
                        )\
                        .order_by('-id')
            porem, nesse caso, quando fazemos apenas com as virgulas ali, ele trata como um AND, ou seja, buscando 'hariel' por exemplo
            só iria aparecer a pesquisa caso o nome e o sobre nome fossem hariel tipo: 'hariel hariel', caso contrario não iria aparecer.
            - do django, na parte do contact_views, importe do django.db.models import Q, usando ele será possivel fazer o 'OR' dentro do
            Django, alterei no codigo de cima ali ja.
            - mas basicamente ele funciona como o OR quando envolvido pelo q assim, ou seja, procurando por exemplo 'hariel' ou so 'pimenta'
            encontrariamos todos os contatos com o sobrenome igual ou nomes.
            - tem que tirar a virgula ali e colocar um | no lugar, assim funcionara como um OR, irei alterar ali encima, fiz no codigo com o phone e o email também
            assim é mais facil de encontrar idepende de como busque.
            da pra usar um api do google na busca e facilitar todo esse trabalho, usando o campo de busca deles.
            - mudei no _header.html, o form no value para {{ request.GET.q.strip}}, assim no campo de pesquisa no site acima, ele vai manter a string que
            você pesquisou, ela não sumirá mais e ficara só o search.
            Tem outra forma de fazer isso também, caso queira saber, é no video 471, essa forma é mais universal. a que usei é mais especifica.
            - agora quando ele não encontra nada nos contatos, ele ainda mantém os indices das colunas, vamos mexer nisso.
            - indo no index, la no começo, quando você poe um if contacts e um endif no final, quer dizer que se ele encontrar um contato
            a tabulação será feita, caso contrario, não mostrara mais os indíces da tabela: {% if contacts %} {% endif %}

12.03.2024: usaremos a classe Paginator do Django, que ja é uma classe praticamente pronta para criar a paginação do site e separar os contatos
            - importamos ele no contact_views, fomos la no index do contact_views, criamos o paginator que é:
            paginator = Paginator(contacts, 10)  
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)  
            isso cria o paginador e o numero das paginas, o page number é para fazer aparecer na url a page e o numero dela 
            - mudei o nome do contact no context para 'page_obj', alterando ali, mudei no index tambem para não quebrar o codigo.
            fiz isso para não quebrar a logica do template fornecido para o paginator.   
            era:
            {% for contact in contacts %}
            ficou:
            {% for contact in page_obj %}
            mudei o if tambem la encima para o page_obj
            - pode notar que agora o site so mostra os 10 primeiros contatos apenas.
            - vou no site que o professor deixou na aula 472, copio a div que faz o pagination, crio um partial novo
            para jogar o pedaço do código que criei, partials são partes do html do base.html nesse caso, que são quebradas ali, para não ficar tudo
            e, um arquivo so , ficando um codigo grande.
            - vou fazer o link do partials com o resto do código do site para o paginator de fato aparecer la, irei incluir no base.html
            - fazendo o include no base.html do pagination, ao atualizar o site ja da para notar que foi criada uma paginação.
            - tentei por um botão e passei muito tempo nele, basicamente mexi no pagination e no style.css, passei mal, depois tenta ver pra colocar
            deixei o next sem, para ver como fica sem os botoes.
            - fiz o mesmo no search, para a url manter com o page junto das informações da busca, para a url ficar correta 
            - adicionei no pagination no href o &q={{ request.GET.q.strip }} depois do ?page, pois assim fica um link mais completo e direto para essa parte
            
            - organizaremos nossa url durante esse video d0o professor
            alterei o path('<int:contact_id>/', views.contact, name='contact'),
            para:
            path('contact/<int:contact_id>/details/', views.contact, name='contact'),
            assim quando voce entrar no contato, fica mais especifico e facil de não se perder do caminho que a url estara fazendo
            - adicionei mais algumas urls do CRUD que faremos com contact, para ter uma noção mais cotidiana de como ficaria

13.03.2024: Nessa aula começaremos a criar o view e o template para a area de adicionar um contato novo.
            - criei o arquivo 'create.html' no template de contact para começas a codar a parte de criar um contato do site.
            - extendemos o base.html e fazemos um html simples de começo, agora vamos criar uma view para renderizar esse template e aparecer no site
            - criamos um 'contact_forms', para trabalharmos com formularios, ja que o 'contact_view' é mais voltado para a parte de ler e exibir coisas, não de criar.
            - no contact forms aproveitamos e copiamos do views os imports para facilitar, criamos um create que retorna o render do request(basicamente faz renderizar).
            - vamos no init da pasta views e importamos tudo de contact form, para o python interpretar nosso arquivo como um módulo.
            - colocamos no urls para ele identificar no site, a url ficou:
            path('contact/create/', views.create, name='create'),
            - apos isso ja da para notar que a url http://127.0.0.1:8000/contact/create/ ja apresenta uma aba nova de create contact.

            - criei o html rapidinho da pagina no create.html, mais detalhes precisos na aula 475 do que cada coisa faz, o css ja foi configurado previamente, então
            não precisei configurar ele.
            - o metodo GET faz com que apareça oque esta sendo mostrado na url, por isso não é tão viável utilizar ele para criar o contato, por conta disso
            utilizamos o método POST, que é mais relacionado com dados sensíveis, que não irão aparecer na url.
            - enctype="multipart/form-data"
            essa parte de cima é relacionada com o envio de arquivos para o site, no caso desse projeto, são arquivos de fotos.

            - apos fazer a parte de enviar o label, quando digitar algo no site e enviar, ira disparar um erro de CSRF, veremos
            sobre ele agora.
            - é um tipo de ataque para pegar dados, dispara esse erro pois o django em si ja automaticamente protege o desenvolvedor ,
            esta la no settings asim que voce cria o projeto logo no começo.
            - o crsf token é um código que vai garantir que os dados que o usuario esta postando na view, vão realmente vir do formularios
            que você esta codando, retirando a proteção que disparava anteriormente, é usado {% csrf_token %} la no create.html.

            - ele explica mais sobre o post em si na aula 477 do curso, se sentir dificuldade, da uma passada la que ele explica bem melhor
            - Essa aula foi mais teorica.

14.03.2024: Começaremos a trabalhar com os forms e utilizaremos o contact para trabalhar com eles para facilitar ainda mais, ja que o contact está estabelecido no site
            - importamos o módulo forms do django para começar a criar com from django 'import forms'
            - Criamos uma classe chamada ContactForm e herdamos ela do forms.Model forms, utilizamos o ModelForm como herança pois ja temos os campos pre estabelecidos
            no contact, não havendo a necessidade de criação de um forms novo.
            - criamos então uma metaclass dentro do ContactForm (Meta classes são utilizadas quando desejamos dar um novo sentido ou outra utilização a outras classes
            estabelecidas, no caso do site é a classe Contact)
            - criamos o campo 'fields' que utilizara dos campos nomeados do django, no caso do site é o 'first_name, last_name e phone'
            - vamos no create e chamamos 'form': CreateForm(), chamamos ele diretamente assim, pois não temos dados, POST nem instancias do modulo, utilizamos ele diretamente
            - isso configura o form mas não faz ele aparecer pra gente no template, pra isso vamos no create, encima de form-group, fazemos um {% for field in form %}
            pegando todos os campos do formulario que digitamos no contact_form, no caso do site seria o 'first_name, last_name e phone', ficando mais ou menos assim:
            {% for field in form %}
                <div class="form-group">
                    <label for="id_first_name">LABEL</label>
                    <input type="text" name="first_name" maxlength="255">
                </div>
            {% endfor %}
            - depois trocamos o for ali e o label, trocamos o for de 'id_first_name' para {{ field.id_for_label }}, pois pelo for que passamos antes, com esse field.id_for_label
            ele busca os id dinamicamente da parte que desejamos la no contact_forms, no caso daqui são os ditos anteriormente 'first_name, last_name e phone'
            a mesma lógica se aplica para o label, trocamos ele por {{field.label}}, pois ele vai pegar os campos dessa label que anteriormente tinhamos pego o id, no caso do
            first_name por exemplo, ele buscou o id do campo first_name, sendo ele(o id) com esse nome, o nome da tabela no site do contact se altera dinamicamente para esse
            campo e a lógica se aplica em todos os outros.
            - refaremos os campos de input, pois do jeito que está não é o ideal, vamos no create, adicionamos um if para confirmar se o método que o usuário usará, sera o de
            POST, caso seja, ele pode renderizar esse form que fizemos antes, passando na classe ContactForm o método POST para enviarmos as informações do formulário.
            - O create fica assim:
            def create(request):  
            if request.method == 'POST':  
                context = {
                    'form': ContactForm(request.POST)
                }
                
                return render(
                    request,
                    'contact/create.html',
                    context
                )
            context = {
                'form': ContactForm()
            }
            
            return render(
                request,
                'contact/create.html',
                context
            )

            
                    '''         
            - o if verifica se o formulario foi postado, caso tenha sido, ele faz o render com o contactform passando POST, caso contrario, ele apresenta um formulario
            limpo.
            - <input type="text" name="first_name" maxlength="255"> apagamos essa parte e colocamos apenas {{ field }}, para poder fazer a parte do if ali encima funcionar
            pois altera o funcionamento de como o campo funciona para poder identificar se foi postado ou não, basicamente isso faz com que se escrevermos algo e apertarmos
            em enviar, o campo continua escrito, podendo verificar oque foi escrito, sem isso ao enviar os campos ficavam vazios novamente.

            - embaixo do fields colocamos o campo {{ fields.errors }}, isso é para aparecer alguma mensagem de erro caso o usuário digite algo errado, mas a mensagem não aparece
            para a mesma aparecer, precisamos sobescrever um método do model chamado clean, ele é disparado antes dos dados serem enviados, vamos alterar ele para verificar dis
            crepâncias e disparar o erro.
            - def clean(self):
                cleaned_data = self.cleaned_data
                return super().clean() 
            alteramos ele assim e pedimos para ele nos entregar a cleaned_data, os dados que o usuário passou, então vamos verificar se ha algo de errado.
            - adicionamos no clean essa função:
            self.add_error(
            'first_name',
            ValidationError(
                'Error',
                code='invalid'
            )
        )
            - chamei uma função que adiciona errors, adicionei no campo first_name e importei o erro validation que verifica se algo esta escrito errado, ai a mensagem
            embaixo que vai aparecer em teoria e o código que esta escrito 'invalido'.
            - depois disso ele explicou mais sobre como funciona os erros aparecendo no site com exemplos, caso queira ver ou tenha ficado com duvida, a aula é a 479
            do curso.

            - passamos o form para um arquivo exclusivo dele, para não poluir tanto o contact_forms.

            - nessa aula vamos focar em configurar os campos e widgets do formulário.
            - Adicionarei um widget nos campos do formulario, no caso os campos são considerados widgets, vou acrescebtar um placeholder nele, para ficar uma caixa de 
            texto escrita dentro dele antes de eu clicar para escrever escrito 'Write here'.
            - FICOU ASSIM:
            widgets = {
                'first_name': forms.TextInput(
                    attrs={
                        'placeholder': 'Write here'
                    }
                ),}
            - outra maneira de fazer essa mesma coisa é acessando o init da class ModelForm que é herdada pelo contactform, dessa maneira aqui, não escreverei no meu código
            tendo em vista que o resultado é o mesmo, manterei o do widgets.
            fica assim:
            class ContactForm(forms.ModelForm):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                        self.fields['first_name'].widget.attrs.update(
                            'class': 'classe-a classe-b',
                            'placeholder': 'Write here'
                        )
            - pronto, escrevendo assi voce obterá o mesmo resultado, adicionando uma claa ao first_name e um placeholder, que muda aquele campo de escrita como ja esta
            alterdo.
            - tem mais uma maneira que ele explica no video, nessa da para trabalhar com algumas coisas a mais, mnas não anotei aqui não, ele começa a facilitar
            a partir dos 10 mminutos de video da aula 481, se pintar a necessidade, da uma passada la.
            
15.03.2024: Nesse video vamos fazzer a validação do formulario, a validação pode ser feita individualmente caso seja necessário em apenas um campo por ex, vou digitar como
            ficaria esse código, ficaria assim:
            def clean_first_name(self):
                    first_name = self.cleaned_data.get.('first_name')

                    if first_name == 'ABC':
                        raise ValidationError(
                            'Não digite ABC neste campo',
                            code='invalid'
                        )
                    return first_name
            Esse exemplo faria com que caso o usuario digitasse 'ABC' no campo do nome, disparasse aquela mensagem de erro aplicadas., da pra trabalhar com o add_error tbm.
            - agora para verificação de erro em mais de um campo, geralmente quando um campo depende do outro, por exemplo uma senha e uma validação de senha,
            ai utilizamos apenas o clean(), como faz com mais de um campo eu digitei no forms, ficou assim:
            def clean(self):       
                cleaned_data = self.cleaned_data
                first_name = self.cleaned_data.get('first_name')
                last_name = self.cleaned_data.get('last_name')
                
                if first_name == last_name:
                    msg = ValidationError(
                            'O primeiro nome não pode ser igual ao segundo.',
                            code='invalid'
                        )
                    self.add_error('first_name', msg)
                    self.add_error('last_name', msg)
                
                return super().clean()
            
            - colocando o restante dos campos no formulário

            - Agora depois de criar o formulario, ele ainda não salva o contato, vamos trabalhar nessa parte agora.
            - voltamos no contact_forms, alteramos o form para ao inves dele ser enviado direto, ele seja uma variavel que é enviada
            fazemos isso para ele passar por um if verificando se tudo foi validado antes de enviar para o bd 
            - passamos o: 
            if form.is_valid():
                ... 
            para verificar se o formulario é valido, se o formulario não levantar nenhum erro, ele entra nesse campo do init.defaultBranch
            fica assim:
            if form.is_valid():
                print('Your form has been validated.')
                form.save()
            assim somente ele ja salva na base de dados, porem caso queira atrelar ou fazer algo antes de salvar é so fazer assim:
            
            if form.is_valid():
                contact = form.save(commit=False) # impede que o contato seja salvo, mas retorna as informações que foram colocadas nos forms
                # aqui voce faz as validações ou atrela da maneira que precisar, como por exemplo:
                contact.show = False
                # e depois é só você chamar novamente a função que ele salva na base de dados
                contact.save()
                print('Your form has been validated.')
                
18.03.2024: comecei hoje adicionando a aba de criação de contatos la na header do meu site, linkando ela com a view create para carregar outra parte do site,
            - trocamos o {% url 'contact:create' %} do create para '{{ form_action }}', ai vamos no create, criamos a form action, que é um reverse do proprio create
            ou seja, ele busca a url do create de dentro do proprio create, no momento em que é criado o contato, depois mudamos para ao inves de quando o contato for validado
            e criado, ao inves de redirecionar para a homepage, ele direciona para o update que irei criar agora, onde vamos poder editar o contato caso for do nosso interesse.
            - criamos a url para adição da view update, e redirecionamos para o update do usuario de id que acabou de ser criado.
            - atualizamos os valores dos returns e damos prosseguimento a parte de criar o update, copiamos o codigo todo do create, vamos até o final, soltamos ele la, ja que
            o código é bem parecido, mudando apenas alguns detalhes, é valido copiar ele pra economizar o tempo. 
            - ele começa a explicar o funcionamento da view passo a passo do video 485 aos 11:58, ve para mais detalhes, estou meio confuso.
            - o create cria o contato, logo em seguida ele joga a gente pro update, pulando diretamente pra views debaixo do update.

            - criaremos os botoes de update e o de delete.
            - vamos no contact.html e adicionamos as linhas de codigo:
            <div class="contact-links">
                <a href="{% url 'contact:update' contact.id %}">Update</a>
            </div>
            Ela criará o botão linkando para a parte de update que criamos na ultima aula, lembrar de por o mesmo css que coloquei nos botôes da paginação aqui
            farei a parte do delete amanha

19.03.2024: Adicionamos dentro do contact-links o botão delete que fica assim:
            <form action="" method="POST">
                <button class="btn btn-link btn-delete" type="submit">Delete</button>
            </form>
            # mexer no botão depois pra deixar da cor certa, vou fazer depois pra não perder muito tempo 
            - basicamente a criação do delete foi igual a do update, os processos são os mesmos, mudando apenas a finalidade dos botões.

            - estamos criando toda a questão de acrescentar imagem aos contatos, colocamos no contact.html o codigo
            {% if contact.picture %}
                <p>
                    <img src="{{ contact.picture.url }}" alt="{{ contact.first_name }} {{ contact.last_name }}">
                </p>
            {% endif %}
            isso faz com que a foto seja renderizada nos contatos, quando clicamos para ver, caso haja foto é claro, a parte que verifica 
            se tem é o if ali.
            - depos vamos nos campos do form e acrescentamos ele nos fields para aparecer na parte de acrescentar e editar um contato, tanto para tirar ou alterar a img.

            - adicionamos essa parte aqui no forms para alterar o link para imagem e deixar so o campo de escolher arquivo.
            picture = forms.ImageField(
                widget=forms.FileInput(
                    attrs={
                        'accept': 'image/*'
                    }
                )
            )
            esse codigo acima realiza isso, a ideia é mostrar a foto atual e te possibilitar mudar escolhendo o arquivo, não tendo que clicar no link para ver a foto.

            - agora essa parte faz aparecer a imagem que ja esta salva no contato caso exista, logo abaixo do campo de enviar, para voce visualizar e alterar
            o codigo é esse feito no create.html do contact.
            {% if field.name == 'picture' and field.value.url %}
                <div class="form-group">
                    <img src="{{ field.value.url }}" alt="">
                </div>
            {% endif %}
            se o calmpo for 'picture' e ele existir no caso ne, ele busca e exibe a imagem dentro do if.
            - acrescentamos no contact form o request  'ContactForm(request.POST, request.FILES)', para solicitar os arquivos no caso as imgs, onde for usado o POST
            no contact_form tem que acrescentar o request.
            - entendi, essa parte de alterar no post faz com que seja possivel agora alterar as fotos, ja que ele faz o post das informações E dos aquivos(FILES).
            # tentar ver depois um método de padronizar o tamanho das fotos.

20.03.2024: faremos o sistema de criar usuário, ja usaremos o do django mesmo pre feito por padrão , vamos em form, minimizamos contactform para ter mais espaço,
            importamos do django.contrib.auth.forms import UserCreationForm, criamos uma classe para criar esse registro de usuario 'RegisterForm'.
            - vamos no template de contact, criamos um novo chamado register.html, copiamos o codigo do create e faremos algumas alterações par se encaixar na
            criação de usuário.
            - no register mudamos e tiramos algumas poucas coisas, como a parte de fotos que não seria necessário na parte de criação do login.
            - para renderizar isso tudo, é preiso uma view, criamos então a user_forms que vai renderizar tudo pra gente.
            - importamos tudo no init com o codigo from .user_forms import *.
            - renderizamos na view do register:
            from django.shortcuts import render
            def register(request):
                return render(
                    request,
                    'contact/register.html',
                    {
                        'form': form
                    }
                )
            criamos um def(register) no user_forms para enviar e salvar o usuario no banco de dados caso o usuario seja validado, renderizando depois o form no render.

            - agora vamos modificar o register form para acrescentar nos campos ja padroes, o campo de primeiro e ultimo nome e o email do usuario.
            fizemos o mesmo processo parecido com todos os outros, importamos o model, ditamos os campos que queremos e sera exibido no register,
            o django ja faz a validação do usuario automaticamente verificando se são iguais ou não, mas o e-mail ele desconsidera, oque faremos é configurar
            par que o django não aceite dois usuarios com o mesmo e-mail.
            o novo ficou assim:
            class RegisterForm(UserCreationForm):
                first_name = forms.CharField(
                    required=True
                )
                
                email = forms.EmailField(
                    required=True
                )
                class Meta:
                    model = User
                    fields = (
                        'first_name',
                        'last_name',
                        'email',
                        'username',
                        'password1',
                        'password2',
                    )
                
                def clean_email(self):
                    email = self.cleaned_data.get('email')
                    
                    if User.objects.filter(email=email).exists():
                        self.add_error(
                            'email',
                            ValidationError('Another user is registered with this email.', code='invalid')
                        )
                    return email
                        
            onde o começo ali ate antes do classe meta é para trabalhar no campo first_name e email, eu escolhi eles so, para obrigar o usuario a ter que ter pelo menos
            o email e o primeiro nome escrito, não é obrigatório ter um segundo nomes.
            a parte do meta eu ja te expliquei mais ou menos antes que é como os outros.
            e o clean email ali é para verificar se ja não ha algum usuario com este meesmo email cadastrado, caso haja, ele não salva o usuario e dispara aquele erro ali
            ate um email valido ser digitado.

22.03.2024: nesse video vamos aprender a fazer as messages, por exemplo quando um usuario conseguir salvar um contato, ira disparar o sucess.

25.03.2024: Hoje vamos fazer o sistema de login e logout  do usuário separamos o forms que estava no register e criamos um partials para ele,
            ja que o forms podera ser usado mais vezes, colamos la e fazemos o include do forms no register novamente para ele voltar a fun-
            cionar.
            - criamos um html para login, fazemos o include igual no register, mudando apenas a header de register para login, agora vamos
            criar uma view para esse login.


26.03.2024: Hoje vou focar em fazer a parte que permite ao usuário editar as informações do contato, com uma view específica e tudo mais.
            criamos o form para isso no forms, o form é o RegisterUpdateForm.
            - Lembre-se de estar logado para fazer isso, pois essas ações posteriormente serão obrigatórias estar logado para realizá-las.
            colocamos o url desse form, depois vamos criar a view para ela poder ser buscada pela url, ai vamos no user_forms pra isso.
            - Criamos a view que inicialmente ficará assim:
            def user_update(request):
                form = RegisterUpdateForm(istance=request.user)
                
                return render(
                    request,
                    'contact/register.html',
                    {
                        'form': form
                    }
                )
            isso é suficiente para o site funcionar nessa parte de update, criamos mais coisas para verificar se o método do formulario for post, ou seja, para enviar
            dados, caso seja e caso o formulário atenda todas as requisições impostas, o usuário é salvo.
            - atualizei o user_update para ter maior ligação com o RegisterUpdateForm, eles juntos fazem o trabalho de possibilitar alterar as informações do usuario,
            com essas alterações até agora ja é possivel alterar os nomes, email, verificar se o email novo que esta colocando ja esta cadastrado, so falta a validação
            e confirmação de alteração de senha, que estou fazendo no momento.
            - fizemos tudo no forms, fizemos o processo de validação de senha do usuario para poder alterá-la, agora é possivel, foi tudo feito pelo forms, em caso de
            duvida, verifique a aula 493 do curso, sobrescrevemos a função save do django para salvar de forma específica que precisamos no validate do user, salvando
            apenas caso as condições da senha sejam atendidas.
            - fizemos com que atualizasse a pagina, caso o formulario de alteração seja valido, você é redirecionado para a pagina novamente, mostrando as alterações feitas.
            
            - Agora vamos fazer um processo para diferenciar os usuarios logados dos não logados.
