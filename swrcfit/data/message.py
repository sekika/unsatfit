EXTRA_MESSAGES = {
    'wait': {
        'es': 'Espere, por favor ...', 'de': 'Bitte warten ...',
        'pt': 'Aguarde, por favor ...', 'ru': 'Пожалуйста, подождите ...',
        'zh': '请稍候 ...',
    },
    'sample': {
        'es': 'Ejemplo de resultado', 'fr': 'Exemple de résultat',
        'de': 'Beispielausgabe', 'pt': 'Exemplo de resultado',
        'ru': 'Пример результата', 'zh': '输出示例',
    },
    'help': {
        'es': '<h2>Cita</h2>\n<p>Por favor, cite este artículo cuando publique resultados de investigación obtenidos con este programa, SWRC Fit o unsatfit. SWRC Fit realiza los cálculos con la biblioteca <a href="https://sekika.github.io/unsatfit/">unsatfit</a>.</p>\n',
        'fr': '<h2>Référence</h2>\n<p>Veuillez citer cet article lorsque vous publiez des résultats obtenus avec ce programme, SWRC Fit ou unsatfit. SWRC Fit effectue les calculs avec la bibliothèque <a href="https://sekika.github.io/unsatfit/">unsatfit</a>.</p>\n',
        'de': '<h2>Zitat</h2>\n<p>Bitte zitieren Sie diesen Artikel, wenn Sie Forschungsergebnisse veröffentlichen, die mit diesem Programm, SWRC Fit oder unsatfit erzielt wurden. SWRC Fit verwendet die Bibliothek <a href="https://sekika.github.io/unsatfit/">unsatfit</a>.</p>\n',
        'pt': '<h2>Citação</h2>\n<p>Por favor, cite este artigo ao publicar resultados de pesquisa obtidos com este programa, SWRC Fit ou unsatfit. O SWRC Fit usa a biblioteca <a href="https://sekika.github.io/unsatfit/">unsatfit</a> para os cálculos.</p>\n',
        'ru': '<h2>Цитирование</h2>\n<p>Пожалуйста, процитируйте эту статью при публикации результатов исследований, полученных с помощью этой программы, SWRC Fit или unsatfit. SWRC Fit выполняет расчёты с библиотекой <a href="https://sekika.github.io/unsatfit/">unsatfit</a>.</p>\n',
        'zh': '<h2>引用</h2>\n<p>使用本程序、SWRC Fit 或 unsatfit 发表研究成果时，请引用本文。SWRC Fit 使用 <a href="https://sekika.github.io/unsatfit/">unsatfit</a> 库进行计算。</p>\n',
    },
    'question': {
        'es': '<h2>Preguntas</h2><p>Envíe sus preguntas e informes de errores al <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">apartado de preguntas y respuestas de unsatfit Discussions</a>. Cree una cuenta de GitHub, inicie sesión y pulse el botón verde «New discussion». Responderé mediante un comentario. Si su consulta es confidencial, por ejemplo porque contiene datos no publicados, contácteme por correo electrónico. La dirección figura en <a href="https://doi.org/10.1002/vzj2.20168">este artículo</a>.</p>',
        'fr': '<h2>Questions</h2><p>Envoyez vos questions et rapports de bogues à la rubrique <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">Q&amp;R de unsatfit Discussions</a>. Créez un compte GitHub, connectez-vous, puis cliquez sur le bouton vert « New discussion ». Je répondrai par un commentaire. Si votre question est confidentielle, par exemple si elle contient des données non publiées, contactez-moi par courriel. L’adresse figure dans <a href="https://doi.org/10.1002/vzj2.20168">cet article</a>.</p>',
        'de': '<h2>Fragen</h2><p>Bitte senden Sie Fragen und Fehlerberichte an <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">Fragen und Antworten in den unsatfit Discussions</a>. Erstellen Sie ein GitHub-Konto, melden Sie sich an und klicken Sie auf die grüne Schaltfläche „New discussion“. Ich antworte per Kommentar. Wenn Ihre Frage vertraulich ist, etwa weil sie unveröffentlichte Daten enthält, kontaktieren Sie mich bitte per E-Mail. Die Adresse steht in <a href="https://doi.org/10.1002/vzj2.20168">diesem Artikel</a>.</p>',
        'pt': '<h2>Perguntas</h2><p>Envie perguntas e relatos de erros para as <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">perguntas e respostas do unsatfit Discussions</a>. Crie uma conta no GitHub, entre e pressione o botão verde «New discussion». Responderei por comentário. Se a pergunta for confidencial, por exemplo por conter dados não publicados, entre em contato por e-mail. O endereço está em <a href="https://doi.org/10.1002/vzj2.20168">este artigo</a>.</p>',
        'ru': '<h2>Вопросы</h2><p>Направляйте вопросы и сообщения об ошибках в раздел <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">вопросов и ответов unsatfit Discussions</a>. Создайте учётную запись GitHub, войдите в неё и нажмите зелёную кнопку «New discussion». Я отвечу в комментарии. Если вопрос конфиденциальный, например содержит неопубликованные данные, свяжитесь со мной по электронной почте. Адрес указан в <a href="https://doi.org/10.1002/vzj2.20168">этой статье</a>.</p>',
        'zh': '<h2>问题</h2><p>请将问题和错误报告发送至 <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">unsatfit Discussions 的问答区</a>。请创建 GitHub 帐户、登录，然后点击绿色的“New discussion”按钮。我会通过评论回复。若问题涉及未发表数据等保密内容，请通过电子邮件联系我。电子邮件地址见<a href="https://doi.org/10.1002/vzj2.20168">本文</a>。</p>',
    },
    'format': {
        'es': '<h2>Formato de los datos de entrada</h2>\n<ul>\n<li>Como en los datos de ejemplo, cada línea de datos numéricos representa un par de valores medidos (h, &theta;) en este orden. <a href="unit.html">Puede utilizarse cualquier unidad</a>.\n<li>En cada línea, los valores se separan con espacios, tabuladores o comas (,).\n<li>Cuando hay más de dos números, solo se leen los dos primeros.\n<li>Las líneas que no empiezan con un número no se consideran datos medidos.</ul>',
        'fr': '<h2>Format des données d’entrée</h2>\n<ul>\n<li>Comme dans les données d’exemple, chaque ligne de données numériques représente une paire de mesures (h, &theta;) dans cet ordre. <a href="unit.html">Toute unité peut être utilisée</a>.\n<li>Sur chaque ligne, les valeurs sont séparées par des espaces, des tabulations ou des virgules (,).\n<li>Lorsqu’il y a plus de deux nombres, seuls les deux premiers sont lus.\n<li>Les lignes ne commençant pas par un nombre ne sont pas considérées comme des données mesurées.</ul>',
        'de': '<h2>Format der Eingabedaten</h2>\n<ul>\n<li>Wie in den Beispieldaten stellt jede Zeile numerischer Daten ein Messwertpaar (h, &theta;) in dieser Reihenfolge dar. <a href="unit.html">Es können beliebige Einheiten verwendet werden</a>.\n<li>Die Werte einer Zeile werden durch Leerzeichen, Tabulatoren oder Kommas (,) getrennt.\n<li>Bei mehr als zwei Zahlen werden nur die ersten beiden gelesen.\n<li>Zeilen, die nicht mit einer Zahl beginnen, werden nicht als Messdaten betrachtet.</ul>',
        'pt': '<h2>Formato dos dados de entrada</h2>\n<ul>\n<li>Como nos dados de exemplo, cada linha de dados numéricos representa um par de valores medidos (h, &theta;) nessa ordem. <a href="unit.html">Qualquer unidade pode ser usada</a>.\n<li>Em cada linha, os valores são separados por espaço, tabulação ou vírgula (,).\n<li>Quando há mais de dois números, apenas os dois primeiros são lidos.\n<li>Linhas que não começam com um número não são consideradas dados medidos.</ul>',
        'ru': '<h2>Формат входных данных</h2>\n<ul>\n<li>Как в примерах, каждая строка числовых данных представляет пару измерений (h, &theta;) в этом порядке. <a href="unit.html">Можно использовать любые единицы измерения</a>.\n<li>Значения в строке разделяются пробелами, табуляцией или запятыми (,).\n<li>Если чисел больше двух, считываются только первые два.\n<li>Строки, не начинающиеся с числа, не считаются измеренными данными.</ul>',
        'zh': '<h2>输入数据格式</h2>\n<ul>\n<li>与示例数据一样，每一行数值数据按此顺序表示一组测量值 (h, &theta;)。<a href="unit.html">可使用任意单位</a>。\n<li>每行中的数值以空格、制表符或逗号 (,) 分隔。\n<li>若一行有两个以上的数值，只读取前两个。\n<li>不以数值开头的行不视为测量数据。</ul>',
    },
    'modelselect': {
        'es': 'Selección de modelos', 'fr': 'Sélection des modèles',
        'de': 'Modellauswahl', 'pt': 'Seleção de modelos',
        'ru': 'Выбор моделей',
    },
    'figoption': {
        'es': 'Opciones de gráfico', 'fr': 'Options du graphique',
        'de': 'Diagrammoptionen', 'pt': 'Opções do gráfico',
        'ru': 'Параметры графика',
    },
    'onemodel': {
        'es': 'Mostrar solo el mejor modelo', 'fr': 'Afficher uniquement le meilleur modèle',
        'de': 'Nur das beste Modell anzeigen', 'pt': 'Mostrar somente o melhor modelo',
        'ru': 'Показать только лучшую модель', 'zh': '仅显示最佳模型',
    },
    'showmore': {
        'es': 'Mostrar más opciones', 'fr': 'Afficher plus d’options',
        'de': 'Weitere Optionen anzeigen', 'pt': 'Mostrar mais opções',
        'ru': 'Показать дополнительные параметры', 'zh': '显示更多选项',
    },
    'selectsample': {
        'fr': 'Sélectionner un exemple', 'de': 'Beispieldaten auswählen',
    },
    'pastehere': {
        'es': 'Pegue aquí los datos', 'fr': 'Collez vos données ici',
        'de': 'Daten hier einfügen', 'pt': 'Cole os dados aqui',
        'ru': 'Вставьте данные сюда', 'zh': '在此粘贴数据',
    },
    'inputerror': {
        'es': 'Error en los datos de entrada', 'fr': 'Erreur dans les données saisies',
        'de': 'Fehler in den Eingabedaten', 'pt': 'Erro nos dados de entrada',
        'ru': 'Ошибка входных данных', 'zh': '输入数据错误',
    },
    'sameh': {
        'es': 'Todos los valores de h son iguales. Se necesitan valores de h diferentes.',
        'fr': 'Toutes les valeurs de h sont identiques. Des valeurs de h différentes sont nécessaires.',
        'de': 'Alle h-Werte sind gleich. Unterschiedliche h-Werte sind erforderlich.',
        'pt': 'Todos os valores de h são iguais. São necessários valores de h diferentes.',
        'ru': 'Все значения h одинаковы. Необходимы разные значения h.',
        'zh': '所有 h 值都相同。需要不同的 h 值。',
    },
    'readformat': {
        'es': 'Consulte el formato de datos de entrada siguiente.',
        'fr': 'Consultez le format des données d’entrée ci-dessous.',
        'de': 'Beachten Sie das untenstehende Format der Eingabedaten.',
        'pt': 'Consulte o formato de dados de entrada abaixo.',
        'ru': 'См. формат входных данных ниже.', 'zh': '请参阅下面的输入数据格式。',
    },
    'result': {
        'es': 'Resultado', 'fr': 'Résultat', 'de': 'Ergebnis',
        'pt': 'Resultado', 'ru': 'Результат', 'zh': '结果',
    },
    'footer': {
        'es': '<a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a> con <a href="https://sekika.github.io/unsatfit/">unsatfit</a> versión VER, creado por AUTHOR, se ejecuta con Python PYV en ARCH. <a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">Ejecutar un servidor local</a>.',
        'fr': '<a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a> avec <a href="https://sekika.github.io/unsatfit/">unsatfit</a> version VER, créé par AUTHOR, fonctionne avec Python PYV sur ARCH. <a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">Exécuter un serveur local</a>.',
        'de': '<a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a> mit <a href="https://sekika.github.io/unsatfit/">unsatfit</a> Version VER, erstellt von AUTHOR, läuft mit Python PYV auf ARCH. <a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">Lokalen Server starten</a>.',
        'pt': '<a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a> com <a href="https://sekika.github.io/unsatfit/">unsatfit</a> versão VER, criado por AUTHOR, é executado com Python PYV em ARCH. <a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">Executar servidor local</a>.',
        'ru': '<a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a> с <a href="https://sekika.github.io/unsatfit/">unsatfit</a> версии VER, созданный AUTHOR, работает с Python PYV на ARCH. <a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">Запустить локальный сервер</a>.',
        'zh': '<a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a> 使用 <a href="https://sekika.github.io/unsatfit/">unsatfit</a> 版本 VER，由 AUTHOR 创建，运行在 ARCH 的 Python PYV 上。<a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">运行本地服务器</a>。',
    },
    'history': {
        'es': 'Este servicio lleva <a href="URL">funcionando <strong>YEAR años</strong></a>.',
        'fr': 'Ce service <a href="URL">fonctionne depuis <strong>YEAR ans</strong></a>.',
        'de': 'Dieser Dienst <a href="URL">läuft seit <strong>YEAR Jahren</strong></a>.',
        'pt': 'Este serviço está <a href="URL">em funcionamento há <strong>YEAR anos</strong></a>.',
        'ru': 'Этот сервис <a href="URL">работает уже <strong>YEAR лет</strong></a>.',
        'zh': '本服务已<a href="URL">持续运行 <strong>YEAR 年</strong></a>。',
    },
}


