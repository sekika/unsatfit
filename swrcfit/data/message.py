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


PERSIAN_MESSAGES = {
    'description': 'SWRC Fit می‌تواند <a href="model.html">چندین مدل هیدرولیکی خاک</a> را بر داده‌های اندازه‌گیری‌شدهٔ <a href="https://en.wikipedia.org/wiki/Water_retention_curve">منحنی نگهداشت آب خاک</a> برازش دهد و پارامترهای هیدرولیکی خاک را تعیین کند. داده‌های اندازه‌گیری‌شدهٔ خود (فشار، محتوای آب) را در کادر متنی زیر وارد کنید و دکمهٔ «محاسبه» را فشار دهید. پیش از استفاده از داده‌های خود، می‌توانید با انتخاب دادهٔ نمونه از منوی کشویی نحوهٔ کار برنامه را بررسی کنید.',
    'calculate': 'محاسبه',
    'wait': 'لطفاً صبر کنید ...',
    'sample': 'نمونهٔ خروجی',
    'help': '<h2>استناد</h2>\n<p>هنگام انتشار نتایج پژوهشی که با این برنامه، SWRC Fit یا unsatfit به دست آمده‌اند، لطفاً به این مقاله استناد کنید. SWRC Fit برای محاسبات از کتابخانهٔ <a href="https://sekika.github.io/unsatfit/">unsatfit</a> استفاده می‌کند.</p>\n',
    'ack': '<h2>سپاسگزاری</h2><ul><li>داده‌های نمونه از <a href="https://doi.org/10.15482/USDA.ADC/1173246">پایگاه دادهٔ UNSODA</a> دربارهٔ ویژگی‌های هیدرولیکی خاک‌های غیراشباع، که توسط US Salinity Laboratory توسعه یافته است، گرفته شده‌اند. برای داده‌های بیشتر، <a href="https://sekika.github.io/unsoda/">نمایشگر UNSODA</a> را ببینید.</li><li>سپاسگزاری مربوط به ترجمه در صفحهٔ هر زبان درج می‌شود. من فقط انگلیسی و ژاپنی صحبت می‌کنم و از کمک برای بهبود ترجمه استقبال می‌کنم.</li></ul>',
    'question': '<h2>پرسش</h2><p>لطفاً پرسش‌ها و گزارش‌های خطا را در بخش <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">پرسش و پاسخ unsatfit Discussions</a> ارسال کنید. یک حساب GitHub بسازید، وارد شوید و دکمهٔ سبز «New discussion» را فشار دهید. من در بخش نظرات پاسخ خواهم داد. اگر پرسش شما محرمانه است، برای نمونه شامل داده‌های منتشرنشده است، از طریق ایمیل با من تماس بگیرید. نشانی ایمیل در <a href="https://doi.org/10.1002/vzj2.20168">این مقاله</a> آمده است.</p>',
    'format': '<h2>قالب داده‌های ورودی</h2>\n<ul>\n<li>مانند داده‌های نمونه، هر سطر از داده‌های عددی یک جفت اندازه‌گیری‌شدهٔ <span class="ltr">(h, &theta;)</span> را به همین ترتیب نشان می‌دهد. <a href="unit.html">می‌توان از هر واحدی استفاده کرد</a>.\n<li>در هر سطر، مقادیر با فاصله، tab یا ویرگول (,) جدا می‌شوند.\n<li>اگر بیش از دو عدد وجود داشته باشد، فقط دو عدد نخست خوانده می‌شوند.\n<li>سطرهایی که با عدد آغاز نمی‌شوند، دادهٔ اندازه‌گیری‌شده محسوب نمی‌شوند.</ul>',
    'modelselect': 'انتخاب مدل',
    'figoption': 'گزینه‌های نمودار',
    'onemodel': 'فقط بهترین مدل را نمایش بده',
    'showmore': 'نمایش گزینه‌های بیشتر',
    'swrc': 'منحنی نگهداشت آب خاک',
    'selectsample': 'انتخاب از داده‌های نمونه',
    'pastehere': 'داده‌های خود را اینجا وارد کنید',
    'inputerror': 'خطا در داده‌های ورودی',
    'sameh': 'همهٔ مقادیر h یکسان هستند. مقادیر متفاوت h لازم است.',
    'readformat': 'قالب داده‌های ورودی را در پایین ببینید.',
    'result': 'نتیجه',
    'footer': '<a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a> با نسخهٔ VER از <a href="https://sekika.github.io/unsatfit/">unsatfit</a>، ساخته‌شده توسط AUTHOR، با Python PYV روی ARCH اجرا می‌شود. <a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">اجرای سرور محلی</a>.',
    'history': 'این سرویس <a href="URL"><strong>YEAR سال</strong> است که در حال اجراست</a>.',
}


