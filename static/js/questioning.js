async function getQuestions() {
    let url = '/questioning/get_questions/1';
    try {
        let res = await fetch(url);
        return await res.json();
    } catch (error) {
        console.log(error);
    }
}

async function ajaxRequest(values, answer_id) {
    //let csrf = $('input[name=csrfmiddlewaretoken]')[0].value;
    if (typeof values == "undefined") {
        let questions = await getQuestions();
        values = JSON.parse(questions);
    } else {
        values[0]['results'].push(answer_id);
    }
    if (values[0]['results'].length < 20) {
        let val = values[0]['questions'].pop();
        let SendInfo = {
            question: val['question'],
            answer_id_1: val['answer_1'],
            answer_id_2: val['answer_2'],
            result_1: val['result_id_1'],
            result_2: val['result_id_2'],
            values: values
        };
        $.ajax({
            type: "POST",
            url: '/questioning/ajax/',
            data: JSON.stringify(SendInfo),
            dataType: 'text',
            success: function (res) {
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
            data: JSON.stringify(values[0]['results']),
            dataType: 'text',
            success: function (res) {
                $("#main_container").html(res);
            },
            error: function (res, error) {
                console.log(error);
            }
        });
    }
}