ITALIAN_MESSAGES = {
    'description': 'SWRC Fit può adattare <a href="model.html">diversi modelli</a> ai dati misurati della <a href="https://en.wikipedia.org/wiki/Water_retention_curve">curva di ritenzione idrica del suolo</a> e determinare i parametri idraulici del suolo. Copiare i dati misurati (pressione, contenuto d’acqua) nella casella di testo sottostante e premere il pulsante «Calcola». Prima di usare dati originali, è possibile selezionare un campione dal menu a discesa.',
    'calculate': 'Calcola',
    'wait': 'Attendere, per favore ...',
    'sample': 'Esempio di risultato',
    'help': '<h2>Citazione</h2>\n<p>Citare questo articolo quando si pubblicano risultati ottenuti con questo programma, SWRC Fit o unsatfit. SWRC Fit esegue i calcoli con la libreria <a href="https://sekika.github.io/unsatfit/">unsatfit</a>.</p>\n',
    'ack': '<h2>Ringraziamenti</h2><ul><li>I dati di esempio provengono dal <a href="https://doi.org/10.15482/USDA.ADC/1173246">database UNSODA</a> delle proprietà idrauliche dei suoli insaturi, sviluppato dall’US Salinity Laboratory. Per altri dati, consultare il <a href="https://sekika.github.io/unsoda/">visualizzatore UNSODA</a>.</li><li>I ringraziamenti per le traduzioni sono riportati nelle rispettive pagine linguistiche.</li></ul>',
    'question': '<h2>Domande</h2><p>Inviare domande e segnalazioni di errori alla sezione <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">Q&amp;A di unsatfit Discussions</a>. Creare un account GitHub, accedere e premere il pulsante verde «New discussion». Risponderò con un commento. Se la domanda è riservata, ad esempio perché contiene dati non pubblicati, contattarmi via e-mail. L’indirizzo è disponibile in <a href="https://doi.org/10.1002/vzj2.20168">questo articolo</a>.</p>',
    'format': '<h2>Formato dei dati di input</h2>\n<ul>\n<li>Come nei dati di esempio, ogni riga numerica rappresenta una coppia di misure (h, &theta;) in questo ordine. <a href="unit.html">È possibile usare qualsiasi unità</a>.\n<li>I valori sono separati da spazi, tabulazioni o virgole (,).\n<li>Se sono presenti più di due numeri, vengono letti solo i primi due.\n<li>Le righe che non iniziano con un numero non sono considerate dati misurati.</ul>',
    'modelselect': 'Selezione dei modelli', 'figoption': 'Opzioni del grafico',
    'onemodel': 'Mostra solo il modello migliore', 'showmore': 'Mostra altre opzioni',
    'swrc': 'Curva di ritenzione idrica del suolo',
    'selectsample': 'Seleziona dai dati di esempio', 'pastehere': 'Incollare qui i dati',
    'inputerror': 'Errore nei dati di input',
    'sameh': 'Tutti i valori di h sono uguali. Sono necessari valori di h diversi.',
    'readformat': 'Consultare il formato dei dati di input riportato di seguito.',
    'result': 'Risultato',
    'footer': '<a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a> con <a href="https://sekika.github.io/unsatfit/">unsatfit</a> versione VER, creato da AUTHOR, è in esecuzione con Python PYV su ARCH. <a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">Eseguire un server locale</a>.',
    'history': 'Questo servizio <a href="URL">è attivo da <strong>YEAR anni</strong></a>.',
}


