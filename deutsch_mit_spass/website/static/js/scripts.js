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

function is_ordering_correct(element, exerciseId) {
    var first = $(element).parents("tr").find("#first").val();
    var second = $(element).parents("tr").find("#second").val();
    var third = $(element).parents("tr").find("#third").val();
    var fourt = $(element).parents("tr").find("#fourt").val();
    $.post('/website/doorderings', {first: first, second: second, third: third, fourt: fourt, id: exerciseId},
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
