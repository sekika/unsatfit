def message(lang, ID, URL='./'):
    """Define localized message"""
    if ID == 'list':
        # Return list of available languages in two-letter codes of ISO 639-1.
        # https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
        # It is used for lang parameter in this function.
        # It appears in the language menu in this order.
        return ['en', 'es', 'fr', 'de', 'pt', 'ru', 'zh', 'ja']
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
        if lang == 'pt':
            return 'Português'
        if lang == 'ru':
            return 'Русский'
        if lang == 'zh':
            return '中文'
        if lang == 'ja':
            return '日本語'
        return lang
    if ID == 'langbar':
        # Make language menu bar
        bar = '[ '
        for i in message('', 'list'):
            language = message(i, 'langname')
            if i != 'en':
                bar += ' | '
            if lang == i:
                bar += '<strong>'+language+'</strong>'
            else:
                bar += '<a href="'+URL+'?lang='+i+'">'+language+'</a>'
        bar += ' ]'
        return bar
    if ID == 'css':
        return 'swrc.css'
    # From here translations to local languages are defined.
    # When translation is not defined, English message is returned.
    if ID == 'news':
        if lang == 'ja':
            return '<strong>[ニュース]</strong><ul><li><a href="https://doi.org/10.1002/vzj2.20168">この論文</a>の線型結合モデルに対応した新しいバージョンになりました。</li><li><a href="https://sekika.github.io/unsoda/">UNSODA viewer</a> と <a href="https://sekika.github.io/unsatfit/">unsatfit</a> もどうぞ。</li></ul>'
        return '<strong>[News]</strong><ul><li>This is a completely new version of SWRC Fit with bimodal models in <a href="https://doi.org/10.1002/vzj2.20168">this publication</a>.</li><li>Please also check <a href="https://sekika.github.io/unsoda/">UNSODA viewer</a> and <a href="https://sekika.github.io/unsatfit/">unsatfit</a>.</li></ul>'
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
            return '<h2>引用</h2>\n<p>SWRC Fit を使った研究成果を公表するときには、この論文を引用して下さい。\n' \
                + '<a href="https://scholar.google.com/citations?view_op=view_citation&hl=ja&user=Gs_ABawAAAAJ&citation_for_view=Gs_ABawAAAAJ:9yKSN-GCB0IC">多くの研究で使われています。</a></p>' \
                + '<ul><li>' + message(lang, 'seki2007') + '</li></ul>' \
                + '<h2>プログラム</h2><p>SWRC Fit は <a href="https://sekika.github.io/unsatfit/">unsatfit</a> のライブラリを使って計算をしています。'
        return '<h2>Citation</h2>\n<p><p>Please cite this paper when you publish your work using this program, SWRC Fit.\n' \
            + '<a href="https://scholar.google.com/citations?view_op=view_citation&hl=en&user=Gs_ABawAAAAJ&citation_for_view=Gs_ABawAAAAJ:9yKSN-GCB0IC">Researches conducted with SWRC Fit</a>.</p>'  \
            + '<ul><li>' + message(lang, 'seki2007') + '</li></ul>' \
            + '<h2>Program</h2><p>SWRC Fit uses <a href="https://sekika.github.io/unsatfit/">unsatfit</a> library.'
    if ID == 'ack':
        if lang == 'ja':
            return '<h2>謝辞</h2><ul><li>サンプルデータはアメリカ農務省塩類研究所が開発した不飽和土壌水分特性の<a href="' + message(lang, 'unsoda') + '">UNSODA データベース</a>から取得しました。<a href="https://sekika.github.io/unsoda/ja/">UNSODA ビューア</a>でさらにデータを閲覧可能です。<li>「土壌の物理性」で<a href="https://www.jstage.jst.go.jp/article/jssoilphysics/148/0/148_45/_article/-char/ja/">お薦めして</a>いただきました。</ul>'
        if lang == 'es':
            return '<h2>Acknowledgement</h2><ul><li>Sample data is from <a href="' + message(lang, 'unsoda') + '">UNSODA database</a> of unsaturated soil hydraulic properties developed by US Salinity Laboratory. See <a href="https://sekika.github.io/unsoda/">UNSODA viewer</a> for more data.</li>' \
                + '<li><a href="https://scholar.google.co.jp/citations?user=a842WTkAAAAJ">Dr. David Moret-Fernandez</a> corrected Spanish.</li></ul>'
        if lang == 'fr':
            return '<h2>Acknowledgement</h2><ul><li>Sample data is from <a href="' + message(lang, 'unsoda') + '">UNSODA database</a> of unsaturated soil hydraulic properties developed by US Salinity Laboratory. See <a href="https://sekika.github.io/unsoda/">UNSODA viewer</a> for more data.</li>' \
                + '<li><a href="https://lhyges.unistra.fr/ACKERER-Philippe?lang=fr">Dr. Philippe Ackerer</a> corrected French.</li></ul>'
        if lang == 'de':
            return '<h2>Acknowledgement</h2><ul><li>Sample data is from <a href="' + message(lang, 'unsoda') + '">UNSODA database</a> of unsaturated soil hydraulic properties developed by US Salinity Laboratory. See <a href="https://sekika.github.io/unsoda/">UNSODA viewer</a> for more data.</li>' \
                + '<li><a href="https://www.ufz.de/index.php?en=39081">Dr. Martin Thullner</a> corrected German.</li></ul>'
        if lang == 'zh':
            return '<h2>感谢</h2><ul><li>Sample data is from <a href="' + message(lang, 'unsoda') + '">UNSODA database</a> of unsaturated soil hydraulic properties developed by US Salinity Laboratory. See <a href="https://sekika.github.io/unsoda/">UNSODA viewer</a> for more data.</li>' \
                + '<li><a href="http://www.iswc.cas.cn/sourcedb_iswc_cas/zw/zjrc/200910/t20091020_2584555.html">Dr. Li Wang</a> corrected Chinese.</li></ul>'
        return '<h2>Acknowledgement</h2><ul><li>Sample data is from <a href="' + message(lang, 'unsoda') + '">UNSODA database</a> of unsaturated soil hydraulic properties developed by US Salinity Laboratory. See <a href="https://sekika.github.io/unsoda/">UNSODA viewer</a> for more data.</li>' \
            + '<li>Acknowledgement for translation is shown in each language page. I speak only English and Japanese. Help in language is always welcome.</li></ul>'
    if ID == 'question':
        if lang == 'ja':
            return '<h2>質問</h2><p>質問は<a href="https://github.com/sekika/unsatfit/discussions/categories/q-a">unsatfit DiscussionsのQ&A</a>に送ってください。GitHub のアカウントを取得しサインインして、緑色の「New discussion」ボタンを押して下さい。日本語での質問も可能です。コメントで返信します。未公開のデータに関する質問など、質問を公開出来ない場合には、メールで質問をしてください。メールアドレスは<a href="https://doi.org/10.1002/vzj2.20168">この論文</a>にあります。</p>'
        return '<h2>Question</h2><p>Please send questions and bug reports to <a href="https://github.com/sekika/unsatfit/discussions/categories/q-a">Q&A at unsatfit Discussions</a>. Get GitHub account, sign in, and press the green "New discussion" button. I will reply by comment. It is preferable to send your question publicly this way, because other people having the same question can find answer on the web. However, if your question is confidential, for example when it includes your unpublished data, please contact me by email. You can find my email address in <a href="https://doi.org/10.1002/vzj2.20168">this paper</a>.</p>'
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
            + '<a href="https://doi.org/10.1002/vzj2.20168">doi:10.1002/vzj2.20168</a>'
    if ID == 'fredlund1994':
        return 'Fredlund, D.G. and Xing, A. (1994): Equations for the soil-water characteristic curve. Can. Geotech. J., 31: 521-532. ' \
            + '<a href="http://dx.doi.org/10.1139/t94-061">doi:10.1139/t94-061</a>'
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
            return '<a href="?lang=ja">SWRC Fit</a> with <a href="https://sekika.github.io/unsatfit/">unsatfit</a> version VER （作成者：AUTHOR）が ARCH の Python PYV で動いています。'
        return '<a href="?lang=' + lang + '">SWRC Fit</a> with <a href="https://sekika.github.io/unsatfit/">unsatfit</a> version VER created by AUTHOR running with Python PYV on ARCH.'
    if ID == 'author':
        if lang == 'ja':
            return '<a href="http://www2.toyo.ac.jp/~seki_k/">関勝寿</a>'
        return '<a href="https://scholar.google.com/citations?user=Gs_ABawAAAAJ">Katsutoshi Seki</a>'
    return '<strong>Message ID error!</strong>'