TURKISH_MESSAGES = {
    'description': 'SWRC Fit, ölçülen <a href="https://en.wikipedia.org/wiki/Water_retention_curve">toprak su tutma eğrisi</a> verilerine <a href="model.html">çeşitli modelleri</a> uydurabilir ve toprak hidrolik parametrelerini belirleyebilir. Ölçüm verilerinizi (basınç, su içeriği) aşağıdaki metin kutusuna yapıştırın ve “Hesapla” düğmesine basın. Kendi verilerinizi kullanmadan önce açılır menüden örnek veri seçerek uygulamayı deneyebilirsiniz.',
    'calculate': 'Hesapla',
    'wait': 'Lütfen bekleyin ...',
    'sample': 'Örnek çıktı',
    'help': '<h2>Atıf</h2>\n<p>Bu program, SWRC Fit veya unsatfit ile elde edilen araştırma sonuçlarını yayımlarken lütfen bu makaleye atıf yapın. SWRC Fit hesaplamalarda <a href="https://sekika.github.io/unsatfit/">unsatfit</a> kütüphanesini kullanır.</p>\n',
    'ack': '<h2>Teşekkür</h2><ul><li>Örnek veriler, US Salinity Laboratory tarafından geliştirilen doygun olmayan toprakların hidrolik özelliklerine ilişkin <a href="https://doi.org/10.15482/USDA.ADC/1173246">UNSODA veritabanından</a> alınmıştır. Daha fazla veri için <a href="https://sekika.github.io/unsoda/">UNSODA görüntüleyicisine</a> bakın.</li><li>Çevirilere ilişkin teşekkürler ilgili dil sayfalarında yer almaktadır.</li></ul>',
    'question': '<h2>Sorular</h2><p>Sorularınızı ve hata bildirimlerinizi <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">unsatfit Discussions Soru-Cevap bölümüne</a> gönderin. Bir GitHub hesabı oluşturun, oturum açın ve yeşil “New discussion” düğmesine basın. Yorumla yanıt vereceğim. Sorunuz gizliyse, örneğin yayımlanmamış veriler içeriyorsa, e-posta ile iletişime geçin. E-posta adresi <a href="https://doi.org/10.1002/vzj2.20168">bu makalede</a> yer almaktadır.</p>',
    'format': '<h2>Girdi verisi biçimi</h2>\n<ul>\n<li>Örnek verilerde olduğu gibi, her sayısal veri satırı bu sırayla bir ölçüm çifti (h, &theta;) gösterir. <a href="unit.html">Herhangi bir birim kullanılabilir</a>.\n<li>Her satırdaki değerler boşluk, sekme veya virgül (,) ile ayrılır.\n<li>İkiden fazla sayı varsa yalnızca ilk ikisi okunur.\n<li>Sayıyla başlamayan satırlar ölçüm verisi sayılmaz.</ul>',
    'modelselect': 'Model seçimi', 'figoption': 'Grafik seçenekleri',
    'onemodel': 'Yalnızca en iyi modeli göster', 'showmore': 'Daha fazla seçenek göster',
    'swrc': 'Toprak su tutma eğrisi',
    'selectsample': 'Örnek verilerden seç', 'pastehere': 'Verileri buraya yapıştırın',
    'inputerror': 'Girdi verisi hatası',
    'sameh': 'Tüm h değerleri aynıdır. Farklı h değerleri gereklidir.',
    'readformat': 'Aşağıdaki girdi verisi biçimine bakın.',
    'result': 'Sonuç',
    'footer': '<a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a>, AUTHOR tarafından oluşturulan <a href="https://sekika.github.io/unsatfit/">unsatfit</a> VER sürümüyle ARCH üzerinde Python PYV kullanarak çalışır. <a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">Yerel sunucu çalıştırma</a>.',
    'history': 'Bu hizmet <a href="URL"><strong>YEAR yıldır</strong> çalışmaktadır</a>.',
}


