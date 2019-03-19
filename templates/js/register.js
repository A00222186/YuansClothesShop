/*$(document).on("click",'#btnregister',function () {
    confirmpwd();
    register();
});*/


var formToJSON=function(){
    return JSON.stringify({
            "username":$('#username').val(),
            "birthday":$('#birthday').val(),
            "gender":$('#gender').val(),
            "userpassword":$('#pwd').val(),
            "permission":$('#permission').val(),
            "statustype":$('#statustype').val()
    });
};

var confirmpwd = function(){
        var pwd=$('#pwd').val();
        var conpwd=$('#conpwd').val();
        if(pwd != conpwd) {
            alert("Inconsistent password entered twice!");
            event.preventDefault();
        }
        return true;
};

var register = function(){
        console.log("start to register user");
        $.ajax({
            type:'POST',
            contentType:'application/json',
            url:"{{ register}}",
            dataType:"json",
            data:formToJSON(),
            success:function(data,textStatus,jqXHR){
                alert("register successfully");
                $('#registerdiv').hidden;

            },
            error:function (jqXHR,textStatus,errorThrown) {
                alert("register error:"+textStatus);
            }

        });
};


$(document).on("click",'#btnregister',function () {
    confirmpwd();
    register();
});