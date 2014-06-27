function is_correct(element, exerciseId, action, answer) {
    var answer = $(element).parents("tr").find("#answer").val() != '' ?
        $(element).parents("tr").find("#answer").val() :
        $(element).parents("tr").find("#answer").text().trim().replace(/\s+/gm,' ');
        $.post('/website/' + action, {answer: answer, id: exerciseId},
            function(data) {
                if (data == "correct") {
                    $(element).parents('tr').find('td:last').html("<span>Richtig</span>")
                } else {
                    $(element).parents('tr').find('td:last').html("<span>Falsh</span>")
                }
            });
}

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("Text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("Text");
    ev.target.appendChild(document.getElementById(data));
}
