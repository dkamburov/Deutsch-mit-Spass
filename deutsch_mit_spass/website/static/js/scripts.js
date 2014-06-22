function is_correct(element, exerciseId) {
    var answer = $(element).parents("tr").find("textarea").val();
    $.post('/website/doexercises', {answer: answer, id: exerciseId},
            function(data) {
                if (data == "correct") {
                    $(element).parents('tr').find('td:last').html("<span>Richtig</span>")
                } else {
                    $(element).parents('tr').find('td:last').html("<span>Falsh</span>")
                }
            });
}