def message(lang, ID, URL='./'):
    """Define localized message"""
    if ID == 'list':
        # Return list of available languages in two-letter codes of ISO 639-1.
        # https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
        # It is used for lang parameter in this function.
        # It appears in the language menu in this order.
        return ['de', 'en', 'es', 'fr', 'it', 'ja', 'pt', 'ru', 'tr', 'zh']
    if ID == 'langname':
        # Return language name in the language
        if lang == 'en':
            return 'English'
        if lang == 'es':
            return 'Español'
        if lang == 'fr':
            return 'Français'
        if lang == 'de':
            return 'Deutsche'
        if lang == 'it':
            return 'Italiano'
        if lang == 'pt':
            return 'Português'
        if lang == 'ru':
            return 'Русский'
        if lang == 'tr':
            return 'Türkçe'
        if lang == 'zh':
            return '中文'
        if lang == 'ja':
            return '日本語'
        return lang
    if ID == 'langbar':
        # Make language selection menu.
        bar = '<form action="' + URL + '" method="get">'
        bar += '<select name="lang" aria-label="Language" onchange="this.form.submit()">'
        for i in message('', 'list'):
            language = message(i, 'langname')
            if lang == i:
                selected = ' selected'
            else:
                selected = ''
            bar += '<option value="' + i + '"' + selected + '>'
            bar += i + ': ' + language + '</option>'
        bar += '</select></form>'
        return bar
    if ID == 'langlinks':
        return ' | '.join(
            '<a href="' + URL + '?lang=' + i + '">'
            + message(i, 'langname') + '</a>'
            for i in message('', 'list')
        )
    if ID == 'css':
        return 'swrc.css'
    translated = EXTRA_MESSAGES.get(ID, {}).get(lang)
    if translated is None:
        translated = {
            'it': ITALIAN_MESSAGES,
            'tr': TURKISH_MESSAGES,
        }.get(lang, {}).get(ID)
    if translated is not None:
        if ID == 'help':
            return translated + '<ul><li>' + message(lang, 'seki2023') + '</li></ul>'
        return translated
    # From here translations to local languages are defined.
    # When translation is not defined, English message is returned.
    if ID == 'news':
        if lang == 'ja':
            return '<strong>[ニュース]</strong><ul><li><a href="https://sekika.github.io/unsatfit/hydrus.html">HYDRUSで関数を使える</a>ようになりました。</li><li><a href="model-ja.html#trimodal">三重モデル</a>を追加しました。</li><li>団粒土に対するdual-VGの精度を向上させた<a href="https://doi.org/10.34467/jssoilphysics.155.0_35">論文</a>が<strong>土壌物理学会賞</strong>を受賞しました。</li><li><a href="https://sekika.github.io/unsoda/">UNSODA viewer</a> と <a href="https://sekika.github.io/unsatfit/">unsatfit</a> と <a href="https://sekika.github.io/hystfit/">hystfit</a> もどうぞ。</li><li>より詳しくは <a href="https://sekika.github.io/unsatfit/#history">history</a>に記載。</li></ul>'
        return '<strong>[News]</strong><ul><li>Functions can now be used in <a href="https://sekika.github.io/unsatfit/hydrus.html">HYDRUS</a>.</li><li><a href="model.html#trimodal">Trimodal models</a> were added.</li><li><a href="https://doi.org/10.34467/jssoilphysics.155.0_35">Improvement of dual-VG model</a> was implemented.</li><li>Please also check <a href="https://sekika.github.io/unsoda/">UNSODA viewer</a>, <a href="https://sekika.github.io/unsatfit/">unsatfit</a> and <a href="https://sekika.github.io/hystfit/">hystfit</a>.<li>Read more at <a href="https://sekika.github.io/unsatfit/#history">history</a>.</ul>'
    if ID == 'description':
        if lang == 'ja':
            return 'SWRC Fit は、<a href="https://github.com/sekika/paper/raw/master/JTUNS/Seki-2017-JTUNS.pdf">土壌水分特性（水分保持曲線）</a>のデータを、<a href="model-ja.html">いくつかのモデル</a>によって近似し、土壌水分特性パラメータを決定することができます。' \
                + '土壌水分特性のデータをテキストボックスに貼り付けて、「計算する」ボタンを押して下さい。' \
                + 'プルダウンメニューからサンプルのデータを選んで、試すことができます。'
        if lang == 'es':
            return 'SWRC Fit puede ajustar <a href="model.html">diferentes modelos</a> de <a href="https://es.slideshare.net/smeseguer/t10-edafologia-ag1012el-agua-en-el-suelo">curva de retención de agua del suelo</a> a los valores medidos. ' \
                + 'Copie sus datos de medida (presión, contenido de agua) en el cuadro de texto de abajo y pulse el botón "Calcular". Antes de usar sus datos originales, puede ver como funciona la aplicación seleccionado diferentes tipos de suelos en el menu desplagable. '
        if lang == 'fr':
            return 'SWRC Fit permet d’ajuster <a href="model.html">différents modèles</a> de <a href="https://en.wikipedia.org/wiki/Water_retention_curve">rétention de l’eau du sol</a> avec des valeurs mesurées. ' \
                + 'Copiez vos données mesurées (pression, teneur en eau)  dans la zone de texte ci-dessous et appuyez sur le bouton "Calculer". Vous pouvez choisir des exemples de données dans le menu déroulant. '
        if lang == 'de':
            return 'SWRC Fit kann <a href="model.html">bodenhydraulische Modelle</a> an gemessene <a href="https://de.wikipedia.org/wiki/Bodenwasserspannung">Bodenwasserspannungskurven</a> anpassen. ' \
                + 'Kopieren Sie Ihre Bodenwasserspannungsdaten in das Textfeld und klicken Sie auf "Berechnen". Sie können Beispieldaten aus dem Pull-Down-Menü auswählen.'
        if lang == 'pt':
            return 'SWRC Fit pode definir água <a href="model.html">diferentes modelos</a> de curva de retenção de água no solo para os valores medidos. ' \
                + 'Copiar os dados de medição (pressão, teor de água) na caixa de texto abaixo e pressione o botão "Calcular". Antes de usar seus dados originais, você pode ver como o aplicativo selecionado diferentes tipos de solos nas obras de menu desplagable.'
        if lang == 'ru':
            return 'ОГХ Приближение (SWRC Fit) может подгонять <a href="model.html">несколько гидравлических моделей почвы</a> к измеренной <a href="https://ru.wikipedia.org/wiki/%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D0%B0%D1%8F_%D0%B3%D0%B8%D0%B4%D1%80%D0%BE%D1%84%D0%B8%D0%B7%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%85%D0%B0%D1%80%D0%B0%D0%BA%D1%82%D0%B5%D1%80%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0">Основная гидрофизическая характеристика</a> (<strong>ОГХ</strong>, кривая водоудерживания). ' \
                + 'Прежде чем использовать исходные данные, вы увидите, как они работают, выбрав образец данных из выпадающего меню.'
        if lang == 'zh':
            return 'SWRC Fit 能够拟合多种<a href="https://zh.wikipedia.org/wiki/%E6%B0%B4%E5%88%86%E6%8C%81%E7%95%99%E6%9B%B2%E7%BA%BF">水分特征曲线</a>的<a href="model.html">模型</a>，测量水分特征数据。' \
                + '在下面的文本框中复制土壤水分特征数据 (压力，含水量)，然后按“计算”按钮。使用原始数据之前，从下拉菜单中选择样本数据可以看到它是如何工作的。'
        return 'SWRC Fit can fit <a href="model.html">several soil hydraulic models</a> to measured <a href="https://en.wikipedia.org/wiki/Water_retention_curve">soil water retention</a> data. ' \
            + 'Copy your soil water retention data in the textbox below and press "Calculate" button. ' \
            + 'Before you use your original data you can see how it works by selecting a sample data from the pulldown menu. '
    if ID == 'calculate':
        if lang == 'ja':
            return '計算する'
        if lang == 'es':
            return 'Calcular'
        if lang == 'fr':
            return 'Calculer'
        if lang == 'de':
            return 'Berechnen'
        if lang == 'pt':
            return 'Calcular'
        if lang == 'ru':
            return 'Рассчитать'
        if lang == 'zh':
            return '计算'
        return 'Calculate'
    if ID == 'wait':
        if lang == 'ja':
            return 'お待ちください ...'
        if lang == 'fr':
            return 'Attendez SVP ...'
        return 'Please wait ...'
    if ID == 'sample':
        if lang == 'ja':
            return '出力例'
        return 'Sample output'
    if ID == 'help':
        if lang == 'ja':
            return '<h2>引用</h2>\n<p>SWRC Fit または unsatfit を使った研究成果を公表するときには、この論文を引用して下さい。SWRC Fit は <a href="https://sekika.github.io/unsatfit/">unsatfit</a> のライブラリを使って計算をしています。</p>\n' \
                + '<ul><li>' + message(lang, 'seki2023') + '</li></ul>'
        return '<h2>Citation</h2>\n<p>Please cite this paper when you publish your work using this program, SWRC Fit or unsatfit. SWRC Fit uses <a href="https://sekika.github.io/unsatfit/">unsatfit</a> library.</p>\n' \
            + '<ul><li>' + message(lang, 'seki2023') + '</li></ul>'
    if ID == 'ack':
        if lang == 'ja':
            return '<h2>謝辞</h2><ul><li>サンプルデータはアメリカ農務省塩類研究所が開発した不飽和土壌水分特性の<a href="' + message(lang, 'unsoda') + '">UNSODA データベース</a>から取得しました。<a href="https://sekika.github.io/unsoda/ja/">UNSODA ビューア</a>でさらにデータを閲覧可能です。<li>「土壌の物理性」で<a href="https://www.jstage.jst.go.jp/article/jssoilphysics/148/0/148_45/_article/-char/ja/">お薦めして</a>いただきました。</ul>'
        if lang == 'es':
            return '<h2>Agradecimientos</h2><ul><li>Los datos de ejemplo proceden de la <a href="' + message(lang, 'unsoda') + '">base de datos UNSODA</a> de propiedades hidráulicas de suelos no saturados, desarrollada por el US Salinity Laboratory. Consulte el <a href="https://sekika.github.io/unsoda/">visor UNSODA</a> para obtener más datos.</li>' \
                + '<li>El <a href="https://scholar.google.co.jp/citations?user=a842WTkAAAAJ">Dr. David Moret-Fernandez</a> revisó la traducción al español.</li></ul>'
        if lang == 'fr':
            return '<h2>Remerciements</h2><ul><li>Les données d’exemple proviennent de la <a href="' + message(lang, 'unsoda') + '">base de données UNSODA</a> sur les propriétés hydrauliques des sols non saturés, développée par le US Salinity Laboratory. Consultez le <a href="https://sekika.github.io/unsoda/">visualiseur UNSODA</a> pour davantage de données.</li>' \
                + '<li>Le <a href="https://www.researchgate.net/profile/Philippe-Ackerer">Dr Philippe Ackerer</a> a révisé la traduction française.</li></ul>'
        if lang == 'de':
            return '<h2>Danksagung</h2><ul><li>Die Beispieldaten stammen aus der <a href="' + message(lang, 'unsoda') + '">UNSODA-Datenbank</a> zu hydraulischen Eigenschaften ungesättigter Böden, die vom US Salinity Laboratory entwickelt wurde. Weitere Daten finden Sie im <a href="https://sekika.github.io/unsoda/">UNSODA-Viewer</a>.</li>' \
                + '<li><a href="https://www.bgr.bund.de/EN/Themen/Wasser/Mitarbeiterseiten/thullnerM_en.html?nn=1548666">Dr. Martin Thullner</a> hat die deutsche Übersetzung korrigiert.</li></ul>'
        if lang == 'zh':
            return '<h2>致谢</h2><ul><li>示例数据来自美国盐渍土实验室开发的、关于非饱和土壤水力性质的 <a href="' + message(lang, 'unsoda') + '">UNSODA 数据库</a>。更多数据请参阅 <a href="https://sekika.github.io/unsoda/">UNSODA 浏览器</a>。</li>' \
                + '<li><a href="http://www.iswc.cas.cn/sourcedb_iswc_cas/zw/zjrc/200910/t20091020_2584555.html">Dr. Li Wang</a> 修订了中文翻译。</li></ul>'
        if lang == 'pt':
            return '<h2>Agradecimentos</h2><ul><li>Os dados de exemplo são do <a href="' + message(lang, 'unsoda') + '">banco de dados UNSODA</a> de propriedades hidráulicas de solos não saturados, desenvolvido pelo US Salinity Laboratory. Consulte o <a href="https://sekika.github.io/unsoda/">visualizador UNSODA</a> para mais dados.</li><li>Os agradecimentos pelas traduções são apresentados em cada página de idioma.</li></ul>'
        if lang == 'ru':
            return '<h2>Благодарности</h2><ul><li>Примерные данные взяты из <a href="' + message(lang, 'unsoda') + '">базы данных UNSODA</a> по гидравлическим свойствам ненасыщенных почв, разработанной US Salinity Laboratory. Дополнительные данные доступны в <a href="https://sekika.github.io/unsoda/">просмотрщике UNSODA</a>.</li><li>Благодарности за переводы приведены на страницах соответствующих языков.</li></ul>'
        return '<h2>Acknowledgement</h2><ul><li>Sample data is from <a href="' + message(lang, 'unsoda') + '">UNSODA database</a> of unsaturated soil hydraulic properties developed by US Salinity Laboratory. See <a href="https://sekika.github.io/unsoda/">UNSODA viewer</a> for more data.</li>' \
            + '<li>Acknowledgement for translation is shown in each language page. I speak only English and Japanese. Help in language is always welcome.</li></ul>'
    if ID == 'question':
        if lang == 'ja':
            return '<h2>質問</h2><p>質問は<a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">unsatfit DiscussionsのQ&A</a>に送ってください。GitHub のアカウントを取得しサインインして、緑色の「New discussion」ボタンを押して下さい。日本語での質問も可能です。コメントで返信します。未公開のデータに関する質問など、質問を公開出来ない場合には、メールで質問をしてください。メールアドレスは<a href="https://doi.org/10.1002/vzj2.20168">この論文</a>にあります。</p>'
        return '<h2>Question</h2><p>Please send questions and bug reports to <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">Q&A at unsatfit Discussions</a>. Get GitHub account, sign in, and press the green "New discussion" button. I will reply by comment. It is preferable to send your question publicly this way, because other people having the same question can find answer on the web. However, if your question is confidential, for example when it includes your unpublished data, please contact me by email. You can find my email address in <a href="https://doi.org/10.1002/vzj2.20168">this paper</a>.</p>'
    if ID == 'format':
        if lang == 'ja':
            return '<h2>入力データ形式</h2>\n<ul>\n<li>サンプルデータのように、測定値の組は (h, &theta;) をこの順番に入力する。<a href="unit.html">単位について</a>。\n' \
                + '<li>それぞれの行において、パラメータはスペース、タブ、またはカンマ(,)で区切る。\n' \
                + '<li>3個以上の数の組があるときには、2つの数だけが読み込まれる。\n' \
                + '<li>数で始まらない行は測定値とは見なされない。' \
                + '</ul>'
        return '<h2>Format of input data</h2>\n<ul>\n<li>As in the sample data, each line of numeric data represents a set of measured (h, &theta;) in this order. <a href="unit.html">Any unit can be used</a>.\n' \
            + '<li>For each line, parameters are separated with space, tab, or comma (,).\n<li>When there are more than 2 numbers only the first 2 numbers are read.\n' \
            + '<li>Lines not beginning with numbers are not regarded as measured data.' \
            + '</ul>'
    if ID == 'seki2007':
        return 'Seki, K. (2007) SWRC fit - a nonlinear fitting program with a water retention curve for soils having unimodal and bimodal pore structure. Hydrol. Earth Syst. Sci. Discuss., 4: 407-437. ' \
            + '<a href="http://dx.doi.org/10.5194/hessd-4-407-2007">doi:10.5194/hessd-4-407-2007</a>'
    if ID == 'seki2022':
        return 'Seki, K., Toride, N., & Th. van Genuchten, M. (2022). Closed-form hydraulic conductivity equations for multimodal unsaturated soil hydraulic properties. Vadose Zone J. 21, e20168. ' \
            + '<a href="https://doi.org/10.1002/vzj2.20168">https://doi.org/10.1002/vzj2.20168</a>'
    if ID == 'seki2023':
        return 'Seki, K., Toride, N., & Th. van Genuchten, M. (2023) Evaluation of a general model for multimodal unsaturated soil hydraulic properties. J. Hydrol. Hydromech. 71(1): 22-34. ' \
            + '<a href="https://doi.org/10.2478/johh-2022-0039">https://doi.org/10.2478/johh-2022-0039</a>'
    if ID == 'fredlund1994':
        return 'Fredlund, D.G. and Xing, A. (1994): Equations for the soil-water characteristic curve. Can. Geotech. J., 31: 521-532. ' \
            + '<a href="http://dx.doi.org/10.1139/t94-061">http://dx.doi.org/10.1139/t94-061</a>'
    if ID == 'unsoda':
        return 'https://doi.org/10.15482/USDA.ADC/1173246'
    if ID == 'modelselect':
        if lang == 'ja':
            return 'モデルの選択'
        if lang == 'zh':
            return '模型选择'
        return 'Model selection'
    if ID == 'figoption':
        if lang == 'ja':
            return 'グラフオプション'
        if lang == 'zh':
            return '图选项'
        return 'Figure option'
    if ID == 'onemodel':
        if lang == 'ja':
            return '最良のモデル1つを表示'
        return 'Show only one model'
    if ID == 'showmore':
        if lang == 'ja':
            return 'さらにオプションを見る'
        return 'Show more options'
    if ID == 'swrc':
        if lang == 'ja':
            return '土壌水分特性曲線'
        if lang == 'es':
            return 'la curva de retención de agua del suelo'
        if lang == 'fr':
            return 'la courbe de rétention d’eau du sol'
        if lang == 'de':
            return 'Wasserspannungskurve'
        if lang == 'pt':
            return 'curva de retenção de água no solo'
        if lang == 'ru':
            return 'ОГХ'
        if lang == 'zh':
            return '水分持留曲线'
        return 'Soil Water Retention Curve'
    if ID == 'selectsample':
        if lang == 'ja':
            return 'サンプルデータから選ぶ'
        if lang == 'es':
            return 'Seleccionar de ejemplo'
        if lang == 'pt':
            return 'Selecione Amostra'
        if lang == 'es':
            return 'Seleccionar de ejemplo'
        if lang == 'ru':
            return 'ыберите из примеров'
        if lang == 'zh':
            return '从示例中选择'
        return 'Select from sample data'
    if ID == 'pastehere':
        if lang == 'ja':
            return 'ここにデータを貼り付ける'
        return 'Paste your data here'
    if ID == 'inputerror':
        if lang == 'ja':
            return '入力データエラー'
        return 'Error in input data'
    if ID == 'sameh':
        if lang == 'ja':
            return 'hがすべて同じ値です。異なるhのデータが必要です。'
        return 'All h values are same. Different values of h are required.'
    if ID == 'readformat':
        if lang == 'ja':
            return '下記の入力データ形式を参照してください。'
        return 'Read the format of input data below.'
    if ID == 'result':
        if lang == 'ja':
            return '計算結果'
        return 'Result'
    if ID == 'wait':
        if lang == 'ja':
            return 'お待ちください ...'
        if lang == 'fr':
            return 'Attendez SVP ...'
        return 'Please wait ...'
    if ID == 'footer':
        if lang == 'ja':
            return '<a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a> with <a href="https://sekika.github.io/unsatfit/">unsatfit</a> version VER （作成者：AUTHOR）が ARCH の Python PYV で動いています。<a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">ローカルサーバーで動かす</a>。'
        return '<a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a> with <a href="https://sekika.github.io/unsatfit/">unsatfit</a> version VER created by AUTHOR running with Python PYV on ARCH. <a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">Run local server</a>.'
    if ID == 'history':
        if lang == 'ja':
            return 'このサービスは<a href="URL"><strong>YEAR年間</strong>運用を続けています</a>。'
        return 'This service has been <a href="URL">running for <strong>YEAR years</strong></a>.'
    if ID == 'author':
        if lang == 'ja':
            return '<a href="https://sekika.github.io/toyo/">関勝寿</a>'
        return '<a href="https://scholar.google.com/citations?user=Gs_ABawAAAAJ">Katsutoshi Seki</a>'
    return '<strong>Message ID error!</strong>'
