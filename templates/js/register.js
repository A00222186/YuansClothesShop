let rooturl="";

let formToJSON=function(){
    return JSON.stringify({
            "username":$('username').val(),
            "birthday":$('birthday').val(),
            "gender":$('gender').val(),
            "userpassword":$('password').val(),
            "permission":"user",
            "statustype":"available"

    });
};

let confirmpwd=function(){
        let pwd=$('pwd').val();
        let conpwd=$('conpwd').val();
        if(pwd !== conpwd)
            alert("two time tep password is not same!")
            return false;

}

let register=function(){
        console.log("start to register user");
        $.ajax({
            type:'POST',
            contentType:'application/json',
            url:rooturl,
            dataType:"json",
            data:formToJSON(),
            success:function(data,textStatus,jqXHR){
                alert("register successfully");
                $('registerdiv').hidden;

            }
        });
}

$(document).on("click",'btnregister',function () {
    confirmpwd();
    register();
})