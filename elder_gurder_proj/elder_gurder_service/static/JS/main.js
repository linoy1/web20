$(document).ready(function() {
    $('#example').DataTable({
        "dom": '<"toolbar">frtip'
    });

    $("div.toolbar").html('<b>Custom tool bar! Text/images etc.</b>');
});
/*people page */


$(document).ready(function() {
    $('#dtBasicExample').DataTable({
        "paging": false // false to disable pagination (or any other option)
    });
    $('.dataTables_length').addClass('bs-select');
});


$(document).ready(function() {
    $('#memployboxes-1').change(function() {
        $('#motherdiv').fadeIn();
    });
    $('#memployboxes-0').change(function() {
        $('#motherdiv').fadeOut();
    });
    $('#femployboxes-1').change(function() {
        $('#fatherdiv').fadeIn();
    });
    $('#femployboxes-0').change(function() {
        $('#fatherdiv').fadeOut();
    });

});