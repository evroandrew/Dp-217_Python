function ajaxRequest(values, answer_id) {
    //let csrf = $('input[name=csrfmiddlewaretoken]')[0].value;
    if (typeof values == "undefined") {
        values = {
            "questions":
                ["Ви б віддали перевагу:", "Ви б віддали перевагу:", "Ви б віддали перевагу:", "Ви б віддали перевагу:",
                    "Ви б віддали перевагу:", "Ви б віддали перевагу:", "Ви б віддали перевагу:", "Ви б віддали перевагу:",
                    "Ви б віддали перевагу:", "Ви б віддали перевагу:", "Ви б віддали перевагу:", "Ви б віддали перевагу:",
                    "Ви б віддали перевагу:", "Ви б віддали перевагу:", "Ви б віддали перевагу:", "Ви б віддали перевагу:",
                    "Ви б віддали перевагу:", "Ви б віддали перевагу:", "Ви б віддали перевагу:", "Ви б віддали перевагу:"],
            "answers":
                ["Доглядати за тваринами", "Керувати будь-яким видом техніки (автомобіль, літак, мотоцикл)",
                    "Допомагати хворим", "Розробляти комп'ютерні програми і алгоритми",
                    "Обробляти фотографії за допомогою комп'ютерних програм", "Стежити за станом, розвитком рослин",
                    "Перевіряти справність систем літака перед вильотом", "Аналізувати і визначати найвигідніші способи доставки товарів в магазини",
                    "Перевіряти правильність заповнення документів, договорів, довіреностей", "Вести свій блог або писати статті для різних видань",
                    "Займатися розведенням і дресируванням породистих собак", "Навчати учнів або студентів",
                    "Обробляти музичні композиції", "Знаходити несправності в автомобілях, ремонтувати їх і виконувати сервісне обслуговування",
                    "Підбирати для туристів оптимальні місця відпочинку, проводити їм екскурсії", "Займатися оформленням виставок і вітрин",
                    "Ремонтувати і налаштовувати комп'ютерну техніку", "Заниматься обработкой и анализом собранных данных",
                    "Дослідити поведінку тварин в штучних лабораторних умовах", "Аналізувати зміни цін акцій на біржі",
                    "Вивчати мікроорганізми і бактерії за допомогою сучасних мікроскопів", "Ремонтувати і налаштовувати комп'ютерну техніку",
                    "Консультувати і допомагати людям за допомогою телефону довіри", "Стежити за курсами валют і акцій, брати участь в торгах",
                    "Брати участь в театральних постановках", "Стежити за станом лісів, вчасно вживати заходів по їх відновленню",
                    "Контролювати роботу промислового обладнання", "Стежити за правопорядком в громадських місцях, за дотриманням правил дорожнього руху",
                    "Проводити оптимізацію роботи сайту, інтернет-магазину, складати продають тексти", "Займатися реставрацією історичних артефактів",
                    "Проводити генетичні дослідження", "Під час залізничних поїздок і перельотів супроводжувати і допомагати пасажирам",
                    "Займатися ландшафтним дизайном, архітектурою будівель", "Створювати нове обладнання для промисловості та вдосконалювати існуючі прилади",
                    "Керувати туристичною групою в поході", "Продавати рідкісні товари, переконуючи клієнта купити",
                    "Займатися прокладкою і монтажем оптоволоконних ліній", "Займатися розміткою даних і навчанням штучних нейронних мереж і штучного інтелекту",
                    "Займатися генної модифікацією", "Створювати додатки для смартфонів"],
            "result_id": [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 2, 4, 1, 2, 4, 1, 3, 0, 3, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 2,
                4, 1, 2, 4, 1, 3, 0, 3],
            "results": []
        };
    } else {
        values['results'].push(answer_id);
    }
    let SendInfo = {
        question: values['questions'].pop(),
        answer_id_1: values['answers'].pop(),
        answer_id_2: values['answers'].pop(),
        result_1: values['result_id'].pop(),
        result_2: values['result_id'].pop(),
        values: values
    };
    console.log(values['results']);
    //$( "demo-container" ).html(res);
    //console.log(JSON.parse(res));
    if (values['results'].length < 20) {
        $.ajax({
            type: "POST",
            url: '/questioning/ajax/',
            data: JSON.stringify(SendInfo),
            dataType: 'text',
            success: function (res) {
                console.log("Update Successful");
                $("#main_container").html(res);
            },
            error: function (res, error) {
                console.log(error);
            }
        });
    } else {
        $.ajax({
            type: "POST",
            url: '/questioning/results/',
            data: JSON.stringify(values),
            dataType: 'text',
            success: function (res) {
                console.log("Update Successful");
                $("#main_container").html(res);
            },
            error: function (res, error) {
                console.log(error);
            }
        });
    }
}