ITALIAN_MESSAGES = {
    'description': 'SWRC Fit può adattare <a href="model.html">diversi modelli</a> ai dati misurati della <a href="https://it.wikipedia.org/wiki/Potenziale_idrico#Curva_di_ritenzione_idrica">curva di ritenzione idrica del suolo</a> e determinare i parametri idraulici del suolo. Copiare i dati misurati (pressione, contenuto d’acqua) nella casella di testo sottostante e premere il pulsante «Calcola». Prima di usare dati originali, è possibile selezionare un campione dal menu a discesa.',
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


KOREAN_MESSAGES = {
    'description': 'SWRC Fit은 측정된 <a href="https://en.wikipedia.org/wiki/Water_retention_curve">토양 수분보유곡선</a> 자료에 <a href="model.html">여러 토양 수리 모형</a>을 적합하여 토양 수리학적 매개변수를 결정할 수 있습니다. 아래 텍스트 상자에 측정 자료(압력, 수분 함량)를 붙여 넣고 “계산” 버튼을 누르십시오. 자신의 자료를 사용하기 전에 풀다운 메뉴에서 예제 자료를 선택하여 프로그램의 작동을 확인할 수 있습니다.',
    'calculate': '계산',
    'wait': '잠시만 기다려 주십시오 ...',
    'sample': '출력 예',
    'help': '<h2>인용</h2>\n<p>이 프로그램, SWRC Fit 또는 unsatfit을 사용하여 얻은 연구 결과를 발표할 때에는 이 논문을 인용해 주십시오. SWRC Fit은 계산에 <a href="https://sekika.github.io/unsatfit/">unsatfit</a> 라이브러리를 사용합니다.</p>\n',
    'ack': '<h2>감사의 글</h2><ul><li>예제 자료는 US Salinity Laboratory에서 개발한 불포화 토양 수리 특성 <a href="https://doi.org/10.15482/USDA.ADC/1173246">UNSODA 데이터베이스</a>에서 가져왔습니다. 더 많은 자료는 <a href="https://sekika.github.io/unsoda/">UNSODA viewer</a>를 참조하십시오.</li><li>번역에 대한 감사 표시는 각 언어 페이지에 기재합니다. 저는 영어와 일본어만 사용하므로 번역 개선에 대한 도움을 환영합니다.</li></ul>',
    'question': '<h2>질문</h2><p>질문과 오류 보고는 <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">unsatfit Discussions의 Q&amp;A</a>에 올려 주십시오. GitHub 계정을 만들고 로그인한 뒤 녹색 “New discussion” 버튼을 누르십시오. 댓글로 답변하겠습니다. 미발표 자료 등 비공개 내용이 포함된 질문은 이메일로 문의하십시오. 이메일 주소는 <a href="https://doi.org/10.1002/vzj2.20168">이 논문</a>에 있습니다.</p>',
    'format': '<h2>입력 자료 형식</h2>\n<ul>\n<li>예제 자료와 같이 각 수치 자료 행은 이 순서로 하나의 측정값 쌍 <span class="ltr">(h, &theta;)</span>을 나타냅니다. <a href="unit.html">어떤 단위도 사용할 수 있습니다</a>.\n<li>각 행의 값은 공백, 탭 또는 쉼표(,)로 구분합니다.\n<li>숫자가 두 개보다 많으면 처음 두 개만 읽습니다.\n<li>숫자로 시작하지 않는 행은 측정 자료로 간주하지 않습니다.</ul>',
    'modelselect': '모형 선택',
    'figoption': '그림 옵션',
    'onemodel': '최적 모형만 표시',
    'showmore': '추가 옵션 표시',
    'swrc': '토양 수분보유곡선',
    'selectsample': '예제 자료에서 선택',
    'pastehere': '여기에 자료를 붙여 넣으십시오',
    'inputerror': '입력 자료 오류',
    'sameh': '모든 h 값이 같습니다. 서로 다른 h 값이 필요합니다.',
    'readformat': '아래의 입력 자료 형식을 참조하십시오.',
    'result': '결과',
    'footer': '<a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a>은 AUTHOR가 개발한 <a href="https://sekika.github.io/unsatfit/">unsatfit</a> 버전 VER을 사용하며, ARCH에서 Python PYV로 실행됩니다. <a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">로컬 서버에서 실행</a>.',
    'history': '이 서비스는 <a href="URL"><strong>YEAR년 동안</strong> 운영되고 있습니다</a>.',
}


INDONESIAN_MESSAGES = {
    'description': 'SWRC Fit dapat mencocokkan <a href="model.html">berbagai model hidraulik tanah</a> dengan data terukur <a href="https://repository.ub.ac.id/148940/1/17_BAB_IV_HASIL_DAN_PEMBAHASAN.pdf">kurva retensi air tanah</a> dan menentukan parameter hidraulik tanah. Tempelkan data pengukuran Anda (tekanan, kadar air) ke kotak teks di bawah lalu tekan tombol “Hitung”. Sebelum menggunakan data Anda sendiri, Anda dapat mencoba program dengan memilih data contoh dari menu tarik-turun.',
    'calculate': 'Hitung',
    'wait': 'Mohon tunggu ...',
    'sample': 'Contoh keluaran',
    'help': '<h2>Sitasi</h2>\n<p>Harap sitasi artikel ini ketika memublikasikan hasil penelitian yang diperoleh dengan program ini, SWRC Fit, atau unsatfit. SWRC Fit menggunakan pustaka <a href="https://sekika.github.io/unsatfit/">unsatfit</a> untuk perhitungan.</p>\n',
    'ack': '<h2>Ucapan terima kasih</h2><ul><li>Data contoh berasal dari <a href="https://doi.org/10.15482/USDA.ADC/1173246">basis data UNSODA</a> mengenai sifat hidraulik tanah tak jenuh yang dikembangkan oleh US Salinity Laboratory. Untuk data lainnya, lihat <a href="https://sekika.github.io/unsoda/">UNSODA viewer</a>.</li><li>Ucapan terima kasih untuk penerjemahan dicantumkan pada halaman tiap bahasa. Saya hanya berbahasa Inggris dan Jepang, sehingga bantuan untuk memperbaiki terjemahan sangat dihargai.</li></ul>',
    'question': '<h2>Pertanyaan</h2><p>Silakan kirim pertanyaan dan laporan kesalahan ke bagian <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">Q&amp;A unsatfit Discussions</a>. Buat akun GitHub, masuk, lalu tekan tombol hijau “New discussion”. Saya akan menjawab melalui komentar. Jika pertanyaan Anda bersifat rahasia, misalnya memuat data yang belum dipublikasikan, silakan hubungi saya melalui email. Alamat email tercantum dalam <a href="https://doi.org/10.1002/vzj2.20168">artikel ini</a>.</p>',
    'format': '<h2>Format data masukan</h2>\n<ul>\n<li>Seperti pada data contoh, setiap baris data numerik menunjukkan satu pasangan nilai terukur <span class="ltr">(h, &theta;)</span> dalam urutan tersebut. <a href="unit.html">Satuan apa pun dapat digunakan</a>.\n<li>Nilai pada setiap baris dipisahkan dengan spasi, tab, atau koma (,).\n<li>Jika terdapat lebih dari dua angka, hanya dua angka pertama yang dibaca.\n<li>Baris yang tidak diawali angka tidak dianggap sebagai data pengukuran.</ul>',
    'modelselect': 'Pemilihan model',
    'figoption': 'Opsi gambar',
    'onemodel': 'Tampilkan hanya model terbaik',
    'showmore': 'Tampilkan opsi lainnya',
    'swrc': 'Kurva retensi air tanah',
    'selectsample': 'Pilih dari data contoh',
    'pastehere': 'Tempelkan data di sini',
    'inputerror': 'Kesalahan pada data masukan',
    'sameh': 'Semua nilai h sama. Diperlukan nilai h yang berbeda.',
    'readformat': 'Lihat format data masukan di bawah.',
    'result': 'Hasil',
    'footer': '<a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a> berjalan dengan versi VER dari <a href="https://sekika.github.io/unsatfit/">unsatfit</a>, dibuat oleh AUTHOR, menggunakan Python PYV pada ARCH. <a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">Menjalankan server lokal</a>.',
    'history': 'Layanan ini <a href="URL">telah berjalan selama <strong>YEAR tahun</strong></a>.',
}


ARABIC_MESSAGES = {
    'description': 'يمكن لبرنامج SWRC Fit ملاءمة <a href="model.html">عدة نماذج هيدروليكية للتربة</a> مع البيانات المقاسة لـ<a href="https://en.wikipedia.org/wiki/Water_retention_curve">منحنى احتفاظ التربة بالماء</a> وتحديد المعلمات الهيدروليكية للتربة. الصق بيانات القياس الخاصة بك (الضغط، المحتوى المائي) في مربع النص أدناه ثم اضغط زر «احسب». قبل استخدام بياناتك، يمكنك تجربة البرنامج باختيار بيانات نموذجية من القائمة المنسدلة.',
    'calculate': 'احسب',
    'wait': 'يرجى الانتظار ...',
    'sample': 'مثال على المخرجات',
    'help': '<h2>الاستشهاد</h2>\n<p>يرجى الاستشهاد بهذه المقالة عند نشر نتائج بحثية تم الحصول عليها باستخدام هذا البرنامج أو SWRC Fit أو unsatfit. يستخدم SWRC Fit مكتبة <a href="https://sekika.github.io/unsatfit/">unsatfit</a> لإجراء الحسابات.</p>\n',
    'ack': '<h2>شكر وتقدير</h2><ul><li>أُخذت البيانات النموذجية من <a href="https://doi.org/10.15482/USDA.ADC/1173246">قاعدة بيانات UNSODA</a> للخصائص الهيدروليكية للتربة غير المشبعة، التي طوّرها US Salinity Laboratory. لمزيد من البيانات، راجع <a href="https://sekika.github.io/unsoda/">UNSODA viewer</a>.</li><li>يُذكر شكر المساهمين في الترجمة في صفحة كل لغة. أنا أتحدث الإنجليزية واليابانية فقط، وأرحب بالمساعدة في تحسين الترجمة.</li></ul>',
    'question': '<h2>الأسئلة</h2><p>يرجى إرسال الأسئلة وتقارير الأخطاء إلى قسم <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">الأسئلة والأجوبة في unsatfit Discussions</a>. أنشئ حسابًا على GitHub، وسجّل الدخول، ثم اضغط زر “New discussion” الأخضر. سأجيب في تعليق. إذا كان سؤالك سريًا، مثل أن يتضمن بيانات غير منشورة، فتواصل معي عبر البريد الإلكتروني. عنوان البريد الإلكتروني موجود في <a href="https://doi.org/10.1002/vzj2.20168">هذه المقالة</a>.</p>',
    'format': '<h2>تنسيق بيانات الإدخال</h2>\n<ul>\n<li>كما في البيانات النموذجية، يمثل كل سطر من البيانات الرقمية زوجًا من القيم المقاسة <span class="ltr">(h, &theta;)</span> بهذا الترتيب. <a href="unit.html">يمكن استخدام أي وحدة</a>.\n<li>تُفصل القيم في كل سطر بمسافة أو tab أو فاصلة (,).\n<li>إذا وُجد أكثر من رقمين، فتُقرأ أول قيمتين فقط.\n<li>الأسطر التي لا تبدأ برقم لا تُعد بيانات قياس.</ul>',
    'modelselect': 'اختيار النموذج',
    'figoption': 'خيارات الشكل',
    'onemodel': 'اعرض أفضل نموذج فقط',
    'showmore': 'عرض مزيد من الخيارات',
    'swrc': 'منحنى احتفاظ التربة بالماء',
    'selectsample': 'اختر من البيانات النموذجية',
    'pastehere': 'الصق البيانات هنا',
    'inputerror': 'خطأ في بيانات الإدخال',
    'sameh': 'جميع قيم h متساوية. يلزم وجود قيم مختلفة لـ h.',
    'readformat': 'راجع تنسيق بيانات الإدخال أدناه.',
    'result': 'النتيجة',
    'footer': 'يعمل <a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a> باستخدام الإصدار VER من <a href="https://sekika.github.io/unsatfit/">unsatfit</a> الذي أنشأه AUTHOR، وباستخدام Python PYV على ARCH. <a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">تشغيل خادم محلي</a>.',
    'history': 'هذه الخدمة <a href="URL">تعمل منذ <strong>YEAR عامًا</strong></a>.',
}


VIETNAMESE_MESSAGES = {
    'description': 'SWRC Fit có thể khớp <a href="model.html">nhiều mô hình thủy lực đất</a> với dữ liệu đo của <a href="https://www.thuvientailieu.vn/tai-lieu/nghien-cuu-thuc-nghiem-xay-dung-duong-dac-trung-am-cua-dat-pf-phuc-vu-xac-dinh-che-do-tuoi-hop-ly-cho-cay-trong-can-tai-51400/">đường cong giữ nước của đất</a> và xác định các tham số thủy lực của đất. Hãy dán dữ liệu đo của bạn (áp suất, hàm lượng nước) vào hộp văn bản bên dưới rồi nhấn nút “Tính toán”. Trước khi sử dụng dữ liệu của riêng mình, bạn có thể thử chương trình bằng cách chọn dữ liệu mẫu từ trình đơn thả xuống.',
    'calculate': 'Tính toán',
    'wait': 'Vui lòng chờ ...',
    'sample': 'Ví dụ kết quả',
    'help': '<h2>Trích dẫn</h2>\n<p>Khi công bố kết quả nghiên cứu thu được bằng chương trình này, SWRC Fit hoặc unsatfit, vui lòng trích dẫn bài báo này. SWRC Fit sử dụng thư viện <a href="https://sekika.github.io/unsatfit/">unsatfit</a> để tính toán.</p>\n',
    'ack': '<h2>Lời cảm ơn</h2><ul><li>Dữ liệu mẫu được lấy từ <a href="https://doi.org/10.15482/USDA.ADC/1173246">cơ sở dữ liệu UNSODA</a> về các đặc tính thủy lực của đất không bão hòa, do US Salinity Laboratory phát triển. Để xem thêm dữ liệu, hãy sử dụng <a href="https://sekika.github.io/unsoda/">UNSODA viewer</a>.</li><li>Lời cảm ơn dành cho người hỗ trợ dịch thuật được ghi trên trang của từng ngôn ngữ. Tôi chỉ sử dụng tiếng Anh và tiếng Nhật, vì vậy rất hoan nghênh mọi hỗ trợ để cải thiện bản dịch.</li></ul>',
    'question': '<h2>Câu hỏi</h2><p>Vui lòng gửi câu hỏi và báo cáo lỗi đến mục <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">Q&amp;A của unsatfit Discussions</a>. Hãy tạo tài khoản GitHub, đăng nhập và nhấn nút xanh “New discussion”. Tôi sẽ trả lời trong phần bình luận. Nếu câu hỏi của bạn mang tính bảo mật, chẳng hạn có chứa dữ liệu chưa công bố, hãy liên hệ với tôi qua email. Địa chỉ email được ghi trong <a href="https://doi.org/10.1002/vzj2.20168">bài báo này</a>.</p>',
    'format': '<h2>Định dạng dữ liệu đầu vào</h2>\n<ul>\n<li>Giống như dữ liệu mẫu, mỗi dòng dữ liệu số biểu thị một cặp giá trị đo <span class="ltr">(h, &theta;)</span> theo thứ tự đó. <a href="unit.html">Có thể sử dụng bất kỳ đơn vị nào</a>.\n<li>Các giá trị trên mỗi dòng được phân tách bằng dấu cách, tab hoặc dấu phẩy (,).\n<li>Nếu có nhiều hơn hai số, chỉ hai số đầu tiên được đọc.\n<li>Các dòng không bắt đầu bằng số không được coi là dữ liệu đo.</ul>',
    'modelselect': 'Chọn mô hình',
    'figoption': 'Tùy chọn hình',
    'onemodel': 'Chỉ hiển thị mô hình tốt nhất',
    'showmore': 'Hiển thị thêm tùy chọn',
    'swrc': 'Đường cong giữ nước của đất',
    'selectsample': 'Chọn từ dữ liệu mẫu',
    'pastehere': 'Dán dữ liệu vào đây',
    'inputerror': 'Lỗi dữ liệu đầu vào',
    'sameh': 'Tất cả các giá trị h đều giống nhau. Cần có các giá trị h khác nhau.',
    'readformat': 'Xem định dạng dữ liệu đầu vào bên dưới.',
    'result': 'Kết quả',
    'footer': '<a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a> chạy với phiên bản VER của <a href="https://sekika.github.io/unsatfit/">unsatfit</a>, do AUTHOR phát triển, sử dụng Python PYV trên ARCH. <a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">Chạy máy chủ cục bộ</a>.',
    'history': 'Dịch vụ này <a href="URL">đã hoạt động được <strong>YEAR năm</strong></a>.',
}


THAI_MESSAGES = {
    'description': 'SWRC Fit สามารถปรับ <a href="model.html">แบบจำลองไฮดรอลิกของดินหลายแบบ</a>ให้เข้ากับข้อมูลที่วัดได้ของ<a href="https://agritech.doae.go.th/wp-content/uploads/2026/01/%E0%B8%AB%E0%B8%A5%E0%B8%B1%E0%B8%81%E0%B8%AA%E0%B8%B9%E0%B8%95%E0%B8%A3-Crop-and-Soil-Science.pdf">เส้นโค้งการกักเก็บน้ำของดิน</a> และใช้หาพารามิเตอร์ไฮดรอลิกของดินได้ ให้วางข้อมูลการวัดของคุณ (ความดัน, ปริมาณน้ำ) ลงในช่องข้อความด้านล่าง แล้วกดปุ่ม “คำนวณ” ก่อนใช้ข้อมูลของคุณเอง คุณสามารถทดลองโปรแกรมโดยเลือกข้อมูลตัวอย่างจากเมนูแบบเลื่อนลงได้',
    'calculate': 'คำนวณ',
    'wait': 'โปรดรอสักครู่ ...',
    'sample': 'ตัวอย่างผลลัพธ์',
    'help': '<h2>การอ้างอิง</h2>\n<p>เมื่อเผยแพร่ผลงานวิจัยที่ได้จากโปรแกรมนี้ SWRC Fit หรือ unsatfit โปรดอ้างอิงบทความนี้ SWRC Fit ใช้ไลบรารี <a href="https://sekika.github.io/unsatfit/">unsatfit</a> ในการคำนวณ</p>\n',
    'ack': '<h2>กิตติกรรมประกาศ</h2><ul><li>ข้อมูลตัวอย่างมาจาก <a href="https://doi.org/10.15482/USDA.ADC/1173246">ฐานข้อมูล UNSODA</a> เกี่ยวกับสมบัติไฮดรอลิกของดินไม่อิ่มตัว ซึ่งพัฒนาโดย US Salinity Laboratory สำหรับข้อมูลเพิ่มเติม โปรดดู <a href="https://sekika.github.io/unsoda/">UNSODA viewer</a></li><li>คำขอบคุณสำหรับผู้ช่วยด้านการแปลจะแสดงไว้ในหน้าของแต่ละภาษา ผมใช้ได้เฉพาะภาษาอังกฤษและภาษาญี่ปุ่น จึงยินดีรับความช่วยเหลือในการปรับปรุงคำแปล</li></ul>',
    'question': '<h2>คำถาม</h2><p>โปรดส่งคำถามและรายงานข้อผิดพลาดไปยังส่วน <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">Q&amp;A ของ unsatfit Discussions</a> สร้างบัญชี GitHub เข้าสู่ระบบ แล้วกดปุ่มสีเขียว “New discussion” ผมจะตอบในความคิดเห็น หากคำถามของคุณเป็นความลับ เช่น มีข้อมูลที่ยังไม่ได้เผยแพร่ โปรดติดต่อทางอีเมล ที่อยู่อีเมลอยู่ใน <a href="https://doi.org/10.1002/vzj2.20168">บทความนี้</a></p>',
    'format': '<h2>รูปแบบข้อมูลนำเข้า</h2>\n<ul>\n<li>เช่นเดียวกับข้อมูลตัวอย่าง แต่ละบรรทัดของข้อมูลตัวเลขจะแสดงค่าที่วัดเป็นคู่ <span class="ltr">(h, &theta;)</span> ตามลำดับนี้ <a href="unit.html">สามารถใช้หน่วยใดก็ได้</a>\n<li>ค่าในแต่ละบรรทัดคั่นด้วยช่องว่าง tab หรือจุลภาค (,)\n<li>หากมีตัวเลขมากกว่าสองค่า จะอ่านเฉพาะสองค่าแรก\n<li>บรรทัดที่ไม่ได้ขึ้นต้นด้วยตัวเลขจะไม่ถือเป็นข้อมูลการวัด</ul>',
    'modelselect': 'เลือกแบบจำลอง',
    'figoption': 'ตัวเลือกรูป',
    'onemodel': 'แสดงเฉพาะแบบจำลองที่ดีที่สุด',
    'showmore': 'แสดงตัวเลือกเพิ่มเติม',
    'swrc': 'เส้นโค้งการกักเก็บน้ำของดิน',
    'selectsample': 'เลือกจากข้อมูลตัวอย่าง',
    'pastehere': 'วางข้อมูลที่นี่',
    'inputerror': 'ข้อผิดพลาดของข้อมูลนำเข้า',
    'sameh': 'ค่า h ทั้งหมดเท่ากัน จำเป็นต้องมีค่า h ที่แตกต่างกัน',
    'readformat': 'ดูรูปแบบข้อมูลนำเข้าด้านล่าง',
    'result': 'ผลลัพธ์',
    'footer': '<a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a> ทำงานด้วย <a href="https://sekika.github.io/unsatfit/">unsatfit</a> เวอร์ชัน VER ซึ่งพัฒนาโดย AUTHOR โดยใช้ Python PYV บน ARCH <a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">การรันเซิร์ฟเวอร์ภายในเครื่อง</a>',
    'history': 'บริการนี้<a href="URL">เปิดใช้งานมาแล้ว <strong>YEAR ปี</strong></a>',
}


POLISH_MESSAGES = {
    'description': 'SWRC Fit może dopasować <a href="model.html">różne modele hydrauliczne gleby</a> do zmierzonych danych <a href="https://agro.icm.edu.pl/agro/element/bwmeta1.element.agro-article-64d1a773-0cc6-49ad-a50f-cda0876ac0a5/c/Use_of_neural_networks.pdf">krzywej retencji wodnej gleby</a> i wyznaczyć parametry hydrauliczne gleby. Wklej dane pomiarowe (ciśnienie, zawartość wody) do pola tekstowego poniżej i naciśnij przycisk „Oblicz”. Przed użyciem własnych danych możesz wypróbować program, wybierając dane przykładowe z menu rozwijanego.',
    'calculate': 'Oblicz',
    'wait': 'Proszę czekać ...',
    'sample': 'Przykładowy wynik',
    'help': '<h2>Cytowanie</h2>\n<p>Publikując wyniki badań uzyskane za pomocą tego programu, SWRC Fit lub unsatfit, proszę zacytować ten artykuł. SWRC Fit wykorzystuje bibliotekę <a href="https://sekika.github.io/unsatfit/">unsatfit</a> do obliczeń.</p>\n',
    'ack': '<h2>Podziękowania</h2><ul><li>Dane przykładowe pochodzą z <a href="https://doi.org/10.15482/USDA.ADC/1173246">bazy danych UNSODA</a> właściwości hydraulicznych gleb nienasyconych, opracowanej przez US Salinity Laboratory. Więcej danych można znaleźć w <a href="https://sekika.github.io/unsoda/">UNSODA viewer</a>.</li><li>Podziękowania za pomoc w tłumaczeniu są podane na stronie każdego języka. Posługuję się tylko językiem angielskim i japońskim, dlatego mile widziana jest pomoc w ulepszaniu tłumaczeń.</li></ul>',
    'question': '<h2>Pytania</h2><p>Pytania i zgłoszenia błędów proszę zamieszczać w sekcji <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a?discussions_q=">Q&amp;A w unsatfit Discussions</a>. Utwórz konto GitHub, zaloguj się i naciśnij zielony przycisk „New discussion”. Odpowiem w komentarzu. Jeśli pytanie jest poufne, na przykład zawiera nieopublikowane dane, proszę skontaktować się ze mną e-mailem. Adres e-mail znajduje się w <a href="https://doi.org/10.1002/vzj2.20168">tym artykule</a>.</p>',
    'format': '<h2>Format danych wejściowych</h2>\n<ul>\n<li>Tak jak w danych przykładowych, każdy wiersz danych liczbowych przedstawia parę zmierzonych wartości <span class="ltr">(h, &theta;)</span> w tej kolejności. <a href="unit.html">Można użyć dowolnych jednostek</a>.\n<li>Wartości w każdym wierszu są rozdzielone spacją, tabulatorem lub przecinkiem (,).\n<li>Jeśli w wierszu znajduje się więcej niż dwie liczby, odczytywane są tylko dwie pierwsze.\n<li>Wiersze, które nie zaczynają się od liczby, nie są traktowane jako dane pomiarowe.</ul>',
    'modelselect': 'Wybór modelu',
    'figoption': 'Opcje wykresu',
    'onemodel': 'Pokaż tylko najlepszy model',
    'showmore': 'Pokaż więcej opcji',
    'swrc': 'Krzywa retencji wodnej gleby',
    'selectsample': 'Wybierz dane przykładowe',
    'pastehere': 'Wklej dane tutaj',
    'inputerror': 'Błąd danych wejściowych',
    'sameh': 'Wszystkie wartości h są takie same. Wymagane są różne wartości h.',
    'readformat': 'Zobacz poniżej format danych wejściowych.',
    'result': 'Wynik',
    'footer': '<a href="https://sekika.github.io/unsatfit/swrcfit.html">SWRC Fit</a> działa z wersją VER biblioteki <a href="https://sekika.github.io/unsatfit/">unsatfit</a>, utworzonej przez AUTHOR, przy użyciu Python PYV na ARCH. <a href="https://github.com/sekika/unsatfit/blob/main/docker/Readme.md">Uruchamianie serwera lokalnego</a>.',
    'history': 'Ta usługa <a href="URL">działa już od <strong>YEAR lat</strong></a>.',
}


def message(lang, ID, URL='./'):
    """Define localized message"""
    if ID == 'list':
        # Return list of available languages in two-letter codes of ISO 639-1.
        # https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
        # It is used for lang parameter in this function.
        # It appears in the language menu in this order.
        return ['ar', 'de', 'en', 'es', 'fa', 'fr', 'id', 'it', 'ja', 'ko', 'pl', 'pt', 'ru', 'th', 'tr', 'vi', 'zh']
    if ID == 'langname':
        # Return language name in the language
        if lang == 'en':
            return 'English'
        if lang == 'es':
            return 'Español'
        if lang == 'fr':
            return 'Français'
        if lang == 'fa':
            return 'فارسی'
        if lang == 'ar':
            return 'العربية'
        if lang == 'id':
            return 'Bahasa Indonesia'
        if lang == 'ko':
            return '한국어'
        if lang == 'pl':
            return 'Polski'
        if lang == 'th':
            return 'ไทย'
        if lang == 'vi':
            return 'Tiếng Việt'
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
        bar = '<form class="ltr" action="' + URL + '" method="get">'
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
            'ar': ARABIC_MESSAGES,
            'fa': PERSIAN_MESSAGES,
            'id': INDONESIAN_MESSAGES,
            'it': ITALIAN_MESSAGES,
            'ko': KOREAN_MESSAGES,
            'pl': POLISH_MESSAGES,
            'th': THAI_MESSAGES,
            'vi': VIETNAMESE_MESSAGES,
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
            return 'SWRC Fit permet d’ajuster <a href="model.html">différents modèles</a> de <a href="https://theses.univ-orleans.fr/public/2016ORLE2039_va.pdf">rétention de l’eau du sol</a> avec des valeurs mesurées. ' \
                + 'Copiez vos données mesurées (pression, teneur en eau)  dans la zone de texte ci-dessous et appuyez sur le bouton "Calculer". Vous pouvez choisir des exemples de données dans le menu déroulant. '
        if lang == 'de':
            return 'SWRC Fit kann <a href="model.html">bodenhydraulische Modelle</a> an gemessene <a href="https://de.wikipedia.org/wiki/Bodenwasserspannung">Bodenwasserspannungskurven</a> anpassen. ' \
                + 'Kopieren Sie Ihre Bodenwasserspannungsdaten in das Textfeld und klicken Sie auf "Berechnen". Sie können Beispieldaten aus dem Pull-Down-Menü auswählen.'
        if lang == 'pt':
            return 'SWRC Fit pode definir água <a href="model.html">diferentes modelos</a> de <a href="https://en.wikipedia.org/wiki/Water_retention_curve">curva de retenção de água no solo</a> para os valores medidos. ' \
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
